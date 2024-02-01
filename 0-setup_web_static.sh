#!/usr/bin/env bash
#Configuration

#install nginx
sudo apt-get update
sudo apt-get install -y nginx

#making directories
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "Hello Phoenix!" | sudo tee /data/web_static/releases/test/index.html >/dev/null

#making symbolic link
link="/data/web_static/current"
target="/data/web_static/releases/test"
[ -L "$link" ] && rm -f "$link"
sudo ln -s "$target" "$link"

#Give ownership of /data/ to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

#Configure to serve to /hbnb_static
text_add="      location /hbnb_static {\
                alias /data/web_static/current/;\
        }"
sudo sed -i "/listen 80 default_server;/a\\
$text_add" /etc/nginx/sites-enabled/default

#Restart nginx to apply changes
sudo service nginx restart
