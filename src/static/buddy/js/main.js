    var app = angular.module('myApp', ['ngTouch', 'ui.grid','restangular',]);

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
        $scope.gridOptions = {};
        console.log("guestdata::"+$scope.guestdata);
        $scope.gridOptions.data = $scope.guestdata;
        $scope.gridOptions.columnDefs = [
           {name: 'fields.joiningtime' },
           {name: 'fields.boozprofileId' },
           {name: 'fields.userId' },
           {name: 'fields.likeStatus' }
       ];


        })
        });

    app.controller('MainCtrl', ['$scope', function ($scope) {

      $scope.myData = [
        {
            "firstName": "Cox",
            "lastName": "Carney",
            "company": "Enormo",
            "employed": true
        },
        {
            "firstName": "Lorraine",
            "lastName": "Wise",
            "company": "Comveyer",
            "employed": false
        },
        {
            "firstName": "Nancy",
            "lastName": "Waters",
            "company": "Fuelton",
            "employed": false
        }
    ];
    }]);