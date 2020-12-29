from rest_framework import status
from rest_framework.response import Response
from rental.models import CarRentalRequest, CloseRentalRequest, Car, Contract, Client
from rental.main.services import save_data, decode_token

from rental.serializers import RentalRequestSerializer, RentalRequestInfoSerializer, CloseRentalRequestSerializer, \
    CloseRentalRequestsList, CarSerializer, ContractInfoSerializer, ContractSerializer, ClientInfoSerializer


class CarRentalRequestEntity:
    def __init__(self, request):
        self.data = request.data
        self.params = request.query_params
        self.token = request.META.get('HTTP_AUTH')

    def approve_car_rental(self):
        return self.update_status_rental_request(self.params['request_id'], self.params['status'])

    @staticmethod
    def update_status_rental_request(request_id, request_status):
        try:
            request = CarRentalRequest.objects.get(id=request_id).get_request()
            request.status = request_status
            request.save()

            return Response("status changed", status=status.HTTP_200_OK)
        except CarRentalRequest.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get_rental_requests(self):
        if self.params.get('car_id') is not None:
            rental_request = CarRentalRequest.objects.get(pk=self.params['id'])
            serializer = RentalRequestInfoSerializer(rental_request)
        else:
            rental_requests = CarRentalRequest.objects.all()
            serializer = RentalRequestInfoSerializer(rental_requests, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def create_request(self):
        decode_info = decode_token(self.token)
        self.data['client'] = Client.objects.get(user_id=decode_info['user_id']).id
        serializer = RentalRequestSerializer(data=self.data)
        return save_data(serializer)


class CloseRentalRequestEntity:
    def __init__(self, request):
        self.data = request.data
        self.params = request.query_params
        self.token = request.META['HTTP_AUTH']

    def close_car_rental(self):
        return self.update_status_close_request(self.params['client_id'], self.params['status'])

    @staticmethod
    def update_status_close_request(client_id, request_status):
        try:
            request = CloseRentalRequest.objects.get(client_id=client_id).get_request()
            request.status = request_status
            request.save()

            return Response("status changed", status=status.HTTP_200_OK)
        except CarRentalRequest.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @staticmethod
    def get_close_rental_requests():
        close_rental_requests = CloseRentalRequest.objects.all()
        serializer = CloseRentalRequestsList(close_rental_requests, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def create_request(self):
        serializer = CloseRentalRequestSerializer(data=self.data)
        return save_data(serializer)


class RequestsHandler:
    def __init__(self, request):
        self.request = request
        self.params = self.request.query_params

    def get_requests(self):
        if self.params['type_requests'] == 'rental':
            return CarRentalRequestEntity(self.request).get_rental_requests()
        elif self.params['type_requests'] == 'close_rental':
            return CloseRentalRequestEntity.get_close_rental_requests()
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def make_action(self):
        if self.params['action'] == 'create_request':
            return CarRentalRequestEntity(self.request).create_request()
        elif self.params['action'] == 'close_rental':
            return CloseRentalRequestEntity(self.request).create_request()
        elif self.params['action'] == 'approve':
            return CarRentalRequestEntity(self.request).approve_car_rental()
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class CarEntity:
    def __init__(self, request):
        self.request = request
        self.data = self.request.data
        self.params = self.request.query_params

    def get_cars_list(self):
        if self.params.get('car_id') is not None:
            car = Car.objects.get(pk=self.params['car_id'])
            serializer = CarSerializer(car, context={'request': self.request})
        else:
            cars = Car.objects.all()
            serializer = CarSerializer(cars, many=True, context={'request': self.request})

        return Response(serializer.data, status=status.HTTP_200_OK)

    def add_new_car(self):
        return save_data(CarSerializer(data=self.data))


class ContractEntity:
    def __init__(self, request):
        self.data = request.data
        self.params = request.query_params

    def get_rental_contracts(self):
        if self.params.get('client_id') is not None:
            contracts = Contract.objects.all().filter(client_id=self.params['client_id'])
        else:
            contracts = Contract.objects.all()

        serializer = ContractInfoSerializer(contracts, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def create_rental_contract(self):
        return save_data(ContractSerializer(data=self.data))


class UserEntity:
    def __init__(self, request):
        self.request = request
        self.token = request.META['HTTP_AUTH']

    def get_user_info(self):
        decode_info = decode_token(self.token)

        if decode_info['user_role'] == 'client':
            serializer = ClientInfoSerializer(Client.objects.get(user=decode_info['user_id']))
        elif decode_info['user_role'] == 'manager':
            serializer = ClientInfoSerializer(Client.objects.get(user=decode_info['user_id']))
        elif decode_info['user_role'] == 'master':
            serializer = ClientInfoSerializer(Client.objects.get(user=decode_info['user_id']))
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_200_OK)
