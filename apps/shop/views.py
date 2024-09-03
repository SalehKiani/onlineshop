from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProductSerializer
from .selectors import selectors
from apps.utils.OTP import generate_otp, verify_otp
from .models import CustomUser

class ProductListAPIView(APIView):

    def get_queryset(self):
        category = self.request.query_params.get('category')
        search = self.request.query_params.get('search')
        return category, search

    def get(self, request):
        category, search = self.get_queryset()
        products = selectors.product_list_fetch(category, search)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class OTPView(APIView):

    @staticmethod
    def post(request):
        phone_number = request.data.get('phone_number')
        user = CustomUser.objects.get(phone_number=phone_number)
        otp = generate_otp(user)
        # Send the OTP via SMS or email
        return Response({'message': 'OTP sent successfully'})


class VerifyOTPView(APIView):

    @staticmethod
    def post(request):
        phone_number = request.data.get('phone_number')
        otp = request.data.get('otp')
        user = CustomUser.objects.get(phone_number=phone_number)
        if verify_otp(user, otp):
            return Response({'message': 'OTP verified successfully'})
        else:
            return Response({'message': 'Invalid OTP'}, status=400)
