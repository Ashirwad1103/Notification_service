from main import app
from request_schema import Message
from notificatiton_service import notification_service


@app.post("/send")
async def send(message: Message):
    response = notification_service.send_notification(message=message)
    return response
