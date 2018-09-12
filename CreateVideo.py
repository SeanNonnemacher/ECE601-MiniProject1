import os

def createVideo(twitter, frameDuration):
    try:
        command = "ffmpeg -r "+frameDuration+" -s 1920x1080 -i Pictures/"+twitter+"%04d.jpg -vcodec mpeg4 -y Videos/"+twitter+".mp4"
        os.system(command)
    except(RuntimeError):
        print("FFmpeg video creation error")
        