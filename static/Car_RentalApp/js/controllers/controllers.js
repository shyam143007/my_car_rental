var map;
var carousel_interval;
app.controller("MainController", ["$scope", "$http", "$anchorScroll", "$location", "$interval", function (scope, http, anchorScroll, location, interval) {
    scope.logo = 'static/Car_RentalApp/Images/logo.gif';

    scope.gotoAnchor = function (anchorName) {
        location.hash(anchorName);
        anchorScroll();
        //slow_scroll(anchorName);
    }

    // car reservation section

    carousel_cars = ['static/Car_RentalApp/Images/car1.png', 'static/Car_RentalApp/Images/car2.png']
    scope.cars = carousel_cars;
    http.get('api_review/car/').success(function (response) {
        scope.registered_cars = response;
        scope.vehicles = response;
        scope.selected_vehicle = scope.vehicles[0];
    });
    scope.intervals = get_intervals();
    scope.startTime = scope.intervals[0];
    scope.leavingTime = scope.intervals[0];
    scope.ages = get_ages();
    scope.selected_age = scope.ages[0];
    scope.show_modal = function () {
        var validations_satisfied = basic_validations(scope);
        if (validations_satisfied == 0) {
            $('#checkoutModal').modal('show');
        }
        else {
            $("#car-select-form-msg").removeClass("hidden");
        }

    }
    scope.remove_alert = function (id) {
        $("#" + id).addClass("hidden");
    }
    scope.reserve_car = function () {
        //var validations_satisfied = basic_validations(scope);
        validations_satisfied = 0;
        person = {
            'first_name': scope.rsrv_firstName,
            'last_name': scope.rsrv_lastName,
            'phone': scope.rsrv_phone,
            'age': scope.selected_age.age,
            'email': scope.rsrv_emailAddress,
            'address': scope.rsrv_address,
            'city': scope.rsrv_city,
            'zip_code': scope.rsrv_zipCode
        }

        validations_satisfied = person_validations(person);
        if (validations_satisfied == 0) {
            car = scope.rsrv_car;
            http.post('/api_review/person/check_user/', data = person).success(function (response) {
                created_person = response;
                car_reservation(scope, http, created_person);
            }).error(function (response) {
                http.post('/api_review/person/', data = person).success(function (response) {
                    created_person = response;
                    car_reservation(scope, http, created_person)
                }).error(function (response) {
                    alert(response);
                });
            });
        }
        else {
            $("#checkout-form-msg").removeClass("hidden");
        }
    }
    scope.clear_values = function () {
        clear_personal_info(scope);
    }

    interval.cancel(carousel_interval);
    carousel_interval = interval(function () {
        var activeCar = $(".active-car");
        var inactiveCar = $(".inactive-car");
        activeCar.removeClass("active-car").addClass("inactive-car");
        inactiveCar.addClass("active-car").removeClass("inactive-car");
        //alert("interval");
    }, 4000);

    //news letter

    scope.sign_up_for_offers = function () {

    }

    // vehicles

    var previous_vehicle;
    scope.change_vehicle = function (new_vehicle) {
        if (new_vehicle == undefined || previous_vehicle == new_vehicle) return;
        scope.selected_vehicle = new_vehicle;
        previous_vehicle = new_vehicle;
    }
    scope.change_vehicle_with_arrows = function (direction) {
        var currentIndex;
        scope.disableUp = false;
        scope.disableDown = false;
        currentIndex = scope.vehicles.indexOf(scope.selected_vehicle);

        if (direction == 'up') {
            if (currentIndex == 0) {
                scope.disableUp = true;
            }
            else {
                scope.selected_vehicle = scope.vehicles[currentIndex - 1];
            }
        }
        else if (direction == 'down') {
            if (currentIndex == scope.vehicles.length - 1) {
                scope.disableDown = true;
            }
            else {
                scope.selected_vehicle = scope.vehicles[currentIndex + 1]
            }
        }
    }

    // contact us

    http.get('api_review/customer_care/').success(function (response) {
        scope.cc_technical_support = [];
        scope.cc_voice_support = [];
        angular.forEach(response, function (each_person, index) {
            if (each_person.staff_type == "VOICE SUPPORT") {
                scope.cc_voice_support.push(each_person);
            }
            else {
                scope.cc_technical_support.push(each_person);
            }
        });
    });
    scope.submit_feedback_message = function () {
        feedback_data = {
            'first_name': scope.fp_firstname,
            'last_name': scope.fp_lastname,
            'phone': scope.fp_telephone,
            'email': scope.fp_email,
            'message': scope.fp_message
        }
        http.post('/api_review/feedback/', data = feedback_data).success(function (response) {
            scope.fp_firstname = scope.fp_lastname = '';
            scope.fp_telephone = scope.fp_message = scope.fp_email = '';
            scope.message = "feedback";
            $('#confirmation').modal('show');
        }).error(function (response) {
            //alert("something went wrong...!");
        });
    }

    //locations

    scope.loc_locations = get_locations();
    scope.loc_address = scope.loc_locations[0];
}]);

