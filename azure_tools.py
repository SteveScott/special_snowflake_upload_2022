from azure.storage.blob import BlobServiceClient, BlobClient
import os
from dotenv import load_dotenv
import io
from pathlib import Path
load_dotenv()
AZURE_STORAGE_KEY=os.getenv('AZURE_STORAGE_KEY')
AZURE_STORAGE_USERNAME=os.getenv('AZURE_STORAGE_USERNAME')
AZURE_STORAGE_CONNECTION_STRING=os.getenv('AZURE_STORAGE_CONNECTION_STRING')
STORAGE_ACCOUNT=os.getenv('STORAGE_ACCOUNT')
CONTAINER_NAME=os.getenv('CONTAINER_NAME')
LOCAL_TEST_PATH = Path('D:\\\\Dropbox\\1Jewelry\\2022\\special_snowflake\\renderings\\AAS-SGC-TMW-NIO.stl_Silver Textured_.jpg')
class AzureTools:

	def __init__(self):
		self.connect_azure()

	def connect_azure(self) -> object:
		 
		self.bsc = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)
		self.container_client = self.bsc.get_container_client(CONTAINER_NAME)
	def search_blob_storage(self) -> str:
		return None

	def upload_image(self, container_name, local_file_name, full_path_to_file) -> str:
		#self.bsc.create_blob_from_path(
        #    container_name, local_file_name, full_path_to_file)
		with open(full_path_to_file, 'rb') as data:
			blob_client = self.container_client.upload_blob(name=local_file_name, data=data)
		properties = blob_client.get_blob_properties()
		print(properties)
if __name__ == '__main__':
	pass
	#at = AzureTools()
	#at.upload_image(CONTAINER_NAME, 'AAS-SGC-TMW-NIO.stl_Silver Textured_.jpg', LOCAL_TEST_PATH)