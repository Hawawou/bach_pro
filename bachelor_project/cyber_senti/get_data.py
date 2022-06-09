# from tweepy.streaming import Stream
# import tweepy as tw
# from tweepy import Stream
# from bachelor_project.settings import env

# class TweetListener(tw.Stream):

#     def on_data(self, data):
#         print(data)
#         return True

#     def on_error(sel, status):
#         print(status)

# access_token = env('TWEET_ACCESS_TOKEN')
# access_token_secret = env('TWEET_ACCESS_TOKEN_SECRET')
# consumer_key = env('TWEET_CONSUMER_KEY')
# consumer_secret = env('TWEET_CONSUMER_SECRET')

# if __name__ == "__main__":
#     # auth = TweetListener(
#     #     consumer_key, consumer_secret,
#     #     access_token, access_token_secret)
#     stream = Stream(consumer_key, consumer_secret,
#         access_token, access_token_secret)
#     twitter_account = "Jessica Nono"
#     stream.filter(track=["HawaOumarr"])
