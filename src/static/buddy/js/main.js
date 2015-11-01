    var app = angular.module('myApp', ['ngTouch', 'ui.grid','restangular','ui.grid', 'ui.grid.edit', 'ui.grid.cellNav']);

    var url = "http://127.0.0.1:8000/api/DummyResponse/1"
    var url2 = "https://api.myjson.com/bins/ulb2"

    app.config(function (RestangularProvider) {
     RestangularProvider.setBaseUrl('http://127.0.0.1:8000/api');
     });

    app.controller('IndexCtrl', function($scope, Restangular) {
            $scope.people = Restangular.all('DummyResponse/1');
            console.log($scope.people)
        });


    app.controller('MainCtrl1', function($scope, $http) {

      $scope.gridOptions = {};

      $scope.gridOptions.columnDefs = [
        {name: 'fields.joiningtime' },
        {name: 'fields.boozprofileId' },
        {name: 'fields.userId' },
        {name: 'fields.likeStatus' }
      ];

      $http.get(url).success( function(response) {
        $scope.guestdata = JSON.parse(response);
        console.log("guestdata::1"+$scope.guestdata);
        $scope.gridOptions.data = $scope.guestdata;
       })
    })

