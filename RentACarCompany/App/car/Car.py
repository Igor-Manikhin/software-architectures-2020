class Car:

    def __init__(self, car_info):
        self.__car_id = None
        self.__car_info = car_info
        self.__car_status = None

    @property
    def carId(self):
        return self.__car_id

    @property
    def carStatus(self):
        return self.__car_status

    @property
    def carInfo(self):
        return self.__car_info

    @carInfo.setter
    def carInfo(self, car_info):
        self.__car_info = car_info

    @carId.setter
    def carId(self, index):
        self.__car_id = index

    @carStatus.setter
    def carStatus(self, car_status):
        self.__car_status = car_status
