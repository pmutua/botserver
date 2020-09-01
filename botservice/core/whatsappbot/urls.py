from django.urls import path
from whatsappbot import views

urlpatterns = [
    path('', views.ChatAPIView.as_view()),
    path('callback', views.CallBackAPIView.as_view()),
]