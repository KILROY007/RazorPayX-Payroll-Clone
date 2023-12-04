import dataclasses
from typing import TYPE_CHECKING
from . import models
import jwt
import datetime
from django.conf import settings

if TYPE_CHECKING :
  from .models import User

@dataclasses.dataclass
class UserDataClass:
  date_of_birth : str 
  phone_number : str
  is_manager : bool 
  first_name :str 
  last_name : str 
  email : str 
  password : str  = None
  id: int = None

  @classmethod
  def from_instance(cls, user: "User") -> "UserDataClass":
    return cls(
        first_name=user.first_name,
        last_name = user.last_name,
        email = user.email,
        phone_number = user.phone_number,
        date_of_birth = user.date_of_birth,
        is_manager = user.is_manager,
        id= user.id,
    )
  
def create_user(user_dc: "UserDataClass") -> "UserDataClass":
  instance = models.User(
      first_name=user_dc.first_name ,
      last_name= user_dc.last_name ,
      email= user_dc.email ,
      date_of_birth= user_dc.date_of_birth ,
      phone_number= user_dc.phone_number ,
      is_manager= user_dc.is_manager
  )
  
  if user_dc.password is not None:
      instance.set_password(user_dc.password)

  instance.save()

  return UserDataClass.from_instance(instance)

@dataclasses.dataclass
class UserLoginDataClass:
  email:str
  password:str

  
   
def user_email_validator(email: str) -> "User":
    user = models.User.objects.filter(email=email).first()

    return user

def create_token(user_id: int) -> str:
    payload = dict(
        id=user_id,
        exp=datetime.datetime.utcnow() + datetime.timedelta(hours=24),
        iat=datetime.datetime.utcnow(),
    )
    token = jwt.encode(payload, settings.JWT_SECRET, algorithm="HS256")

    return token