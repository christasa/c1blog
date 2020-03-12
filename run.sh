#! /usr/bin/env sh

# Wait postgresql
sleep 10

python manage.py makemigrations 
python manage.py migrate




python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('${SUPUSER}', '${EMAIL}', '${SUPPASSWD}') if not User.objects.filter(username='${SUPUSER}').exists() else 0"
export SUPUSER=''
unset SUPUSER
export SUPPASSWD=''
unset SUPPASSWD
unset EMAIL


BASE_DIR=$(pwd)

exec gunicorn --chdir=${BASE_DIR} -w 2  -b 0.0.0.0:8000 -u root -g root --access-logfile - c1blog.wsgi:application

