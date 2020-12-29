from rest_framework import generics
from rest_framework.views import APIView

from rental.main.auth_signup import Authentication
from rental.main.entities import RequestsHandler, CarEntity, ContractEntity, UserEntity


class SignupNewUser(APIView):
    @staticmethod
    def post(request):
        return Authentication(request).signup_user()


class AuthorizationUser(APIView):
    @staticmethod
    def post(request):
        return Authentication(request).auth_user()


class ContractsList(APIView):
    @staticmethod
    def get(request):
        return ContractEntity(request).get_rental_contracts()

    @staticmethod
    def post(request):
        return ContractEntity(request).create_rental_contract()


class UserInfo(APIView):
    @staticmethod
    def get(request):
        return UserEntity(request).get_user_info()


class RentalRequest(APIView):
    @staticmethod
    def post(request):
        return RequestsHandler(request).make_action()


class TechInspectionRequest(APIView):
    def post(self, request):
        pass


class CarsList(generics.GenericAPIView):
    @staticmethod
    def get(request):
        return CarEntity(request).get_cars_list()

    @staticmethod
    def put(request):
        return CarEntity(request).add_new_car()


class RequestsList(APIView):
    @staticmethod
    def get(request):
        return RequestsHandler(request).get_requests()


class TechInspectionRequestsList(APIView):
    def get(self, request):
        pass
