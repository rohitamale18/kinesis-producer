import os
from src.logger import get_logger
import boto3
import tweepy

logger = get_logger(__name__)


class Authorization(object):

    def __init__(self) -> None:
        self.value = None

    def set_key(self, key):
        self.value = os.getenv(key)

    def get_key(self):
        return self.value

    @staticmethod
    def validate_env_existence(key) -> bool:
        if key not in os.environ:
            logger.info(f"Environment variable, {key} not present in system")
            return False
        else:
            return True


class AWSClient(Authorization):

    def __init__(self) -> None:
        # super().__init__()
        self.access_key_value = None
        self.secret_access_key_value = None
        self.client = None
        self.aws_session = boto3.Session
        self.access_key_name = "AWS_ACCESS_KEY_ID"
        self.secret_access_key_name = "AWS_SECRET_ACCESS_KEY"
        self.get_aws_client()

    def set_aws_keys(self) -> None:
        if self.validate_env_existence(self.access_key_name):
            self.set_key(self.access_key_name)
            self.access_key_value = self.get_key()

        if self.validate_env_existence(self.secret_access_key_name):
            self.set_key(self.secret_access_key_name)
            self.secret_access_key_value = self.get_key()

    def set_aws_session(self) -> None:
        try:
            self.aws_session = boto3.Session(aws_access_key_id=self.access_key_value,
                                             aws_secret_access_key=self.secret_access_key_value,
                                             region_name="us-east-1")
        except Exception as e:
            logger.error(f"Failed to set AWS Session. Error: {str(e)}")

    def get_aws_client(self):
        self.set_aws_keys()
        self.set_aws_session()

        try:
            self.client = self.aws_session.client('firehose')
        except Exception as e:
            logger.info(f"Exception occurred while initiating AWS Connection: {str(e)}")


class TwitterClient(Authorization):

    def __init__(self) -> None:
        # super().__init__()
        self.twitter_api = tweepy.API
        self.twitter_access_key_id_value = None
        self.twitter_secret_access_key_value = None
        self.twitter_access_token_value = None
        self.twitter_secret_access_token_value = None
        self.twitter_access_key_id = "TWITTER_API_KEY"
        self.twitter_secret_access_key = "TWITTER_API_SECRET_KEY"
        self.twitter_access_token_name = "TWITTER_ACCESS_TOKEN"
        self.twitter_secret_access_token_name = "TWITTER_ACCESS_SECRET_TOKEN"
        self.set_twitter_api()

    def set_twitter_authorization(self) -> None:
        if self.validate_env_existence(self.twitter_access_key_id):
            self.set_key(self.twitter_access_key_id)
            self.twitter_access_key_id_value = self.get_key()

        if self.validate_env_existence(
                self.twitter_secret_access_key):
            self.set_key(self.twitter_secret_access_key)
            self.twitter_secret_access_key_value = self.get_key()

        if self.validate_env_existence(self.twitter_access_token_name):
            self.set_key(self.twitter_access_token_name)
            self.twitter_access_token_value = self.get_key()

        if self.validate_env_existence(
                self.twitter_secret_access_token_name):
            self.set_key(self.twitter_secret_access_token_name)
            self.twitter_secret_access_token_value = self.get_key()

    def set_twitter_api(self):
        self.set_twitter_authorization()
        try:
            auth = tweepy.OAuthHandler(self.twitter_access_key_id_value,
                                       self.twitter_secret_access_key_value)
            auth.set_access_token(self.twitter_access_token_value,
                                  self.twitter_secret_access_token_value)
            self.twitter_api = tweepy.API(auth)

        except Exception as e:
            logger.error(f"Failed to set Twitter Session. Error: {str(e)}")
