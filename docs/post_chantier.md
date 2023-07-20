# Actions à effectuer après le chantier

## Corrections des erreurs ignorées pendant le traitement

* Notices illisibles : _aucun document pour le moment_
* Notices sans type de document : corriger les notices individuellement, le nombre ne devrait pas être élevé
* Notices sans date de publication :
  * ???
* Notices sans exemplaire :
  * ???
* Notices possédant déjà deux 328 :
  * ???
* Notices possédant une 328 sans $a ni $b :
  * ???
* Notices sans établissement de soutenance :
  * ???

Une fois tout cela effectué, procéder aux modifications de suppression des types de documents dans Koha et dans Bokeh ([voir dans les opérations à effectuer](./operations_logiciels.md))
## Modifier les notices pour mettre les nouveaux types de travaux d'étudiants

## Corriger les notices cataloguées avec les nouvelles consignes avant le feu vert

## Corriger les notices de reproduction

* Les numéros nationaux de thèse pour les reproductions : utiliser le biblionumber du document original plutôt que celui de la reproduction

## Gestion plus précise de la passerelle Sudoc

## Vérifications post-traitement

* Exécuter la requête SQL permettant de vérifier qu'il ne reste plus aucun document contenant les anciens types de document : `SELECT biblionumber FROM biblioitems WHERE itemtype IN ("MEME", "MHMONP", "MEMU", "MES", "PFE", "THES", "TPFE")` (à utiliser dans le rapport ID 1334)

## Mise en place de l'automatisation des rapports de contrôle

* Rapport identifiant les documents sans 328 / avec une 328$a / avec une 328$b oncorrecte : ID 1428 (prod) `_PYHTON_W_etudiants_sans_328`
  * À finaliser quand le mapping sera fini
* Rapport identifiant les documents sans 029 ou la mauvaise forme en 029 : ID 1427 (prod) `_PYHTON_W_etudiants_sans_029.sql`
  * À finaliser avec le mapping, pour remplacer `^\d{4}_[A-Z]+_` par `^\d{4}_(TPFE|MEMU|MASTERE|PFE)_` en remplissant la liste des codes valides