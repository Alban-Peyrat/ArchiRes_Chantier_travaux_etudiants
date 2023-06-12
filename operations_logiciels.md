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
                'multiOptions' => ['' => 'Tous',
                                    'HTYP10001' => 'Mastère',
                                    'HTYP10002' => 'Mémoire ENSA',
                                    'HTYP10004' => 'Mémoire universitaire' ,
                                    'HTYP10005' => 'MES',
                                    'HTYP10003' => 'Mémoire HMONP',
                                    'HTYP10006' => 'PFE',
                                    'HTYP10007' => 'Thèse',
                                    'HTYP10008' => 'TPFE'],'autocomplete'=>'off'])



// Pour la partie "ne conserver que la facette T38" :
//                                   'T38-T29-T32-T30-T31-T34-T39-T40' => 'Travaux d\'étudiants',
// Devient
                                   'T38' => 'Travaux d\'étudiants',
```