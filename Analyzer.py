import time
import json
import re
from textblob import TextBlob
from pyspark import SparkContext
from pyspark.streaming import StreamingContext


def clean_tweet(tweet):

    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w +:\ / \ / \S +)", " ", tweet).split())


def get_tweet_sentiment(tweet):

    analysis = TextBlob(tweet)

    if analysis.sentiment.polarity > 0:
        return 'positive:'+tweet
    elif analysis.sentiment.polarity == 0:
        return 'neutral:'+tweet
    else:
        return 'negative:'+tweet


sc = SparkContext("local[2]", "Twitter Demo")
ssc = StreamingContext(sc, 10)
lines = ssc.socketTextStream("localhost", 9092)


lines.foreachRDD(lambda rdd: rdd.map(lambda x:str(clean_tweet(x))).filter(lambda x:len(x)>0)
                 .map(lambda x:str(get_tweet_sentiment(x))).coalesce(1).saveAsTextFile("./tweets/%f"% time.time()) )


ssc.start()
ssc.awaitTermination()