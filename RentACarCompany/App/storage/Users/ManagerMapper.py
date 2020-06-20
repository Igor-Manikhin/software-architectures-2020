from App.storage.DataGateway import DataGateway
from App.users.Manager import Manager


class ManagerMapper:
    gateway = DataGateway.conn
    cursor = DataGateway.getCursor()

    @staticmethod
    def getManagersAll():
        query_str = 'SELECT * FROM "Managers"'
        ManagerMapper.cursor.execute(query_str)
        return ManagerMapper.cursor.fetchall()

    @staticmethod
    def getManagerById(index):
        query_str = 'SELECT * FROM "Managers" WHERE id = %(index)s'
        ManagerMapper.cursor.execute(query_str, {'index': index})
        record = ManagerMapper.cursor.fetchone()
        if len(record) == 0:
            print("Запись не найдена!")
        else:
            return record

    @staticmethod
    def getManagerByLogin(login):
        query_str = 'SELECT * FROM "Managers" WHERE "first_name" = %(login)s OR email = %(login)s'
        ManagerMapper.cursor.execute(query_str, {'login': login})
        record = ManagerMapper.cursor.fetchone()
        if len(record) == 0:
            print("Запись не найдена!")
        else:
            manager = Manager(record[:5])
            return manager

    @staticmethod
    def authManager(index, password):
        auth = False
        query_str = 'SELECT password FROM "Managers" WHERE id = %(index)s'
        ManagerMapper.cursor.execute(query_str, {'index': index})
        record = ManagerMapper.cursor.fetchone()

        if password == record[0]:
            auth = True

        return auth

    @staticmethod
    def addManager(data):
        query_str = 'SELECT * FROM "Managers" WHERE email = %(email)s'
        ManagerMapper.cursor.execute(query_str, {'email': data[2]})
        if len(ManagerMapper.cursor.fetchall()) == 0:
            query_str = 'INSERT INTO "Managers" (first_name, last_name, email, birth_date, password) ' \
                        'VALUES (%s, %s, %s, %s, %s)'
            ManagerMapper.cursor.execute(query_str, data)
            ManagerMapper.gateway.commit()
        else:
            print("Запись в базе данных уже существует")

    @staticmethod
    def updateManagerInfoById(index, data):
        data_list = data
        data_list.append(index)

        query_str = 'UPDATE "Managers" SET first_name = %s, last_name = %s, email = %s, birth_date = %s WHERE id = %s'
        ManagerMapper.cursor.execute(query_str, data)
        ManagerMapper.gateway.commit()

    @staticmethod
    def closeConnection():
        ManagerMapper.cursor.close()

