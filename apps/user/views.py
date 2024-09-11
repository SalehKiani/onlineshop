from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.user.services.OTP import generate_otp
from .serializers import (GeneratePhoneOTPSerializer,
                         GenerateEmailOTPSerializer,
                         VerifyEmailOTPSerializer,
                         VerifyPhoneOTPSerializer)
from apps.user.services.user import UserService
from apps.user.services.OTP import generate_otp, verify_otp
from apps.user.services.token import TokenService


# Create your views here.
class RegisterByPhoneView(APIView):
    serializer_class = GeneratePhoneOTPSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        user = UserService.create_user(phone_number=serializer.validated_data['phone_number'], password=serializer.validated_data['password'])

        # Generate OTP
        otp_obj = generate_otp(user)
        otp = otp_obj.otp

        # Send OTP via SMS
        # mock
        print(otp)

        return Response("otp has been sent", status=status.HTTP_200_OK)


class RegisterByEmailView(APIView):
    serializer_class = GenerateEmailOTPSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        user = UserService.create_user(email=serializer.validated_data['email'], password=serializer.validated_data['password'])

        # Generate OTP
        otp_obj = generate_otp(user)
        otp = otp_obj.otp

        # Send OTP via Email
        # mock
        print(otp)

        return Response("otp has been sent", status=status.HTTP_200_OK)


class VerifyPhoneOTPView(APIView):
    def post(self, request):
        serializer = VerifyPhoneOTPSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        result = verify_otp(phone_number=serializer.validated_data['phone_number'], otp=serializer.validated_data['code'])

        if not result:
            return Response("Invalid OTP", status=status.HTTP_400_BAD_REQUEST)


        user_obj = UserService.get_user(phone_number=serializer.validated_data['phone_number'])
        access, refresh = TokenService.generate(user_obj)

        return Response({'refresh': refresh, 'access': access}, status=status.HTTP_200_OK)


class VerifyEmailOTPView(APIView):
    def post(self, request):
        serializer = VerifyEmailOTPSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        result = verify_otp(email=serializer.validated_data['email'], otp=serializer.validated_data['code'])

        if not result:
            return Response("Invalid OTP", status=status.HTTP_400_BAD_REQUEST)


        user_obj = UserService.get_user(email_address=serializer.validated_data['email'])
        access, refresh = TokenService.generate(user_obj)

        return Response({'refresh': refresh, 'access': access}, status=status.HTTP_200_OK)