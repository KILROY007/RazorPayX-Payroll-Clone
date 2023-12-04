from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField

class CustomUserManager(BaseUserManager):
  def create_user(self, email , password = None , **extra_fields ):
       
        if not email:
            raise ValueError('Users must have an email address')
      
        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

  def create_superuser(self,  email, password=None ,  **extra_fields):
      
      extra_fields.setdefault('is_staff', True)
      extra_fields.setdefault('is_superuser', True)
      extra_fields.setdefault('is_active', True)
      extra_fields.setdefault('date_of_birth', '2000-01-01')

      return self.create_user(
          email,
          password,
          **extra_fields
      )

class User(AbstractUser):
  username = None
  first_name = models.CharField(verbose_name="First Name", max_length=255)
  last_name = models.CharField(verbose_name="Last Name", max_length=255)
  email = models.EmailField(verbose_name="Email", max_length=255, unique=True)
  password = models.CharField(max_length=255)
  date_of_birth = models.DateField(verbose_name="Date of Birth")
  phone_number = PhoneNumberField(region="IN", unique= True , )
  is_manager = models.BooleanField(default= False, verbose_name= "Is Manager")

  objects = CustomUserManager()

  USERNAME_FIELD = "email"
  REQUIRED_FIELDS = []
    
