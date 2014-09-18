angular.module('demo', ['ngAnimate'])
    .config(['$httpProvider', function($httpProvider) {
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    }
    ])
    .controller('MainCtrl', function(
        $scope, $http
        ){
        var retobj, newItem, url = '/api/v1/job/';
        $scope.items = [];
        $http.get(url + '?format=json')
            .success(function(data, status) {
                $scope.status = status;
                $scope.items = data.objects;
                retobj = data;
            })
            .error(function(data, status) {
                $scope.data = data || "Request failed";
                $scope.status = status;
            });
        $scope.removejob = function (i) { $scope.items.splice(i,1)}

        $scope.add = function() {
            newItem = {
                company: '',
                title: '',
                date_end: '2014-01-01',
                date_start: '2012-01-01'
            };
            $scope.items.push(newItem);
            $http.post(url,newItem);
        };
        $scope.save = function () {
            retobj = {};
            retobj.objects = $scope.items;
            $http.put(url, retobj);
        }
    })