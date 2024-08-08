#!/usr/bin/bash

sed -i 's/\[]/\["54.173.177.44"]/' /home/ubuntu/books_reviews/jktech/settings.py

python manage.py migrate
python manage.py makemigrations
python manage.py collectstatic
sudo service gunicorn restart
sudo service nginx restart

