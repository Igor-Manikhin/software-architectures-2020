from App.storage.DataGateway import DataGateway
from App.users.Master import Master


class MasterMapper:
    gateway = DataGateway.conn
    cursor = DataGateway.getCursor()

    @staticmethod
    def getMastersAll():
        query_str = 'SELECT * FROM "Masters"'
        MasterMapper.cursor.execute(query_str)
        return MasterMapper.cursor.fetchall()

    @staticmethod
    def getMasterById(index):
        query_str = 'SELECT * FROM "Masters" WHERE id = %(index)s'
        MasterMapper.cursor.execute(query_str, {'index': index})
        record = MasterMapper.cursor.fetchone()
        if len(record) == 0:
            print("Запись не найдена!")
        else:
            return record

    @staticmethod
    def getMasterByLogin(login):
        query_str = 'SELECT * FROM "Masters" WHERE "first_name" = %(login)s OR email = %(login)s'
        MasterMapper.cursor.execute(query_str, {'login': login})
        record = MasterMapper.cursor.fetchone()
        if len(record) == 0:
            print("Запись не найдена!")
        else:
            master = Master(record[:5])
            return master

    @staticmethod
    def authMaster(index, password):
        auth = False
        query_str = 'SELECT password FROM "Masters" WHERE id = %(index)s'
        MasterMapper.cursor.execute(query_str, {'index': index})
        record = MasterMapper.cursor.fetchone()

        if password == record[0]:
            auth = True

        return auth

    @staticmethod
    def addMaster(data):
        query_str = 'SELECT * FROM "Masters" WHERE email = %(email)s'
        MasterMapper.cursor.execute(query_str, {'email': data[2]})
        if len(MasterMapper.cursor.fetchall()) == 0:
            query_str = 'INSERT INTO "Masters" (first_name, last_name, email, birth_date, password) ' \
                        'VALUES (%s, %s, %s, %s, %s)'
            MasterMapper.cursor.execute(query_str, data)
            MasterMapper.gateway.commit()
        else:
            print("Запись в базе данных уже существует")

    @staticmethod
    def updateMasterInfoById(index, data):
        data_list = data
        data_list.append(index)

        query_str = 'UPDATE "Masters" SET first_name = %s, last_name = %s, email = %s, birth_date = %s WHERE id = %s'
        MasterMapper.cursor.execute(query_str, data)
        MasterMapper.gateway.commit()

    @staticmethod
    def closeConnection():
        MasterMapper.cursor.close()

