from LambdaAWS import LambdaAWS
from SimpleQueueService import SimpleQueueService
from DynamoDB import DynamoDB
from BucketS3 import BucketS3


def test_lambdas():
    lambdaAWS = LambdaAWS()
    lambdaAWS.list_lambda_functions()
    function_name = "helloLambda"
    lambdaAWS.invoke_lambda_function(function_name)


def test_sqs():
    sqs = SimpleQueueService()
    sqs.send_message()
    sqs.recive_message()


def test_dynamo():
    dynamo = DynamoDB()
    dynamo.put_item()


def test_bucket():
    bucket = BucketS3()
    bucket.create_and_send_file()


if __name__ == "__main__":
    # test_lambdas()
    # test_sqs()
    # test_dynamo()
    test_bucket()
