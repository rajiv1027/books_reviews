#!/usr/bin/bash

sed -i 's/\[]/\["3.87.108.126"]/' /home/ubuntu/jktech/jktech_app/settings.py

python manage.py migrate
python manage.py makemigrations
python manage.py collectstatic
sudo service gunicorn restart
sudo service nginx restart
