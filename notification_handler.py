import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from abc import ABC, abstractmethod
from celery_app import celery_app
from request_schema import Message


class NotificationHandler(ABC):
    @abstractmethod
    @celery_app.task
    def send(self, message):
        pass


class EmailHandler(NotificationHandler):
    def __init__(self):
        self.smtp_server = ""
        self.smtp_port = ""

    def create_email_message(self, sender_email, receiver_email, subject, body):
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        
        body = body
        
        message.attach(MIMEText(body, "plain"))
        return message

    @celery_app.task
    def send(self, message):
        sender_email = message.sender_email
        receiver_email = message.receiver_email
        password = message.password
        subject = message.subject
        body = message.body

        message = self.create_email_message(sender_email=sender_email, receiver_email=receiver_email, subject=subject, body=body)
        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(message)

        pass

class SMSHandler(NotificationHandler):
    def __init__(self):
        pass

    def send(self, message):
        pass

class NotificationHandlerInterface: 
    def __init__(self, notification_handler: NotificationHandler) -> None:
        self.notification_handler = notification_handler 

    def send(self, message: Message):
        self.notification_handler.send(message=message)
        pass