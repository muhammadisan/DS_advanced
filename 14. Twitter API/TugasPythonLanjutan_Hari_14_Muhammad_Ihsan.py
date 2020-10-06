import tweepy

consumer_key = "consumer_key"
consumer_secret = "consumer_secret"
access_token = "access_token"
access_token_secret = "access_token_secret"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

username = "jokowi"
limit_tweet = 200

tweets = api.user_timeline(id=username, count=limit_tweet)

tweet_covid = 0
for tweet in tweets:
  if ('covid' or 'corona' or 'pandemi') in tweet.text.lower():
    tweet_covid += 1

print('banyak tweet pak Jokowi yang diambil:', limit_tweet)
print('banyak tweet pak Jokowi membicarakan Covid dalam tweetnya:', tweet_covid)