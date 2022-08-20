import os
import glob

file_list = glob.glob('D://Dropbox/1Jewelry/2022/special_snowflake/thousand_rendered_snowflakes/*.stlbak')
for filePath in file_list:
    try:
        os.remove(filePath)
    except:
        print(f'failed to remove {filePath}')
            