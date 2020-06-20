from App.storage.DataGateway import DataGateway
from App.contract.Contract import Contract
from datetime import datetime


class ContractMapper:
    gateway = DataGateway.conn
    cursor = DataGateway.getCursor()

    @staticmethod
    def getContractsAll():
        query_str = 'SELECT * FROM "Contracts"'
        ContractMapper.cursor.execute(query_str)
        records = ContractMapper.cursor.fetchall()

        return records

    @staticmethod
    def getContractByClientId(index):
        query_str = 'SELECT * FROM "Contracts" WHERE client_id = %(index)s'
        ContractMapper.cursor.execute(query_str, {'index': index})
        record = ContractMapper.cursor.fetchone()
        main_data = record[1:6]
        main_data.append(record[7])
        contract = Contract(main_data)
        contract.contractId = record[0]
        contract.contractStatus = record[6]

        return contract

    @staticmethod
    def addContract(data):

        query_str = 'INSERT INTO "Contracts" (client_id, manager_id, car_id, rental_period, ' \
                    'reason_hire, status, date_create) VALUES (%s, %s, %s, %s, %s, %s, %s)'
        ContractMapper.cursor.execute(query_str, data)
        ContractMapper.gateway.commit()

    @staticmethod
    def updateContractStatusById(index, status):
        query_str = 'UPDATE "Contracts" SET status = %s WHERE id = %s'
        ContractMapper.cursor.execute(query_str, [status, index])
        ContractMapper.gateway.commit()

    @staticmethod
    def closeConnection():
        ContractMapper.cursor.close()
