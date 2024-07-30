#!/bin/bash

# Check if running as root
if [ "$EUID" -ne 0 ]; then
    echo "Please run as root"
    exit
fi

# Install pip and Pillow using apt and pip
echo "Installing pip and Pillow..."
sudo apt-get update
sudo apt-get install -y python3-pip
sudo pip install Pillow

# Install Python dependencies
# No dependencies needed

# Create symbolic link for exify.py
ln -s "$(pwd)/exify.py" /usr/local/bin/exify

clear

echo "Installation complete. Launch a new terminal and you'll be able to run 'exify' from any directory."
