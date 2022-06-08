from tweepy.streaming import Stream
import tweepy as tw
from tweepy import Stream

class TweetListener(tw.Stream):

    def on_data(self, data):
        print(data)
        return True

    def on_error(sel, status):
        print(status)

access_token = "1247811144942682112-LAWA6x3iemoa40nxu2tQakXeK1HNzp"
access_token_secret = "vslVzHNQWs961DEIK3PRHEizejvylMCWqAUy3BaqvlSiZ"
consumer_key = "YQwfghS2GZePhmy1LRaKu1JT4"
consumer_secret = "tCnZskF26CBKg2a6NSrciZFDgActEpumP4fPmpbY7FxJDs8nZo"

if __name__ == "__main__":
    # auth = TweetListener(
    #     consumer_key, consumer_secret,
    #     access_token, access_token_secret)
    stream = Stream(consumer_key, consumer_secret,
        access_token, access_token_secret)
    twitter_account = "Jessica Nono"
    stream.filter(track=["HawaOumarr"])
