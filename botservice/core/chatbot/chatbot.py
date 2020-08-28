from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.ext.django_chatterbot import settings

chatterbot = ChatBot(**settings.CHATTERBOT)


