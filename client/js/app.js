"use strict";

/* App Module */

var Appy = angular.module('appy', ['appyFilters', 'appyServices']).
config(['$routeProvider', '$locationProvider', '$httpProvider',  
	function($routeProvider,$locationProvider, $httpProvider) {
		
		$routeProvider.
		when('/home', {templateUrl: '/static/partials/home.html',   controller: HomeCtrl}).

		when('/edit', {
			templateUrl: '/static/partials/chooseEdit.html',   
			controller: EditCtrl
		}).

		when('/create', {
			templateUrl: '/static/partials/createEdit.html',   
			controller: CreateEditCtrl
		}).

		when('/edit/:appyId', {
			templateUrl: '/static/partials/createEdit.html',   
			controller: CreateEditCtrl
		}).

		when('/users/login', {templateUrl: '/static/partials/login.html',   controller: LoginCtrl}).
		when('/users/logout', {templateUrl: '/static/partials/logout.html',   controller: LogoutCtrl}).
		when('/users/create', {templateUrl: '/static/partials/createAccount.html',   controller: CreateAccountCtrl}).
		otherwise({redirectTo: '/home'});


    //Intercept 401 not authorized and redirect to login page
    var interceptor = ['$location', '$q', function($location, $q) {
			function success(response) {
				return response;
			}

			function error(response) {

				if(response.status === 401) {
					$location.path('/users/login');
					return $q.reject(response);
				}
				else {
					return $q.reject(response);
				}
			}

			return function(promise) {
				return promise.then(success, error);
			};
    }];

    $httpProvider.responseInterceptors.push(interceptor);

    //Add XSRF token to every header
    var csrf = $.cookie('csrftoken');
    $httpProvider.defaults.headers.common['X-CSRFToken'] = csrf;

  }]);

Appy.run(function(Users){
	Users.checkSessionActive();
});