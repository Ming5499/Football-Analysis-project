import boto3
import os


folder_path = '/home/ubuntu/data'
def list_file(folder_path):
    if os.path.exists(folder_path):
        file_list = os.listdir(folder_path)
        file_names = []
        print("File names in the 'data' folder:")
        for file_name in file_list:
            if os.path.isfile(os.path.join(folder_path, file_name)):
                print(file_name)
                file_names.append(file_name)
    else:
        print("Folder path doesn't exist")
        file_names = []  
    return file_names

def upload_to_s3(folder_path, bucket_name):
    file_names = list_file(folder_path)
    if file_names:
        s3_client = boto3.client('s3')
        for file_name in file_names:
            object_key = f"folder_name/{file_name}.csv"  
            with open(os.path.join(folder_path, file_name), 'rb') as file:
                s3_client.put_object(Bucket=bucket_name, Key=object_key, Body=file)
    else:
        print("No files found in the 'data' folder.")