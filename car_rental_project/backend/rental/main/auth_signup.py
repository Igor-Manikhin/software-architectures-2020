from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response

from rental.main.services import generate_token, save_data
from rental.models import User
from rental.serializers import ClientInfoSerializer, ManagerSerializer, MechanicSerializer


class Authentication:
    def __init__(self, request):
        self.data = request.data
        self.params = request.query_params

    def auth_user(self):
        response_body = dict(status=status.HTTP_200_OK)
        user = get_object_or_404(User, login=self.data['login'])

        if not user.check_password(self.data['password']):
            response_body['status'] = status.HTTP_400_BAD_REQUEST
        else:
            response_body['data'] = dict(token=generate_token(self.data['login'], user.id, self.params['user_role']))

        return Response(**response_body)

    def signup_user(self):
        if self.get_user(self.data['user']['login']) is None:
            if self.params['user_role'] == 'client':
                return save_data(ClientInfoSerializer(data=self.data))
            elif self.params['user_role'] == 'manager':
                return save_data(ManagerSerializer(data=self.data))
            else:
                return save_data(MechanicSerializer(data=self.data))
        else:
            return Response("user is found!!", status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get_user(login):
        try:
            user = User.objects.get(login=login)
        except User.DoesNotExist:
            user = None

        return user
