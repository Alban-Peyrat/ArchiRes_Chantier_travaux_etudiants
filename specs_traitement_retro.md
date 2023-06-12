# Spécifications du traitement rétrospectif

* Récupérer le libellé correspondant au code présent en 099$t à l'aide du mapping
* Générer une 029 :
  * Indicateurs = `__`
  * $a = `FR`
  * $m = `{214$d}_{099$t}_{995$b}_{001}`
    * Prendre le 995 avec le $5 le plus ancien
    * Si le 995 choisi a un $8 IN ["DEFS", "SEIN", "TOLB", "PVDM", "VILM"], utiliser la valeur du 995$8 plutôt que le 995$b
    * Pour le 214$d :
      * Ne conserver que la première chaîne de caractère composée de 4 chiffres successifs
      * Si plusieurs 214$d, prendre celui avec la valeur la plus ancienne
      * Si aucun 214$d ne correspond à ces critères, prendre le 210$d et appliquer la même logique
      * Si après la 210, toujours rien : ne pas traiter
* Générer une 328 :
  * SAUF SI :
    * une 328$b est déjà présente sur la notice
    * une 328$a matchant l'une des expressions régulières suivantes se trouve dans la notice :
      * `^[^:]* : [^:]* : [^:]* : [^:]* : \d*$`
      * `^[^:]* : [^:]* : [^:]* : \d*$`
      * `^[^:]* : [^:]* : \d*$`
      * `^[^/]* / [^,]*, \d*$`
      * `^[^:]*:[^:]*:\d*$`
      * `^[^/]*/[^,]*,\d*$`
      * `^[^:]*:[^:]*:[^:]*:\d*$`
      * `^[^\.]*\. [^\.]*\. [^\.]*\. \d*$`
      * `^[^\.]*\. [^\.]*\. \d*$`
      * `^[^-]* - [^,]*, \d*$`
      * `^\s*Travail personnel de fin d['|’]études.*`
      * `^\s*Travaux de fin d['|’]études.*`
      * `^\s*Projet\s*de fin d['|’]études.*`
      * `^\s*M[é|e]moire.*`
      * `^\s*Mast[e|è]r.*`
      * `^\s*MES.*`
      * `^\s*PFE.*`
      * `^\s*TPFE.*`
      * `^\s*HMONP.*`
      * `^\s*DEA.*`
      * `^\s*DESS.*`
      * `^\s*DPEA.*`
      * `^[^:]*: Th[è|e]se.*`
      * `^\s*\(?Th[è|e]se.*`
      * `^\s*\(?Th\..*`
      * `^\s*Doctorat.*`
      * `^\s*M[é|e]m\..*`
      * `^\s*Travail personnel d'étude et de recherche en paysage.*`
  * Indicateurs : `_0`
  * $b = `{libellé correspondant au code présent en 099$t à l'aide du mapping}`
  * $c = `Architecture`
  * $e = `{214$c}`
  * $d = `{214$d}`
    * Pour la 214$d, même procédé que pour la 029
    * Pour la 214$c, prendre le premier $c
    * Si aucune 214 n'a de valeur en $c, prendre le premier $c avec une valeur dans les 210
    * si après la 210, toujours rien : ne pas traiter
* Modifier la 099$t pour forcer la valeur `TE`