from App.users.User import User
from App.contract.Contract import Contract
from App.car.Car import Car
from datetime import datetime


class Manager(User):

    def createContract(self, storage, client_login):
        client = storage.getUser('Client', client_login)
        request = storage.getRequest('Car_Rental', client.userId)
        current_date = datetime.date(datetime.now(tz=None))
        data = [request[1], self.userId, request[2], request[4], request[3], current_date]
        Contract(data).saveContract(storage)

    def closeContract(self, storage, client_login):
        current_date = datetime.date(datetime.now(tz=None))
        storage.closeContract(self.userId, client_login, current_date)

    def addNewCar(self, storage, data):
        storage.addNewCarInList(Car(data))

    def updateCarInfo(self, storage, new_data, vin_number):
        storage.updateCarInfo(new_data, vin_number)

    def getRentsHistory(self, storage):
        return storage.getRentsHistoryAllClients()

    def getIncomingRequests(self, storage, request_type):
        return storage.getAllRequests(request_type)
