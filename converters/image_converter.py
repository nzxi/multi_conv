from PIL import Image


def convert_image(in_img, out_img):
    img = Image.open(in_img)
    img.convert("RGB").save(out_img)