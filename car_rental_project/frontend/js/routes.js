App.config(function($routeProvider, $locationProvider){
    $routeProvider.when('/', {
        resolve: {
            check: ($location, $http, user) => {
                       if(user.isUserLoggedIn()){
                           $location.path("/account/profile");
                       }
                   }
        },
        templateUrl:'views/main.html',
        controller:'main'
    })
    .when('/account/profile', {
    	resolve: {
            check: ($location, $http, user) => {
                       if(!user.isUserLoggedIn()){
                           user.currentURL($location.path());
                           $location.path("/");
                       }
                   }
        },
    	templateUrl:'views/account.html',
        controller:'profile'
    })
    .when('/account/active-rental', {
    	resolve: {
            check: ($location, $http, user) => {
                       if(!user.isUserLoggedIn()){
                           user.currentURL($location.path());
                           $location.path("/");
                       }
                   }
        },
    	templateUrl:'views/account.html',
        controller:'active-rental'
    })
    .when('/account/rental-requests', {
    	resolve: {
            check: ($location, $http, user) => {
                       if(!user.isUserLoggedIn()){
                           user.currentURL($location.path());
                           $location.path("/");
                       }
                   }
        },
    	templateUrl:'views/account.html',
        controller:'rental-requests'
    })
    .when('/account/rental-request/:id', {
    	resolve: {
            check: ($location, $http, user) => {
                       if(!user.isUserLoggedIn()){
                           user.currentURL($location.path());
                           $location.path("/");
                       }
                   }
        },
    	templateUrl:'views/account.html',
        controller:'rental-request-detail'
    })
    .when('/account/rental-cars-list', {
    	resolve: {
            check: ($location, $http, user) => {
                       if(!user.isUserLoggedIn()){
                           user.currentURL($location.path());
                           $location.path("/");
                       }
                   }
        },
    	templateUrl:'views/account.html',
        controller:'rental-cars-list'
    })
    .when('/account/rental-cars-list/:id', {
    	resolve: {
            check: ($location, $http, user) => {
                       if(!user.isUserLoggedIn()){
                           user.currentURL($location.path());
                           $location.path("/");
                       }
                   }
        },
    	templateUrl:'views/account.html',
        controller:'car-detail'
    })
    .when('/account/create-rental-request/:id', {
    	resolve: {
            check: ($location, $http, user) => {
                       if(!user.isUserLoggedIn()){
                           user.currentURL($location.path());
                           $location.path("/");
                       }
                   }
        },
    	templateUrl:'views/account.html',
        controller:'rental-request'
    })
    .when('/logout', {
        resolve: {
            deadResolve: function($location, user){
                            user.clearData();
                            $location.path('/');
                        }
        }
    })

    $locationProvider.html5Mode(true);
    $locationProvider.hashPrefix('!');
});
