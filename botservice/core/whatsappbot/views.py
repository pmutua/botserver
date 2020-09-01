from twilio.twiml.messaging_response import MessagingResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import requests
import datetime
import emoji
import random
import json

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import os
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC1371371565de40e129313dea78dc79d5'
auth_token = 'de0a12b5d1acfaee6b93f2f3e7a57f37'
client = Client(account_sid, auth_token)


class ChatAPIView(APIView):
    def post(self, request, format=None):

        # print(request.data)
        # retrieve incoming message from POST request in lowercase
        incoming_msg = request.data['Body'].lower()

        # create Twilio XML response
        resp = MessagingResponse()
        msg = resp.message()

        print(request.data)

        # responded = False

        if incoming_msg == 'hello':
            response = emoji.emojize("""*Hi! Welcome to RevenueSure*
            \nYou can give me the following commands:
            \n*Commands:*
            \n1. parking - go to parking
            \n2. sbp - go to single business permits
            \n3. lr - go to landrates
            \n4. rent - go to rent section
            \n5. bill - pay a specific bill
            \n6. me - go to your profile
            \n7. help - view commands
            """,
                                     use_aliases=True)

            body = msg.body(response)

            response = client.messages.create(
                body=response,
                from_='whatsapp:+14155238886',
                #   status_callback='https://feeb1763bc3e.ngrok.io/whatsapp/callback/',
                to='whatsapp:+254722212132')

            print(response.sid)

            # print(body)
            responded = True
            return Response(str(body), status=status.HTTP_200_OK)
        elif incoming_msg == 'parking':
            response = emoji.emojize("""*select option*
            \nYou can give me the following commands:
            \n1. Daily Parking
            \n2. Topup Daily Parking
            \n3. Seasonal Parking
            \n4. Offstreet Parking
            \n5. Penalties
            \n6. Parking Status
            \n7. Offloading Zone
            """,
                                     use_aliases=True)

            body = msg.body(response)

            response = client.messages.create(
                body=response,
                from_='whatsapp:+14155238886',
                #   status_callback='https://feeb1763bc3e.ngrok.io/whatsapp/callback/',
                to='whatsapp:+254722212132')

            print(response.sid)

            # print(body)
            responded = True


            # print(body)
            # data=json.dumps(body)
            # print(body)
            return Response(str(body), status=status.HTTP_200_OK)

        elif incoming_msg == '1':
            response = emoji.emojize("""
            \nWhat is your Vehicle's Number Plate?
            """,use_aliases=True)

            body = msg.body(response)

            response = client.messages.create(
                body=response,
                from_='whatsapp:+14155238886',
                #   status_callback='https://feeb1763bc3e.ngrok.io/whatsapp/callback/',
                to='whatsapp:+254722212132')

            print(response.sid)

            # print(body)
            responded = True


            # print(body)
            # data=json.dumps(body)
            # print(body)
            return Response(str(body), status=status.HTTP_200_OK)


