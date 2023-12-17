#!/bin/bash

# Check if running as root
if [ "$EUID" -ne 0 ]; then
    echo "Please run as root"
    exit
fi

# Install required packages (adjust based on your needs)
apt-get update
sudo pip install pillow

# Install Python dependencies
# No dependencies needed

# Create symbolic link for exify.py
ln -s "$(pwd)/exify.py" /usr/local/bin/exify

clear

echo "Installation complete. You can now run 'exify' from any directory."
