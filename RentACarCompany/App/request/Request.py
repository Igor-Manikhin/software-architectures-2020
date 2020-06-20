class Request:

    def __init__(self, request_type, client_id, car_id):
        self.__request_id = None
        self.__request_type = request_type
        self.__client_id = client_id
        self.__car_id = car_id
        self.__status = None

    @property
    def requestInfo(self):
        return [self.__client_id, self.__car_id]

    @property
    def requestId(self):
        return self.__request_id

    @property
    def requestType(self):
        return self.__request_type

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

    @requestId.setter
    def requestId(self, index):
        self.__request_id = index

    def saveRequest(self, storage):
        storage.saveClientRequest(self.requestType, self.requestInfo)


class RequestCarRental(Request):

    def __init__(self, client_id, data_obj):
        super().__init__("Car_Rental", client_id, data_obj[0])
        self.__rental_period = data_obj[2]
        self.__reason_hire = data_obj[1]

    @property
    def requestInfo(self):
        req_info = super().requestInfo
        req_info.append(self.__reason_hire)
        req_info.append(self.__rental_period)
        req_info.append('В обработке')

        return req_info


class RequestCloseCarRental(Request):

    def __init__(self, client_id, data_obj):
        super().__init__("Close_Car_Rental", client_id, data_obj[0])
        self.__contract_id = data_obj[1]

    @property
    def requestInfo(self):
        req_info = super().requestInfo
        req_info.append(self.__contract_id)
        req_info.append('В обработке')

        return req_info
