#!/usr/bin/bash

sed -i 's/\[]/\["54.144.250.113"]/' /home/ubuntu/jktech/jktech/settings.py

python manage.py migrate
python manage.py makemigrations
python manage.py collectstatic
sudo service gunicorn restart
sudo service nginx restart
