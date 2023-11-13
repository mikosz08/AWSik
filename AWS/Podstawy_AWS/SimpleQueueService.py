import boto3


class SimpleQueueService:
    queue_url = "https://sqs.eu-central-1.amazonaws.com/216552612841/MySQS"
    sqs = boto3.client("sqs")

    def send_message(self):
        response = self.sqs.send_message(QueueUrl=self.queue_url, MessageBody="Penguin")
        print(response["MessageId"])

    def recive_message(self):
        messages = self.sqs.receive_message(
            QueueUrl=self.queue_url, MaxNumberOfMessages=1, WaitTimeSeconds=10
        )

        if "Messages" in messages:
            for message in messages["Messages"]:
                print(message["Body"])
                self.sqs.delete_message(
                    QueueUrl=self.queue_url, ReceiptHandle=message["ReceiptHandle"]
                )