'use strict';

/* Directives */
Appy.directive('draggable', function(){
	return{
		restrict: 'A',
		link: function(scope, element, attrs){
			$(element).draggable({
				addClass: false,
	            helper: 'clone', 
	            grid: [ 5, 5 ],
	            opacity: 0.9,
	            cursor: "crosshair",
	            snap: true,
	            revert: 'invalid',
	            start: function( event, ui ) { },
	            stop: function( event, ui ) { }
			});
		}
	}
})
Appy.directive('droppable', function($compile) {
    return {
        restrict: 'A',
        link: function($scope,element,attrs){
            $(element).droppable({
                accept: ".draggableDevice",
	            activeClass: 'droppable-active',
	            hoverClass: 'droppable-hover',
	            drop: function(event, ui){
	            	var id = ui.draggable.data('id');
	            	var devices = $scope.devices;
	            	var device = {};
	            	var appyDevice = {};
	            	appyDevice.device = {}; 
	            	appyDevice.inputs = [];
	            	appyDevice.outputs = [];

	            	for (var i = $scope.appy.appyDevices.length - 1; i >= 0; i--) {
	            		if($scope.appy.appyDevices[i].device.baseDevice.id === id){
	            			if($(event.target).hasClass('inputDevices')){
	            				var inputs = $scope.appy.appyDevices[i].inputs;
	            				if(inputs.length===0){
	            					$scope.appy.appyDevices[i].inputs = [{}];
	            				}
			            	}
			            	else if($(event.target).hasClass('outputDevices')){
			            		var outputs = $scope.appy.appyDevices[i].outputs;
			            		if(outputs.length===0){
	            					$scope.appy.appyDevices[i].outputs = [{}];
	            				}
			            	}

			            	$scope.$apply();
	            			return;
	            		}

	            	};

	            	for (var i = devices.length - 1; i >= 0; i--) {
	            		if(devices[i].id==id){
	            			appyDevice.device = devices[i];
	            			if($(event.target).hasClass('inputDevices')){
	            				appyDevice.inputs = [{}];
			            		$scope.appy.appyDevices.push(appyDevice);
			            	}
			            	else if($(event.target).hasClass('outputDevices')){
			            		appyDevice.outputs = [{}];
			            		$scope.appy.appyDevices.push(appyDevice);
			            	}

			            	$scope.$apply();
	            			return;
	            		}
	            	};
		            

	            	
	            }
    		});
    	}
    }
}
);

Appy.directive("repeatPassword", function() {
    return {
        require: "ngModel",
        link: function(scope, elem, attrs, ctrl) {
            var otherInput = elem.inheritedData("$formController")[attrs.repeatPassword];

            ctrl.$parsers.push(function(value) {
                if(value === otherInput.$viewValue) {
                    ctrl.$setValidity("dontMatch", true);
                    return value;
                }
                ctrl.$setValidity("dontMatch", false);
            });

            otherInput.$parsers.push(function(value) {
                ctrl.$setValidity("dontMatch", value === ctrl.$viewValue);
                return value;
            });
        }
    };
})
