import boto3
import datetime


class DynamoDB:
    dynamodb = boto3.resource("dynamodb")

    def put_item(self):
        table_name = "MyDynamoTable"
        table = self.dynamodb.Table(table_name)

        item = {
            "ID": 1,
            "Name": "Adam",
            "Age": 35,
            "JobTitle": "Software Developer",
            "Skills": ["Python", "DynamoDB", "AWS", "Serverless"],
            "CreatedAt": datetime.datetime.now().isoformat(),
            "IsActive": True,
            "Project": {
                "Name": "Cloud Migration",
                "Status": "In Progress",
                "Deadline": "2023-12-31",
            },
            "EmploymentHistory": [
                {"Company": "TechCorp", "Role": "Junior Developer", "Years": 2},
                {"Company": "DevFactory", "Role": "Mid-Level Developer", "Years": 3},
                {"Company": "Innovatech", "Role": "Senior Developer", "Years": 4},
            ],
        }

        response = table.put_item(Item=item)

        print(response)
