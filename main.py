'''
MULTI CONV
by https://github.com/nzxi

This project is absolute shit. I only made it because I needed to convert a jpeg to png
It functions, so why bother optimise it?
Fuck, it's Python, how well can you really optimise it?

'''


import os
from converters.image_converter import convert_image
from converters.video_converter import convert_video

TITLE = r"""
·························································
: __  __ _   _ _   _____ ___    ____ ___  _   ___     __:
:|  \/  | | | | | |_   _|_ _|  / ___/ _ \| \ | \ \   / /:
:| |\/| | | | | |   | |  | |  | |  | | | |  \| |\ \ / / :
:| |  | | |_| | |___| |  | |  | |__| |_| | |\  | \ V /  :
:|_|  |_|\___/|_____|_| |___|  \____\___/|_| \_|  \_/   :
·························································
    By nzxi@github
"""

# Image formats supported by pillow
img_formats = [
    "BMP",
    "EPS",
    "GIF",
    "ICNS",
    "ICO",
    "JPEG",
    "JPEG2000",
    "MSP",
    "PCX",
    "PCD",
    "TGA",
    "TIFF",
    "WEBP",
    "PNG",
    "PPM",
    "PGM",
    "PBM",
    "XBM",
    "XPM"
]

# Make it a tuple cause endswith() only supports str and tuple
img_formats = tuple(img_formats)

video_formats = [
    "MP4",
    "MOV",
    "M4V",
    "MKV",
    "AVI",
    "WMV",
    "FLV",
    "WEBM",
    "MPEG",
    "MPG",
    "GIF"
]

video_formats = tuple(video_formats)


# Function to clear the console.
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Take input image and output image check to see if its all good.
def convert_thatshit():
    input_image = input("Which image do you wanna convert?: ")
    while not os.path.exists(input_image) or not input_image.upper().endswith(img_formats):
         input_image = input("File doesn't exist or is invalid. Try again: ")
    output_image = input("Save image as: ")
    while os.path.exists(output_image) or not output_image.upper().endswith(img_formats):
         output_image = input("File already exists OR is not a valid image type! Again: ")
    convert_image(input_image, output_image)
    # Pure laziness here
    global message
    message = f"Saved image as: {output_image}"

# Shits copy pasted lmao fuck this
# Didn't test this sh
def convert_thatvideo():
    input_video = input("Which video do you wanna convert?: ")
    while not os.path.exists(input_video) or not input_video.upper().endswith(video_formats):
         input_video = input("File doesn't exist or is invalid. Try again: ")
    output_video = input("Save video as: ")
    while os.path.exists(output_video) or not output_video.upper().endswith(video_formats):
         output_video = input("File already exists OR is not a valid video type! Again: ")
    convert_video(input_video, output_video)
    global message
    message = f"Saved video as: {output_video}"



# Main function
def main():
    while True:
        clear_screen()
        print(TITLE)
        print("Available Options:")
        print(" 1. Image conversion")
        print(" 2. Video conversion")
        choice = input("Choose an option: ")

        if choice == '1':
            convert_thatshit()
            clear_screen()
            print(message)
            input("Press any key to continue...")
        elif choice == '2':
            convert_thatvideo()
            clear_screen()
            print(message)
            input("Press any key to continue...")
        else:
             input("Invalid option!\n Press any key to continue...")

# Why am I doing this? Why not just lookup jpeg to png on the internet?
# To be fair this does convert videos as well so maybe its a bit less useless than I thought it would be
if __name__ == '__main__':
        main()
