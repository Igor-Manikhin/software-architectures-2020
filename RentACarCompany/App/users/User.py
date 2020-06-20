class User:

    def __init__(self, user_data):
        self.__user_id = user_data[0]
        self.__first_name = user_data[1]
        self.__last_name = user_data[2]
        self.__email = user_data[3]
        self.__date_birth = user_data[4]
        self.__login_status = False

    @property
    def userInfo(self):
        return [self.__user_id, self.__first_name, self.__last_name, self.__email, self.__date_birth]

    @property
    def userId(self):
        return self.__user_id

    @property
    def isAuth(self):
        return self.__login_status

    @userInfo.setter
    def userInfo(self, user_data):
        self.__first_name = user_data[0]
        self.__last_name = user_data[1]
        self.__email = user_data[2]
        self.__date_birth = user_data[3]

    @userId.setter
    def userId(self, index):
        self.__user_id = index

    def verifyLogin(self):
        return self.__login_status

    def signIn(self, storage, role, password):
        self.__login_status = storage.userVerifyPassword(self.userId, role, password)

    def signOut(self):
        self.__login_status = False
