"use strict";

/* Controllers */

	function HomeCtrl($scope) {
		
	}

	function CreateEditCtrl($scope, $routeParams, Devices, Users, Appy) {
		if(!Users.requireAuthentication()){
			return;
		}
		else{
			$scope.appyId = $routeParams.appyId;
			$scope.devicesLoading = true;
			$scope.devices = Devices.get(function(){
				$scope.devicesLoading = false;
			});
			$scope.saving = false;
			$scope.savingText = "Save Appy";
			$scope.$watch(
				'appy', 
				function() { 
					$scope.savingText = "Save Appy";
				}, 
				true
			);

			if($scope.appyId){
				$scope.appy = Appy.get({
						appyId: $scope.appyId
				},
				function(response){
					var appyDevices = response.appyDevices;
					var getAction = function(id, actions){
						for (var i = actions.length - 1; i >= 0; i--) {
							if(actions[i].id == id)	{
								return actions[i];
							}
							
						};
						alert("Error matching actions");
						return undefined;
					}
					for (var i = appyDevices.length - 1; i >= 0; i--) {
						var currentDevice = appyDevices[i];
						var inputs = currentDevice.inputs;
						var outputs = currentDevice.outputs;
						var actionValue;
						for (var j = inputs.length - 1; j >= 0; j--) {
							actionValue = getAction(inputs[j].id, currentDevice.device.baseDevice.inputs);
							inputs[j].value = actionValue;
						};
						for (var k = outputs.length - 1; k >= 0; k--) {
							actionValue = getAction(outputs[k].id, currentDevice.device.baseDevice.outputs);
							outputs[k].value = actionValue;
						};
					};
				});
				$scope.isCreate = false;
				
			}else{
				$scope.appy = {};
				$scope.appy.appyDevices = [];
				$scope.isCreate = true;
			}

			
			$scope.saveAppy = function(){
				$scope.saving = true;
				$scope.savingText = "Saving";
				var saveHandler = function(response){
					$scope.saving = false;
					$scope.savingText = "Saved";
				}
				if($scope.appyId){
					Appy.save(
						$scope.appy,
						saveHandler
					);
				}
				else{
					Appy.create(
						$scope.appy,
						saveHandler
					);
				}

			};
			$scope.removeDevice = function(deviceIndex, isInput){
				var appyDevice = $scope.appy.appyDevices[deviceIndex];
				if(isInput){
					appyDevice.inputs = [];
				}else{
					appyDevice.outputs = [];
				}

				if(	(appyDevice.inputs.length===0 )&&
					(appyDevice.outputs.length===0) ){
					$scope.appy.appyDevices.splice(deviceIndex, 1);
				}
			};

			$scope.removeAction = function(actions, index){
				actions.splice(index, 1);
			};
		}
	}

	function EditCtrl($scope, Appys, Appy) {
		$scope.appysLoading = true;
		$scope.appys = Appys.get(function(result){
			$scope.appysLoading = false;
		});

		$scope.deleteAppy= function(appy, index){
			Appy.delete({appyId: appy.id});
			$scope.appys.splice(index, 1);
		};
	}

	function CreateAccountCtrl($scope, Users) {
		$scope.submit = function(){
			Users.create(this.username, this.email, this.password, this.repeatPassword);
		};
	}

	function LoginFormCtrl($scope, Users){
		
		$scope.submit = function(){
			Users.login({
					username: this.username, 
					password: this.password
			});
		};

	}

	function LogoutCtrl(Users){
		
		Users.logout();
	}

	function LoginCtrl() {

	}

