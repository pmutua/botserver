#!/bin/sh

set -e

gunicorn --bind 0.0.0.0:8000 core.wsgi:application

# if [ "$DATABASE" = "postgres" ]
# then
#     echo "Waiting for postgres..."

#     while ! nc -z $SQL_HOST $SQL_PORT; do
#       sleep 0.1
#     done

#     echo "PostgreSQL started"
# fi


# python manage.py collectstatic --no-input

# # python manage.py flush --no-input

# # python manage.py migrate

# uswgi --socket :8000 --master --enable-threads --module core.wsgi


# exec "$@"