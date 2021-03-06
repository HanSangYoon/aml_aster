# Generated by Django 2.2.1 on 2019-05-08 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FacebookFriends',
            fields=[
                ('no_index', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(default=None, max_length=255, null=True)),
                ('origin_ph', models.CharField(default=None, max_length=255, null=True)),
                ('friends_name', models.CharField(default=None, max_length=255, null=True)),
                ('friends_info', models.CharField(default=None, max_length=255, null=True)),
                ('friends_id', models.CharField(default=None, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FacebookInfo',
            fields=[
                ('no_index', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(default=None, max_length=255, null=True)),
                ('origin_ph', models.CharField(default=None, max_length=255, null=True)),
                ('username', models.CharField(default=None, max_length=255, null=True)),
                ('gender', models.CharField(default=None, max_length=255, null=True)),
                ('phone_number', models.CharField(default=None, max_length=255, null=True)),
                ('birthday', models.CharField(default=None, max_length=255, null=True)),
                ('company1', models.CharField(default=None, max_length=255, null=True)),
                ('company2', models.CharField(default=None, max_length=255, null=True)),
                ('company3', models.CharField(default=None, max_length=255, null=True)),
                ('university1', models.CharField(default=None, max_length=255, null=True)),
                ('university2', models.CharField(default=None, max_length=255, null=True)),
                ('university3', models.CharField(default=None, max_length=255, null=True)),
                ('address1', models.CharField(default=None, max_length=255, null=True)),
                ('address2', models.CharField(default=None, max_length=255, null=True)),
                ('address3', models.CharField(default=None, max_length=255, null=True)),
                ('contact1', models.CharField(default=None, max_length=255, null=True)),
                ('contact2', models.CharField(default=None, max_length=255, null=True)),
                ('contact3', models.CharField(default=None, max_length=255, null=True)),
                ('contact4', models.CharField(default=None, max_length=255, null=True)),
                ('friends_cnt', models.IntegerField(default=None, null=True)),
                ('insertedTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='FacebookPost',
            fields=[
                ('no_index', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(default=None, max_length=255, null=True)),
                ('origin_ph', models.CharField(default=None, max_length=255, null=True)),
                ('post_text', models.TextField(default=None, null=True)),
                ('post_info', models.CharField(default=None, max_length=255, null=True)),
                ('post_date', models.DateField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GmailInfo',
            fields=[
                ('no_index', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(default=None, max_length=255, null=True)),
                ('origin_ph', models.CharField(default=None, max_length=255, null=True)),
                ('mail_cnt', models.IntegerField(default=None, null=True)),
                ('insertedTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='GmailList',
            fields=[
                ('no_index', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(default=None, max_length=255, null=True)),
                ('origin_ph', models.CharField(default=None, max_length=255, null=True)),
                ('gmail_sender', models.CharField(default=None, max_length=255, null=True)),
                ('gmail_sender_email', models.CharField(default=None, max_length=255, null=True)),
                ('gmail_title', models.CharField(default=None, max_length=255, null=True)),
                ('gmail_contents', models.TextField(default=None, null=True)),
                ('gmail_date', models.DateField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InstagramFollow',
            fields=[
                ('no_index', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(default=None, max_length=255, null=True)),
                ('origin_ph', models.CharField(default=None, max_length=255, null=True)),
                ('follow_id', models.CharField(default=None, max_length=255, null=True)),
                ('follow_name', models.CharField(default=None, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InstagramFollower',
            fields=[
                ('no_index', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(default=None, max_length=255, null=True)),
                ('origin_ph', models.CharField(default=None, max_length=255, null=True)),
                ('follower_id', models.CharField(default=None, max_length=255, null=True)),
                ('follower_name', models.CharField(default=None, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InstagramInfo',
            fields=[
                ('no_index', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(default=None, max_length=255, null=True)),
                ('origin_ph', models.CharField(default=None, max_length=255, null=True)),
                ('page_id', models.CharField(default=None, max_length=255, null=True)),
                ('username', models.CharField(default=None, max_length=255, null=True)),
                ('intro', models.CharField(default=None, max_length=255, null=True)),
                ('homepage', models.CharField(default=None, max_length=255, null=True)),
                ('company1', models.CharField(default=None, max_length=255, null=True)),
                ('post_cnt', models.IntegerField(default=None, null=True)),
                ('follower_cnt', models.IntegerField(default=None, null=True)),
                ('follow_cnt', models.IntegerField(default=None, null=True)),
                ('insertedTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='InstagramPost',
            fields=[
                ('no_index', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(default=None, max_length=255, null=True)),
                ('origin_ph', models.CharField(default=None, max_length=255, null=True)),
                ('post_text', models.TextField(default=None, null=True)),
                ('post_place', models.CharField(default=None, max_length=255, null=True)),
                ('post_info', models.CharField(default=None, max_length=255, null=True)),
                ('post_like', models.IntegerField(default=None, null=True)),
                ('post_view', models.IntegerField(default=None, null=True)),
                ('post_date', models.DateField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TwitterFollower',
            fields=[
                ('no_index', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(default=None, max_length=255, null=True)),
                ('origin_ph', models.CharField(default=None, max_length=255, null=True)),
                ('follower_name', models.CharField(default=None, max_length=255, null=True)),
                ('follower_page_id', models.CharField(default=None, max_length=255, null=True)),
                ('follower_info', models.CharField(default=None, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TwitterFollowing',
            fields=[
                ('no_index', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(default=None, max_length=255, null=True)),
                ('origin_ph', models.CharField(default=None, max_length=255, null=True)),
                ('following_name', models.CharField(default=None, max_length=255, null=True)),
                ('following_page_id', models.CharField(default=None, max_length=255, null=True)),
                ('following_info', models.CharField(default=None, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TwitterInfo',
            fields=[
                ('no_index', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(default=None, max_length=255, null=True)),
                ('origin_ph', models.CharField(default=None, max_length=255, null=True)),
                ('username', models.CharField(default=None, max_length=255, null=True)),
                ('page_id', models.CharField(default=None, max_length=255, null=True)),
                ('tweet_cnt', models.IntegerField(default=None, null=True)),
                ('following_cnt', models.IntegerField(default=None, null=True)),
                ('follower_cnt', models.IntegerField(default=None, null=True)),
                ('joined_date', models.DateField(default=None, null=True)),
                ('insertedTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TwitterTrends',
            fields=[
                ('no_index', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(default=None, max_length=255, null=True)),
                ('origin_ph', models.CharField(default=None, max_length=255, null=True)),
                ('trends_name', models.CharField(default=None, max_length=255, null=True)),
                ('trends_tweet_cnt', models.CharField(default=None, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TwitterTweet',
            fields=[
                ('no_index', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(default=None, max_length=255, null=True)),
                ('origin_ph', models.CharField(default=None, max_length=255, null=True)),
                ('tweet_name', models.CharField(default=None, max_length=255, null=True)),
                ('tweet_page_id', models.CharField(default=None, max_length=255, null=True)),
                ('tweet_text', models.TextField(default=None, null=True)),
                ('tweet_date', models.DateField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='YoutubeCommentHistory',
            fields=[
                ('no_index', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(default=None, max_length=255, null=True)),
                ('origin_ph', models.CharField(default=None, max_length=255, null=True)),
                ('video_name', models.CharField(default=None, max_length=255, null=True)),
                ('video_comment', models.CharField(default=None, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='YoutubeInfo',
            fields=[
                ('no_index', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(default=None, max_length=255, null=True)),
                ('origin_ph', models.CharField(default=None, max_length=255, null=True)),
                ('username', models.CharField(default=None, max_length=255, null=True)),
                ('subscribe_cnt', models.IntegerField(default=None, null=True)),
                ('insertedTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='YoutubeRecentVideo',
            fields=[
                ('no_index', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(default=None, max_length=255, null=True)),
                ('origin_ph', models.CharField(default=None, max_length=255, null=True)),
                ('video_channel_name', models.CharField(default=None, max_length=255, null=True)),
                ('video_name', models.CharField(default=None, max_length=255, null=True)),
                ('video_info', models.CharField(default=None, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='YoutubeSubscribe',
            fields=[
                ('no_index', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(default=None, max_length=255, null=True)),
                ('origin_ph', models.CharField(default=None, max_length=255, null=True)),
                ('channel_name', models.CharField(default=None, max_length=255, null=True)),
                ('channel_info', models.CharField(default=None, max_length=255, null=True)),
                ('subscribe_cnt', models.IntegerField(default=None, null=True)),
                ('channel_sub_cnt', models.IntegerField(default=None, null=True)),
                ('channel_video_cnt', models.IntegerField(default=None, null=True)),
            ],
        ),
    ]
