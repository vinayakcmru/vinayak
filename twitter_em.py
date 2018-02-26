import tweepy

def login_to_twitter(consumer_key, consumer_secret, access_token, access_token_secret):
 
    auth = tweepy.OAuthHandler(consumer_key,  consumer_secret)
    auth.set_access_token(access_token,       access_token_secret)
 
    api = tweepy.API(auth)
    ret = {}
    ret['api'] = api
    ret['auth'] = auth
    return  api
 
 
 
def post_tweets():
 
    consumer_key	   =   'LYtkfKiEhvZC8ESwKhjrWzW0x'
    consumer_secret	   =   'yYA6rSrviGciwjpzJWlIqYg0PG6opeIL9CbaNOSUzxgclA2MVW'
    access_token	   =   '899683933712859136-1j7j7JBvthNB0PxhTUVvLsPv84bqgnE'
    access_token_secret=   'OBej4V3amu0OG0yS0M66dvpO9aKz6SzJueS8O4C2J1v7P'
 
    message = "Hello,\nwhere are you"
 
    api = login_to_twitter(consumer_key, consumer_secret, access_token, access_token_secret )
 
    ret = api.update_status(status=message)
 
 
if __name__ == '__main__':
    post_tweets()
