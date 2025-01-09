from ..models.teacher import Teacher
from ..models.session import Session
from fastapi import APIRouter, Body
from typing import List
from pydantic import BaseModel
from fastapi.responses import JSONResponse

router = APIRouter()

# Define the Pydantic model for session data
class SessionData(BaseModel):
    openTimeSlots: List[str]
    receivedRequests: List[str]
    genderRestriction: str

@router.post("/createSession/{teacher_id}")
async def create_session(teacher_id: int, session_data: SessionData):
    try:
        # Create a new Session object
        new_session = Session(**session_data.model_dump())
        
        # Retrieve the teacher (replace with actual database logic)
        teacher = get_teacher_by_id(teacher_id)
        if not teacher:
            return JSONResponse(status_code=404, content={"message": "Teacher not found"})
        
        # Add the session to the teacher
        teacher.createSession(new_session)
        
        return JSONResponse(status_code=201, content={"message": "Session created successfully"})
    except Exception as e:
        print(e)
        return JSONResponse(status_code=400, content={"message": "Failed to create session", "error": str(e)})

# Stub for getting a teacher by ID (replace with actual database retrieval logic)
def get_teacher_by_id(teacher_id: int) -> Teacher:
    # In a real application, fetch the teacher from a database
    return Teacher()  # Placeholder
