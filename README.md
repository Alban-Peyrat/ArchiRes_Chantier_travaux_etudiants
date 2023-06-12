# Chantier du changement des types de travaux d'étudiants

Le but de ce chantier est de passer la notion de type de travaux d'étudiants du type de document à un champ spécifique.

Auparavant, il existait 8 types de documents correspondant à différents types de travaux d'étudiants (sur un total de 28 types de documents).
Avec ce changement, il restera 21 types de documents, dont un seul _Travaux d'étudiants_ pour tous les travaux d'étudiants.
Ainsi, la recherche par de travaux d'étudiants dans Koha peut se faire plus facilement sans devoir sélectionner les 8 (comme ce qui est en place dans notre portail).
Par ailleurs, la solution choisie permet de conserver la possibilité d'interroger des types de travaux d'étudiants spécifiquement à l'aide d'un autre index, et même de la rajouter sur la recherche avancée sur le portail (seuls les filtres dans les résultats de recherche permettaient de le faire).
Enfin, cela permet de clarifier toutes les notions employées (certains types étaient vagues) et permet de prendre en compte plus facilement les demandes d'ajout de type de travaux d'étudiants.

## Nombre de notice

* Nombre de notices concernées par un traitement rétrospectif : 903XX notices
* Nombre de notices du traitement rétrospectif avec une 328 : 144XX notices
  * Nombre de notices avec une 328$b : 750-800 notices
  * Nombre de notices dont le traitement rétrospectifs rajoutera une seconde 328 : 2XX notices

## Liste des Types de travaux d'étudiants

__À établir__

|Code|Libellé|Définition|
|---|---|---|
|MEME|Mémoire ENSA||
|MHMONP|Mémoire HMONP||
|MEMU|Mémoire universitaire||
|MES|MES||
|PFE|PFE||
|THES|Thèse||
|TPFE|TPFE||
|TE|Travaux d'étudiants||


|Code|Libellé|Définition|
|---|---|---|
|CEAA|CEAA (Certificat d'études approfondies en architecture)||
|DPEA|DPEA (Diplôme propre aux ENSA)||
|DSA|DSA (Diplôme de spécialisation et d'approfondissement)||
|MASTERE|Mastère||
|MES|MES (Mémoire de master)||
|RAPL|Rapport d'études (licence)|(ancien mémoire ensa)|
|MHMONP|Mémoire HMONP||
|MEMU|Mémoire universitaire||
|PFE|PFE (Projet de fin d'études)||
|THES|Thèse||
|TPFE|TPFE (Travail personnel de fin d'études)||
|TATE|Travaux d'ateliers|(anciens Travaux d'étudiants)||

## Nouvelles règles de catalogage des travaux d'étudiants :

* 099$t = Travaux d'étudiants (`TE`)
* 029 _OBLIGATOIRE_ :
  * Indicateurs = `__`
  * $a = `FR`
  * $m = `{AAAA}_{code du type de travaux d'étudiant}_{code de l'école}_{biblionumber}`
    * Exemple : `2023_PFE_MLVL_123456`
* 328 _Obligatoire_ :
  * Indicateurs = `_0`
  * $b = `{libellé du type de travaux d'étudiant}`
  * $c = `Architecture` (ou autres, le rétrospectif se fera sur `Architecture` uniquement)
  * __$e__ = `{Nom de l'école (comme en 214$c)}`
  * __$d__ = `{Année}`
  * __Le $e est avant le $d__

## Rechercher sur les types de travaux d'étudiants

* Pour rechercher dans Koha :
  * Via son code, rechercher dans l'index `diss` la forme suivante `*_{code}_*`
    * Exemple : `renard diss:*_PFE_*`
  * Via son libellé, rechercher dans l'index `diss` le nom ou le sigle s'il apparaît entre parenthèse dans le libellé
    * Exemples : `renard diss:Mastère` ou `renard diss:PFE`
  * Via l'onglet `Types de travaux d'étudiants` dans la recherche avancée
* Pour rechercher dans Bokeh :
  * Dans le menu de recherche avancée, utiliser le champ `Types de travaux d'étudiants` situé sous les types de documents.
    * L'utilisation de ce champ restreint forcément la liste de résultat à uniquement des documents contenant le type de docuemnt `Travaux d'étudiant`
  * Effectuer en premier lieu une recherche, puis filtrer les résultats à partir de la liste des filtres à gauche de la liste des résultats grâce au filtre `Types de travaux d'étudiants`

## Liste des autres fichiers de documentation

* [Demandes à effectuer auprès des prestataires](./demandes_prestataires.md)
* [Opérations à effectuer dans les différents logiciels du SID](./operations_logiciels.md)
* [Spécifications du traitement rétrospectif](./specs_traitement_retro.md)
* [Actions à effectuer après le chantier](./post_chantier.md)
