#!/usr/bin/env bash
#Configuration

#making directories
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "Hello Phoenix!" > /data/web_static/releases/test/index.html

#making symbolic link
link="/data/web_static/current"
target="/data/web_static/releases/test"
[ -L "$link" ] && rm -f "$link"
ln -s "$target" "$link"

#Give ownership of /data/ to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

#Configure to serve to /hbnb_static
text_add="      location /hbnb_static {\
                alias /data/web_static/current/;\
        }"
sed -i "/listen 80 default_server;/a\\
$text_add" /etc/nginx/sites-enabled/default

#Restart nginx to apply changes
sudo service nginx restart
