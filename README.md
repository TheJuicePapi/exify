-------------------------------------------------------------------------------------------------------------------------------------------

# Exify - by TheJuicePapi

-------------------------------------------------------------------------------------------------------------------------------------------

![Screenshot_2024-08-07_01-26-52-1](https://github.com/user-attachments/assets/68fbf87a-7a15-47dd-a01b-2cb9f6fee8d7)



---------------------
![Screenshot_2024-08-07_01-09-58](https://github.com/user-attachments/assets/d4728d39-5c0b-47b6-8163-a7f77dfd0054)
![Screenshot_2024-08-07_01-10-48](https://github.com/user-attachments/assets/17e564fa-9b9b-44b1-a352-4f2948a0e556)






DESCRIPTION

Exify is a powerful Python script designed to delve into the depths of image metadata using the Exif format. Leveraging the Pillow library, Exify extracts a wealth of information, including GPS coordinates, from images within a specified folder. This script not only serves as an informative tool for understanding image properties but also offers practical features like generating Google Maps URLs based on extracted GPS data. 

-------------------------------
KEY FEATURES

Comprehensive Metadata Exploration: Uncover a treasure trove of Exif metadata, providing insights into various aspects of your images.

GPS Coordinate Conversion: Effortlessly convert GPS coordinates to decimal degrees, allowing for a more intuitive understanding of geographical locations.

Interactive Google Maps Integration: Seamlessly generate Google Maps URLs based on GPS coordinates, enabling users to visualize image locations with a single click.

Flexible Output Options: Choose between displaying results directly in the terminal or saving detailed information to a text file ('exif_data.txt').  Comprehensive Metadata Exploration: Uncover a treasure trove of Exif metadata, providing insights into various aspects of your images.

--------------------------------
 
INSTALLATION & USAGE

Git clone installation:

1. 'git clone https://github.com/TheJuicePapi/exify.git'
2. 'cd exify'
3. 'sudo chmod +x install.sh exify.py'
4. 'sudo ./install.sh'
5. Exit and open a new terminal to use 'exify' shortcut 

-------------------------------

DEPENDANCIES

For this script to work you will need to have pillow and pip installed. The install.sh should automatically install them for you.
If not then use:

* sudo apt-get install -y python3-pip
* sudo pip3 install Pillow

-------------------------------

CONFIGURATION

Once you download the git and use the install.sh to create a shortcut you can then launch the script from anywhere by simply typing 'exify'.
Make sure to go into the exify directory and add the images youd like to grab the exif data from and place them into the images folder that's present in
the exify folder. 

* Remember that not all images can have their exif data extracted *

Once you have added the images you can then run the script and chose your output option.

-------------------------------

This scipt has been tested on my RPI 4b running a kali linux arm.
Enjoy and use responsibly
