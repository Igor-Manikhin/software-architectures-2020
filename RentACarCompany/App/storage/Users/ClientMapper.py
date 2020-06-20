from App.storage.DataGateway import DataGateway
from App.users.Client import Client


class ClientMapper:
    gateway = DataGateway.conn
    cursor = DataGateway.getCursor()

    @staticmethod
    def getClientsAll():
        query_str = 'SELECT * FROM "Clients"'
        ClientMapper.cursor.execute(query_str)
        return ClientMapper.cursor.fetchall()

    @staticmethod
    def getClientById(index):
        query_str = 'SELECT * FROM "Clients" WHERE id = %(index)s'
        ClientMapper.cursor.execute(query_str, {'index': index})
        record = ClientMapper.cursor.fetchone()
        if len(record) == 0:
            print("Запись не найдена!")
        else:
            return record

    @staticmethod
    def getClientByLogin(login):
        query_str = 'SELECT * FROM "Clients" WHERE "first_name" = %(login)s OR email = %(login)s'
        ClientMapper.cursor.execute(query_str, {'login': login})
        record = ClientMapper.cursor.fetchone()
        if len(record) == 0:
            print("Запись не найдена!")
        else:
            client = Client(record[:5])
            return client

    @staticmethod
    def authClient(index, password):
        auth = False
        query_str = 'SELECT password FROM "Clients" WHERE id = %(index)s'
        ClientMapper.cursor.execute(query_str, {'index': index})
        record = ClientMapper.cursor.fetchone()

        if password == record[0]:
            auth = True

        return auth

    @staticmethod
    def addClient(data):
        query_str = 'SELECT * FROM "Clients" WHERE email = %(email)s'
        ClientMapper.cursor.execute(query_str, {'email': data[2]})
        records = ClientMapper.cursor.fetchall()
        if len(records) == 0:
            query_str = 'INSERT INTO "Clients" (first_name, last_name, email, birth_date, password) VALUES (%s, %s, ' \
                        '%s, %s, %s) '
            ClientMapper.cursor.execute(query_str, data)
            ClientMapper.gateway.commit()
        else:
            print("Запись в базе данных уже существует")

    @staticmethod
    def updateClientInfoById(index, data):
        data_list = data
        data_list.append(index)

        query_str = 'UPDATE "Clients" SET first_name = %s, last_name = %s, email = %s, birth_date = %s WHERE id = %s'
        ClientMapper.cursor.execute(query_str, data)
        ClientMapper.gateway.commit()

    @staticmethod
    def closeConnection():
        ClientMapper.cursor.close()
