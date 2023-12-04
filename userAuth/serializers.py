from rest_framework import serializers
from .models import User
from phonenumber_field.serializerfields import PhoneNumberField
from . import services 

class RegisterSerializers(serializers.Serializer):
  id = serializers.IntegerField(read_only=True)
  first_name = serializers.CharField()
  last_name = serializers.CharField()
  email = serializers.EmailField()
  date_of_birth = serializers.DateField()
  phone_number = PhoneNumberField()
  password = serializers.CharField(write_only=True)
  is_manager = serializers.BooleanField()

  def validate(self, data: "services.UserDataClass" ):
    if data.email:
      if User.objects.filter(email = data.email).exists():
        raise serializers.ValidationError('Email has been already used')
      
    if data.phone_number:
      if User.objects.filter(phone_number = data.phone_number ).exists():
        raise serializers.ValidationError('Phone number has been already used')

    return data
  
  def to_internal_value(self, validated_data):
    data = super().to_internal_value(validated_data)

    return services.UserDataClass(**data)
  
class LoginSerializers(serializers.Serializer):
  email = serializers.EmailField()

  def validate(self, data : "services.UserLoginDataClass") ->  "services.UserLoginDataClass" :
    if  data.email:
      if  User.objects.filter(email = data.email).first() is None:
        raise serializers.ValidationError('Email doesn`t exist, Please register')
      
    return data
  
  
    

  

