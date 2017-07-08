/*jslint browser: true*/
/*global $, jQuery, document, mhajax, modal_field_edit*/
var seller_detail = (function () {
    'use strict';

    var $edited_field_panel;

    function callback_editBegin(event) {
        $edited_field_panel =
            $(event.delegateTarget).closest('.field-panel');

        modal_field_edit.show(
            $edited_field_panel.find('span.field-name').text(),
            $edited_field_panel.find('p.field-value').text(),
            $(document).data('url_restapi')
        );
    }

    function callback_editSuccess(newValue) {
        $edited_field_panel
            .find('p.field-value')
            .text(newValue);
    }

    function populateFields() {
        var
            seller = $(document).data('seller'),
            $holder = $('#seller-fields'),
            $template = $holder.children('div.field-panel.template');

        if (seller.editable) {
            $template
                .find('span.field-edit')
                .children('a')
                .click(callback_editBegin);
        } else {
            $template
                .find('span.field-edit')
                .remove();
        }

        seller.fields.forEach(function (field) {
            var $cloned =
                $template
                .clone(true, true)
                .appendTo($holder)
                .removeClass('template')
                .removeClass('hidden');
            $cloned
                .find('span.field-name')
                .text(field.name);
            $cloned
                .find('p.field-value')
                .text(field.value);
        });
    }

    return {
        ready: function () {
            populateFields();
            modal_field_edit.init(callback_editSuccess);
        }
    };
}());
