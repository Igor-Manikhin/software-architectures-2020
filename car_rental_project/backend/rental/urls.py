from django.conf.urls import url

from rental.views import AuthorizationUser, SignupNewUser, UserInfo, RequestsList, RentalRequest, CarsList,\
                         ContractsList

urlpatterns = [
    url(r'authUser', AuthorizationUser.as_view(), name='auth_user'),
    url(r'^signupUser$', SignupNewUser.as_view(), name='signup_user'),
    url(r'^getUser$', UserInfo.as_view(), name='get_user'),
    url(r'^requests$', RequestsList.as_view(), name='requests'),
    url(r'^rentalRequest$', RentalRequest.as_view(), name='car_rental_request'),
    url(r'^carsList$', CarsList.as_view(), name='cars_list'),
    url(r'^contracts$', ContractsList.as_view(), name='cars_list')
]
