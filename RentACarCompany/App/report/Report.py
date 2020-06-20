class Report:

    def __init__(self, master, contract):
        self.__report_id = None
        self.__contract_info = contract.contrac_info
        self.__master_info = master.user_info
        self.__description = dict(TechDamages={}, PhysDamages={})

    @property
    def reportId(self):
        return self.__report_id

    @property
    def reportInfo(self):
        return {
            'mechanicInfo': self.__master_Info,
            'description': self.__description
        }

    @reportId.setter
    def reportId(self, index):
        self.__report_id = index

    def addTechDamage(self, damage_info, number):
        self.__description['TechDamages'][str(number)] = damage_info

    def addPhysDamage(self, damage_info, number):
        self.__description['PhysDamages'][str(number)] = damage_info
