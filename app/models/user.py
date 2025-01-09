class User:
    def __init__(self, firstName: str, lastName: str, 
                email: str, id: int, bio: str, 
                timeZone: str):

        self.__firstName = firstName
        self.__lastName = lastName
        self.__email = email
        self.__id = id
        self.__bio = bio
        self.timeZone = timeZone

    def getFirstName(self):
        return self.__firstName

    def getLastName(self):
        return self.__lastName

    def getEmail(self):
        return self.__email

    def getId(self):        
        return self.__id

    def getBio(self):
        return self.__bio

    def getFullName(self):
        return f"{self.__firstName} {self.__lastName}"

    def __str__(self):  
        return f"{self.__firstName} {self.__lastName}"
    
    

