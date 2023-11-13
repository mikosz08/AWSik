import os
import boto3
import random
import string


class BucketS3:
    def create_and_send_file(self):
        file_path = "file_for_bucket.txt"

        bucket_name = "my-bucket-mqs"

        s3 = boto3.client("s3")
        object_key = "file_for_bucket.txt"
        s3.upload_file(file_path, bucket_name, object_key)

        print(
            f"Plik {file_path} został przesłany do pojemnika {bucket_name} jako {object_key}."
        )
