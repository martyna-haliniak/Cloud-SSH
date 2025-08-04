#!/bin/bash

# update
sudo apt update -y
# upgrade
sudo apt upgrade -y
# install nginx
sudo apt install nginx -y
    # nginx -version     -->  checks if worked
    # sudo systemctl status nginx  --> press q to get out of it
            # Public IPv4 address 3.122.206.189 | open address 
            # go on the IP address on the instance summary page
            # http needed in securitry settings as well as ssh

# restart nginx
sudo systemctl restart nginx
# enagble nginx
sudo systemctl enable nginx
