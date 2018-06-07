from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Create your models here.

class CustomUser(AbstractUser):
    phone_regex = RegexValidator(regex=r'^\d{10}$',
            message="Phone No. must be a valid with 10 digits")

    name = models.CharField(max_length = 255)
    phone_number = models.CharField(validators=[phone_regex],
            max_length=10, blank=False)
    email_remind_status = models.BooleanField(default=False)
    phone_remind_status = models.BooleanField(default=False)
    service_failures = models.TextField(blank=True,null=True)
    email_activation_timestamp = models.DateTimeField(null=True)
    phone_activation_timestamp = models.DateTimeField(null=True)


