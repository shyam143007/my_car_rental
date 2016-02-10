var app = angular.module("car_rental", ["ngRoute"]);

app.config(["$interpolateProvider", "$httpProvider", function (interpolateProvider, httpProvider) {
    interpolateProvider.startSymbol("{$").endSymbol("$}");
    httpProvider.defaults.xsrfCookieName = "csrftoken";
    httpProvider.defaults.xsrfHeaderName = "X-CSRFToken";
}]);

app.config(["$routeProvider", "$locationProvider", function (routeProvider, locationProvider) {
    routeProvider.when('/', {
        templateUrl: 'static/Car_RentalApp/partials/Main.html',
        controller: 'MainController',
        reloadOnSearch: false
    }).otherwise({ redirectTo: "/" });
    locationProvider.html5Mode(true);
}]);

app.directive("datepicker", function () {
    return {
        restrict: "A",
        link: function (scope, element, attrs) {

            element.datepicker({ minDate: 0 });

            scope.$watch("startDate", function (val) {
                if (val == undefined) return;

                var startDate = new Date(val);
                var endDate = new Date(scope.leavingDate);
                var dateDiff = startDate - endDate
                var newDate = new Date(val);
                newDate.setHours(0, 0, 0, 0);
                newDate.setDate(startDate.getDate() + 1);
                var ele = $("#drop-off-date").datepicker("option", "minDate", newDate);
                if (dateDiff > 0 || scope.leavingDate == undefined) {
                    scope.leavingDate = "{0}/{1}/{2}".format(newDate.getMonth().toString(), newDate.getDate().toString(), newDate.getYear().toString());
                }
            });
        }
    };
});

app.directive("myMaps", function () {
    return {
        template: "<div></div>",
        restrict: 'EC',
        replace: true,
        link: function (scope, element, attr) {
            scope.$watch('loc_address', function (location) {
                prepare_map(location.location.lat, location.location.lng, attr);
            });
        }
    }
});

//app.directive("carCarousel", function () {
//    return {
//        restrict: "E",
//        replace: true,
//        templateUrl: "static/Car_RentalApp/partials/car_carousel.html"
//    }
//});

function prepare_map(lat, lng, attr) {
    var lat_lng = new google.maps.LatLng(lat, lng);
    var map_options = get_map_options(lat_lng)
    var map = new google.maps.Map(document.getElementById(attr.id), map_options);
    marker = set_marker(lat_lng);
    marker.setMap(null);
    marker.setMap(map);
}

function set_marker(lat_lng) {
    var marker = new google.maps.Marker({
        position: lat_lng,
        draggable: true
    });
    return marker;
}

function get_map_options(lat_lng) {
    var map_options = {
        center: lat_lng,
        zoom: 8,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    }
    return map_options;
}

