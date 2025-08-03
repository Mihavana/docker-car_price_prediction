$(document).ready(function() {
    $('#model').select2({
        // Laisser `tags` à `false` ou ne pas le spécifier pour désactiver la saisie libre.
        placeholder: "Sélectionner un modèle",
        allowClear: true // Optionnel : permet de vider le champ
    });
});