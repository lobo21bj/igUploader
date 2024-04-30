import argparse
import os
import sys
import time

from PIL import Image

from browser import post_to_instagram
from crop import ImageCropper

current_path = os.path.dirname(os.path.abspath(__file__))

USERNAME = 'nicofischer.ok'
PASSWORD = 'Crecer91218'

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("image", type=open, action="store")
    parser.add_argument("caption", type=str, action="store")
    parser.add_argument("-c", "--crop", default=False, action="store_true")
    parser.add_argument("--share", default=False, action="store_true")

    args = parser.parse_args()

    if args.crop:
        cropper = ImageCropper()
        cropper.set_file(args.image.name)
        cropper.run()
        photo = cropper.outputname
    else:
        photo = args.image.name

    if photo is not None:
        post_to_instagram(current_path, USERNAME, PASSWORD, photo, args.caption, args.share)
    else:
        print(
            "Your selection was not saved. Hit <SPACE> to save it, and continue to posting it."
        )