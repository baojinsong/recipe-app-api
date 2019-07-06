from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,\
    PermissionsMixin

class UserManager(BaseUserManager):

    def create_user(self,email,password=None,**extra_fields):
        """创建和保存一个用户"""
        user=self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

class User(AbstractBaseUser,PermissionsMixin):
    """用户模型"""
    email=models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    object = UserManager()

    USERNAME_FIELD = "email"



