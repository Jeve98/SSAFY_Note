from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# Custom User Model로 대체 (커스텀 하지 않더라도 상속 받을 것을 권장)
class User(AbstractUser):
    pass