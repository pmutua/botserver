# nccg-chatbot


ChatterBot is a machine-learning based conversational dialog engine build in Python which makes it possible to generate responses based on collections of known conversations. The language independent design of ChatterBot allows it to be trained to speak any language.

An example of typical input would be something like this:

user: Good morning! How are you doing?
bot: I am doing very well, thank you for asking.
user: You're welcome.
bot: Do you like hats?

How it works
An untrained instance of ChatterBot starts off with no knowledge of how to communicate. Each time a user enters a statement, the library saves the text that they entered and the text that the statement was in response to. As ChatterBot receives more input the number of responses that it can reply and the accuracy of each response in relation to the input statement increase. The program selects the closest matching response by searching for the closest matching known statement that matches the input, it then returns the most likely response to that statement based on how frequently each response is issued by the people the bot communicates with.




pip install pipenv

pipenv lock 

pipenv install --ignore-pipfile 

python manage.py migrate django_chatterbot


RUN:
----

docker-compose exec db psql --username=hello_django --dbname=hello_django_dev


docker-compose exec web manage.py migrate django_chatterbot

docker-compose exec web python manage.py migrate --noinput


docker volume inspect django-on-docker_postgres_data




RUN chmod +x entrypoint.sh

DOCKER:
-------

docker build -f ./core/Dockerfile -t nccgbot:latest ./core


docker run -d -p 8000:8000 -e "SECRET_KEY=please_change_me" -e "DEBUG=1" -e "DJANGO_ALLOWED_HOSTS=*" nccg-chatbot_web  python /usr/src/app/manage.py runserver 0.0.0.0:8000


Remobe dangling images 

docker rmi -f $(docker images -f "dangling=true" -q)


install spacy==2.3.2 manually


docker-compose -f docker-compose-deploy.yml build --no-cache




List all containers (only IDs) docker ps -aq.
Stop all running containers. docker stop $(docker ps -aq)
Remove all containers. docker rm $(docker ps -aq)
Remove all images. docker rmi $(docker images -q)


# TODO 

- Remove nccbot service 



Django first-time initialization and Training:


% python manage.py migrate --run-syncdb
% python manage.py migrate train



# SET WEBHOOK 

https://api.telegram.org/bot1270864149:AAEABZByVcIWGNvOjainjiIgs2g5zArcKSk/setWebhook?url=https://af2f23f0c1d5.ngrok.io/tbot/webhook/