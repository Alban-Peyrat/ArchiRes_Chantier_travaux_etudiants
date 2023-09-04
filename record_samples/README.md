# Informations sur les documents de test (record_sample)

_Permet de tester [`traitement_retro.py`](../traitement_retro.py)_

* 187601 : typedoc TE
* 373225 : typedoc MEME
* 496806 : typedoc MHMONP
* 316762 : typedoc MEMU
* 69805 : typedoc MES
* 104362 : typedoc PFE
* 355828 : typedoc THES
* 38146 : typedoc TPFE
* 147575 : une 214$d
* 46152 : aucune 210/4 $d
* 47638 : deux 214$d
* 141444 : aucune date en 214$d
* 296096 : aucune 214$d mais une 210$d
* 206638 : aucune 214$d mais plusieurs 210$d
* 181337 : aucune 214$d et aucune date en 210$d
* 189257 : aucun exemplaire
* 495695 : trois exemplaires de différentes écoles
* 193351 : un exemplaire d'une ancienne école
* 187725 : deux exemplaires dont le plus vieux est d'une ancienne école
* 514591 : deux 328
* 118074 : déjà une 328$b
* 171164 : 328$a : `^[^:]* : [^:]* : [^:]* : [^:]* : \d*$`
* 116124 : 328$a : `^[^:]* : [^:]* : [^:]* : \d*$`
* 95071 : 328$a : `^[^:]* : [^:]* : \d*$`
* 10106 : 328$a : `^[^/]* / [^,]*, \d*$`
* 516748 : 328$a : `^[^:]*:[^:]*:\d*$`
* 116581 : 328$a : `^[^/]*/[^,]*,\d*$`
* 458269 : 328$a : `^[^:]*:[^:]*:[^:]*:\d*$`
* 183474 : 328$a : `^[^\.]*\. [^\.]*\. [^\.]*\. \d*$`
* 183215 : 328$a : `^[^\.]*\. [^\.]*\. \d*$`
* 499434 : 328$a : `^[^-]* - [^,]*, \d*$`
* 503413 : 328$a : `^\s*Travail personnel de fin d['|’]études.*`
* 493504 : 328$a : `^\s*Travaux de fin d['|’]études.*`
* 238437 : 328$a : `^\s*Projet\s*de fin d['|’]études.*`
* 139810 : 328$a : `^\s*M[é|e]moire.*`
* 407763 : 328$a : `^\s*Mast[e|è]r.*`
* 415256 : 328$a : `^\s*MES.*`
* 444603 : 328$a : `^\s*PFE.*`
* 424408 : 328$a : `^\s*TPFE.*`
* 515369 : 328$a : `^\s*HMONP.*`
* 236262 : 328$a : `^\s*DEA.*`
* 240352 : 328$a : `^\s*DESS.*`
* 374970 : 328$a : `^\s*DPEA.*`
* 173316 : 328$a : `^[^:]*: Th[è|e]se.*`
* 118157 : 328 $a : `^\s*\(?Th[è|e]se.*`
* 320052 : 328$a : `^\s*\(?Th\..*`
* 438757 : 328$a : `^\s*Doctorat.*`
* 194293 : 328$a : `^\s*M[é|e]m\..*`
* 494676 : 328$a : `^\s*Travail personnel d'étude et de recherche en paysage.*`
* 125306 : 328$a hors regex
* 147576 : un 214$c
* 147463 : aucune 210/4 $c
* 147499 : deux 214$c
* 147509 : aucun 214$c mais un 210$c
* 147560 : aucun 214$c mais plusieurs 210$c

# Informations sur les documents de test (record_sample2)

_Permet de tester [`traitement_retro_for_errors.py`](../traitement_retro_for_errors.py)_

