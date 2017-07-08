/*jslint browser: true*/
/*global $, jQuery, document, mhajax*/
var modal_field_edit = (function () {
    "use strict";

    var
        $modal,
        $title,
        $field_value,
        //
        name_of_field,
        restapi_patch_url,
        //
        callback_onPatchSuccess;

    function callback_onSave() {
        var jsonified =
            '{"' + name_of_field + '": "' + $field_value.val() + '"}';
        mhajax.patch(restapi_patch_url, jsonified)
            .done(function (data) {
                callback_onPatchSuccess(data[name_of_field]);
                $modal.modal('hide');
            });
    }

    return {

        init: function (onPatchSuccess) {
            callback_onPatchSuccess = onPatchSuccess;
            $modal = $(".modal-field-edit");
            $title = $modal.find('.title-field-name');
            $field_value = $modal.find('.field-value');
            $modal.find('.btn-save').click(callback_onSave);
        },

        show: function (field_name, field_value, patch_url) {
            name_of_field = field_name;
            restapi_patch_url = patch_url;
            $title.text(field_name);
            $field_value.val(field_value);
            $modal.modal('show');
        }
    };
}());