class CallBackAPIView(APIView):
    def post(self, request, format=None):
        data = request.data
        print(data)
        return Response(str(data), status=status.HTTP_200_OK)

        # elif incoming_msg == 'quote':
        #     # returns a quote
        #     r = requests.get('https://api.quotable.io/random')

        #     if r.status_code == 200:
        #         data = r.json()
        #         quote = f'{data["content"]} ({data["author"]})'

        #     else:
        #         quote = 'I could not retrieve a quote at this time, sorry.'

        #     msg.body(quote)
        #     responded = True

        # elif incoming_msg == 'cat':
        #     # return a cat pic
        #     msg.media('https://cataas.com/cat')
        #     responded = True

        # elif incoming_msg == 'dog':
        #     # return a dog pic
        #     r = requests.get('https://dog.ceo/api/breeds/image/random')
        #     data = r.json()
        #     msg.media(data['message'])
        #     responded = True

        # elif incoming_msg.startswith('recipe'):

        #     # search for recipe based on user input (if empty, return featured recipes)
        #     search_text = incoming_msg.replace('recipe', '')
        #     search_text = search_text.strip()

        #     data = json.dumps({'searchText': search_text})

        #     result = ''
        #     # updates the Apify task input with user's search query
        #     r = requests.put(
        #         'https://api.apify.com/v2/actor-tasks/o7PTf4BDcHhQbG7a2/input?token=qTt3H59g5qoWzesLWXeBKhsXu&ui=1',
        #         data=data,
        #         headers={"content-type": "application/json"})
        #     if r.status_code != 200:
        #         result = 'Sorry, I cannot search for recipes at this time.'

        #     # runs task to scrape Allrecipes for the top 5 search results
        #     r = requests.post(
        #         'https://api.apify.com/v2/actor-tasks/o7PTf4BDcHhQbG7a2/runs?token=qTt3H59g5qoWzesLWXeBKhsXu&ui=1'
        #     )
        #     if r.status_code != 201:
        #         result = 'Sorry, I cannot search Allrecipes.com at this time.'

        #     if not result:
        #         result = emoji.emojize(
        #             "I am searching Allrecipes.com for the best {} recipes. :fork_and_knife:"
        #             .format(search_text),
        #             use_aliases=True)
        #         result += "\nPlease wait for a few moments before typing 'get recipe' to get your recipes!"
        #     msg.body(result)
        #     responded = True

        # elif incoming_msg == 'get recipe':
        #     # get the last run details
        #     r = requests.get(
        #         'https://api.apify.com/v2/actor-tasks/o7PTf4BDcHhQbG7a2/runs/last?token=qTt3H59g5qoWzesLWXeBKhsXu'
        #     )

        #     if r.status_code == 200:
        #         data = r.json()

        #         # check if last run has succeeded or is still running
        #         if data['data']['status'] == "RUNNING":
        #             result = 'Sorry, your previous query is still running.'
        #             result += "\nPlease wait for a few moments before typing 'get recipe' to get your recipes!"

        #         elif data['data']['status'] == "SUCCEEDED":

        #             # get the last run dataset items
        #             r = requests.get(
        #                 'https://api.apify.com/v2/actor-tasks/o7PTf4BDcHhQbG7a2/runs/last/dataset/items?token=qTt3H59g5qoWzesLWXeBKhsXu'
        #             )
        #             data = r.json()

        #             if data:
        #                 result = ''

        #                 for recipe_data in data:
        #                     url = recipe_data['url']
        #                     name = recipe_data['name']
        #                     rating = recipe_data['rating']
        #                     rating_count = recipe_data['ratingcount']
        #                     prep = recipe_data['prep']
        #                     cook = recipe_data['cook']
        #                     ready_in = recipe_data['ready in']
        #                     calories = recipe_data['calories']

        #                     result += """
        #                         *{}*
        #                         _{} calories_
        #                         Rating: {:.2f} ({} ratings)
        #                         Prep: {}
        #                         Cook: {}
        #                         Ready in: {}
        #                         Recipe: {}
        #                         """.format(name, calories, float(rating), rating_count, prep, cook, ready_in,url)

        #             else:
        #                 result = 'Sorry, I could not find any results for {}'.format(
        #                     search_text)

        #         else:
        #             result = 'Sorry, your previous search query has failed. Please try searching again.'

        #     else:
        #         result = 'I cannot retrieve recipes at this time. Sorry!'

        #     msg.body(result)
        #     responded = True

        # elif incoming_msg == 'news':
        #     r = requests.get(
        #         'https://newsapi.org/v2/top-headlines?sources=bbc-news,the-washington-post,the-wall-street-journal,cnn,fox-news,cnbc,abc-news,business-insider-uk,google-news-uk,independent&apiKey=3ff5909978da49b68997fd2a1e21fae8'
        #     )

        #     if r.status_code == 200:
        #         data = r.json()
        #         articles = data['articles'][:5]
        #         result = ''

        #         for article in articles:
        #             title = article['title']
        #             url = article['url']
        #             if 'Z' in article['publishedAt']:
        #                 published_at = datetime.datetime.strptime(
        #                     article['publishedAt'][:19], "%Y-%m-%dT%H:%M:%S")
        #             else:
        #                 published_at = datetime.datetime.strptime(
        #                     article['publishedAt'], "%Y-%m-%dT%H:%M:%S%z")
        #             result += """
        #                 *{}*
        #                 Read more: {}
        #                 _Published at {:02}/{:02}/{:02} {:02}:{:02}:{:02} UTC_
        #                 """.format(title, url, published_at.day, published_at.month, published_at.year,
        #                                     published_at.hour, published_at.minute, published_at.second)

        #     else:
        #         result = 'I cannot fetch news at this time. Sorry!'

        #     msg.body(result)
        #     responded = True

        # elif incoming_msg.startswith('statistics'):
        #     # runs task to aggregate data from Apify Covid-19 public actors
        #     requests.post(
        #         'https://api.apify.com/v2/actor-tasks/5MjRnMQJNMQ8TybLD/run-sync?token=qTt3H59g5qoWzesLWXeBKhsXu&ui=1'
        #     )

        #     # get the last run dataset items
        #     r = requests.get(
        #         'https://api.apify.com/v2/actor-tasks/5MjRnMQJNMQ8TybLD/runs/last/dataset/items?token=qTt3H59g5qoWzesLWXeBKhsXu'
        #     )

        #     if r.status_code == 200:
        #         data = r.json()

        #         country = incoming_msg.replace('statistics', '')
        #         country = country.strip()
        #         country_data = list(
        #             filter(lambda x: x['country'].lower().startswith(country),
        #                    data))

        #         if country_data:
        #             result = ''

        #             for i in range(len(country_data)):
        #                 data_dict = country_data[i]
        #                 last_updated = datetime.datetime.strptime(
        #                     data_dict.get('lastUpdatedApify', None),
        #                     "%Y-%m-%dT%H:%M:%S.%fZ")

        #                 result += """
        #                         *Statistics for country {}*
        #                         Infected: {}
        #                         Tested: {}
        #                         Recovered: {}
        #                         Deceased: {}
        #                         Last updated: {:02}/{:02}/{:02} {:02}:{:02}:{:03} UTC
        #                         """.format(data_dict['country'], data_dict.get('infected', 'NA'),
        #                                                 data_dict.get('tested', 'NA'), data_dict.get('recovered', 'NA'),
        #                                                 data_dict.get('deceased', 'NA'), last_updated.day,
        #                                                 last_updated.month, last_updated.year, last_updated.hour,
        #                                                 last_updated.minute, last_updated.second)
        #         else:
        #             result = "Country not found. Sorry!"

        #     else:
        #         result = "I cannot retrieve statistics at this time. Sorry!"

        #     msg.body(result)
        #     responded = True

        # elif incoming_msg.startswith('meme'):
        #     r = requests.get(
        #         'https://www.reddit.com/r/memes/top.json?limit=20?t=day',
        #         headers={'User-agent': 'your bot 0.1'})

        #     if r.status_code == 200:
        #         data = r.json()
        #         memes = data['data']['children']
        #         random_meme = random.choice(memes)
        #         meme_data = random_meme['data']
        #         title = meme_data['title']
        #         image = meme_data['url']

        #         msg.body(title)
        #         msg.media(image)

        #     else:
        #         msg.body('Sorry, I cannot retrieve memes at this time.')

        #     responded = True

        # if not responded:
        #     msg.body(
        #         "Sorry, I don't understand. Send 'hello' for a list of commands."
        #     )

        # return HttpResponse(str(resp))