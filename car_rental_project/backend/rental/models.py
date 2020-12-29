from django.contrib.postgres.fields import DateRangeField
from django.db import models


class User(models.Model):
    login = models.EmailField()
    password = models.CharField(max_length=200)

    def check_password(self, password):
        return self.password == password


class Manager(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)


class Mechanic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)


class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    credit_card_info = models.TextField()


class Car(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    body_type = models.CharField(max_length=30)
    number_packages = models.IntegerField
    engine = models.CharField(max_length=30)
    engine_power = models.IntegerField
    max_speed = models.IntegerField
    fuel_type = models.CharField(max_length=10)
    transmission = models.CharField(max_length=10)
    drive = models.CharField(max_length=10)
    brakes = models.CharField(max_length=10)
    car_image = models.ImageField(upload_to='static/images')
    car_status = models.CharField(max_length=10)


class Contract(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    manager_id = models.ForeignKey(Manager, on_delete=models.CASCADE)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    rental_period = DateRangeField()
    purpose_acquisition = models.CharField(max_length=50)
    payment_method_info = models.CharField(max_length=50)
    date_created = models.DateField()
    date_closed = models.DateField()
    status = models.CharField(max_length=50)

    def get_client_info(self):
        return Client.objects.get(id=self.client_id)

    def get_manager_info(self):
        return Manager.objects.get(id=self.manager_id)

    def get_car_info(self):
        return Car.objects.get(id=self.car_id)


class InspectionReport(models.Model):
    contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE)
    mechanic_id = models.ForeignKey(Mechanic, on_delete=models.CASCADE)
    tech_damage_description = models.TextField()
    phys_damage_description = models.TextField()
    total_cost = models.IntegerField
    date_inspection = models.DateField()
    date_created_report = models.DateField()

    def get_contract_info(self):
        return Contract.objects.get(id=self.contract_id)

    def get_mechanic_info(self):
        return Contract.objects.get(id=self.mechanic_id)


class Request(models.Model):
    request_type = models.CharField(max_length=20)
    date_created = models.DateField()
    status = models.CharField(max_length=50)


class CarRentalRequest(models.Model):
    request_id = models.ForeignKey(Request, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    rental_period = DateRangeField()
    purpose_acquisition = models.CharField(max_length=50)

    def get_client_info(self):
        return Client.objects.get(id=self.client)

    def get_car_info(self):
        return Car.objects.get(id=self.car)

    def get_request(self):
        return self.request_id


class TechInspectionRequest(models.Model):
    request_id = models.ForeignKey(Request, on_delete=models.CASCADE)
    manager_id = models.ForeignKey(Manager, on_delete=models.CASCADE)
    contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)

    def get_manager_info(self):
        return Manager.objects.get(id=self.manager_id)

    def get_contract_info(self):
        return Contract.objects.get(id=self.manager_id)


class CloseRentalRequest(models.Model):
    request_id = models.ForeignKey(Request, on_delete=models.CASCADE)
    contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE)

    def get_contract_info(self):
        return Contract.objects.get(id=self.contract_id)

    def get_request(self):
        return self.request_id


class Notification(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    notification_text = models.CharField(max_length=200)
    date_receipt = models.DateField()

    def get_client_info(self):
        return Client.objects.get(id=self.client_id)
