from pathlib import Path
import os
from PIL import Image
OLD_SNOWFLAKES_PATH = Path('D:\\\\Dropbox\\1Jewelry\\2022\\special_snowflake\\renderings')
NEW_SNOWFLAKES_PATH = Path('D:\\\\Dropbox\\1Jewelry\\2022\\special_snowflake\\renderings_rotated')

all_snowflakes = os.listdir(OLD_SNOWFLAKES_PATH)
for snowflake_input in all_snowflakes:
    with Image.open(OLD_SNOWFLAKES_PATH / snowflake_input) as input_image:
        angle = 180
        output = input_image.rotate(angle)
        output.save(NEW_SNOWFLAKES_PATH / snowflake_input)
