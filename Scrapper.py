import os
import tweepy
import re
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import socket
import json

access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""


class TweetsListener(StreamListener):
    def __init__(self, csocket):
        self.client_socket = csocket

    def on_data(self, data):
        try:
            data1= json.loads(data)
            line = data1.get('text')
            line2 = clean_tweet(line)
            print(str(line2))
            self.client_socket.send(line.encode('utf-8'))
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

def clean_tweet(tweet):

    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w +:\ / \ / \S +)", " ", tweet).split())

def main():
    s = socket.socket()
    s.bind(("localhost", 9092))

    print("Waiting for consumer's request...")

    s.listen(5)
    c, addr = s.accept()

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    twitter_stream = Stream(auth, TweetsListener(c))
    twitter_stream.filter(track=['#trump','#obama'])

if __name__ == "__main__":
    main()
