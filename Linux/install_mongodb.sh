#!/bin/bash

# Import MongoDB public GPG key
curl -fsSL https://pgp.mongodb.com/server-6.0.asc | \
  sudo gpg -o /usr/share/keyrings/mongodb-server-6.0.gpg \
  --dearmor

# Add the MongoDB repository
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-6.0.gpg ] https://repo.mongodb.org/apt/ubuntu noble/mongodb-org/6.0 multiverse" | \
  sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list

# Update packages and install MongoDB
sudo apt update -y
sudo apt install -y mongodb-org

# Enable and start the MongoDB service
sudo systemctl enable mongod
sudo systemctl start mongod

# Allow connections from all IPs by updating bindIp
sudo sed -i 's/bindIp: 127.0.0.1/bindIp: 0.0.0.0/' /etc/mongod.conf

# Restart MongoDB to apply changes
sudo systemctl restart mongod