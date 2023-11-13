import json
import boto3


class LambdaAWS:
    def list_lambda_functions(self):
        lambda_client = boto3.client("lambda", region_name="eu-central-1")

        try:
            response = lambda_client.list_functions()
            funs = response["Functions"]

            print("Available lambdas [λ]:")
            for function in funs:
                print(function["FunctionName"])
        except Exception as e:
            print(e)
        return funs

    def invoke_lambda_function(self, function_name):
        lambda_client = boto3.client("lambda", region_name="eu-central-1")

        try:
            input_event = {"myValue": 2, "myPow": 3}

            response = lambda_client.invoke(
                FunctionName=function_name,
                InvocationType="RequestResponse",
                Payload=json.dumps(input_event),
            )

            response_payload = response["Payload"].read()

            print(f"\nOutput of the {function_name}:")
            print(response_payload.decode("utf-8"))
        except Exception as e:
            print(e)