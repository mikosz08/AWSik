# AWS Basic Stuff


### File Descriptions

- **`BucketS3.py`**  
  Handles operations on Amazon S3, such as creating folders, uploading files, listing folders, and listing files.

- **`DynamoDB.py`**  
  Demonstrates adding items to a DynamoDB table.

- **`LambdaAWS.py`**  
  Provides functionality to list Lambda functions and invoke a specific Lambda function with a sample event.

- **`SimpleQueueService.py`**  
  Handles sending and receiving messages from an SQS queue.

- **`Podstawy_AWS.py`**  
  The main file that integrates all the above modules and allows testing them.

## Requirements

- Python 3.10 or newer
- `boto3` library
- AWS account with appropriate permissions for S3, DynamoDB, Lambda, and SQS

## Installation

   ```bash
   git clone <REPOSITORY_URL>
   cd AWSik/AWS/Podstawy_AWS
   python -m venv env_aws
   source env_aws/bin/activate  # Linux/Mac
   env_aws\Scripts\activate     # Windows
   pip install boto3
