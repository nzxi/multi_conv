import os
from converters.image_converter import convert_image

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


# Function to clear the console.
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Take input image and output image check to see if its all good.
def convert_thatshit():
    input_image = input("Which image do you wanna convert?: ")
    while not os.path.exists(input_image) or not input_image.upper().endswith(img_formats):
         input_image = input("File doesn't exist or is invalid. Try again: ")
    output_image = input("Save image as: ")
    convert_image(input_image, output_image)
    # Pure laziness here
    global message
    message = f"Saved image as: {output_image}"

# Main function
def main():
    while True:
        clear_screen()
        print(TITLE)
        print("Available Options:")
        print(" 1. Image conversion")
        choice = input("Choose an option: ")

        if choice == '1':
            convert_thatshit()
            clear_screen()
            print(message)
            input("Press any key to continue...")

# Why am I doing this? Why not just lookup jpeg to png on the internet?
if __name__ == '__main__':
        main()