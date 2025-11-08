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


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')



def convert_thatshit():
    input_image = input("Which image do you wanna convert?: ")
    output_image = input("Save image as: ")
    convert_image(input_image, output_image)
    global message
    message = f"Saved image as: {output_image}"


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

if __name__ == '__main__':
        main()