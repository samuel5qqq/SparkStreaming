# SparkStreaming
we want to do the sentiment analysis for all the tweets for #trump, #obama and collect their
location information (city or state or country).

### Installing
Environment: Apache Spark, Kafka(optional)

## Program description
### Scrapper
<p>The scrapper will collect all tweets and sends them to Kafka for
analytics. </p>

a. Collecting tweets in real-time with particular hash tags. For example, we
will collect all tweets with #trump, #obama.</br>
b. After getting tweets we will filter them based on their locations. If any
tweet does not have location, we will discard them.
c. After filtering, we will send them (tweets with location) to sentiment analyzer through socket.
d. Scrapper program will run infinitely and should take hash tag as
input parameter while running.

### Sentiment Analyzer
Sentiment Analysis is the process of determining whether a piece of
writing is positive, negative or neutral. It's also known as opinion mining,
deriving the opinion or attitude of a speaker.

## Authors

* **Samuel Chen** - *Initial work*
