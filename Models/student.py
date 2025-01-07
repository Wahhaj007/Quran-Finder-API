from user import User
from enum import Enum

class Skill(Enum):
    Beginner = "beginner"
    Intermediate = "intermediate"
    Advanced = "advanced"


class Student(User):
    __scheduldAppointment : list
    skillLevel : Skill
    __reqestSent: list

    def __init__(self,skillLevel:Skill):
        super().__init__()
        self.__scheduldAppointment = []
        self.skillLevel = skillLevel
        self.__reqestSent = [] 

    def setSkillLevel(self,skillLevel):
        self.skillLevel = skillLevel

    def getSkillLevel(self):    
        return self.skillLevel

    def setScheduldAppointment(self,scheduldAppointment):
        self.__scheduldAppointment = scheduldAppointment

    def getScheduldAppointment(self):
        return self.__scheduldAppointment

    def setReqestSent(self,reqestSent):
        self.__reqestSent = reqestSent

    def getReqestSent(self):
        return self.__reqestSent


    
