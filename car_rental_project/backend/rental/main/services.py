from datetime import datetime
from datetime import timedelta

import jwt
from rest_framework import status
from rest_framework.response import Response

from Car_rental.settings import SECRET_KEY


def generate_token(login, user_id, user_role, expiration_hours=600000):
    exp = datetime.utcnow() + timedelta(hours=expiration_hours)
    return jwt.encode({'user_id': user_id, 'email': login, 'user_role': user_role, 'exp': exp}, SECRET_KEY,
                      algorithm='HS256')


def decode_token(token):
    return jwt.decode(token, SECRET_KEY, algorithms=['HS256'])


def save_data(serializer):
    if serializer.is_valid():
        serializer.save()
        return Response("request created", status=status.HTTP_200_OK)
    else:
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
