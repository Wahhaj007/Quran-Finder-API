from fastapi import FastAPI
from app.routes import teacherRoutes

app = FastAPI()


app.include_router(teacherRoutes.router, prefix="/teacher", tags=["teacher"])
@app.get("/")
async def root():    
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

@app.get("/get-all-sessions")
async def get_all():
    return "list_of_available_sessions_for_teacher_id"



