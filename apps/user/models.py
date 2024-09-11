from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.utils.validators import validate_phone_number

class User(AbstractUser):
    email = models.CharField(max_length=100, unique=True, null=True, blank=True)
    phone_number = models.IntegerField(unique=True, null=True, blank=True, validators=[validate_phone_number])

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

        ordering = ['-date_joined']



class OTP(models.Model):
    user = models.ForeignKey(User, related_name='otps', on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    expiry = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"OTP for {self.user.username}"
