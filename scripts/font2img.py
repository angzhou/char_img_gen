# coding=utf-8
"""
  read fonts in ..\fonts and write character to png
  run `chcp 65001` before running this program
"""

import sys
import os
import codecs
import json
import platform
import random

from PIL import Image, ImageDraw, ImageFont

from fonts_info import font_files, y_shift

# change these to suit your need
SAVE_DIR = "F:\\charimgs"

if platform.system() is not "Windows":
    exit("Please run under Windows!")

if len(sys.argv) < 2:
    exit("Must supply a 2-letter category")

cats = os.listdir(os.path.join("..", "char_lists"))
cats = [c[:2] for c in cats if c.endswith(".txt")]

cat = sys.argv[1]
if cat not in cats:
    exit("Invalid category: %s" % cat)

if os.path.isfile("%s.json" % cat):
    # config file found
    f = open("%s.json" % cat)
    config = json.loads(f.read())
    f.close()
    if isinstance(config['foreground'], list):
        config['foreground'] = tuple(config['foreground'])
    if isinstance(config['background'], list):
        config['background'] = tuple(config['background'])

else:
    config = {"size": 96,
              "mode": "L",
              "foreground": 255,
              "background": 0,
              "rotation": 0
              }

SIZE = config['size']

fonts = [f for f in font_files if cat in font_files[f]]

FONTS_DIR = os.path.join("..", "fonts")

label_file = codecs.open(os.path.join("..", "char_lists", "%s.txt" % cat),
                         encoding="utf-8")
labels = label_file.readlines()
label_file.close()
labels = [a.strip() for a in labels]

save_dir = os.path.join(SAVE_DIR, cat)
if not os.path.isdir(save_dir):
    os.mkdir(save_dir)

for f in fonts:
    font_path = os.path.join("..", "fonts", f)
    # If we keep the font size the same as img size
    # characters such as  Â, Î will be cut off at the top, 
    #  and j, ç, ÿ, ą will be truncated at the bottom.
    # So we reduce font size so that they all fit into image of size SIZE
    if cat in ('ws', 'mo'):
        font = ImageFont.truetype(font_path, int(SIZE * 0.82))
    else:
        font = ImageFont.truetype(font_path, SIZE)

    for label in labels:
        im = Image.new(config['mode'], (SIZE, SIZE), config['background'])
        draw = ImageDraw.Draw(im)
        code = ord(label)
        # if code < 0x17f:  # this is not enough
        if cat == 'ws':
            # in windows, we can not create different directories for 'a' and  'A', 
            # or for 'å' and 'Å'
            # So for all ascii and other latin chararacters, 
            # we use decimal code as directory name
            dest_dir = os.path.join(save_dir, str(code))
        else:
            dest_dir = os.path.join(save_dir, label)

        if not os.path.isdir(dest_dir):
            os.mkdir(dest_dir)

        if f[:-4] in y_shift:
            y_start = y_shift[f[:-4]]
        else:
            y_start = 0
        draw.text((0, y_start), label, font=font, fill=config['foreground'])

        if isinstance(config['rotation'], list):
            angle = random.randint(config['rotation'][0], config['rotation'][1])
        else:
            angle = config['rotation']

        if angle:
            # rotate and get rid of black edges
            im2 = im.convert("RGBA")
            im2 = im2.rotate(angle)
            im = Image.new(config['mode'], (SIZE, SIZE), config['background'])
            im.paste(im2, im2)

        im.save(os.path.join(dest_dir, "%04X_font_%s.png" % (code, f[:-4])), "PNG")
        del draw
