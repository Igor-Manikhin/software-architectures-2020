from App.storage.DataGateway import DataGateway
from App.car.Car import Car


class CarMapper:
    gateway = DataGateway.conn
    cursor = DataGateway.getCursor()

    @staticmethod
    def getCarsAll():
        query_str = 'SELECT * FROM "Cars"'
        CarMapper.cursor.execute(query_str)
        return CarMapper.cursor.fetchall()

    @staticmethod
    def getCarByVIN(number):
        query_str = 'SELECT * FROM "Cars" WHERE vin_number = %(vin_number)s'
        CarMapper.cursor.execute(query_str, {'vin_number': number})
        record = CarMapper.cursor.fetchone()
        car = Car(record[1:12])
        car.carId = record[0]
        car.carStatus = record[12]
        return car

    @staticmethod
    def getCarById(index):
        query_str = 'SELECT * FROM "Cars" WHERE id = %(index)s'
        CarMapper.cursor.execute(query_str, {'index': index})
        return CarMapper.cursor.fetchone()

    @staticmethod
    def setCarStatusById(index, status):
        query_str = 'UPDATE "Cars" SET car_status = %s WHERE id = %s'
        CarMapper.cursor.execute(query_str, [status, index])
        CarMapper.gateway.commit()

    @staticmethod
    def addNewCar(data):
        query_str = 'INSERT INTO "Cars" (brand, model, body_type, vin_number, engine_type, engine_power, max_speed' \
                    ', fuel_type, transmission_type, drive_type, count_brakes, car_status) VALUES (%s, %s, %s, %s, %s, ' \
                    '%s, %s, %s, %s, %s, %s, %s)'
        CarMapper.cursor.execute(query_str, data)
        CarMapper.gateway.commit()

    @staticmethod
    def updateCarInfoByVIN(number, data):

        data_list = data
        data_list.append(number)

        query_str = 'UPDATE "Cars" SET brand = %s, model = %s, body_type = %s, engine_type = %s, ' \
                    'engine_power = %s, ' \
                    'max_speed = %s, fuel_type = %s, transmission_type = %s, drive_type = %s, ' \
                    'count_brakes = %s ' \
                    'WHERE vin_number = %s'

        CarMapper.cursor.execute(query_str, data_list)
        CarMapper.gateway.commit()

    @staticmethod
    def closeConnection():
        CarMapper.cursor.close()
