class Contract:

    def __init__(self, data):
        self.__contract_id = None
        self.__client_id = data[0]
        self.__manager_id = data[1]
        self.__car_id = data[2]
        self._rental_period = data[3]
        self.__reason_hire = data[4]
        self.__date_create = data[5]
        self.__status = None

    @property
    def getRequisites(self):
        return dict(name_of_organization='Car rental company',
                    INN='7720239606', KPP='500801001', OGRN='1027739513394',
                    OKPO='51069045', Account='40817810570000123456')

    @property
    def contractStatus(self):
        return self.__status

    @property
    def contractId(self):
        return self.__contract_id

    @property
    def carId(self):
        return self.__car_id

    @property
    def contractInfo(self):
        return [self.__client_id, self.__manager_id,
                self.__car_id, self._rental_period,
                self.__reason_hire, self.__status, self.__date_create]

    @contractId.setter
    def contractId(self, index):
        self.__contract_id = index

    @contractStatus.setter
    def contractStatus(self, status):
        self.__status = status

    def saveContract(self, storage):
        self.contractStatus = "Ожидает заключения"
        storage.saveContract(self.contractInfo, self.__client_id)
