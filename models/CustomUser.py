from typing import Any, Optional
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    """
    Custom manager for CustomUser model with methods to create regular and super users.
    """

    def create_user(self, email: str, password: Optional[str] = None, **extra_fields: Any) -> 'CustomUser':
        """
        Create and return a regular user with the given email and password.
        
        Parameters
        ----------
        email : str
            The email address of the user.
        password : Optional[str]
            The password for the user.
        **extra_fields : Any
            Additional fields for the user.
        
        Returns
        -------
        CustomUser
            The created user instance.
        
        Raises
        ------
        ValueError
            If the email is not provided.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email: str, password: Optional[str] = None, **extra_fields: Any) -> 'CustomUser':
        """
        Create and return a superuser with the given email and password.
        
        Parameters
        ----------
        email : str
            The email address of the superuser.
        password : Optional[str]
            The password for the superuser.
        **extra_fields : Any
            Additional fields for the superuser.
        
        Returns
        -------
        CustomUser
            The created superuser instance.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model that extends AbstractBaseUser and PermissionsMixin.
    
    Attributes
    ----------
    email : EmailField
        The email address of the user.
    first_name : CharField
        The first name of the user.
    last_name : CharField
        The last name of the user.
    date_of_birth : DateField
        The date of birth of the user.
    phone_number : CharField
        The phone number of the user.
    address : CharField
        The address of the user.
    is_active : BooleanField
        Indicates whether the user is active.
    is_staff : BooleanField
        Indicates whether the user is a staff member.
    date_joined : DateTimeField
        The date and time when the user joined.
    """
    email: models.EmailField = models.EmailField(unique=True)
    first_name: models.CharField = models.CharField(max_length=30, blank=True)
    last_name: models.CharField = models.CharField(max_length=30, blank=True)
    date_of_birth: Optional[models.DateField] = models.DateField(blank=True, null=True)
    phone_number: Optional[models.CharField] = models.CharField(max_length=15, blank=True, null=True)
    address: models.CharField = models.CharField(max_length=255, blank=True)
    is_active: models.BooleanField = models.BooleanField(default=True)
    is_staff: models.BooleanField = models.BooleanField(default=False)
    date_joined: models.DateTimeField = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD: str = 'email'
    REQUIRED_FIELDS: list[str] = []

    def __str__(self) -> str:
        """
        Return a string representation of the user.
        
        Returns
        -------
        str
            The email of the user.
        """
        return self.email
