from typing import Optional

from apps.user.models import User


class UserService:
    @staticmethod
    def create_user(email: str = None, phone_number: str = None, password: str = None) -> User:
        if (email is None and phone_number is None):
            raise ValueError('one of email of phone number is required')
        elif password is None:
            raise ValueError('password is required')

        if email is not None and phone_number is None:
            username = email
        elif phone_number is not None and email is None:
            username = str(phone_number)
        else:
            raise ValueError('user is made by one of email or phone number!')

        user_obj = User.objects.create(
            username=username,
            password=password,
            email=email,
            phone_number=phone_number,
        )

        return user_obj

    @staticmethod
    def get_user(email_address: str = None, phone_number: int = None) -> Optional[User]:
        user_obj = User.objects.filter(
            email=email_address,
            phone_number=phone_number,
        )

        if user_obj:
            return user_obj[0]

        return None
