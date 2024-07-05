import os
from azure.storage.blob import BlobServiceClient

AZURE_STORAGE_CONNECTION_STRING = "your_connection_string"
CONTAINER_NAME = "your_container_name"
BLOB_NAMES = ["skinmodel50.pt", "skinmodelEff.pt", "VGG_19_Augmentation.pt"]
LOCAL_PATH = "models"

def download_blob(blob_name):
    blob_service_client = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)
    blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=blob_name)
    
    local_file_path = os.path.join(LOCAL_PATH, blob_name)
    os.makedirs(LOCAL_PATH, exist_ok=True)

    with open(local_file_path, "wb") as download_file:
        download_file.write(blob_client.download_blob().readall())
    print(f"Downloaded {blob_name} to {local_file_path}")

if __name__ == "__main__":
    for blob_name in BLOB_NAMES:
        download_blob(blob_name)
    print("All files downloaded!")
