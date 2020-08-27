# nccg-chatbot

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


docker run -d \
    -p 8006:8000 \
    -e "SECRET_KEY=please_change_me" -e "DEBUG=1" -e "DJANGO_ALLOWED_HOSTS=*" \
    nccgbot python /usr/src/app/manage.py runserver 0.0.0.0:8000


Remobe dangling images 

docker rmi -f $(docker images -f "dangling=true" -q)


install spacy==2.3.2 manually