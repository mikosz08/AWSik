import boto3
import random
import string


class BucketS3:
    def __init__(self):
        self.s3 = boto3.client("s3")
        self.bucket_name = "my-bucket-mqs"

    def create_folder_and_upload_files(self, folder_name, num_files):
        folder_key = folder_name + "/"
        self.s3.put_object(Bucket=self.bucket_name, Key=folder_key)

        for i in range(num_files):
            random_string = "".join(random.choices(string.ascii_lowercase, k=10))
            file_name = f"{folder_name}/file_{i+1}.txt"
            file_content = f"Random Content: {random_string}"

            self.s3.put_object(
                Bucket=self.bucket_name, Key=file_name, Body=file_content
            )

        print(f"Folder '{folder_name}' utworzony i pliki zostały dodane.")

    def setup_user_folder(self, count: int):
        for i in range(count):
            folder_name = f"scraping_{i}"
            num_files_to_create = 3
            bucket.create_folder_and_upload_files(folder_name, num_files_to_create)

    def list_folders(self):
        folders = []
        response = self.s3.list_objects_v2(Bucket=self.bucket_name, Delimiter="/")

        for prefix in response.get("CommonPrefixes", []):
            folder_name = prefix.get("Prefix").rstrip("/")
            folders.append(folder_name)

        return folders

    def list_files_in_folder(self, folder_name):
        files = []
        prefix = folder_name + "/"
        response = self.s3.list_objects_v2(Bucket=self.bucket_name, Prefix=prefix)

        for obj in response.get("Contents", []):
            file_name = obj.get("Key")
            if file_name != prefix:
                files.append(file_name)

        return files

    def get_user_folder_contents(self, user_folder_name):
        files = self.list_files_in_folder(user_folder_name)
        print(f"Lista plików w folderze użytkownika:'{user_folder_name}':")
        for file in files:
            print(file)

    def save_single_file(self, folder_name, file_name, file_content):
        key = f"{folder_name}/{file_name}"
        obj = boto3.resource("s3").Object(self.bucket_name, key)
        obj.put(Body=file_content)
        print(f"Plik '{file_name}' został zapisany w folderze '{folder_name}'.")

    def save_batch_files(self, folder_name, file_contents):
        for file_name, file_content in file_contents.items():
            key = f"{folder_name}/{file_name}"
            obj = boto3.resource("s3").Object(self.bucket_name, key)
            obj.put(Body=file_content)
        print("Pliki zostały pomyślnie zapisane w folderze.")


bucket = BucketS3()

# Adds 4 folders with random files.
bucket.setup_user_folder(4)

# List folders in bucket.
folders_list = bucket.list_folders()
print("Lista folderów:")
for folder in folders_list:
    print(folder)
    # List files in folders.
    files = bucket.list_files_in_folder(folder)
    print("Lista plików wewnątrz:")
    for file in files:
        print(file)

# Check single folder.
user_folder_to_check = "user_folder_8"
bucket.get_user_folder_contents(user_folder_to_check)

# Signle & Batch upload.
folder_to_save = "user_folder_0"
file_to_save = "file_single.txt"
file_content_single = "This is single upload."
bucket.save_single_file(folder_to_save, file_to_save, file_content_single)

batch_files = {
    "file_batch_1.txt": "This is",
    "file_batch_2.txt": "batch upload",
}
bucket.save_batch_files(folder_to_save, batch_files)