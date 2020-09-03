from django.urls import path
from telegrambot import views

from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    # path('', views.SendMessageAPIView.as_view()),
    path('webhook/', csrf_exempt(views.TutorialBotView.as_view())),
]