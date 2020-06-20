from App.storage.DataGateway import DataGateway


class RentsHistoryMapper:
    gateway = DataGateway.conn
    cursor = DataGateway.getCursor()

    @staticmethod
    def getRentsHistoryAllClients():
        query_str = 'SELECT * FROM "Rentals_History"'
        return RentsHistoryMapper.cursor.execute(query_str)

    @staticmethod
    def getRentsHistoryClientById(index):
        query_str = 'SELECT * FROM "Rentals_History" WHERE client_id = %(index)s'
        RentsHistoryMapper.cursor.execute(query_str, {'index': index})
        return RentsHistoryMapper.cursor.fetchall()

    @staticmethod
    def addNewHistoryRecord(data):
        query_str = 'INSERT INTO "Rentals_History" (client_id, manager_id, car_id, contract_id, date_begin_rent,' \
                    ' date_end_rent) VALUES (%s, %s, %s, %s, %s, %s)'
        RentsHistoryMapper.cursor.execute(query_str, data)
        RentsHistoryMapper.gateway.commit()

    @staticmethod
    def delRentsHistoryCliendById(index):
        query_str = 'DELETE FROM "Rentals_History" WHERE client_id = %(index)s'
        RentsHistoryMapper.cursor.execute(query_str, {'index': index})
        RentsHistoryMapper.gateway.commit()

    @staticmethod
    def closeConnection():
        RentsHistoryMapper.cursor.close()