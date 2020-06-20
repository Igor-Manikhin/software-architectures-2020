from App.request.Request import *
from App.users.User import User


class Client(User):

    def createRequestForCarRent(self, storage, data_obj):
        RequestCarRental(self.userId, data_obj).saveRequest(storage)

    def createRequestForCloseCarRent(self, storage, data_obj):
        RequestCloseCarRental(self.userId, data_obj).saveRequest(storage)

    def getRentsHistory(self, storage):
        return storage.getRentsHistoryClient(self.userId)

    def concludeContract(self, storage):
        storage.concludeContract(self.userId)
