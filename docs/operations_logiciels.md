# Opérations à effectuer dans les différents logiciels du SID

# Dans Koha

* Supprimer de la valeur autorisée `typedoc` les valeurs : MEME, MHMONP, MEMU, MES, PFE, THES, TPFE
  * [Voir #MT40622 sur pourqoi pas `ccode`](https://suivi.biblibre.com/view.php?id=40622)
* Créer la valeur autorisée `diss` avec comme valeur l'ensemble des codes voulus entre `"*_{code}_*"`
  * Exemple : `"*_PFE_*"` : Projet de fin d'étude
* Dans la préférence système `AdvancedSearchTypes`, rajouter `diss` entre `typedoc` et `coll`
* Dans la préférence système `IntranetUserJS`, rajouter `$("#advsearch-tab-diss a:contains('Autre chose')").text("Types de travaux d'étudiants");` dans le `$(document).ready()` du début

## Dans Bokeh

* Création d'une nouvelle facette dynamique (Cosmogramme) sur la 029$v :
  * Libellé : Types de travaux d'étudiants
  * Libellé dans les résultats de recherche : Types de travaux d'étudiants
  * Règles :
    * Zone : 029
    * Libellé : $v
    * Position du libellé : 1
    * Longueur du libellé : 0
* Ajouter la facette dynamique dans les filtres possibles des résultats de recherche
  * __Sur tous les profils__
  * _Profil → Propriétés des modules → Configuration du résultat de recherche → Facettes à afficher_
  * Placer _Types de travaux d'étudiants_ entre _Types de documents_ et _Bibliothèque_
* Retirer les codes de types de documents non utilisés du profil de données `Unimarc Koha` dans le Cosmogramme
* Modifier dans le sous menu _En ligne → Bibliothèque Numérique ArchiRès_ :
  * Le lien pour les PFE : `/recherche/simple/expressionRecherche/*/multifacets/HTYP100{XX}/tri/annee%20desc,%20alpha_titre%20asc`
  * Le lien pour les TPFE : `/recherche/simple/expressionRecherche/*/multifacets/HTYP100{XX}/tri/annee%20desc,%20alpha_titre%20asc`
  * Le lien pour les mémoires (= MES) : renommer en `Accès aux mémoires de master (MES)` + `/recherche/simple/expressionRecherche/*/multifacets/HTYP100{XX}/tri/annee%20desc,%20alpha_titre%20asc`
  * Ajouter un lien vers un site pour les HMONP : `Accès aux mémoires HMONP` : `/recherche/simple/expressionRecherche/*/multifacets/HTYP100{XX}/tri/annee%20desc,%20alpha_titre%20asc`

## Dans le Git pour Bokeh

* _Recherche avancée : visuel_ : Modifier dans `ensa.css` :
  * le sélecteur `.form-group.container-fluid.no-gutters.py-1.wrapper_zendafi_form_advancedsearch_custommultifacetstypedoc.default_form_wrapper_zendafi_form_advancedsearch_custommultifacetstypedoc label.multi-element-label.col-form-label.col-form-label-sm` pour rajouter un autre sélecteur (avec une virgule) :
    * `.form-group.container-fluid.no-gutters.py-1.wrapper_zendafi_form_advancedsearch_custommultifacetstypethesis.default_form_wrapper_zendafi_form_advancedsearch_custommultifacetstypethesis label.multi-element-label.col-form-label.col-form-label-sm`
    * _Permet d'afficher les options sur 3 colonnes_
  * le sélecteur `.form-group.container-fluid.no-gutters.py-1.wrapper_zendafi_form_advancedsearch_custommultifacetstypedoc.default_form_wrapper_zendafi_form_advancedsearch_custommultifacetstypedoc .col-sm label + br` pour rajouter un autre sélecteur (avec une virgule) :
    * `.form-group.container-fluid.no-gutters.py-1.wrapper_zendafi_form_advancedsearch_custommultifacetstypethesis.default_form_wrapper_zendafi_form_advancedsearch_custommultifacetstypethesis .col-sm label + br`
    * _Permet d'afficher les options des 3 colonnes sur la même lignes_
  * Le sélecteur `.form-group.container-fluid.no-gutters.py-1.wrapper_zendafi_form_advancedsearch_rechthesaurussuj.default_form_wrapper_zendafi_form_advancedsearch_rechthesaurussuj , .form-group.container-fluid.no-gutters.py-1.wrapper_zendafi_form_advancedsearch_thesaurus.default_form_wrapper_zendafi_form_advancedsearch_thesaurus , .form-group.container-fluid.no-gutters.py-1.wrapper_zendafi_form_advancedsearch_titr.default_form_wrapper_zendafi_form_advancedsearch_titr` (sur deux lignes, historiquement 730+731) pour rajouter un autre sélecteur (avec une virgule) :
    * `.form-group.container-fluid.no-gutters.py-1.wrapper_zendafi_form_advancedsearch_custommultifacetstypethesis.default_form_wrapper_zendafi_form_advancedsearch_custommultifacetstypethesis`
    * _Pour afficher un fonds gris et mieux distinguer les types de documents des types de travaux étudiants_
* _Recherche avancée_ Rajouter après les types de documents les types de travaux d'étudiants et ne conserver que la facette `T38` pour le libellé `Travaux étudiants` des types de document :
  * Supposément, ce code là fait qui est demandé pour les types de travaux d'étudiants (à compléter selon le mapping + code des facettes) *voir `formulaire_travaux_etudiants.php` dans Archires_Structure_Technique + explroateur de fichier en base test, appliqué sur le profil page d'accueil v2* :

``` PHP
  // Partie du formulaire consacrée aux types de travaux d'étudiants
  ->addElement('multiCheckbox', 'custom_multifacets_typethesis',
               ['label' => $form->_('Types de travaux d\'étudiants'),
                'onkeypress' => 'if (event.keyCode == 13) {$(this.form).submit();return false; }',
                'multiOptions' => ['T38' => 'Tous',
                                    'HTYP100' => 'CCJP (Concepteur et créateur de jardin dans le paysage)',
                                    'HTYP100' => 'CEAA (Certificat d\'études approfondies en architecture)',
                                    'HTYP100' => 'CESP (Certificat d\'études supérieures paysagères)',
                                    'HTYP100' => 'DPEA (Diplôme propre aux ENSA)',
                                    'HTYP100' => 'DSA (Diplôme de spécialisation et d\'approfondissement)',
                                    'HTYP100' => 'Mastère',
                                    'HTYP10003' => 'Mémoire de master (MES)',
                                    'HTYP10008' => 'Mémoire HMONP (Habilitation à la maîtrise d\'œuvre en son nom propre)',
                                    'HTYP10007' => 'Mémoire universitaire',
                                    'HTYP10005' => 'PFE (Projet de fin d\'études)',
                                    'HTYP10004' => 'Rapport d\'études (Licence)',
                                    'HTYP10002' => 'Thèse',
                                    'HTYP10001' => 'TPFE (Travail personnel de fin d\'études)',
                                    'HTYP10006' => 'Travaux d\'ateliers'],'autocomplete'=>'off'])



// Pour la partie "ne conserver que la facette T38" :
//                                   'T38-T29-T32-T30-T31-T34-T39-T40' => 'Travaux d\'étudiants',
// Devient
                                   'T38' => 'Travaux d\'étudiants',
```

* _Affichage dans la liste des résultats_ Modifier la XSLT de la liste des résultats pour afficher entre les auteurs et l'éditeur le contenu du 029$v si la variable `typedoc` = `TE` et qu'une 029$v existe
  * Supposément, quelque chose comme ce code doit fonctionner :

``` XSLT
<!-- À mettre entre la section Auteurs (qui est commentée) et la section Editeur -->
<!-- ******** types de travaux étudiants *********** -->

<xsl:if test="($typedoc='TE' and marc:datafield[@tag=029]/marc:subfield[@code='v'])">
<dd><xsl:value-of select="marc:datafield[@tag=029]/marc:subfield[@code='v']"/></dd>
</xsl:if>
```

* _Affichage dans la notice_ Modifier la XSLT des notices pour remplacer le type de documents _Travaux étudiants_ en rouge dans la notice par les types de travaux d'étudiants si le type de documents est égal à `TE`
  * Supprimer également les lignes concernant les types de documents : MEME, MHMONP, MEMU, MES, PFE, THES, TPFE
  * Supposément, quelque chose comme ce code doit fonctionner :
  * _Fonctionne avec 1 029$v, notice de livre, 2 029 dont une seule avec $m (quelle que soit la position de la 029 avec le $v), une 029 sans $v_

``` XSLT
<!-- À supprimer (lignes ~4X) -->
<xsl:when test="$typedoc='MEME'"><xsl:text>Mémoire ENSA</xsl:text></xsl:when>
<xsl:when test="$typedoc='MEMU'"><xsl:text>Mémoire universitaire</xsl:text></xsl:when>
<xsl:when test="$typedoc='MES'"><xsl:text>MES</xsl:text></xsl:when>
<xsl:when test="$typedoc='MHMONP'"><xsl:text>Mémoire HMONP</xsl:text></xsl:when>
<xsl:when test="$typedoc='PFE'"><xsl:text>PFE</xsl:text></xsl:when>
<xsl:when test="$typedoc='THES'"><xsl:text>Thèse</xsl:text></xsl:when>
<xsl:when test="$typedoc='TPFE'"><xsl:text>TPFE</xsl:text></xsl:when>
<xsl:when test="$typedoc='TE'"><xsl:text>Travaux d'étudiants</xsl:text></xsl:when>

<!-- Rajouter avec les autres définitions de variables (ligne 25) -->
<xsl:variable name="diss"><xsl:value-of select="marc:datafield[@tag=029]/marc:subfield[@code='v']"/></xsl:variable>

<!-- Ajouter à la fin du xsl:choose sur $typedoc (~ligne 59) -->
<xsl:when test="($typedoc='TE' and string-length($diss) > 0)"><xsl:value-of select="$diss"/></xsl:when><!-- DOIT ÊTRE AVANT LE $typedoc = 'TE'-->
<xsl:when test="$typedoc='TE'"><xsl:text>Travaux d'étudiants</xsl:text></xsl:when>

```