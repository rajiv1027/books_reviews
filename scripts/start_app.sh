#!/usr/bin/bash

sed -i 's/\[]/\["52.23.220.101"]/' /home/ubuntu/books_reviews/jktech/settings.py

python manage.py migrate
python manage.py makemigrations
python manage.py collectstatic --noinput > /tmp/collectstatic_output.log 2>&1
sudo service gunicorn restart
sudo service nginx restart

