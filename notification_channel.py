from abc import ABC, abstractmethod
from request_schema import Message
import re
from notification_handler import NotificationHandlerInterface, EmailHandler



class NotificationChannel(ABC):
    @abstractmethod
    def send_notification(self, message: Message):
        pass


class Email(NotificationChannel):
    def __init__(self):
        self.topic = ""

    def check_is_email_valid(self, email: str):
        pattern = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    def send_notification(self, message: Message): 
        if not self.check_is_email_valid(email=message.content.sender_email):
            return
        if not self.check_is_email_valid(email=message.content.receiver_email):
            return 
        
        notication_handler_interface = NotificationHandlerInterface(EmailHandler())
        notication_handler_interface.notification_handler.send.delay(message)
        


        pass

class SMS(NotificationChannel):
    def __init__(self):
        self.topic = ""

    def send_notification(self, message: Message):
        pass


class NotificationInterface:
    def set_notification_channel(self, notification_channel: NotificationChannel):
        self.notification_channel = notification_channel

    def send_notification(self, message: Message):
        self.notification_channel.send_notification(message=message)
        pass
