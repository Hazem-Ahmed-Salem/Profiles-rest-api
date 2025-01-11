from django.db import models
from django.contrib.auth.models import AbstractBaseUser ,BaseUserManager ,PermissionsMixin




class UserProfileManger(BaseUserManager):
    """Manger for user profiles"""

    def create_user(self,email,name,password=None):
        """create a new user profile"""
        
        if not email :
            raise ValueError('users must have an email address')
        email = self.normalize_email(email)
        """Creates a new model for that user"""
        user = self.model(email=email,name=name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,email,name,password):
        """creates a superuser with given details"""

        user = self.create_user(email,name,password)
        user.is_superuser= True
        user.is_staff = True
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser,PermissionsMixin):
    """DataBase Model for Users in the system"""

    email           = models.EmailField(max_length=255,unique=True)
    name            = models.CharField(max_length=255)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)

    objects = UserProfileManger()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrive full name of the user"""
        return self.name
    
    def get_short_name(self):
        """Retrive short name of the user"""
        self.name

    def __str__(self):
        """Return string representation of our user"""
        return self.email


