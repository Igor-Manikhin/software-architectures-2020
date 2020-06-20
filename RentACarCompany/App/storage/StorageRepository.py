from App.storage.Users.ClientMapper import ClientMapper
from App.storage.Users.ManagerMapper import ManagerMapper
from App.storage.Users.MasterMapper import MasterMapper
from App.storage.Contract.Contract import ContractMapper
from App.storage.RentsHistory.RentsHistory import RentsHistoryMapper
from App.storage.Car.CarMapper import CarMapper
from App.storage.Requests.RequestMapper import *


class StorageRepository:

    def getUser(self, role, login):
        if role == 'Client':
            return ClientMapper.getClientByLogin(login)
        elif role == 'Manager':
            return ManagerMapper.getManagerByLogin(login)
        else:
            return MasterMapper.getMasterByLogin(login)

    def getCar(self, vin_number):
        return CarMapper.getCarByVIN(vin_number)

    def getAllRequests(self, request_type):
        if request_type == 'Car_Rental':
            return CarRentalMapper.getCarRentalRequestsAll()
        elif request_type == 'Close_Car_Rental':
            return CloseCarRentalMapper.getCloseCarRentalRequestsAll()
        else:
            return TechInspectMapper.getTechInspectRequestsAll()

    def getRequest(self, request_type, client_id):

        if request_type == 'Car_Rental':
            return CarRentalMapper.getCarRentalRequestByClientId(client_id)
        else:
            return CloseCarRentalMapper.getCloseCarRentalRequestByClientId(client_id)

    def getContract(self, client_id):
        return ContractMapper.getContractByClientId(client_id)

    def authUser(self, role, login,  password):

        user = self.getUser(role, login)
        user.signIn(self, role, password)
        return user.isAuth

    def userVerifyPassword(self, index, role, password):
        if role == 'Client':
            return ClientMapper.authClient(index, password)
        elif role == 'Manager':
            return ManagerMapper.authManager(index, password)
        else:
            return MasterMapper.authMaster(index, password)

    def signUpUser(self, data_obj, role):
        data = data_obj

        if role == 'Client':
            ClientMapper.addClient(data)
        elif role == 'Manager':
            ManagerMapper.addManager(data)
        else:
            MasterMapper.addMaster(data)

    def saveClientRequest(self, request_type, request_data):

        if request_type == 'Car_Rental':
            CarRentalMapper.addCarRentalRequest(request_data)
        else:
            CloseCarRentalMapper.addCloseCarRentalRequest(request_data)

    def saveContract(self, data, client_id):
        ContractMapper.addContract(data)

    def closeContract(self, manager_id, client_login, current_date):
        client = self.getUser('Client', client_login)
        contract = self.getContract(client.userId)
        contract_info = contract.contractInfo
        ContractMapper.updateContractStatusById(contract.contractId, 'Закрыт')
        data = [client.userId, contract_info[1], contract_info[2], contract.contractId, contract_info[6], current_date]
        RentsHistoryMapper.addNewHistoryRecord(data)
        CloseCarRentalMapper.delCloseCarRentalRequestByClientId(client.userId)

    def concludeContract(self, client_id):
        contract = self.getContract(client_id)
        ContractMapper.updateContractStatusById(contract.contractId, 'заключён')
        CarMapper.updateCarStatusById(contract.carId, 'находится в прокате')
        CarRentalMapper.delCarRentalRequestByClientId(client_id)

    def addNewCarInList(self, car):
        car_info = car.carInfo
        car_info.append('доступен')
        CarMapper.addNewCar(car_info)

    def updateCarInfo(self, data, vin_number):
        car = self.getCar(vin_number)
        car.carInfo = data
        CarMapper.updateCarInfoByVIN(car.carInfo)

    def getCarsList(self):
        return CarMapper.getCarsAll()

    def getRentsHistoryClient(self, client_id):
        return RentsHistoryMapper.getRentsHistoryClientById(client_id)

    def getRentsHistoryAllClients(self):
        return RentsHistoryMapper.getRentsHistoryAllClients()

    def getIncomingRequests(self):
        return CarRentalMapper.getCarRentalRequestsAll()
