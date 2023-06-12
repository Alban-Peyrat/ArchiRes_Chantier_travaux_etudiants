# Actions à effectuer après le chantier

## Vérifications post-traitement

* Exécuter la requête SQL permettant de vérifier qu'il ne reste plus aucun document contenant les anciens types de document : `SELECT biblionumber FROM biblioitems WHERE itemtype IN ("MEME", "MHMONP", "MEMU", "MES", "PFE", "THES", "TPFE")` (à utiliser dans le rapport ID 1334)

## Mise en place de l'automatisation des rapports de contrôle

* Rapport identifiant les documents sans 328 / avec une 328$a / avec une 328$b oncorrecte : ID 1428 (prod) `_PYHTON_W_etudiants_sans_328`
  * À finaliser quand le mapping sera fini
* Rapport identifiant les documents sans 029 ou la mauvaise forme en 029 : ID 1427 (prod) `_PYHTON_W_etudiants_sans_029.sql`
  * À finaliser avec le mapping, pour remplacer `^\d{4}_[A-Z]+_` par `^\d{4}_(TPFE|MEMU|MASTERE|PFE)_` en remplissant la liste des codes valides