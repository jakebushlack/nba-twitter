import tweepy
import pandas

print("scrape")
print("query")


def tweet(tweet_contents):
    try:
        auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
        auth.set_access_token(keys.access_token, keys.access_token_secret)
        api = tweepy.API(auth)
        disclaimer = "Stats courtesy of Basketball-Reference.com"
        api.update_status(tweet_contents + '\n\n' + disclaimer)
    except Exception as e:
        print(len(tweet_contents) + len(disclaimer))
        print(e)
