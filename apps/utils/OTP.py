from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from apps.shop.models import OTP
import random


def generate_otp(user):
    otp = OTP.objects.create(user=user, otp=str(random.randint(100000, 999999)), expiry=timezone.now() + timezone.timedelta(minutes=10))
    return otp

def verify_otp(user, otp):
    try:
        otp_obj = OTP.objects.get(user=user, otp=otp)
        if otp_obj.expiry > timezone.now():
            return True
        else:
            return False
    except ObjectDoesNotExist:
        return False
