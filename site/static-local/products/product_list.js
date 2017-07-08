/*jslint browser: true*/
/*global $, jQuery, document, mhajax, alert */
var product_list = (function () {
    'use strict';

    var basket_restapi_url;

    function callback_onAddToBasket(event) {
        var
            $btn,
            product_id,
            jsonified;

        $btn = $(event.delegateTarget);
        product_id = $btn.data('product-id');
        if (!product_id) {
            alert("no product_id");
        }
        jsonified =
            '{"product": '
            + product_id +
            ', "quantity": 1, "comment": "" }';

        mhajax.post(basket_restapi_url, jsonified)
            .done(function () {
                $btn.attr("disabled", true);
            });
    }

    function syncWithBasket() {
        mhajax.get_json(basket_restapi_url)
            .done(function (data) {
                $('.btn-product-to-basket').each(function (index, element) {
                    var
                        $btn,
                        product_id,
                        should_disable;

                    $btn = $(element);
                    product_id = $btn.data('product-id');
                    should_disable = data.some(function (basketsale) {
                        return product_id === basketsale.product;
                    });
                    $btn.attr("disabled", should_disable);
                });
            });
    }

    function callback_onPaginationSubmit(event) {
        var
            $a,
            page,
            $form;

        $a = $(event.delegateTarget);
        page = $a.data('page');
        $form = $('#form-pagination');
        $form.find('input[name="page"]').val(page);
        $form.submit();
    }

    return {
        init: function (restapi_url) {
            basket_restapi_url = restapi_url;
            syncWithBasket();
            $('.btn-product-to-basket').click(callback_onAddToBasket);
            $('#form-pagination')
                .find('span.page-links')
                .children('a')
                .click(callback_onPaginationSubmit);
        }
    };
}());
