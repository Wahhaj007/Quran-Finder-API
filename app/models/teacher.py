from typing import List, Optional
from .user import User
from .session import Session


class Teacher(User):
    def __init__(self, session: Optional[Session] = None, bio: str = ""):
        super().__init__()
        self.__sessions: List[Session] = []
        if session:
            self.__sessions.append(session)
        self.__bio = bio

    def getBio(self):
        return self.__bio

    def setBio(self, bio: str):
        self.__bio = bio

    def getSessions(self):
        return self.__sessions

    def createSession(self, session: Session):
        self.__sessions.append(session)

    def setSessions(self, sessions: List[Session]):
        self.__sessions = sessions

    def __str__(self):
        return f"{self.getFirstName()} {self.getLastName()}"