* 187601 : typedoc TE
* 373225 : typedoc MEME
* 496806 : typedoc MHMONP
* 316762 : typedoc MEMU
* 69805 : typedoc MES
* 104362 : typedoc PFE
* 355828 : typedoc THES
* 38146 : typedoc TPFE
* 1733169998 : no typedoc
* 1733169999999 : mauvais typedoc
* 147575 : une 214$d
* _obsolète_ 46152 : aucune 210/4 $d
* 47638 : deux 214$d
* _obsolète_ 141444 : aucune date en 214$d
* 296096 : aucune 214$d mais une 210$d
* 206638 : aucune 214$d mais plusieurs 210$d
* _obsolète_ 181337 : aucune 214$d et aucune date en 210$d
* 3663 : aucune 214$d ni 210$d mais une date de publication en 100$a
* 45545 : aucune date en 214$d, pas de 210, aps de date de publication en 100$a mais une date en 214$a comprise entre 1900 et 2050
* 45546 : pas de 214, aucune date en 210$d, pas de date de publication en 100$a mais une date en 210$a comprise entre 1900 et 2050
* 455469999 : pas de 214, aucune date en 210$d, pas de date de publication en 100$a mais une date en 210$a inférieure à 1900
* 455469998 : pas de 214, aucune date en 210$d, pas de date de publication en 100$a mais une date en 210$a supérieure à 2050
* 48611 : pas de date en 214$d, pas de 210, pas de date de publication en 100$a, pas de date en 214 mais une date de création en 100$a
* 65812 : pas de date en 214$d, pas de 210, pas de 100$a, pas de date en 214
* _obsolète_ 189257 : aucun exemplaire
* 495695 : trois exemplaires de différentes écoles
* 193351 : un exemplaire d'une ancienne école
* 187725 : deux exemplaires dont le plus vieux est d'une ancienne école
* 20404 : aucun exemplaire mais une ville en 214$c
* 24864 : aucun exemplaire mais un terme spécifique en 214$c
* 24865 : aucun exemplaire, pas de ville ou terme spécifique en 214$c mais un terme spécifique en 210$c
* 37612 : aucun exemplaire, pas de ville ou terme spécifique en 214$c mais une ville en 210$c
* 37618 : aucun exemplaire, pas de ville ou terme spécifique en 210/4$c mais une ville en 214$a
* 37621 : aucun exemplaire, pas de ville ou terme spécifique en 210/4$c, pas de ville en 214$a mais une ville en 210$a
* 37623 : aucun exemplaire, pas de ville ou terme spécifique en 210/4$c, pas de ville en 210/4$a mais une ville en 710$a
* 37625 : aucun exemplaire, pas de ville ou terme spécifique en 210/4$c, pas de ville en 210/4$a mais un terme spécifique en 710$a
* 37629 : aucun exemplaire, pas de ville ou terme spécifique en 210/4$c, pas de ville en 210/4$a, pas de ville ou terme spécifique en 710$a mais une ville en 711$a
* 37630 : aucun exemplaire, pas de ville ou terme spécifique en 210/4$c, pas de ville en 210/4$a, pas de ville ou terme spécifique en 710$a mais un terme spécifique en 711$a
* 37632 : aucun exemplaire, pas de ville ou terme spécifique en 210/4$c, pas de ville en 210/4$a, pas de ville ou terme spécifique en 710/1$a mais une ville en 712$a
* 37638 : aucun exemplaire, pas de ville ou terme spécifique en 210/4$c, pas de ville en 210/4$a, pas de ville ou terme spécifique en 710/1$a mais un terme spécifique en 712$a
* 3763099998 : aucun exemplaire, pas de ville ou terme spécifique en 210/4$c, pas de ville en 210/4$a, pas de ville ou terme spécifique en 710/1/2$a
* 514591 : deux 328
* 118074 : déjà une 328$b
* 171164 : 328$a : `^[^:]* : [^:]* : [^:]* : [^:]* : \d*$`
* 116124 : 328$a : `^[^:]* : [^:]* : [^:]* : \d*$`
* 95071 : 328$a : `^[^:]* : [^:]* : \d*$`
* 10106 : 328$a : `^[^/]* / [^,]*, \d*$`
* 516748 : 328$a : `^[^:]*:[^:]*:\d*$`
* 116581 : 328$a : `^[^/]*/[^,]*,\d*$`
* 458269 : 328$a : `^[^:]*:[^:]*:[^:]*:\d*$`
* 183474 : 328$a : `^[^\.]*\. [^\.]*\. [^\.]*\. \d*$`
* 183215 : 328$a : `^[^\.]*\. [^\.]*\. \d*$`
* 499434 : 328$a : `^[^-]* - [^,]*, \d*$`
* 503413 : 328$a : `^\s*Travail personnel de fin d['|’]études.*`
* 493504 : 328$a : `^\s*Travaux de fin d['|’]études.*`
* 238437 : 328$a : `^\s*Projet\s*de fin d['|’]études.*`
* 139810 : 328$a : `^\s*M[é|e]moire.*`
* 407763 : 328$a : `^\s*Mast[e|è]r.*`
* 415256 : 328$a : `^\s*MES.*`
* 444603 : 328$a : `^\s*PFE.*`
* 424408 : 328$a : `^\s*TPFE.*`
* 515369 : 328$a : `^\s*HMONP.*`
* 236262 : 328$a : `^\s*DEA.*`
* 240352 : 328$a : `^\s*DESS.*`
* 374970 : 328$a : `^\s*DPEA.*`
* 173316 : 328$a : `^[^:]*: Th[è|e]se.*`
* 118157 : 328 $a : `^\s*\(?Th[è|e]se.*`
* 320052 : 328$a : `^\s*\(?Th\..*`
* 438757 : 328$a : `^\s*Doctorat.*`
* 194293 : 328$a : `^\s*M[é|e]m\..*`
* 494676 : 328$a : `^\s*Travail personnel d'étude et de recherche en paysage.*`
* 125306 : 328$a hors regex
* 147576 : un 214$c
* _obsolète_ 147463 : aucune 210/4 $c
* 147499 : deux 214$c
* 147509 : aucun 214$c mais un 210$c
* 147560 : aucun 214$c mais plusieurs 210$c
* 10138 : aucun 210/4$c, date entre 1985 et 2005
* 32548 : aucun 210/4$c, date avant 1985
* 68254 : aucun 210/4$c, date après 2006