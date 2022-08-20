import os
from dotenv import load_dotenv
from pathlib import Path
import pandas as pd

load_dotenv()
#get environment variables
RENDERINGS_PATH=Path(os.getenv('RENDERINGS_PATH'))
STL_PATH=Path(os.getenv('STL_PATH'))
class ShopifyTools:
	def __init__(self):
		pass

	def main(self):
		#set path to snowflakes
		#list all snowflakes locally
		snowflakes = os.listdir(STL_PATH)
		#create an empty dataframe with fields and dtypes defined
		export_df = pd.DataFrame()
		for snowflake in snowflakes:
			# get the type of showflake
			is_1in = self.is_one_inch(snowflake)
			# get the rendering.
			# if the rendering doesn't exist locally, continue and warn.
			# check if rendering exists on Azure
				#if it does, return url
				#if it doesn't, upload and return url
			# is the snowflake a pendant or ornament?
			# look up a dictionary of shopify information, 
			# add line to CSV 
		#return csv, index=False
	def create_one_inch_row(seed: str, img_url: str):
		return {
			'Handle': f"special-snowflake-{seed}",
			'Title' : "Silver Pendant" , 
			'Body (HTML)': "a silver snowflake, about one inch across. Each pendant is one-of-a-kind, no one else can have your snowflake.",
			'Vendor': 'Shapeways' ,
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
			'Image Src': f"'{img_url}'",
			'Image Position': '',
			'Image Alt Text': 'A silver snowflake pendant',
			'Gift Card': 'FALSE',
			'SEO Title': 'Special Snowflake Pendant. No two are alike',
			'SEO Description': '',
			'Google Shopping': '',
			'Google Product Category': '',
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
			'Variant Image': f"'{img_url}'",
			'Variant Weight Unit': 'g',
			'Variant Tax Code': '',
			'Cost per item': '40.00',
			'Price / International': '100',
			'Compare At Price / International':'',
			'Status': 'active'
			 }

	def create_two_inch_row(seed: str, img_url: str):
		return {
			'Handle': f"special-snowflake-{seed}",
			'Title' : "White Plastic Ornament" , 
			'Body (HTML)': "A white snowflake ornament, about two inches across. Each snowflake is one-of-a-kind, no one else can have your snowflake.",
			'Vendor': 'Shapeways' ,
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
			'Image Src': f"'{img_url}'",
			'Image Position': '',
			'Image Alt Text': 'A silver snowflake pendant',
			'Gift Card': 'FALSE',
			'SEO Title': 'Special Snowflake Ornament. No two are alike',
			'SEO Description': '',
			'Google Shopping': '',
			'Google Product Category': '',
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
			'Variant Image': f"'{img_url}'",
			'Variant Weight Unit': 'g',
			'Variant Tax Code': '',
			'Cost per item': '9.00',
			'Price / International': '20',
			'Compare At Price / International':'',
			'Status': 'active'
			 }
	def is_one_inch(self, snowflake: str) -> bool:
		snowflake_split = snowflake.split('.')
		assert snowflake_split[-1] == 'stl'
		print(snowflake_split[-2])
		print(snowflake_split[-2][-3:])

		if snowflake_split[-2][-3:] != '_2x':
			return True
		else:
			return False
