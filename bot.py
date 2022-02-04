import assembler
import creds
import tweepy

class MyStreamListener(tweepy.Stream):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        if tweet.in_reply_to_status_id is not None or \
            tweet.user.id == self.me.id:
            # This tweet is a reply or I'm its author so, ignore it
            return
        if not tweet.favorited:
            # Mark it as Liked, since we have not done it yet
            try:
                tweet.favorite()
            except Exception as e:
                
        if not tweet.retweeted:
            # Retweet, since we have not retweeted it yet
            try:
                tweet.retweet()
            except Exception as e:
            
        if not user.following():
            # follow, since we have not followed yet
            try:
                tweet.user.follow()
            except Exception as e:
                

    def on_error(self, status):
        print("Error detected")

api = tweepy.Client(bearer_token = creds.BEARER_TOKEN, consumer_key = creds.API_KEY, consumer_secret = creds.API_KEY_SECRET, access_token = creds.ACCESS_TOKEN, 
                    access_token_secret = creds.ACCESS_TOKEN_SECRET, wait_on_rate_limit=True)

stream = tweepy.Stream(user)
listener = MyStreamListener(stream)
stream.filter(track=["Ethan Exline", "HTWTABW", "Fact", "Random"], languages=["en"])

trends_result = api.trends_place(1)
trends = trends_result[0]["trends"]

tweeted = False
while not tweeted:
    printFact = assembler.returnFact()
    printFact += " #" + trends[0]["name"]
    if len(printFact) <= 140:
        print(printFact) # tweeting functionality will happen here
        tweeted = True
    else:
        continue