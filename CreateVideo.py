import os

def createVideo(username, frameDuration):
    try:
        command = "ffmpeg -r "+frameDuration+" -s 1920x1080 -i "+username+"Images/"+username+"%04d.jpg -vcodec mpeg4 -y Videos/"+username+".mp4"
        os.system(command)
    except:
        print("FFmpeg video creation error")
        