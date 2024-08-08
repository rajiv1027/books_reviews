#!/usr/bin/bash

sudo systemctl daemon-reload
sudo rm -f /etc/nginx/sites-enabled/default

sudo cp /home/ubuntu/books_reviews/nginx/nginx.conf /etc/nginx/sites-available/jktech
sudo ln -s /etc/nginx/sites-available/jktech /etc/nginx/sites-enabled/

sudo gpasswd -a www-data ubuntu
sudo systemctl restart nginx