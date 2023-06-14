# Informations sur le traitement

## Export de Koha

* L'export des données de Koha via l'option dans _Outils_ timeout après 5 minutes : des paquets de 30 000 notices semblent passer
* Poids des fichiers _(base de test)_ :
  * Lot 1 (30 000 notices) : 42,3 mo
  * Lot 2 (30 000 notices) : 43,9 mo
  * Lot 3 (29 055 notices) : 55,2 mo

## Traitement des notices

* Traitement lot 1 :
  * Temps de traitement : 1min 11sec
  * ~~Poids du log après le lot 1 : 9,53 mo~~
    * ~~Mais seulement 66XX notices → retirer le niveau DEBUG des logs~~
  * Poids du log après le lot 1 (niveau INFO) : 3,44mo
  * Poids du fichier de sortie : 45,9 mo
  * Poids du fichier d'erreurs : 9ko
  * Nombre d'erreurs : 360
* Traitement lot 2 :
  * Temps de traitement : 1min 10sec
  * Poids du log après le lot 1 (niveau INFO) : 3,43mo
  * Poids du fichier de sortie : 44,3 mo
  * Poids du fichier d'erreurs : 93ko
  * Nombre d'erreurs : 3144
* Traitement lot 3 :
  * Temps de traitement : 1min 12sec
  * Poids du log après le lot 1 (niveau INFO) : 3,33mo
  * Poids du fichier de sortie : 56,9 mo
  * Poids du fichier d'erreurs : 19ko
  * Nombre d'erreurs : 669

## Erreurs en base de test

_Une partie des erreurs plus rares sont probablement dues à mes tests_

* Nombre total : __4173__
* Nombre de notices illisibles : 0
* Nombre de notices sans type de document : 1 _pas dans le lot de test_
* Nombre de notices sans date de publication : 1699
* Nombre de notices sans exemplaire : 859
* Nombre de notices possédant déjà deux 328 : 10
* Nombre de notices possédant une 328 sans $a ni $b : 19
* Nombre de notices sans établissement de soutenance : 1585