    var app = angular.module('myApp', ['ngTouch', 'ui.grid','restangular','ui.grid', 'ui.grid.edit', 'ui.grid.cellNav']);

    var url = "http://127.0.0.1:8000/api/DummyResponse/1"

    app.config(function (RestangularProvider) {
     RestangularProvider.setBaseUrl('http://127.0.0.1:8000/api');
     });

    app.controller('IndexCtrl', function($scope, Restangular) {
            $scope.people = Restangular.all('DummyResponse/1');
            console.log($scope.people)
        });

    app.controller('ajax', function($scope, $http) {
        $http.get(url).success( function(response) {
        $scope.guestdata = response;

       $scope.gridOptions.columnDefs = [
       {name: 'fields.joiningtime' },
       {name: 'fields.boozprofileId' },
       {name: 'fields.userId' },
       {name: 'fields.likeStatus' }
  ];
        console.log("guestdata::"+$scope.guestdata);
        $scope.gridOptions.data = $scope.guestdata;




        })
        });

    app.controller('MainCtrl1', function($scope, $http) {

      $scope.gridOptions = {};

      $scope.gridOptions.columnDefs = [
        {name: 'fields.joiningtime' },
        {name: 'fields.boozprofileId' },
        {name: 'fields.userId' },
        {name: 'fields.likeStatus' }
      ];

      $http.get('http://127.0.0.1:8000/api/DummyResponse/1').success( function(response) {
        $scope.guestdata = response;
        console.log("guestdata::1"+$scope.guestdata);
        $scope.gridOptions.data = $scope.guestdata;
       })
    })

