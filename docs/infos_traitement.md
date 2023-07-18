# Informations sur le traitement

## Préparer l'export

* Créer et exécuter un rapport SQL listant les biblionumbers (`SELECT biblionumber FROM biblioitems WHERE itemtype IN ("MEME", "MHMONP", "MEMU", "MES", "PFE", "THES", "TPFE", "TE")`)
* Diviser l'export en retirant l'en-tête et faire des paquets de 25-30 000 notices
* Dans Koha _Outils → Catalogue → Exporter les données_, exporter les notices :
  * En utilisant les fichiers créés
  * Avec les exemplaires

## Export de Koha

* L'export des données de Koha via l'option dans _Outils_ timeout après 5 minutes : des paquets de 30 000 notices semblent passer
* Poids des fichiers _(base de test)_ :
  * Lot 1 (30 000 notices) : 42,3 mo
  * Lot 2 (30 000 notices) : 43,9 mo
  * Lot 3 (29 055 notices) : 55,2 mo
* Poids des fichiers _(base de production)_ :
  * Lot 1 (25 000 notices) : 35 558 ko
  * Lot 2 (25 000 notices) : 37 463 ko
  * Lot 3 (25 000 notices) : 43 810 ko
  * Lot 4 (18 666 notices __(en fait il en manque 536636 qui a été supprimée entre temps)__) : 41 558 ko

## Traitement des notices

### Base de test

* Traitement lot 1 :
  * Temps de traitement : 1min 11sec
  * ~~Poids du log après le lot 1 : 9,53 mo~~
    * ~~Mais seulement 66XX notices → retirer le niveau DEBUG des logs~~
  * Poids du log (niveau INFO) : 3,44mo
  * Poids du fichier de sortie : 45,9 mo
  * Poids du fichier d'erreurs : 9ko
  * Nombre d'erreurs : 360
* Traitement lot 2 :
  * Temps de traitement : 1min 10sec
  * Poids du log (niveau INFO) : 3,43mo
  * Poids du fichier de sortie : 44,3 mo
  * Poids du fichier d'erreurs : 93ko
  * Nombre d'erreurs : 3144
* Traitement lot 3 :
  * Temps de traitement : 1min 12sec
  * Poids du log (niveau INFO) : 3,33mo
  * Poids du fichier de sortie : 56,9 mo
  * Poids du fichier d'erreurs : 19ko
  * Nombre d'erreurs : 669

### Erreurs en base de test

_Une partie des erreurs plus rares sont probablement dues à mes tests_

* Nombre total : __4173__
* Nombre de notices illisibles : 0
* Nombre de notices sans type de document : 1 _pas dans le lot de test_
* Nombre de notices sans date de publication : 1699
* Nombre de notices sans exemplaire : 859
* Nombre de notices possédant déjà deux 328 : 10
* Nombre de notices possédant une 328 sans $a ni $b : 19
* Nombre de notices sans établissement de soutenance : 1585

### Base de prod

* Traitement lot 1 :
  * Temps de traitement : 0 min 59 sec
  * Poids du log (niveau INFO) : 2 941 ko
  * Poids du fichier de sortie : 38 526 ko
  * Poids du fichier d'erreurs : 9 ko
  * Nombre d'erreurs : 322
  * Nombre de notices du fichier de sortie : 24 678
* Traitement lot 2 :
  * Temps de traitement : 0 min 59 sec
  * Poids du log (niveau INFO) : 2 933 ko
  * Poids du fichier de sortie : 38 524 ko
  * Poids du fichier d'erreurs : 72 ko
  * Nombre d'erreurs : 2362
  * Nombre de notices du fichier de sortie : 22 638
* Traitement lot 3 :
  * Temps de traitement : 1 min 01 sec
  * Poids du log (niveau INFO) : 2 934 ko
  * Poids du fichier de sortie : 44 857 ko
  * Poids du fichier d'erreurs : 33 ko
  * Nombre d'erreurs : 1234
  * Nombre de notices du fichier de sortie : 23 766
* Traitement lot 4 :
  * Temps de traitement : 0 min 46 sec
  * Poids du log (niveau INFO) : 2 194 ko
  * Poids du fichier de sortie : 42 880 ko
  * Poids du fichier d'erreurs : 7 ko
  * Nombre d'erreurs : 209
  * Nombre de notices du fichier de sortie : 18 456
* Total de notices dans les fichiers : __89 538__

### Erreurs en base de production

* Nombre total : __4127__
* Nombre de notices illisibles : 0
* Nombre de notices sans type de document : 0
* Nombre de notices sans date de publication : 1734
* Nombre de notices sans exemplaire : 773
* Nombre de notices possédant déjà deux 328 : 14
* Nombre de notices possédant une 328 sans $a ni $b : 19
* Nombre de notices sans établissement de soutenance : 1587