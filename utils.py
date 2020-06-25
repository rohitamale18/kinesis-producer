import os
from typing import Tuple


def get_access_keys() -> Tuple:
    """
    extract access keys from environment variables
    :return:
    """
    aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
    twitter_access_key_id = os.getenv("TWITTER_API_KEY")
    twitter_secret_access_key = os.getenv("TWITTER_API_SECRET_KEY")
    twitter_access_token = os.getenv("TWITTER_ACCESS_TOKEN")
    twitter_secret_access_token = os.getenv("TWITTER_ACCESS_SECRET_TOKEN")

    return (aws_access_key_id,
            aws_secret_access_key,
            twitter_access_key_id,
            twitter_secret_access_key,
            twitter_access_token,
            twitter_secret_access_token)


if __name__ == '__main__':
    print(get_access_keys())
