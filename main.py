
from fastapi import FastAPI
from request_schema import Message
from notificatiton_service import notification_service


app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World"}

@app.post("/send")
async def send(message: Message):
    response = notification_service.send_notification(message=message)
    return response