function get_intervals() {
    intervals = [];
    time = 12 * 2;
    interval = 2; //1 for 1 hour, 2 for 1/2 hour and 4 for 15 mins.
    total_time = time * interval
    for (var i = 0; i < total_time; i++) {
        if (i / (12 * interval) >= 1) {
            date = "";
            hour = ~~(i / interval) - 12;
            if (hour == 0) {
                date += "12";
            }
            else {
                date += hour;
            }
            if (i % 2 == 0) {
                date += ":00";
            }
            else {
                date += ":30";
            }
            date += " PM";
            intervals.push({ val: date, display: date });
        }
        else {
            date = "";
            hour = ~~(i / interval);
            if (hour == 0) {
                date += "12";
            }
            else {
                date += hour;
            }
            if (i % 2 == 0) {
                date += ":00";
            }
            else {
                date += ":30"
            }
            date += " AM";
            intervals.push({ val: date, display: date });
        }
    }
    return intervals;
}

function get_ages() {
    ages = [];

    for (var i = 18; i <= 100; i++) {
        ages.push({ age: i, val: i });
    }

    return ages;
}

function get_locations() {
    locations = [];
    locations.push({ location: { lat: 17.385044, lng: 78.486671 }, name: "Hyderabad, Telangana" });
    locations.push({ location: { lat: 17.4611, lng: 78.5014 }, name: "Kharkhana, Telangana" });
    locations.push({ location: { lat: 17.4449, lng: 78.4694 }, name: "Begumpet, Telangana" });
    locations.push({ location: { lat: 17.4372, lng: 78.3444 }, name: "Gachibowli, Telangana" });
    locations.push({ location: { lat: 17.5030, lng: 78.5070 }, name: "Alwal, Telangana" });
    return locations;
}

function basic_validations(scope) {
    var error = 0;

    if (validateNotEmpty(scope.rsrv_car)) { return error = 1; }
    if (validateNotEmpty(scope.pickUpLocation)) { return error = 1; }
    if (validateNotEmpty(scope.droppingLocation)) { return error = 1; }
    if (validateNotEmpty(scope.startDate)) { return error = 1; }
    if (validateNotEmpty(scope.leavingDate)) { error = 1; }
    return error;
}

function person_validations(person) {
    var error = 0;

    // empty fields validation.
    if (validateNotEmpty(person['first_name'])) { return error = 1; }
    if (validateNotEmpty(person['last_name'])) { return error = 1; }
    if (validateNotEmpty(person['phone'])) { return error = 1; }
    if (validateNotEmpty(person['age'])) { return error = 1; }
    if (validateNotEmpty(person['email'])) { return error = 1; }
    if (validateNotEmpty(person['address'])) { return error = 1; }
    if (validateNotEmpty(person['city'])) { return error = 1; }
    if (validateNotEmpty(person['zip_code'])) { return error = 1; }



    return error;
}

function car_reservation(scope, http, created_person) {
    if (created_person != undefined) {
        pickUpTime = scope.startDate + " " + scope.startTime.display;
        droppingTime = scope.leavingDate + " " + scope.leavingTime.display;
        reserve_car = {
            'source': scope.pickUpLocation,
            'destination': scope.droppingLocation,
            'pick_up_time': pickUpTime,
            'dropping_time': droppingTime,
            'car': car.id,
            'person': created_person.email
        }
        http.post('/api_review/car_reservation/', data = reserve_car).success(function (response) {
            $('#checkoutModal').modal('hide');
            scope.rsrv_car = undefined;
            scope.pickUpLocation = scope.droppingLocation = "";
            scope.startDate = scope.leavingDate = "";
            scope.message = "booking";
            $("#confirmation").modal("show");
        }).error(function (response) {
            alert(response);
        });
    }
}

function clear_personal_info(scope) {
    scope.rsrv_firstName = scope.rsrv_lastName = scope.rsrv_phone = "";
    scope.rsrv_emailAddress = scope.rsrv_city = scope.rsrv_zipCode = "";
    scope.rsrv_address = scope.rsrv_confirmEmailAddress = "";
}

function slow_scroll(name) {
    var tag = $("#" + name);
    $('html, body').animate({ scrollTop: tag.offset().tag }, 1000);
}