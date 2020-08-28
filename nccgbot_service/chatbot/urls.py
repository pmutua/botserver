from django.conf.urls import url
from chatbot.views import ChatterBotApiView


urlpatterns = [
    url(r'^chatbot/', ChatterBotApiView.as_view(), name='chatbot'),
]