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

def main():
    print(TITLE)
    print("Available Options:")
    print(" 1. Image conversion")
    choice = input("Choose an option: ")

