let App = angular.module("frontendApp", ["ngRoute"]);

App.service('user', function() {
	let loggedIn = false;
    let currentURL = "/account/profile";

    this.isUserLoggedIn = () => {
        if(localStorage.getItem("token")){
            loggedIn = true;
        }

        return loggedIn;
    } 

	this.saveData = (data) => {
        localStorage.setItem('token', data.token);
    }

    this.currentURL = (url) => {
        currentURL = url;
    }

    this.isCurrentURL = () => {
        return currentURL;
    }

    this.clearData = () => {
        localStorage.removeItem('token');
        loggedIn = false;
    }
});
       

App.controller('main', function($scope, $http, $location, user) {
	$scope.authUser = () => {
		let data = {'login': $scope.email, 'password': $scope.password}

		$http.post(`http://127.0.0.1:8000/api/v1/authUser?user_role=${$scope.user_mode}`, data).then((data) => {
			user.saveData(data.data);
			$location.path(user.isCurrentURL());
		})
	}
});

App.controller('active-rental', function($scope, $http, $location, user) {
	$scope.nav_account = {page: 2};
});

App.controller('profile', function($scope, $http) {
	$scope.nav_account = {page: 1};

	$http.get("http://127.0.0.1:8000/api/v1/getUser", {'headers': {'Auth': localStorage.getItem("token")}}).then((data) => {
		$scope.name = data.data.name;
		$scope.email = data.data.user.login;
		$scope.password = data.data.user.password;
	});
});

App.controller('rental-requests', function($scope, $http, $routeParams) {
	$scope.nav_account = {page: 3};

	$http.get("http://127.0.0.1:8000/api/v1/requests?type_requests=rental").then((data) => {
        if(data.data.length > 0){
            $scope.rentalRequests = data.data;
        };
    });
});

App.controller('rental-request-detail', function($scope, $http, $routeParams) {
	$scope.nav_account = {page: 7};

	$http.get(`http://127.0.0.1:8000/api/v1/requests?type_requests=rental&request_id=${$routeParams.id}`).then((data) => {
        $scope.rentalRequest = data.data[0];
    });

     $scope.approve = () => {
    	$http.post(`http://127.0.0.1:8000/api/v1/rentalRequest?action=approve&request_id=${$routeParams.id}&status=approved`).then((data) => {
			alert("Запрос на прокат одобрен!");
		})
    }

    $scope.cancel = () => {
    	$http.post(`http://127.0.0.1:8000/api/v1/rentalRequest?action=approve&request_id=${$routeParams.id}&status=cancelled`).then((data) => {
			alert("Запрос на прокат отклонён!");
		})
    }
});

App.controller('rental-cars-list', function($scope, $http) {
	$scope.nav_account = {page: 4};

	$http.get("http://127.0.0.1:8000/api/v1/carsList").then((data) => {
        if(data.data.length > 0){
            $scope.cars = data.data;
        };
    });
});

App.controller('car-detail', function($scope, $routeParams, $http) {
	$scope.nav_account = {page: 5};

	$http.get(`http://127.0.0.1:8000/api/v1/carsList?car_id=${$routeParams.id}`).then((data) => {
        $scope.car = data.data;

        switch(data.data.car_status) {
        	case "leisure":
        		$scope.status = "свободен";
        		break;
        	case "available_for_rent":
        		$scope.status = "находится в прокате";
        		break;
        	default:
        		$scope.status = "находится на техническом обслуживании";
        		break;
        }
    });
});

App.controller('rental-request', function($scope, $routeParams, $http) {
	$scope.nav_account = {page: 6};
	$scope.data={};

	$scope.rentalRequest = () => {
		let data = {};
		let start_date = new Date($scope.data.start_date).toISOString().slice(0,10);
		let end_date = new Date($scope.data.end_date).toISOString().slice(0,10);
		let purpose = $scope.data.purpose;

		data.rental_period = [start_date, end_date];
		data.purpose_acquisition = purpose;
		data.car = $routeParams.id;

		$http.post("http://127.0.0.1:8000/api/v1/rentalRequest?action=create_request", data, {'headers': {'Auth': localStorage.getItem("token")}}).then((data) => {
			alert("Заявка на приобретение в прокат автомобиля успешно создана");
		});
	}
});
