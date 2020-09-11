import json
import os
import emoji
import requests
from django.http import JsonResponse
from django.views import View

from rest_framework.views import APIView

from .models import tb_tutorial_collection
BOT_TOKEN =  "1270864149:AAEABZByVcIWGNvOjainjiIgs2g5zArcKSk"
TELEGRAM_URL = "https://api.telegram.org/bot"
TUTORIAL_BOT_TOKEN = BOT_TOKEN
# os.getenv("TUTORIAL_BOT_TOKEN", "error_token")

import telegram

from telegram.ext.commandhandler import CommandHandler
from telegram.ext.updater import Updater
from telegram.ext.dispatcher import Dispatcher
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
# ====================================================================================

from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.replykeyboardmarkup import ReplyKeyboardMarkup
from telegram.replykeyboardremove import ReplyKeyboardRemove
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters


# from telegram import Bot


# initializing the bot with API
bot = telegram.Bot(token=BOT_TOKEN)


# getting the bot details
print(bot.get_me())


updater = Updater(token=BOT_TOKEN, use_context=True)



# def start(update: Update, context: CallbackContext):
#     """
#     the callback for handling start command
#     """
#     # getting the bot from context
#     # documentation: https://python-telegram-bot.readthedocs.io/en/latest/telegram.bot.html#telegram-bot
#     bot: Bot = context.bot

#     # sending message to the chat from where it has received the message
#     # documentation: https://python-telegram-bot.readthedocs.io/en/latest/telegram.bot.html#telegram.Bot.send_message
#     bot.send_message(chat_id=update.effective_chat.id,
#                      text="You have just entered start command")

# update = Update
# context = CallbackContext

def help_command(chat_id ):
    # defining the keyboard layout
    kbd_layout = [['Option 1', 'Option 2'], ['Option 3', 'Option 4'],["Option 5"]]


    # converting layout to markup
    # documentation: https://python-telegram-bot.readthedocs.io/en/stable/telegram.replykeyboardmarkup.html
    kbd = ReplyKeyboardMarkup(kbd_layout)

    bot.send_message(
        chat_id,
        '1) To receive a list of available currencies press /exchange.\n' +
        '2) Click on the currency you are interested in.\n' +
        '3) You will receive a message containing information regarding the source and the target currencies, ' +
        'buying rates and selling rates.\n' +
        '4) Click “Update” to receive the current information regarding the request. ' +
        'The bot will also show the difference between the previous and the current exchange rates.\n' +
        '5) The bot supports inline. Type @<botusername> in any chat and the first letters of a currency.',
        reply_markup=kbd
    )

    # sending the reply so as to activate the keyboard
    # update.message.reply_text(text="Select Options", reply_markup=kbd)




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

                # Create buttons to slect language:
            keyboard = [[send_report[LANG], view_map[LANG]],[view_faq[LANG], view_about[LANG]]]

            reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)
            self.send_message(msg, t_chat["id"])

        
        elif text == "start":

            # help_command(t_chat["id"])

            updates = bot.get_updates()
            print([u.message.text for u in updates])


        # elif text == "start":
        #     chat["counter"] += 1
        #     tb_tutorial_collection.save(chat)

        #     msg = emoji.emojize("Greetings! I can show you PrivatBank exchange rates.\n" + "To get the exchange rates press /exchange.\n" + "To get help press /help.",use_aliases=True)
        #     self.send_message(msg, t_chat["id"])

        elif text =="exchange":

            chat["counter"] += 1

            keyboard = telegram.InlineKeyboardMarkup(
               [InlineKeyboardButton('USD', callback_data='get-USD')] 
            )

            # keyboard.row(telegram.InlineKeyboardButton('USD', callback_data='get-USD'))
            # keyboard.row(
            #     telegram.InlineKeyboardButton('EUR', callback_data='get-EUR'),
            #     telegram.InlineKeyboardButton('RUR', callback_data='get-RUR')
            #     )
            tb_tutorial_collection.save(chat)
            

            bot.send_message(
                t_chat["id"],
                reply_markup=keyboard
            )


            # self.send_message(msg, t_chat["id"])

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

        elif text == "dp":
            chat["counter"] += 1
            tb_tutorial_collection.save(chat)
            msg = emoji.emojize("""*Daily Parking*
            \nWhat is your vehicle number plate?
            """,use_aliases=True)
            self.send_message(msg, t_chat["id"])

        elif text == "tdp":
            chat["counter"] += 1
            tb_tutorial_collection.save(chat)
            msg = emoji.emojize("""*Topup Daily Parking*
            \nWhat is your vehicle number plate?
            """,use_aliases=True)
            self.send_message(msg, t_chat["id"])

        elif text == "sp":
            chat["counter"] += 1
            tb_tutorial_collection.save(chat)
            msg = emoji.emojize("""*Seasonal Parking*
            \nWhat is your vehicle number plate?
            """,use_aliases=True)
            self.send_message(msg, t_chat["id"])

        elif text == "op":
            chat["counter"] += 1
            tb_tutorial_collection.save(chat)
            msg = emoji.emojize("""*Offstreet Parking*
            \nWhat is your vehicle number plate?
            """,use_aliases=True)
            self.send_message(msg, t_chat["id"])

        elif text == "p":
            chat["counter"] += 1
            tb_tutorial_collection.save(chat)
            msg = emoji.emojize("""*Penalties*
            \nWhat is your vehicle number plate?
            """,use_aliases=True)
            self.send_message(msg, t_chat["id"])

        elif text == "ps":
            chat["counter"] += 1
            tb_tutorial_collection.save(chat)
            msg = emoji.emojize("""*Parking Status*
            \nWhat is your vehicle number plate?
            """,use_aliases=True)
            self.send_message(msg, t_chat["id"])

        elif text == "oz":
            chat["counter"] += 1
            tb_tutorial_collection.save(chat)
            msg = emoji.emojize("""*Offloading Zone*
            \nWhat is your vehicle number plate?
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


# # register a handler (here command handler)
# # documentation: https://python-telegram-bot.readthedocs.io/en/latest/telegram.ext.dispatcher.html#telegram.ext.Dispatcher.add_handler
# dispatcher.add_handler(
#     # it can accept all the telegram.ext.Handler, CommandHandler inherits Handler class
#     # documentation: https://python-telegram-bot.readthedocs.io/en/latest/telegram.ext.commandhandler.html#telegram-ext-commandhandler
#     CommandHandler("start", start))

# # starting polling updates from Telegram
# # documentation: https://python-telegram-bot.readthedocs.io/en/latest/telegram.ext.updater.html#telegram.ext.Updater.start_polling
# updater.start_polling()