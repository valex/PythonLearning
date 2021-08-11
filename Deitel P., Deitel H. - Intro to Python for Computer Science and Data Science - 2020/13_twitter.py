# https://developer.twitter.com/en/docs/twitter-api/api-reference-index

import tweepy
import keys
from tweetutilities import print_tweets

auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# ----------------------------------------------------
# Getting Account Info
# GET users/show
# https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-users-show
# https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/user
# ----------------------------------------------------
# nasa = api.get_user('nasa')

# print(nasa.id)
# # 11348282

# print(nasa.name)
# # NASA

# print(nasa.screen_name)
# # NASA

# print(nasa.description)
# # There's space for everybody. ✨

# # most recent tweet
# print(nasa.status.text)

# print(nasa.followers_count)
# # 47842042

# print(nasa.friends_count)
# # 175

# me = api.me()

# print(me.screen_name)

# ----------------------------------------------------
# Tweepy Cursors
# https://docs.tweepy.org/en/v3.10.0/cursor_tutorial.html
# ----------------------------------------------------

# followers = []

# cursor = tweepy.Cursor(api.followers, screen_name='nasa')

# for account in cursor.items(10):
#     followers.append(account.screen_name)

# print( 'Followers:', ' '.join(sorted(followers, key=lambda s: s.lower())) )
# # Followers: BlentKa68053253 daentastic Gobinda92521395 MaghrabiYasin MarlonDlcp MrTabish1 Nikoskouman19 REYC32 SaverioParrella TiktokSaad

# followers = []
# cursor = tweepy.Cursor(api.followers, screen_name='nasa', count=200)

# for account in cursor.items(200):
#     followers.append(account.screen_name)

# print( 'Followers:', ' '.join(sorted(followers, key=lambda s: s.lower())) )
# # Followers: 200 items

# friends = []
# cursor = tweepy.Cursor(api.friends, screen_name='nasa')

# for friend in cursor.items(10):
#     friends.append(friend.screen_name)

# print( 'Friends:', ' '.join(sorted(friends, key=lambda s: s.lower())) )
# # Friends: Aki_Hoshide Astro_Megan Astro_Pam dominickmatthew KathyLueders NASA_Gateway NASAArtemis SenBillNelson Thom_astro uaespaceagency

# nasa_tweets = api.user_timeline(screen_name='nasa', count=3)
# for tweet in nasa_tweets:
#     print(f'{tweet.user.screen_name}: {tweet.text}\n')

# my_tweets = api.home_timeline(screen_name='nasa', count=3)
# for tweet in my_tweets:
#     print(f'{tweet.user.screen_name}: {tweet.text}\n')


# ----------------------------------------------------
# Searching Recent Tweets
# ----------------------------------------------------

# tweets = api.search(q='Mars Opportunity Rover', count=3)
# print_tweets(tweets)

# tweets = api.search(q='from:nasa since:2021-08-10', count=3)
# print_tweets(tweets)

# tweets = api.search(q='#collegefootball', count=3)
# print_tweets(tweets)

# ----------------------------------------------------
# Spotting Trends
# ----------------------------------------------------


