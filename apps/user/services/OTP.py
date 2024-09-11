from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from apps.user.models import OTP, User
import random


def generate_otp(user):
    OTP.objects.filter(user=user).delete()
    otp = OTP.objects.create(user=user, otp=str(random.randint(100000, 999999)), expiry=timezone.now() + timezone.timedelta(minutes=2))
    return otp

def verify_otp(email: str = None, phone_number:str = None, otp:str = None) -> bool:
    try:
        if email:
            user = User.objects.get(email=email)
        elif phone_number:
            user = User.objects.get(phone_number=phone_number)
        else:
            return False
        otp_obj = OTP.objects.get(user=user, otp=otp)
        if otp_obj.expiry > timezone.now():
            return True
        else:
            return False
    except ObjectDoesNotExist:
        return False
