from django.urls import path
from . import views

urlpatterns = [
    path('register/email/request/', views.RegisterByEmailView.as_view(), name='register-email-request'),
    path('register/email/verify/', views.VerifyEmailOTPView.as_view(), name='register-email-verify'),
    path('register/phone-number/request/', views.RegisterByPhoneView.as_view(),
         name='register-phone-number-request'),
    path('register/phone-number/verify/', views.VerifyPhoneOTPView.as_view(),
         name='register-phone-number-verify'),
]
