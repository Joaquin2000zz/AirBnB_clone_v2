#!/usr/bin/env bash
# install NGINX and restart the service
if [ "$(dpkg-query -W -f="${Status}" nginx 2>/dev/null | grep -c "ok installed")" -eq 0 ]
then
  sudo apt-get update
  sudo apt-get install nginx -y
fi
# creating folders needed if dosen't already exist
mkdir -p ~/data/web_static/releases/test/
mkdir -p ~/data/web_static/shared
mkdir -p ~/data/web_static/current
# creating html file
echo -e "<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>" > ~/data/web_static/releases/test/index.html
# creating simbolic link
ln -sf ~/data/web_static/releases/test/ ~/data/web_static/current
# giving owner to the ubuntu user and group with the same group
chown -R ubuntu:ubuntu ~/data/
sudo sed -i '/\tserver_name _;/a \\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
sudo service nginx restart
