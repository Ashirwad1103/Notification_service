from enums import ChannelEnums
from notification_channel import NotificationInterface, Email
from request_schema import Message
from notification_handler import NotificationHandlerInterface, EmailHandler

class NotificationService: 
    def send_notification(self, message: Message):
        notification_handler = NotificationInterface()
        if message.type == ChannelEnums.EMAIL:
            notification_handler.set_notification_channel(notification_channel=Email())
        # elif condition for sms channel goes here 


        notification_handler.send_notification(message=message)

class NotificationHandlerService: 
    def send(self, message):
        notification_handler = NotificationHandlerInterface()
        if message.type == ChannelEnums.EMAIL:
            notification_handler.set_notification_handler(notification_handler=EmailHandler())
        # elif condition for sms channel goes here 
            
        notification_handler.send(message=message)
 


notification_service = NotificationService()
notification_handler_service = NotificationHandlerService()
