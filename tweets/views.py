from django.shortcuts import render
from tweets.models import Tweets
from tweets.api_keys import ApyKeys
import tweepy
# Create your views here.
def home(request):
    if request.method == 'POST':
        consumer_key = ApyKeys.Comsumer_key()
        consumer_secret_key = ApyKeys.Comsumer_secret_key()
        bearer_token = ApyKeys.Bearer_Token()
        access_token = ApyKeys.Access_Token()
        access_secret_token = ApyKeys.Access_Secret_Token()
        
        keyword = request.POST['keyword']

        client = tweepy.Client(bearer_token,consumer_key,consumer_secret_key,access_token,access_secret_token)
        response = client.search_recent_tweets(query = keyword,max_results = 100)
    
        for tweet in response.data:
            if tweet.text[:2] == 'RT':
                Tweets.objects.create(id_tweet = str(tweet.id),retweet = True,tweetText = tweet.text[2:])
            else:
                Tweets.objects.create(id_tweet = str(tweet.id),retweet = False,tweetText = tweet.text)

    tweets = Tweets.objects.all()

    return render(request,'tweets/home.html',{'tweets':tweets})
