/*jslint browser: true*/
/*global $, mhajax */
var basketsale_list = (function () {
    'use strict';

    var basket_restapi_url;

    function updateSellerBlockHeading($seller_block) {
        var
            est_pickup_time = 0,
            $items = $seller_block.find('.list-group').children('.list-group-item');

        $items.each(
            function (index, element) {
                var item_preparation_time = $(element).data('preparation-time');
                if (est_pickup_time < item_preparation_time) {
                    est_pickup_time = item_preparation_time;
                }
            }
        );

        $seller_block.find('span.basketsales-count').text($items.length);
        $seller_block.find('span.est-pickup-time').text(est_pickup_time);
    }

    function checkValueDifference($item) {
        var
            quantity_change,
            comment_change;

        quantity_change =
            Number($item.data('saved-quantity'))
            !==
            Number($item.find('input[name="quantity"]').val());
        comment_change =
            $item.data('saved-comment')
            !==
            $item.find('input[name="comment"]').val();

        $item.find('.row-quantity').toggleClass('bg-warning', quantity_change);
        $item.find('.row-comment').toggleClass('bg-warning', comment_change);
        $item.find('.btn-update-basketsale')
            .toggleClass("hidden", !(quantity_change || comment_change));
    }

    function checkBasketEmptyVisibility() {
        if (0 === $('.container-fluid').children('.seller-block').length) {
            $('.basket-empty').show();
        } else {
            $('.basket-empty').hide();
        }
    }

    function callback_onUpdate(event) {
        var
            $item,
            quantity_val,
            comment_val,
            basketsale_id,
            jsonified,
            url;

        $item = $(event.delegateTarget).closest('.list-group-item');
        quantity_val = $item.find('input[name="quantity"]').val();
        comment_val = $item.find('input[name="comment"]').val();
        basketsale_id = $item.data('basketsale-id');

        jsonified = ['{', '"quantity":', quantity_val, ',',
            '"comment":"', comment_val, '"}'].join('');

        url = [basket_restapi_url, basketsale_id, '/'].join('');
        mhajax.patch(url, jsonified)
            .done(function (data) {
                $item.data('saved-quantity', data.quantity);
                $item.data('saved-comment', data.comment);
                checkValueDifference($item);
            });
    }

    function callback_onDelete(event) {
        var
            $itemdiv,
            basketsale_id,
            url;

        $itemdiv = $(event.delegateTarget).closest('.list-group-item');
        basketsale_id = $itemdiv.data('basketsale-id');

        url = [basket_restapi_url, basketsale_id, '/'].join('');
        mhajax.Delete(url)
            .done(function () {
                var
                    $itemparent = $itemdiv.parent('.list-group'),
                    $seller_block = $itemparent.closest('.seller-block');
                $itemdiv.remove();
                if (0 === $itemparent.children('.list-group-item').length) {
                    // that was the last sale from this Seller
                    // we can remove the Seller block as well
                    $seller_block.remove();
                } else {
                    updateSellerBlockHeading($seller_block);
                }
                checkBasketEmptyVisibility();
            });
    }

    function callback_onSomeChange(event) {
        var $item = $(event.delegateTarget).closest('.list-group-item');

        checkValueDifference($item);
    }

    return {
        init: function (restapi_url) {
            basket_restapi_url = restapi_url;
            checkBasketEmptyVisibility();
            $('.list-group-item').each(function (index, element) {
                checkValueDifference($(element));
            });
            $('.btn-update-basketsale').click(callback_onUpdate);
            $('.btn-delete-basketsale').click(callback_onDelete);
            $('input[name="quantity"]').change(callback_onSomeChange);
            $('input[name="comment"]').change(callback_onSomeChange).keyup(callback_onSomeChange);
            $('.seller-block').each(
                function (index, element) {
                    updateSellerBlockHeading($(element));
                }
            );
        }
    };
}());
