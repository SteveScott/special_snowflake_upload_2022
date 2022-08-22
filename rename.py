from pathlib import Path
import os
from dotenv import load_dotenv
import shutil

load_dotenv

RENDERINGS_PATH = Path('D:\\\\Dropbox\\1Jewelry\\2022\\special_snowflake\\renderings_rotated\\')
NEW_RENDERINGS_PATH = Path('D:\\\\Dropbox\\1Jewelry\\2022\\special_snowflake\\renamed_renderings\\')


def rename_images(filename: str) -> str:
    seed = filename[:15]
    period_split_list = filename.split('.')
    if len(period_split_list) == 2:
        first_part = period_split_list[0]
        material = first_part.split('_')[1]
        if material == 'Shapeways White':
            return f"{seed}_ShapewaysWhite.jpg"
        if material == 'Silver Textured':
            return f'{seed}_SilverTextured.jpg'

    if len(period_split_list) == 3:
        if period_split_list[1][:6] == 'stl_Si':
            return f"{seed}_SilverTextured.jpg"
        elif period_split_list[1][:6] == 'stl_Sw':
            return f"{seed}_ShapewaysWhite.jpg"
        elif period_split_list[2][:6] == 'stl_Sh':
            return None
        elif period_split_list[2][:6] == 'stl_Si':
            return f'{seed}_SilverTextured.jpg'

def main():
    snow_renders = os.listdir(RENDERINGS_PATH)
    for rendering in snow_renders:
        new_filename = rename_images(rendering)
        if new_filename is None:
            continue
        shutil.copy(RENDERINGS_PATH / rendering, NEW_RENDERINGS_PATH / new_filename)

if __name__ == '__main__':
    main()
