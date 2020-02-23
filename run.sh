#! /usr/bin/env sh

# Wait postgresql
sleep 5

python manage.py makemigrations \
    && python manage.py migrate



if [ -n "${SUPUSER}" ];then
  echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('${SUPUSER}', '${EMAIL}', '${SUPPASSWD}')" | python manage.py shell 2>/dev/null &
  export SUPUSER=''
  unset SUPUSER
  export SUPPASSWD=''
  unset SUPPASSWD
  unset EMAIL
fi

BASE_DIR=$(pwd)

exec gunicorn --chdir=${BASE_DIR} -w 2  -b 0.0.0.0:8000 -u root -g root --access-logfile - c1blog.wsgi:application

