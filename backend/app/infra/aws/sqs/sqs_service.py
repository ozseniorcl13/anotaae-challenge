import os

import boto3
from botocore.exceptions import BotoCoreError, ClientError


class SQSService:
    def __init__(self):
        self.sqs = boto3.client("sqs", region_name=os.getenv("AWS_REGION"))

    def send_message(self, queue_url: str, message_body: str, delay_seconds: int = 0):
        try:
            self.sqs.send_message(
                QueueUrl=queue_url, MessageBody=message_body, DelaySeconds=delay_seconds
            )
        except (BotoCoreError, ClientError) as error:
            print(f"Erro ao enviar mensagem: {error}")
