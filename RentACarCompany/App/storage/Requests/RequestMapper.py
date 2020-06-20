from App.storage.DataGateway import DataGateway
from datetime import datetime


gateway = DataGateway.conn
cursor = DataGateway.getCursor()


class CarRentalMapper:

    @staticmethod
    def getCarRentalRequestsAll():
        query_str = 'SELECT * FROM "Car_Rental_Requests"'
        cursor.execute(query_str)
        return cursor.fetchall()

    @staticmethod
    def getCarRentalRequestByClientId(index):
        query_str = 'SELECT * FROM "Car_Rental_Requests" WHERE client_id = %(index)s'
        cursor.execute(query_str, {'index': index})
        return cursor.fetchone()

    @staticmethod
    def addCarRentalRequest(data):
        request_data = data
        request_data.append(datetime.date(datetime.now(tz=None)))

        query_str = 'INSERT INTO "Car_Rental_Requests" (client_id, car_id, reason_hire,' \
                    ' rental_period, status, date_create) VALUES (%s, %s, %s, %s, %s, %s)'
        cursor.execute(query_str, request_data)
        gateway.commit()

    @staticmethod
    def setStatusCarRentalRequest(index, status):
        query_str = 'UPDATE "Car_Rental_Requests" SET status = %s WHERE id = %s'
        cursor.execute(query_str, [status, index])
        gateway.commit()

    @staticmethod
    def delCarRentalRequestByClientId(index):
        query_str = 'DELETE FROM "Car_Rental_Requests" WHERE client_id = %(index)s'
        cursor.execute(query_str, {'index': index})
        gateway.commit()


class CloseCarRentalMapper:

    @staticmethod
    def getCloseCarRentalRequestsAll():
        query_str = 'SELECT * FROM "Close_Car_Rental_Requests"'

        cursor.execute(query_str)
        return cursor.fetchall()

    @staticmethod
    def getCloseCarRentalRequestByClientId(index):
        query_str = 'SELECT * FROM "Close_Car_Rental_Requests" WHERE client_id = %(index)s'

        cursor.execute(query_str, {'index': index})
        return cursor.fetchone()

    @staticmethod
    def addCloseCarRentalRequest(data):
        current_date = datetime.date(datetime.now(tz=None))
        request_data = data
        request_data.append(current_date)

        query_str = 'INSERT INTO "Close_Car_Rental_Requests" (client_id, car_id, contract_id,' \
                    'status, date_create) VALUES (%s, %s, %s, %s, %s)'

        cursor.execute(query_str, data)
        gateway.commit()

    @staticmethod
    def setStatusCloseCarRentalRequest(index, status):
        query_str = 'UPDATE "Close_Car_Rental_Requests" SET status = %s WHERE id = %s'
        cursor.execute(query_str, [status, index])
        gateway.commit()

    @staticmethod
    def delCloseCarRentalRequestByClientId(index):
        query_str = 'DELETE FROM "Close_Car_Rental_Requests" WHERE client_id = %(index)s'

        cursor.execute(query_str, {'index': index})
        gateway.commit()


class TechInspectMapper:

    @staticmethod
    def getTechInspectRequestsAll():
        query_str = 'SELECT * FROM "Tech_Inspection_Requests"'

        cursor.execute(query_str)
        return cursor.fetchall()

    @staticmethod
    def getTechInspectRequestById(index):
        query_str = 'SELECT * FROM "Tech_Inspection_Requests" WHERE id = %(index)s'

        cursor.execute(query_str, {'index': index})
        return cursor.fetchone()

    @staticmethod
    def addTechInspectRequest(data):
        query_str = 'INSERT INTO "Tech_Inspection_Requests" (client_id, manager_id, contract_id, ' \
                    'footing, status, date_create) VALUES (%s, %s, %s, %s, %s, %s)'

        cursor.execute(query_str, data)
        gateway.commit()

    @staticmethod
    def setStatusTechInspectRequest(index, status):
        query_str = 'UPDATE "Tech_Inspection_Requests" SET status = %s WHERE id = %s'
        cursor.execute(query_str, [status, index])
        gateway.commit()

    @staticmethod
    def delTechInspectRequestById(index):
        query_str = 'DELETE FROM "Tech_Inspection_Requests" WHERE id = %(index)s'
        cursor.execute(query_str, {'index': index})
        gateway.commit()
