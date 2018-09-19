import os
import tweepy
import wget
from tweepy import OAuthHandler

#Enter given keys
CONSUMER_KEY = "enterKey"
CONSUMER_SECRET = "enterKey"
ACCESS_KEY = "enterKey"
ACCESS_SECRET = "enterKey"


def getPictures(username, numImages):
    auth = authoriseTwitterApi()
    api = tweepy.API(auth)
    downloadImages(api, username, numImages)
 
#Authorizes twitter keys
def authoriseTwitterApi():
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    return auth
 
#Creates folder for user images
def createFolder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
        
#Download images from the media url    
def downloadImages(api, username, numImages):
    status = tweepy.Cursor(api.user_timeline, screen_name=username, include_rts=True, exclude_replies=True, tweet_mode='extended').items()
    folderName = username + "Images"
    createFolder(folderName)
    downloaded = 0

    for tweet_status in status:
        
        if(downloaded >= numImages):
            break
    
        for media_url in getMediaUrls(tweet_status):
            print(media_url)
            file_name = username + '{:04}'.format(downloaded) + '.jpg'
            wget.download(media_url, folderName+'/'+file_name)
            downloaded += 1

#Returns media urls for tweets with pictures
def getMediaUrls(tweet_status):
    media = tweet_status._json.get('extended_entities', {}).get('media', [])
    if (len(media) == 0):
        return []
    else:
        return [item['media_url'] for item in media]
        
    
    
    
    