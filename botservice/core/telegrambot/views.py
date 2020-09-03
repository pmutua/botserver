import json
import os
import emoji
import requests
from django.http import JsonResponse
from django.views import View

from rest_framework.views import APIView

from .models import tb_tutorial_collection
BOT_TOKEN =  '1270864149:AAEABZByVcIWGNvOjainjiIgs2g5zArcKSk'
TELEGRAM_URL = "https://api.telegram.org/bot"
TUTORIAL_BOT_TOKEN = BOT_TOKEN
# os.getenv("TUTORIAL_BOT_TOKEN", "error_token")


# https://api.telegram.org/bot<token>/setWebhook?url=<url>/webhooks/tutorial/
class TutorialBotView(APIView):
    def post(self, request, *args, **kwargs):
        t_data = json.loads(request.body)
        t_message = t_data["message"]
        t_chat = t_message["chat"]

        try:
            text = t_message["text"].strip().lower()
        except Exception as e:
            return JsonResponse({"ok": "POST request processed"})

        text = text.lstrip("/")

        print(t_data)
        chat = tb_tutorial_collection.find_one({"chat_id": t_chat["id"]})
        if not chat:
            chat = {
                "chat_id": t_chat["id"],
                "counter": 0
            }
            response = tb_tutorial_collection.insert_one(chat)
            # we want chat obj to be the same as fetched from collection
            chat["_id"] = response.inserted_id

        if text == "+":
            chat["counter"] += 1
            tb_tutorial_collection.save(chat)
            msg = f"Number of '+' messages that were parsed: {chat['counter']}"
            self.send_message(msg, t_chat["id"])

        elif text == "help":
            chat["counter"] += 1
            tb_tutorial_collection.save(chat)

            msg = emoji.emojize("""*Hi! Welcome to RevenueSure*
            \nYou can give me the following commands:
            \n*Commands:*
            \n1. parking - go to parking
            \n2. sbp - go to single business permits
            \n3. lr - go to landrates
            \n4. rent - go to rent section
            \n5. bill - pay a specific bill
            \n6. me - go to your profile
            \n7. help - view commands
            """,use_aliases=True)
            self.send_message(msg, t_chat["id"])

        elif text == "parking":
            chat["counter"] += 1
            tb_tutorial_collection.save(chat)
            msg = emoji.emojize("""*select option*
            \nYou can give me the following commands:
            \n1. Daily Parking
            \n2. Topup Daily Parking
            \n3. Seasonal Parking
            \n4. Offstreet Parking
            \n5. Penalties
            \n6. Parking Status
            \n7. Offloading Zone
            """,use_aliases=True)
            self.send_message(msg, t_chat["id"])

        elif text == "parking":
            chat["counter"] += 1
            tb_tutorial_collection.save(chat)
            msg = emoji.emojize("""*select option*
            \nYou can give me the following commands:
            \n1. *dp* -  Daily Parking
            \n2. *tdp* - Topup Daily Parking
            \n3. *sp* - Seasonal Parking
            \n4. *op* - Offstreet Parking
            \n5. *p* - Penalties
            \n6. *ps* - Parking Status
            \n7. *oz* - Offloading Zone
            """,use_aliases=True)
            self.send_message(msg, t_chat["id"])
        elif text == "restart":
            blank_data = {"counter": 0}
            chat.update(blank_data)
            tb_tutorial_collection.save(chat)
            msg = "The Tutorial bot was restarted"
            self.send_message(msg, t_chat["id"])
        else:
            msg = "Unknown command"
            self.send_message(msg, t_chat["id"])

        return JsonResponse({"ok": "POST request processed"})

    @staticmethod
    def send_message(message, chat_id):
        data = {
            "chat_id": chat_id,
            "text": message,
            "parse_mode": "Markdown",
        }
        response = requests.post(
            f"{TELEGRAM_URL}{TUTORIAL_BOT_TOKEN}/sendMessage", data=data
        )