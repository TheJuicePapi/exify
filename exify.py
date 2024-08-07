#!/usr/bin/env python3

import os
import sys
import time
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def create_google_maps_url(gps_coords):
    dec_deg_lat = convert_decimal_degrees(float(gps_coords["lat"][0]), float(gps_coords["lat"][1]), float(gps_coords["lat"][2]), gps_coords["lat_ref"])
    dec_deg_lon = convert_decimal_degrees(float(gps_coords["lon"][0]), float(gps_coords["lon"][1]), float(gps_coords["lon"][2]), gps_coords["lon_ref"])
    return f"https://maps.google.com/?q={dec_deg_lat},{dec_deg_lon}"

def convert_decimal_degrees(degree, minutes, seconds, direction):
    decimal_degrees = degree + minutes / 60 + seconds / 3600
    if direction == "S" or direction == "W":
        decimal_degrees *= -1
    return decimal_degrees


def clear_terminal():
    os.system('clear')

clear_terminal()
    
def print_logo():
    print("\033[1;36m" + """ 
       ███████╗██╗░░██╗██╗███████╗██╗░░░██╗
       ██╔════╝╚██╗██╔╝██║██╔════╝╚██╗░██╔╝
       █████╗░░░╚███╔╝░██║█████╗░░░╚████╔╝░
       ██╔══╝░░░██╔██╗░██║██╔══╝░░░░╚██╔╝░░
       ███████╗██╔╝╚██╗██║██║░░░░░░░░██║░░░
       ╚══════╝╚═╝░░╚═╝╚═╝╚═╝░░░░░░░░╚═╝░░░
   \033[0m""")
    print("       Image data extractor - TheJuicePapi")

def print_options_menu():
    print("\033[1;34m" + """\
 ╔═════════════════════════════════════════════╗
 ║  How would you like to receive the output:  ║
 ║                                             ║
 ║         1 - File      2 - Terminal          ║
 ╚═════════════════════════════════════════════╝
\033[1;39m""")

def print_image_info_menu():
    print("\033[1;38m" + """\
           +----------------------------------------+
           |        Image Information Menu          |
           +----------------------------------------+
\033[0m""")

def process_image(file_path):
    try:
        image = Image.open(file_path)
        print(f"\033[1;36m{'=' * 48}\033[1;36m{file_path}\033[1;36m{'=' * 48}")

        gps_coords = {}
        if hasattr(image, "_getexif") and image._getexif() is not None:
            for tag, value in image._getexif().items():
                tag_name = TAGS.get(tag, tag)
                if tag_name == "GPSInfo":
                    for key, val in value.items():
                        print(f"{GPSTAGS.get(key)} - {val}")
                        if GPSTAGS.get(key) == "GPSLatitude":
                            gps_coords["lat"] = val
                        elif GPSTAGS.get(key) == "GPSLongitude":
                            gps_coords["lon"] = val
                        elif GPSTAGS.get(key) == "GPSLatitudeRef":
                            gps_coords["lat_ref"] = val
                        elif GPSTAGS.get(key) == "GPSLongitudeRef":
                            gps_coords["lon_ref"] = val
                else:
                    print(f"{tag_name}: {value}")

            if gps_coords:
                print(create_google_maps_url(gps_coords))

    except IOError:
        print(f"Unsupported file format: {file_path}")

def main():
    print_logo()

    while True:
        try:
            print_options_menu()
            output_choice = int(input("Enter choice: "))
            if output_choice in [1, 2]:
                break
            else:
                print("You entered an incorrect option, please try again.")
        except ValueError:
            print("Invalid option, please try again.")

    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Find the images folder dynamically
    images_folder = os.path.join(script_directory, "images")

    # Check if the 'images' folder is not present and try an alternative location
    if not os.path.exists(images_folder):
        alt_images_folder = os.path.join(os.path.expanduser("~"), "exify", "images")
        if os.path.exists(alt_images_folder):
            images_folder = alt_images_folder
        else:
            alt_images_folder = os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), "images")
            if os.path.exists(alt_images_folder):
                images_folder = alt_images_folder
            else:
                print("No 'images' folder found.")
                return
    
    files = os.listdir(images_folder)

    if not files:
        print("No files present in the 'images' folder.")
        return

    for file in files:
        file_path = os.path.join(images_folder, file)
        process_image(file_path)

    if output_choice == 1:
        with open("exif_data.txt", "w") as file:
            sys.stdout = file
            for file in files:
                file_path = os.path.join(images_folder, file)
                process_image(file_path)

if __name__ == "__main__":
    main()
