from App.users.User import User
from App.report.Report import Report


class Master(User):

    def createReport(self, storage, client_id):
        contract = storage.getContract(client_id)
        print(contract)


    def getIncomingRequests(self, storage):
        return storage.getAllRequests('Tech_Inspection')
