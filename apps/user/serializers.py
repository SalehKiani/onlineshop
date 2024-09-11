from rest_framework import serializers


class GeneratePhoneOTPSerializer(serializers.Serializer):
    phone_number = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, required=True)

class GenerateEmailOTPSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=8, required=True)

class VerifyPhoneOTPSerializer(serializers.Serializer):
    phone_number = serializers.CharField(required=True)
    code = serializers.CharField(min_length=6, max_length=6, required=True)

class VerifyEmailOTPSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    code = serializers.CharField(min_length=6, max_length=6, required=True)