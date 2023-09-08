# Actions à effectuer après le chantier

## Corrections des erreurs ignorées pendant le traitement

[Voir les erreurs en base de production dans le fichier contenant les informations de traitement](./infos_traitement.md#erreurs-en-base-de-production)

Le script permettant de traiter ces cas est [`traitement_retro_for_errors.py`](../traitement_retro_for_errors.py), une fourche de l'original.

Une fois tout cela effectué, procéder aux modifications de suppression des types de documents dans Koha et dans Bokeh ([voir dans les opérations à effectuer](./operations_logiciels.md))

### Notices sans date de publication

_Rajouter ces 3 vagues à la place de l'erreur_

#### Première vague : 100 position 9-12

* Récupérer la date en 100 avce l'expression régulière `(?<=^.{9})\d{4}` (chaîne de 4 chiffres après 9 caractères qui commencent l'expression) → 297 matchs, resterait 1445, mais c'est la plus efficace

#### Deuxième vague : rechercher dans toute la 210/214 en cas d'erreur de catalogage

* Transformer les 214 et 210 en une chaîne de caractères, puis utiliser l'expression régulière `\d{4}` (chaîne de 4 chiffres) pour récupère ce qui ressemble à une année et que la date soit comprise entre 1900 et 2050 → 37 pour les 214, 2 pour les 210 → c'est moins sûr mais reste pertinent de ce que j'ai vu, resterait 1398
  * Ce qui reste à majoritairement pas de 214/210 (7 ont des 210, 132 ont des 214, 1259 aucun)

#### Troisième vague : utiliser la date de création de la notice en 100

* Utiliser l'expression régulière `^\d{4}` sur les 100, ce qui récupère l'année de création de la notice
  * Doit fonctionner dans 100% des cas restants
  * Mais la date de création n'est pas forcément égale à la date de soutenance
  * Donc __en 328, mettre la date entre crochets et avec un `?` en fin__ (nécessite de créer un flag)

### Notices sans exemplaires

_Rajouter à la place de l'erreur_

#### Première vague : rechercher un terme précis en 210/4$c

* Rechercher en 214$c/210$c un terme spécifique puis le transformer (ex : nom de ville, "La Défense")

#### Deuxième vague : rechercher un terme précis en 210/4$a

* _Ne pas faire pour les parisiennes, Versailles et Marseille_
* Rechercher en 214$a/210$a le nom de la ville puis le transformer

#### Troisième vague : rechercher un terme précis en 710/1/2$a

* Rechercher en 710/1/2$a un terme spécifique puis le transformer (ex : nom de ville, "La Défense")

#### Quatrième vage : manuel

* Possiblement peu de résultats restants, donc les traiter manuellement

### Notices sans établissement de soutenance

_Rajouter à la place de l'erreur_

