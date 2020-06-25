import boto3
from src.authorization import AWSAuthorization
import logging


class AWSClient(AWSAuthorization):

    def __init__(self):
        self.firehose_client = None
        self.AWSSession = None
        self.AWSAuth = AWSAuthorization()

    def get_aws_authorization(self):
        self.AWSSession = self.AWSAuth.aws_session

    def set_firehose_client(self):
        try:
            self.client = boto3.client('firehose', region_name='us-east-1',
                                       aws_access_key_id=self.aws_access_key,
                                       aws_secret_access_key=self.aws_secret_access_key
                                       )
        except Exception as e:
            logging.info(f"Exception occurred while initiating AWS Connection: {str(e)}")


class TwitterClient(object):

    def __init__(self, firehose_stream_name):
        self.firehose_client = None
        self.stream_name = firehose_stream_name
        self.aws_access_key = None
        self.aws_secret_access_key = None
        self.set_aws_authorization()
        self.set_firehose_client()

    def set_aws_authorization(self):
        obj = AWSAuthorization()
        self.aws_access_key = obj.access_key_value
        self.aws_secret_access_key = obj.secret_access_key_value

    def set_firehose_client(self):
        try:
            self.client = boto3.client('firehose', region_name='us-east-1',
                                       aws_access_key_id=self.aws_access_key,
                                       aws_secret_access_key=self.aws_secret_access_key
                                       )
        except Exception as e:
            logging.info(f"Exception occurred while initiating AWS Connection: {str(e)}")