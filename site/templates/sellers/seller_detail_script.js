/*jslint browser: true*/
/*global $, jQuery, document, mhajax, modal_field_edit, seller_detail*/
(function () {
    "use strict";

    var seller = {
        editable: "{% if object.user.id == user.id %}yes{% endif %}",
        fields: [
            {
                name: "info",
                value: "{{ object.info }}"
            },
            {
                name: "address",
                value: "{{ object.address }}"
            },
            {
                name: "presentation_name",
                value: "{{ object.presentation_name }}"
            },
            {
                name: "administrative_name",
                value: "{{ object.administrative_name }}"
            }
        ]
    };
    $(document).data('seller', seller);
    $(document).data('url_restapi', "{% url 'restapi:seller-detail' object.id %}");
    seller_detail.ready();
}());
