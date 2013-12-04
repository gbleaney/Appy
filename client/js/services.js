'use strict';

/* Services */

angular.module('appyServices', ['ngResource']).
factory('Devices', function($resource){
    return $resource('/api/devices', {}, {
        get: { method:'GET', isArray:true }
    });
}).
factory('Appys', function($resource){
    return $resource(
        '/api/appys', 
        {},
        {
            get: {
                method:'GET', 
                isArray:true
            }
        }
    );
}).
factory('Appy', function($resource){
    return $resource(
        '/api/appys/:appyId', 
        { appyId: '@appyId ' },
        {
            create: {
                method:'POST'
            },
            save: {
                method:'PUT'
            },
            delete: {
                method:'DELETE'
            },
            get: {
                method:'GET'
            }
        }
    );
    
}).
factory('Users', function($http, $rootScope, $location){
    return {
        login: function(user) {
            $http({
                method: 'POST',
                url: '/api/sessions', 
                data: user,
            }).
            success(function(result){
                console.log("Successful Login:");
                console.log(result);
                $rootScope.user = result;
                $location.path("/create");
                // success(user);
            }).error(function(error){
                alert("Error in Users. Check console for more info.");
                console.log("Failed Login:");
                console.log(error);
            });
        },
 
        logout: function() {
            $http({
                method: 'DELETE',
                url: '/api/sessions', 
                data: {},
            }).
            success(function(result){
                console.log("Successful logout:");
                console.log(result);
                $rootScope.user = undefined;

            }).error(function(error){
                alert("Error in Users logout. Check console for more info.");
                console.log("Failed Login:");
                console.log(error);
            });
        },

        create: function(username, email, password, passwordConfirm){
            if(password!=passwordConfirm){
                alert("Passwords must be equal");
                return;
            }
            $http({
                method: 'POST',
                url: '/api/users', 
                data: {
                    username:username, 
                    password:password, 
                    email: email
                },
            }).
            success(function(result){
                console.log("Successful Account Create:");
                console.log(result);
                $rootScope.user = result;
                $location.path("/home");

            }).error(function(error){
                alert("Error in User create. Check console for more info.");
                console.log("Failed Account Create:");
                console.log(error);

            });
        },

        checkSessionActive: function(){
            $http({
                method: 'GET',
                url: '/api/sessions', 
                data: {},
            }).
            success(function(result){
                console.log("Successfully got active user:");
                console.log(result);
                $rootScope.user = result;

            }).error(function(error){
                console.log("Failed to load current session:");
                console.log(error);
                $rootScope.user = undefined;
            });
        },

        requireAuthentication: function(){
            //TODO: find a way to persist login past refresh
            //var sessionid = $.cookie('sessionid');
            if($rootScope.user){
                return true;
            }
            else {
                $location.path("/users/login");
                return false;
            }
        },
        loggedIn: function(){
            if($rootScope.user){
                return true;
            }
            else {
                return false;
            }
        },
        loggedOut: function(){
            if(!$rootScope.user){
                return true;
            }
            else {
                return false;
            }
        },

    };
} );
