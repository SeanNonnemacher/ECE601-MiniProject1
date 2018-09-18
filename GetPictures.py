import os
import json
import tweepy
import wget
from tweepy import OAuthHandler


CONSUMER_KEY = "EnterKey"
CONSUMER_SECRET = "EnterKey"
ACCESS_KEY = "EnterKey"
ACCESS_SECRET = "EnterKey"


def getPictures(username, numImages):
    auth = authorise_twitter_api()
    api = tweepy.API(auth)
    downloadImages(api, username, numImages)
    #test(api, numImages, username)
 
def test(api, numImages, username):
    folderName = username + "Images"
    timeline = api.user_timeline(count=100, screen_name = username)
    downloaded = 0 
    for tweet in timeline: 
        file_name = username + '{:04}'.format(downloaded) + '.jpg'
        for media in tweet.entities.get("media",[{}]):
            #checks if there is any media-entity
            if media.get("type",None) == "photo":
                print("1")
                # checks if the entity is of the type "photo"
                wget.download(media["media_url"], folderName+'/'+file_name)
                downloaded += 1
     
def authorise_twitter_api():
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    return auth
 
 
@classmethod   
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status


def create_folder(output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
        
def downloadImages(api, username, numImages):
    status = tweepy.Cursor(api.user_timeline, screen_name=username, include_rts=True, exclude_replies=True, tweet_mode='extended').items()
    folderName = username + "Images"
    create_folder(folderName)
    downloaded = 0

    for tweet_status in status:
        
        if(downloaded >= numImages):
            break
    
        for media_url in tweet_media_urls(tweet_status):
            print(media_url)
            file_name = username + '{:04}'.format(downloaded) + '.jpg'
            wget.download(media_url, folderName+'/'+file_name)
            downloaded += 1


def tweet_media_urls(tweet_status):
    media = tweet_status._json.get('extended_entities', {}).get('media', [])
    if (len(media) == 0):
        return []
    else:
        return [item['media_url'] for item in media]
        
    
    
    
    