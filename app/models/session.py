class Session:
    __openTimeSlots : list
    __recievedRequests : list
    __GenderRestriction : str
    __sessionID : str

    def __init__(self, openTimeSlots: list, recievedRequests: list, GenderRestriction: str):
        self.__openTimeSlots = openTimeSlots
        self.__recievedRequests = recievedRequests
        self.__GenderRestriction = GenderRestriction
        self.__sessionID = ""
    
    def getOpenTimeSlots(self):
        return self.__openTimeSlots

    def getRecievedRequests(self):
        return self.__recievedRequests

    def getGenderRestriction(self):
        return self.__GenderRestriction
    
    def setOpenTimeSlots(self, openTimeSlots):
        self.__openTimeSlots = openTimeSlots

    def setRecievedRequests(self, recievedRequests):
        self.__recievedRequests = recievedRequests

    def setGenderRestriction(self, GenderRestriction):
        self.__GenderRestriction = GenderRestriction

    def __str__(self):
        return f"{self.__openTimeSlots} {self.__recievedRequests} {self.__GenderRestriction}"

    def __repr__(self):
        return f"{self.__openTimeSlots} {self.__recievedRequests} {self.__GenderRestriction}"
    
