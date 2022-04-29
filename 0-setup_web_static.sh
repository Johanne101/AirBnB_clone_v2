#!/usr/bin/env bash
# Write a Bash script that sets up your web servers for the deployment of web_static
# Install NGINX
sudo apt-get -y update
sudo apt-get install nginx ufw -y
sudo ufw allow 'Nginx HTTP'

# Create directories 
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

# Create a Fake HTML file

echo "Fake HTML file test passed" | sudo tee /data/web_static/releases/test/index.html

#Symbolic link

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

#Give ownership to user and group

sudo chown -hR ubuntu:ubuntu /data/

# Update the Nginx configuration

sudo sed -i "42i\ \n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default

# Restart Server

sudo service nginx restart
