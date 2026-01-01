from django.db import models
from ecommerce.models import BaseModel
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email,password):
        if not email:
            raise ValueError('Email is required!!')
        email=self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_superuser(self,email, password):
        user=self.create_user(email,password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
class User(AbstractBaseUser, PermissionsMixin):
    email=models.EmailField(unique=True)
    full_name=models.CharField(max_length=50, blank=True)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)


    objects=UserManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    class Meta:
        swappable = 'AUTH_USER_MODEL'

    def __str__(self):
        return self.email if not self.full_name else self.full_name
