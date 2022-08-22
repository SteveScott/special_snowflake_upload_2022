import os
from dotenv import load_dotenv
from pathlib import Path
import pandas as pd
import logging
import shopify_template

load_dotenv()
#get environment variables
RENDERINGS_PATH=Path(os.getenv('RENDERINGS_PATH'))
STL_PATH=Path(os.getenv('STL_PATH'))
BLOB_URL=os.getenv('BLOB_URL')
ROOT=Path(os.getenv('ROOT'))
class ShopifyTools:
	def __init__(self):
		pass

	def main(self):
		#set path to snowflakes
		#list all snowflakes locally
		snowflakes = os.listdir(STL_PATH)
		#create an empty dataframe with fields and dtypes defined
		export_df = pd.DataFrame(columns=shopify_template.columns)
		for snowflake in snowflakes:
			seed = snowflake[:15]
			rendering_filename = self.get_rendering_filename(snowflake)

			is_this_two_inch = self.is_two_inch(snowflake)
			# assume it is on azure.
			if is_this_two_inch:
				this_row = self.create_two_inch_row(seed, BLOB_URL + rendering_filename)
			else:
				this_row = self.create_one_inch_row(seed, BLOB_URL + rendering_filename)
			export_df = export_df.append(this_row, ignore_index=True)
		export_df.to_csv(ROOT / 'upload_list.csv', index=False)
		export_test = export_df[:6]
		export_test.to_csv(ROOT / 'upload_test.csv')
	
	def get_rendering_path(self, snowflake: str) -> Path:
		is_2in = self.is_two_inch(snowflake)
		seed = snowflake.split('.')[-2][:15]
		if is_2in:
			return RENDERINGS_PATH / f'{seed}_ShapewaysWhite.jpg'
		else:
			return RENDERINGS_PATH / f'{seed}_SilverTextured.jpg'

	def get_rendering_filename(self, stl_filename: str) -> str:
		seed = stl_filename.split('.')[-2][:15]
		is_2in = self.is_two_inch(stl_filename)
		if is_2in:
			return f'{seed}_ShapewaysWhite.jpg'
		else:
			return f'{seed}_SilverTextured.jpg'


	def create_one_inch_row(self, seed: str, img_url: str):
		return {
			'Handle': f"special-snowflake-{seed}",
			'Title' : f"{seed}" , 
			'Body (HTML)': "a silver snowflake, about one inch across. Each pendant is one-of-a-kind, no one else can have your snowflake.",
			'Vendor': 'BaroquePlusPlus LLC' ,
			'Standardized Product Type': '336', # - Apparel & Accessories > Jewelry > Charms & Pendants
			'Custom Product Type':'',
			'Tags':"Special Snowfake, pendant, silver" ,
			'Published': 'TRUE',
			'Option1 Name': 'Size',
			'Option1 Value': '1\'\'',
			'Option2 Name': 'Material',
			'Option2 Value': 'Sterling Silver',
			'Option3 Name':'',
			'Option3 Value':'',
			'Variant SKU':f"ss22-sv-1in-{seed}",
			'Variant Grams':'0.0',
			'Variant Inventory Tracker': 'shopify',
			'Variant Inventory Qty': '1',
			'Variant Inventory Policy': 'deny',
			'Variant Fulfillment Service': 'manual',
			'Variant Price': '78.0',
			'Variant Compare At Price': '',
			'Variant Requires Shipping': 'TRUE',
			'Variant Taxable': 'TRUE',
			'Variant Barcode': '',
			'Image Src': f"{img_url}",
			'Image Position': '',
			'Image Alt Text': 'A silver snowflake pendant',
			'Gift Card': 'FALSE',
			'SEO Title': 'Special Snowflake Pendant. No two are alike',
			'SEO Description': '',
			'Google Shopping / Google Product Category': '',
			'Google Shopping / Gender': '',
			'Google Shopping / Age Group':'',
			'Google Shopping / MPN':'',
			'Google Shopping / AdWords Grouping':'',
			'Google Shopping / AdWords Labels':'',
			'Google Shopping / Condition':'',
			'Google Shopping / Custom Product':'',
			'Google Shopping / Custom Label 0':'',
			'Google Shopping / Custom Label 1':'',
			'Google Shopping / Custom Label 2':'',
			'Google Shopping / Custom Label 3':'',
			'Google Shopping / Custom Label 4':'',
			'Variant Image': f"{img_url}",
			'Variant Weight Unit': 'g',
			'Variant Tax Code': '',
			'Cost per item': '40.00',
			'Price / International': '100',
			'Compare At Price / International':'',
			'Status': 'active'
			 }

	def create_two_inch_row(self, seed: str, img_url: str):
		return {
			'Handle': f"special-snowflake-{seed}",
			'Title' : f"{seed}", 
			'Body (HTML)': "A white snowflake ornament, about two inches across. Each snowflake is one-of-a-kind, no one else can have your snowflake.",
			'Vendor': 'BaroquePlusPlus LLC' ,
			'Standardized Product Type': '3169', #- Home & Garden > Decor > Seasonal & Holiday Decorations > Holiday Ornaments
			'Custom Product Type':'',
			'Tags':"Special Snowfake, ornament, white, plastic" ,
			'Published': 'TRUE',
			'Option1 Name': 'Size',
			'Option1 Value': '2\'\'',
			'Option2 Name': 'Material',
			'Option2 Value': 'White Nylon',
			'Option3 Name':'',
			'Option3 Value':'',
			'Variant SKU':f"ss22-wp-2in-{seed}",
			'Variant Grams':'0.0',
			'Variant Inventory Tracker': 'shopify',
			'Variant Inventory Qty': '1',
			'Variant Inventory Policy': 'deny',
			'Variant Fulfillment Service': 'manual',
			'Variant Price': '18.00',
			'Variant Compare At Price': '',
			'Variant Requires Shipping': 'TRUE',
			'Variant Taxable': 'TRUE',
			'Variant Barcode': '',
			'Image Src': f"{img_url}",
			'Image Position': '',
			'Image Alt Text': 'A silver snowflake pendant',
			'Gift Card': 'FALSE',
			'SEO Title': 'Special Snowflake Ornament. No two are alike',
			'SEO Description': '',
			'Google Shopping / Google Product Category': '',
			'Google Shopping / Gender': '',
			'Google Shopping / Age Group':'',
			'Google Shopping / MPN':'',
			'Google Shopping / AdWords Grouping':'',
			'Google Shopping / AdWords Labels':'',
			'Google Shopping / Condition':'',
			'Google Shopping / Custom Product':'',
			'Google Shopping / Custom Label 0':'',
			'Google Shopping / Custom Label 1':'',
			'Google Shopping / Custom Label 2':'',
			'Google Shopping / Custom Label 3':'',
			'Google Shopping / Custom Label 4':'',
			'Variant Image': f"{img_url}",
			'Variant Weight Unit': 'g',
			'Variant Tax Code': '',
			'Cost per item': '9.00',
			'Price / International': '20',
			'Compare At Price / International':'',
			'Status': 'active'
			 }

	def is_two_inch(self, snowflake: str) -> bool:
		snowflake_split = snowflake.split('.')
		assert snowflake_split[-1] == 'stl'
		if snowflake_split[-2][-3:] == '_2x':
			return True
		else:
			return False
	
	
		
