import os

#Creates video from given folder of images
def createVideo(username, frameDuration):
    videoFolder = "Videos"
    createFolder(videoFolder)
    
    try:
        command = "ffmpeg -r "+frameDuration+" -s 1920x1080 -i "+username+"Images/"+username+"%04d.jpg -vcodec mpeg4 -y Videos/"+username+".mp4"
        os.system(command)
    except:
        print("FFmpeg video creation error")
        
#Creates folder for videos if it does not exist
def createFolder(folder):
    try:
        if not os.path.exists(folder):
            os.makedirs(folder)
    except:
        print("Video folder not successfully created")