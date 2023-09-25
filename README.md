# Chantier du changement des types de travaux d'étudiants

Le but de ce chantier est de passer la notion de type de travaux d'étudiants du type de document à un champ spécifique.

Auparavant, il existait 8 types de documents correspondant à différents types de travaux d'étudiants (sur un total de 28 types de documents).
Avec ce changement, il restera 21 types de documents, dont un seul _Travaux d'étudiants_ pour tous les travaux d'étudiants.
Ainsi, la recherche par de travaux d'étudiants dans Koha peut se faire plus facilement sans devoir sélectionner les 8 (comme ce qui est en place dans notre portail).
Par ailleurs, la solution choisie permet de conserver la possibilité d'interroger des types de travaux d'étudiants spécifiquement à l'aide d'un autre index, et même de la rajouter sur la recherche avancée sur le portail (seuls les filtres dans les résultats de recherche permettaient de le faire).
Enfin, cela permet de clarifier toutes les notions employées (certains types étaient vagues) et permet de prendre en compte plus facilement les demandes d'ajout de type de travaux d'étudiants.

## Nombre de notice

* Nombre de notices concernées par un traitement rétrospectif : 93 666 notices
* Nombre de notices du traitement rétrospectif avec une 328 : 144XX notices
  * Nombre de notices avec une 328$b : 750-800 notices
  * Nombre de notices dont le traitement rétrospectifs rajoutera une seconde 328 : 2XX notices

## Liste des Types de travaux d'étudiants

