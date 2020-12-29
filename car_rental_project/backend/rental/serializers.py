from datetime import datetime

from rest_framework import serializers

from rental.models import User, Client, Manager, Mechanic, CarRentalRequest, Car, Request, CloseRentalRequest, Contract


class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = [field.name for field in model._meta.fields]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ClientInfoSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Client
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create(**validated_data.pop('user'))
        client = Client.objects.create(user=user, **validated_data)

        return client


class ClientInfoRentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class ManagerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'


class ManagerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Manager
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create(**validated_data.pop('user'))
        client = Manager.objects.create(user=user, **validated_data)

        return client


class MechanicSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Mechanic
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create(**validated_data.pop('user'))
        client = Mechanic.objects.create(user=user, **validated_data)

        return client


class RentalRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarRentalRequest
        fields = ['rental_period', 'car', 'client', 'purpose_acquisition']

    def create(self, validated_data):
        request = Request.objects.create(request_type="rental", date_created=datetime.now(), status="process")
        rental_request = CarRentalRequest.objects.create(request_id=request, **validated_data)

        return rental_request


class RentalRequestInfoSerializer(serializers.ModelSerializer):
    car = CarSerializer()
    client = ClientInfoRentalSerializer()

    class Meta:
        model = CarRentalRequest
        fields = '__all__'


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'


class ContractInfoSerializer(serializers.ModelSerializer):
    car_id = CarSerializer()
    client_id = ClientInfoRentalSerializer()
    manager_id = ManagerInfoSerializer()

    class Meta:
        model = Contract
        fields = '__all__'


class CloseRentalRequestsList(serializers.ModelSerializer):
    contract_id = ContractInfoSerializer()

    class Meta:
        model = CloseRentalRequest
        fields = '__all__'


class CloseRentalRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CloseRentalRequest
        fields = ['contract_id']

    def create(self, validated_data):
        request = Request.objects.create(request_type="close_rental", date_created=datetime.now(), status="process")
        rental_request = CloseRentalRequest.objects.create(request_id=request, **validated_data)

        return rental_request
