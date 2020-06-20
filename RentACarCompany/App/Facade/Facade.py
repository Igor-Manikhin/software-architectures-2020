from App.storage.StorageRepository import StorageRepository


class Facade:

    def __init__(self):
        self.__repository = StorageRepository()

    @property
    def getRepository(self):
        return self.__repository

    def registration(self, data, role):
        self.getRepository.signUpUser(data, role)

    def authentication(self, role, login, password):
        is_auth = self.getRepository.authUser(role, login, password)
        return is_auth

    def logout(self, role, login):
        user = self.getRepository.getUser(role, login)
        user.signOut()

    def createRequestCarRent(self, login, data_obj):
        user = self.getRepository.getUser('Client', login)
        user.createRequestForCarRent(self.getRepository, data_obj)

    def createRequestCloseCarRent(self, login, data_obj):
        user = self.getRepository.getUser('Client', login)
        user.createRequestForCloseCarRent(self.getRepository, data_obj)

    def concludeContract(self, login):
        user = self.getRepository.getUser('Client', login)
        user.concludeContract(self.getRepository)

    def getCarsList(self):
        return self.getRepository.getCarsList()

    def addCarInList(self, manager_login, data):
        manager = self.getRepository.getUser('Manager', manager_login)
        manager.addNewCar(self.getRepository, data)

    def updateCarInfo(self, manager_login, vin_number, data):
        manager = self.getRepository.getUser('Manager', manager_login)
        manager.updateCarInfo(self.getRepository, data, vin_number)

    def createContract(self, manager_login, client_login):
        manager = self.getRepository.getUser('Manager', manager_login)
        manager.createContract(self.getRepository, client_login)

    def closeContract(self, manager_login, client_login):
        manager = self.getRepository.getUser('Manager', manager_login)
        manager.closeContract(self.getRepository, client_login)

    def getRentsHistoryAllClients(self, manager_login):
        manager = self.getRepository.getUser('Manager', manager_login)
        manager.getRentsHistory(self.getRepository)

    def getIncomingRequests(self, manager_login, request_type):
        manager = self.getRepository.getUser('Manager', manager_login)
        return manager.getIncomingRequests(self.getRepository, request_type)

    def getIncomingTechRequests(self, master_login):
        master = self.getRepository.getUser('Master', master_login)
        return master.getIncomingRequests(self.getRepository)

    def createReportTechInspection(self, master_login):
        master = self.getRepository.getUser('Master', master_login)
        master.createReport()

# test = Facade().authentication('Client', "Игорь", "619456adm")
# print(test)
# Facade().logout('Master', 'Игорь')
# data = ['Семён', 'Сафонов', 'semyon.manikhin@mail.ru', '1996-12-31', 'Cronos1123']
# Facade().registration(data, "Master")

data_1 = [0, "деловая поездка", '(2020-06-19, 2020-06-30)']
data_2 = [0, 0]

# Facade().createRequestCarRent("Семён", data_1)
# Facade().createRequestCloseCarRent("Семён", data_2)

# car = Facade().getRepository.getCar('2C4GJ453XYR693697')
# print(car)
# Facade().createContract('Игорь', 'Семён')
# Facade().closeContract('Игорь', 'Семён')
# contract = Facade().getRepository.getContract(0)
# print(contract.contractInfo)
# requests = Facade().getIncomingRequests('Игорь', 'Car_Rental')
# Facade().concludeContract('Семён')
# tech = Facade().getIncomingTechRequests('Игорь')
