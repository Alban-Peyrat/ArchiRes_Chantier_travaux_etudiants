# Demandes à effectuer auprès des prestataires

Chronologie obligatoire de certaines opérations :

1. Modification de _transform.yaml_ entre Koha-Bokeh
1. Création de la facette dynamique dans Bokeh
1. Import des notices dans Koha
1. Mises à jour d'Elastic Search dans Koha + réindexation des notices
1. ~~Import total dans Bokeh~~ _Passe dans l'import incrémentiel_
1. Ajout des identifiants des facettes dans le formulaire de recherche avancée (+ mettre en commentaires ceux qui n'ont pas encore été générés)

## Prestataire Koha

* _Affichage Koha_ Modifier la XSLT de la préférence système `XSLTDetailsDisplay` (`/home/koha/xslt/intranet/UNIMARCslim2intranetDetail.xsl`) pour afficher :
    * dans l'idéal, la même chose que la XSLT de Bokeh. Voilà une version qui ressemblerait plus à Koha :

``` XSLT
 <xsl:if test="marc:datafield[@tag=328]">
 <li>
    <strong>Note de thèse :</strong>
 <xsl:text> </xsl:text>
 <xsl:for-each select="marc:datafield[@tag=328]">
 <xsl:if test="marc:subfield[@code='z']">
 <xsl:value-of select="marc:subfield[@code='z']"/>
 <xsl:text> : </xsl:text>
</xsl:if>
<xsl:if test="marc:subfield[@code='a']">
 <xsl:value-of select="marc:subfield[@code='a']"/>
 <xsl:text> : </xsl:text>
</xsl:if>
<xsl:if test="marc:subfield[@code='b']">
 <xsl:value-of select="marc:subfield[@code='b']"/>
 <xsl:text> : </xsl:text>
</xsl:if>
<xsl:if test="marc:subfield[@code='c']">
 <xsl:value-of select="marc:subfield[@code='c']"/>
 <xsl:text> : </xsl:text>
</xsl:if>
<xsl:if test="marc:subfield[@code='e']">
 <xsl:value-of select="marc:subfield[@code='e']"/>
 <xsl:text> : </xsl:text>
</xsl:if>
<xsl:if test="marc:subfield[@code='d']">
 <xsl:value-of select="marc:subfield[@code='d']"/>
 <xsl:text>  </xsl:text>
</xsl:if>
 <xsl:choose><xsl:when test="position()=last()"><xsl:text>.</xsl:text></xsl:when><xsl:otherwise><xsl:text>; </xsl:text></xsl:otherwise></xsl:choose>
 </xsl:for-each>
 </li>
 </xsl:if>
```

* _Fonctionnel pour Bokeh_ Modifier le fichier _transform.yaml_ appliqué entre les exports Koha et l'import Bokeh pour :
  * Extraire en 029$w le code du type de travaux d'étudiant
  * Traduire le code du type de travaux d'étudiant en son libellé en 029$v
  * Supposément, ce code là fait qui est demandé (à compléter selon le mapping) :

``` Perl
---
# AR268 : isoler le type de travaux d'étudiants
# 1. Isoler le code en 029w
-
 condition : $f099t eq "TE" and $f029m=~/(?<=_)[^_]*(?=_)/ 
 forceupdate :
  $f029w : \&get_w_etud_code("$f029m")
-
 subs: >
    sub get_w_etud_code { my $string=shift; $string =~ /(?<=_)([^_]*)(?=_)/; $1; }
---
#2. Libelle du code (plusieurs regles au cas ou plusieurs 029)
condition : $f099t eq "TE" and $f029w eq 'CCJP'
forceupdate :
 $f029v : "CCJP (Concepteur et cr\x{00e9}ateur de jardin dans le paysage)"
---
condition : $f099t eq "TE" and $f029w eq 'CEAA'
forceupdate :
 $f029v : "CEAA (Certificat d'\x{00e9}tudes approfondies en architecture)"
---
condition : $f099t eq "TE" and $f029w eq 'CESP'
forceupdate :
 $f029v : "CESP (Certificat d'\x{00e9}tudes sup\x{00e9}rieures paysag\x{00e8}res)"
---
condition : $f099t eq "TE" and $f029w eq 'DPEA'
forceupdate :
 $f029v : "DPEA (Dipl\x{00f4}me propre aux ENSA)"
---
condition : $f099t eq "TE" and $f029w eq 'DSA'
forceupdate :
 $f029v : "DSA (Dipl\x{00f4}me de sp\x{00e9}cialisation et d'approfondissement)"
---
condition : $f099t eq "TE" and $f029w eq 'MASTERE'
forceupdate :
 $f029v : "Mast\x{00e8}re"
---
condition : $f099t eq "TE" and $f029w eq 'MES'
forceupdate :
 $f029v : "M\x{00e9}moire de master (MES)"
---
condition : $f099t eq "TE" and $f029w eq 'RAPL'
forceupdate :
 $f029v : "Rapport d'\x{00e9}tudes (Licence)"
---
condition : $f099t eq "TE" and $f029w eq 'MHMONP'
forceupdate :
 $f029v : "M\x{00e9}moire HMONP (Habilitation \x{00e0} la ma\x{00ee}trise d'\x{0153}uvre en son nom propre)"
---
condition : $f099t eq "TE" and $f029w eq 'MEMU'
forceupdate :
 $f029v : "M\x{00e9}moire universitaire"
---
condition : $f099t eq "TE" and $f029w eq 'PFE'
forceupdate :
 $f029v : "PFE (Projet de fin d'\x{00e9}tudes)"
---
condition : $f099t eq "TE" and $f029w eq 'THES'
forceupdate :
 $f029v : "Th\x{00e8}se"
---
condition : $f099t eq "TE" and $f029w eq 'TPFE'
forceupdate :
 $f029v : "TPFE (Travail personnel de fin d'\x{00e9}tudes)"
---
condition : $f099t eq "TE" and $f029w eq 'TATE'
forceupdate :
 $f029v : "Travaux d'ateliers"

```

* _Recherche dans Koha_ Rajouter le 029m dans `dissertation-information` et dans `identifier-standard` puis réindexer ElasticSearch
* _Recherche dans Koha_ Rajouter dans les index de recherches sélectionnables de la recherche avancée `dissertation-information` avec le libellé `Travaux d'étudiants (328, 029$m)`, entre _Titre propre_ et _Titres liés_
* _Traitement rétrospectif_ Quelle est la meilleure manière de modifier les 903XX notices ?
  * Sachant que les modifications templates ne fonctionneront probablement pas
  * Le téléchargement de notices dans le réservoir avec un matching sur le biblionumber + ne pas traiter les exemplaires ?
    * Quelle taille de lot recommandée ?
    * __Réponse__ : peut varier, mais pas plus de 1000 probablement
  * L'API svc/biblio/$biblio en GET puis POST ?
    * Faut-il mettre un intervalle entre les requêtes ?
    * __Réponse__ : risque d'être assez lent et de tomber dans les limites du protocole xeb
  * Une autre solution que je ne connais pas ?
    * __Réponse__ : import avec `bulkmarcimport`, probablement pas de limite de taille de lot
* _Passerelle Sudoc_ Modifier dans la passerelle Sudoc-Koha `items.yaml` pour changer la condition d'attribution du 995$r = `TE` de `la 099t égale PFE ou TPFE` à `la 099t égale TE`

``` Perl
# Ancienne version
-
 condition: $f099t=~/^(PFE|TPFE)$/ and defined $f995 #MT38450
 forceupdate:
  $f995r: TE
  $f995o: 3

# Nouvelle version
-
 condition: $f099t eq "TE" and defined $f995 #MT38450
 forceupdate:
  $f995r: TE
  $f995o: 3
```

* _Passerelle Sudoc_ Modifier dans la passerelle Sudoc-Koha `transformiso.yaml` pour changer la condition d'attribution du 099$t :
  * Remplacer dans l'attribution du 099$t = `THES` la valeur attribuée au 099$t par `TE`
  * Supprimer l'attribution du 099$t = `TPFE`
  * Supprimer l'attribution du 099$t = `PFE`
  * Ajouter une nouvelle attribution du 099$t pour la valeur `TE`

``` Perl
# À supprimer
-
 condition: ($ldr7 eq "m") and ($ldr6 eq "a") and $f930a=~/^(TPFE|TPFEpays)/
 forceupdatefirst:
  f099t: TPFE
-
 condition: ($ldr7 eq "m") and ($ldr6 eq "a") and $f930a=~/^(PFE)/
 forceupdatefirst:
  f099t: PFE
# - #MT38450
#  condition: ($ldr7 eq "m") and ($ldr6 eq "a") and $f930a=~/(MES|U MES)/
#  forceupdatefirst:
#   f099t: MES

# À modifier
# --- Ancienne valeur
-
 condition: ($ldr7 eq "m") and ($ldr6 eq "a") and defined $f029b
 forceupdatefirst:
  f099t: THES

# --- Nouvelle valeur
-
 condition: ($ldr7 eq "m") and ($ldr6 eq "a" or $ldr6 eq "l") and defined $f029b
 forceupdatefirst:
  f099t: TE
```

* _Passerelle Sudoc_ : rajouter le champ 029 aux champs protégés dans Koha
* _Passerelle Sudoc_ : Vérifier qu'aucun autre paramétrage n'est susceptible d'être impacté (je n'en ai pas vu d'autres)