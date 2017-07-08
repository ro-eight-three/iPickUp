/*jslint browser: true*/
/*global $, jQuery, document, alert, console */
var mhajax = (function () {
    "use strict";

    var is_setup_done = false;

    function getCookie(name) {
        var
            i,
            cookie,
            cookies,
            cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            cookies = document.cookie.split(';');
            for (i = 0; i < cookies.length; i += 1) {
                cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    function setupCsrf() {

        if (!is_setup_done) {
            var csrftoken = getCookie('csrftoken');

            $(document).ajaxError(function (xhr, error) {
                console.debug(xhr);
                console.debug(error);
                alert("Ajax error! error dumped on console");
            });

            $.ajaxSetup({
                beforeSend: function (xhr, settings) {
                    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", csrftoken);
                    }
                }
            });
            is_setup_done = true;
        }
    }

    return {
        patch: function (url, data) {
            setupCsrf();
            return $.ajax({
                type: "PATCH",
                url: url,
                dataType: "json",
                contentType: "application/json",
                data: data
            });
        },

        post: function (url, data) {
            setupCsrf();
            return $.ajax({
                type: "POST",
                url: url,
                dataType: "json",
                contentType: "application/json",
                data: data
            });
        },

        Delete: function (url) {
            setupCsrf();
            return $.ajax({
                type: "DELETE",
                url: url
            });
        },

        load_url_into: function (url, jqelem) {
            setupCsrf();
            return jqelem.load(url);
        },

        get_json: function (url) {
            setupCsrf();
            return $.ajax({
                type: "GET",
                url: url,
                dataType: "json"
            });
        }
    };
}());