|Code|Libellé|Code facette Bokeh|Définition|
|---|---|---|---|
|CCJP|CCJP (Concepteur et créateur de jardin dans le paysage)|ø|Projet personnel de conception de jardin ou parc pour valider la formation professionnalisante Conception et création de jardin dans le paysage, enseignée à l'Ecole nationale supérieure de paysage (Versailles).|
|CEAA|CEAA (Certificat d'études approfondies en architecture)|ø|Mémoire rédigé pour obtenir un certificat d’études approfondies en architecture, certificat qui n'est ouvert qu’aux architectes DPLG. Ces certificats, qui confèrent une spécialisation, peuvent se dérouler sur plusieurs années. Chaque école détermine les matières enseignées au sein de leur CEAA et les conditions d’admission.|
|CESP|CESP (Certificat d'études supérieures paysagères)|ø|Mémoire pour obtenir le Certificat d'études supérieures paysagères (CESP), formation professionnalisante en conception du paysage, enseignée à l'Ecole nationale supérieure de paysage (Versailles et Marseille). |
|DPEA|DPEA (Diplôme propre aux ENSA)|ø|Mémoire pour obtenir un diplôme de spécialisation aux études d'architecture, équivalent à un master spécialisé (sur bac+3)|
|DSA|DSA (Diplôme de spécialisation et d'approfondissement)|ø|Mémoire pour obtenir un diplôme de spécialisation et d'approfondissement d'arhitecture (sur bac+5)|
|MASTERE|Mastère|HTYP10009|Mémoire d'obtention d'un mastère, diplôme labellisé par la Conférence des Grandes Ecoles (CGE) (sur bac+4 ou bac+5)|
|MES|Mémoire de master (MES)|HTYP10003|Mémoire de Master 2 ou ""mémoire de fin d'études"" (ENSA Nancy) - ENSP : Mémoire de Master TDPP (Théories et démarches du projet de paysage) : parcours du Master 2 Agrosciences, Environnement, Territoires, Paysage, Forêt de l'Université Paris-Saclay - Mémoire Master Patrimoine et création par le projet, parcours du Master 2 Humanités  et industries créatives, de l'Université CY Cergy Paris|
|MHMONP|Mémoire HMONP (Habilitation à la maîtrise d'œuvre en son nom propre)|HTYP10008|Mémoire de l’année d'Habilitation à la maîtrise d'œuvre en son nom propre) dite « 6ème année » menant à assumer les responsabilités de l'architecte en tant qu'auteur de son projet architectural. Ils sont conservés dans quelques bibliothèques, mais souvent d'accès restreints aux étudiants de ce cursus.|
|MEMU|Mémoire universitaire|HTYP10007|Mémoire de maîtrise ou de master émanant d'universités|
|PFE|PFE (Projet de fin d'études)|HTYP10005|Depuis la réforme des études en 2007 qui harmonise les diplômes au niveau européen ( licence, master, doctorat), l’étudiant obtient le diplôme d’Etat d’architecte ou le diplôme d'Etat de paysagiste à l’issue du master après soutenance du Projet de fin d'études (PFE).|
|RAPL|Rapport d'études (Licence)|HTYP10004|_(ancien Mémoire ENSA)_ Correspond également aux mémoires de TPER|
|THES|Thèse|HTYP10002|Thèse de doctorat soutenue à l’université dans diverses disciplines liées à l’architecture, au paysage et à l’urbanisme, ou dans les écoles d’architecture ou de paysage à l’issue du troisième cycle d’études en architecture ou en paysage|
|TPFE|TPFE (Travail personnel de fin d'études)|HTYP10001|Le TPFE  permettait la délivrance du titre de DPLG ( diplômé par le gouvernement) pour l’architecte jusqu'en 2007 et pour le paysagiste jusqu'en 2019.|
|TATE|Travaux d'ateliers|HTYP10006|_(anciens Travaux d'étudiants)_ Productions d'étudiants et/ou d'enseignants au sein d'un atelier/cours/workshop|

### Ancienne liste des types de document (Travaux étudiants)

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

## Nouvelles règles de catalogage des travaux d'étudiants :

* 099$t = Travaux d'étudiants (`TE`)
* 029 _OBLIGATOIRE_ :
  * Indicateurs = `__`
  * $a = `FR`
  * $m = `{AAAA}_{code du type de travaux d'étudiant}_{code de l'école}_{biblionumber}`
    * Exemple : `2023_PFE_MLVL_123456`
    * __Dans le cas d'une reproduction (ex : version scannée d'une version papier), mettre le biblionumber du document original__
* 328 _Obligatoire_ :
  * Indicateurs = `_0`
  * $b = `{libellé du type de travaux d'étudiant}`
  * $c = `Architecture` (ou autres, le rétrospectif se fera sur `Architecture` uniquement)
  * __$e__ = `{Nom de l'école (comme en 214$c)}`
  * __$d__ = `{Année}`
  * __Le $e est avant le $d__

_Les documents (peu nombreux) provenant du Sudoc ne sont actuellement pas pris en compte dans ce nouveau procédé lors de l'import de leur données_

## Rechercher sur les types de travaux d'étudiants

* Pour rechercher dans Koha :
  * Via son code, rechercher dans l'index `diss` la forme suivante `*_{code}_*`
    * Exemple : `renard diss:*_PFE_*`
  * Via son libellé, rechercher dans l'index `diss` le nom ou le sigle s'il apparaît entre parenthèse dans le libellé
    * Exemples : `renard diss:Mastère` ou `renard diss:PFE`
  * Via l'onglet `Types de travaux d'étudiants` dans la recherche avancée
  * _Temporaire : tant que tous les types de documents n'ont pas été traité, rechercher `typedoc:{code}` pour retrouver ces cas-là_
* Pour rechercher dans Bokeh :
  * Dans le menu de recherche avancée, utiliser le champ `Types de travaux d'étudiants` situé sous les types de documents.
    * L'utilisation de ce champ restreint forcément la liste de résultat à uniquement des documents contenant le type de docuemnt `Travaux d'étudiant`
  * Effectuer en premier lieu une recherche, puis filtrer les résultats à partir de la liste des filtres à gauche de la liste des résultats grâce au filtre `Types de travaux d'étudiants`

## Liste des autres fichiers de documentation

* [Demandes à effectuer auprès des prestataires](./docs/demandes_prestataires.md)
* [Opérations à effectuer dans les différents logiciels du SID](./docs/operations_logiciels.md)
* [Spécifications du traitement rétrospectif](./docs/specs_traitement_retro.md)
* [Actions à effectuer après le chantier](./docs/post_chantier.md)
* [Informations sur le traitement](./docs/infos_traitement.md)
