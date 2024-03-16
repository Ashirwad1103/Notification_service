from pydantic import BaseModel
from typing import Union
from enums import ChannelEnums




class EmailNotificationPayload(BaseModel):
    sender_email: str 
    receiver_email: str
    password: str
    subject: str
    body: str

class SMSNotificationPayload(BaseModel):
    sender_mob_no: str
    receiver_mob_no: str
    text: str
    

class Message(BaseModel):
    type: ChannelEnums
    # user_id: str
    content: Union[EmailNotificationPayload, SMSNotificationPayload]