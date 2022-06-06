from django.db import models

# Create your models here.

class Tweets(models.Model):
    id_tweet = models.CharField(max_length=200)
    retweet = models.BooleanField()
    tweetText = models.TextField()

    def __str__(self):
        return self.id_tweet