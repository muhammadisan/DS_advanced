import tweepy

consumer_key = "consumer_key"
consumer_secret = "consumer_secret"
access_token = "access_token"
access_token_secret = "access_token_secret"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

Indonesia_woe = 23424846
    
trends = api.trends_place(Indonesia_woe)

import re
import pandas as pd

pos_list = open("./kata_positif.txt", "r")
pos_kata = pos_list.readlines()
neg_list = open("./kata_negatif.txt", "r")
neg_kata = neg_list.readlines()
############################### topik 1
search_words = "IKAN HIU MAKAN TOMAT"
date_since = "2020-09-07"
new_search = search_words + " -filter:retweets"

tweets = tweepy.Cursor(api.search, q=new_search, lang="id", since=date_since).items(2000)

items = []
for tweet in tweets:
  items.append (' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet.text).split()))
hasil = pd.DataFrame(data=items, columns=['tweet'])

tweet_sentiment = []
for item in items:
  count_p = 0
  count_n = 0
  for kata_pos in pos_kata:
    if kata_pos.strip() in item:
      count_p += 1
  for kata_neg in neg_kata:
    if kata_neg.strip() in item:
        count_n += 1
  tweet_sentiment.append(count_p - count_n)

hasil['value'] = tweet_sentiment
############################### topik 2
search_words1 = "Kemenkesgagap"
date_since1 = "2020-09-07"
new_search1 = search_words1 + " -filter:retweets"

tweets1 = tweepy.Cursor(api.search, q=new_search1, lang="id", since=date_since1).items(2000)

items1 = []
for tweet in tweets1:
  items1.append (' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet.text).split()))
hasil1 = pd.DataFrame(data=items1, columns=['tweet'])

tweet_sentiment1 = []
for item in items1:
  count_p = 0
  count_n = 0
  for kata_pos in pos_kata:
    if kata_pos.strip() in item:
      count_p += 1
  for kata_neg in neg_kata:
    if kata_neg.strip() in item:
        count_n += 1
  tweet_sentiment1.append(count_p - count_n)

hasil1['value'] = tweet_sentiment1

import matplotlib.pyplot as plt
import numpy as np

labels, counts = np.unique(tweet_sentiment, return_counts=True)
plt.bar(labels, counts, align='center')
plt.gca().set_xticks(labels)
plt.show()
display(hasil)

labels1, counts1 = np.unique(tweet_sentiment1, return_counts=True)
plt.bar(labels1, counts1, align='center')
plt.gca().set_xticks(labels1)
plt.show()
display(hasil1)

print('--IKAN HIU MAKAN TOMAT--')
print('rataan nilai sentiment:', np.mean(tweet_sentiment))
print('mediian nilai sentiment:', np.median(tweet_sentiment))
print('\n')
print('--Kemenkesgagap--')
print('rataan nilai sentiment:', np.mean(tweet_sentiment1))
print('mediian nilai sentiment:', np.median(tweet_sentiment1))

# trend mengenai IKAN HIU MAKAN TOMAT cenderung positif, terlihat 
# juga dari tweet-tweetnya bahwa topik ini lebih ke ranah hiburan.

# trend mengenai Kemenkesgagap bersentiment netral, sedikit condong ke positif
# distribusinya mendekati distribusi normal, banyak tweet bersentimen positif
# dan tweet bersentiment negatif nyaris sama banyak. Nilai modusnya adalah netral
# topik di trend ini topik dengan bahasan yang cukup serius