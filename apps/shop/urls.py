from django.urls import path
from . import views

urlpatterns = [
        path('products/', views.ProductListAPIView.as_view()),
        path('otp/', views.OTPView.as_view()),
        path('verify-otp/', views.VerifyOTPView.as_view()),
]
