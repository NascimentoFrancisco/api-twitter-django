# Generated by Django 4.0.5 on 2022-06-06 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_tweet', models.CharField(max_length=200)),
                ('retweet', models.BooleanField()),
                ('tweetText', models.TextField()),
            ],
        ),
    ]