* Créer une chaîne de texte à partir du code école
  * Si la date est strictement inférieur à 1985, l'appellation `Unité pédagogique d'architecture` est utilisée
  * Si la date est supérieure ou égale à 1985 et strictement inférieur à 2005, l'appellation `EA` est utilisée
  * Sinon, conserve l'appelation `ENSA` / `ENSAP`
    * _Les anciennes unités pédagogiques d'architecture, rattachées au Ministère de l'Équipement et du Logement, deviennent, en 1985, des « écoles d'architecture », qui retrouvent leur affiliation au Ministère de la Culture, puis en 2005, sont nommées « écoles nationales supérieures d'architecture » (ENSA)._
  * Doit fonctionner dans 100% des cas qui arrivent jusque là

### Notices possédant déjà deux 328

Seulement 14 notices, traitées manuellement

### Notices possédant une 328 sans $a ni $b

Seulement 19 notices, traitées manuellement

### Informations sur le traitement

* Nombre de notices à traiter : 4094
* Traitement du lot :
  * Temps de traitement : 0 min 9 sec
  * Poids du log (niveau INFO) : 480 ko
  * Poids du fichier de sortie : 5 352 ko
  * Poids du fichier d'erreurs : 2 ko
  * Nombre d'erreurs : 28
  * Nombre de notices du fichier de sortie : __4 066__
* Erreurs :
  * Nombre total : __28__
  * Nombre d'échec d'identification de l'école : 28
    * __Ces notices seront traitées manuellement__

## Vérifications post-traitement

* Exécuter la requête SQL permettant de vérifier qu'il ne reste plus aucun document contenant les anciens types de document : `SELECT biblionumber FROM biblioitems WHERE itemtype IN ("MEME", "MHMONP", "MEMU", "MES", "PFE", "THES", "TPFE")` (à utiliser dans le rapport ID 1334)

## Mise en place de l'automatisation des rapports de contrôle

* ~~Rapport identifiant les documents sans 328 / avec une 328$a / avec une 328$b incorrecte : ID 1428 (prod) `_PYHTON_W_etudiants_sans_328`~~
  * Certaines 328 ayant été laissées telles qu'elles, ce rapport est moins pertinent car beaucup de résultats seraient incorrects
* Rapport identifiant les documents sans 029 ou la mauvaise forme en 029 : ID 1427 (prod) `_PYHTON_W_etudiants_sans_029.sql`
  * Regarde cherche dans lu 029$m l'expression régulière `^\\d{4}_(CCJP|CEAA|CESP|DPEA|DSA|MASTERE|MES|MHMONP|MEMU|PFE|RAPL|THES|TPFE|TATE)_`

## Mise en place d'un rapport permettant de compter le nombre de documents par types de travaux étudiants

Rapport ID 1443, permet de filtrer sur l'école

``` SQL
SELECT COUNT(biblionumber) AS "Nombre de notices",
    REGEXP_SUBSTR(ExtractValue(bm.metadata, '//datafield[@tag="029"]/subfield[@code="m"]'), "(?<=^\\d{4}_)[A-Z]+(?=_[A-Z]{4})") AS w_etud_type
FROM biblio b
JOIN biblio_metadata bm USING(biblionumber)
JOIN biblioitems bi USING(biblionumber)

WHERE (
    ExtractValue(bm.metadata, '//datafield[@tag="029"]/subfield[@code="m"]') REGEXP CONCAT("^\\d{4}_(CCJP|CEAA|CESP|DPEA|DSA|MASTERE|MES|MHMONP|MEMU|PFE|RAPL|THES|TPFE|TATE)_", <<Bibliothèque |branches>>)
    AND bi.itemtype = "TE"
)

GROUP BY w_etud_type

ORDER BY w_etud_type asc

/* Rapport ID (test) : 1402
Rapport ID (prod) : 1443

Compte le nombre de documents par types de travaux d'étudiants pour une école */
```

Rapport ID 1444, permet de filtrer par école ou type de travaux étudiants depuis un tableur (exporte la partie `{Type W etud}_{Code École}`)

``` SQL
SELECT COUNT(biblionumber) AS "Nombre de notices",
    REGEXP_SUBSTR(ExtractValue(bm.metadata, '//datafield[@tag="029"]/subfield[@code="m"]'), "(?<=^\\d{4}_)[A-Z]+_[A-Z]{4}") AS w_etud_type
FROM biblio b
JOIN biblio_metadata bm USING(biblionumber)
JOIN biblioitems bi USING(biblionumber)

WHERE (
    ExtractValue(bm.metadata, '//datafield[@tag="029"]/subfield[@code="m"]') REGEXP "^\\d{4}_(CCJP|CEAA|CESP|DPEA|DSA|MASTERE|MES|MHMONP|MEMU|PFE|RAPL|THES|TPFE|TATE)_"
    AND bi.itemtype = "TE"
)

GROUP BY w_etud_type

ORDER BY w_etud_type asc

/* Rapport ID (test) : 1402
Rapport ID (prod) : 1444

Compte le nombre de documents par types de travaux d'étudiants */
```

## Modifier les notices pour mettre les nouveaux types de travaux d'étudiants

## Corriger les notices cataloguées avec les nouvelles consignes avant le feu vert

## Corriger les notices de reproduction

* Les numéros nationaux de thèse pour les reproductions : utiliser le biblionumber du document original plutôt que celui de la reproduction

## Gestion plus précise de la passerelle Sudoc

