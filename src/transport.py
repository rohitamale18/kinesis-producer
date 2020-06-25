import tweepy
import json
from src.authorization import AWSClient, TwitterClient


class StreamListener(tweepy.StreamListener):

    def __init__(self, aws_client, delivery_stream):
        self.aws_client = aws_client
        self.delivery_stream_name = delivery_stream
        self.filters = ['created_at', 'id', 'id_str', 'text']

    def on_data(self, tweet):

        tweet = json.loads(tweet)
        filtered = {}
        try:
            for key in self.filters:
                filtered[key] = tweet[key]
            # message = "|".join(str(val) for val in filtered.values())
            # encodedValues = bytes(message, 'utf-8')
            self.aws_client.put_record(DeliveryStreamName=self.delivery_stream_name,
                                       Record={'Data': json.dumps(filtered)})
            print(tweet)
        except Exception as e:
            print(e)

    def on_error(self, status_code):
        if status_code == 420:
            return False


def main():
    aws_client = AWSClient()
    twitter_client = TwitterClient()
    stream_listener = StreamListener(aws_client=aws_client.client,
                                     delivery_stream='twitter-stream')
    stream = tweepy.Stream(auth=twitter_client.twitter_api.auth,
                           listener=stream_listener)
    stream.filter(
        track=["corona"]
    )


if __name__ == "__main__":
    main()
