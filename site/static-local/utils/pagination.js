/*jslint browser: true*/
/*global $*/
var pagination = (function () {
    "use strict";

    function replaceUrlParam(paramName, paramValue) {
        var
            url = window.location.href,
            pattern = new RegExp('\\b(' + paramName + '=).*?(&|$)');
        if (url.search(pattern) >= 0) {
            return url.replace(pattern, '$1' + paramValue + '$2');
        }
        return url + (url.indexOf('?') > 0 ? '&' : '?') + paramName + '=' + paramValue;
    }

    return {

        init: function () {
            $('div.pagination')
                .children('span.page-links')
                .find('a')
                .each(function (index, element) {
                    var
                        $a,
                        page;
                    $a = $(element);
                    page = $a.data('page');
                    $a.attr('href', replaceUrlParam('page', page));
                });
        }
    };
}());
