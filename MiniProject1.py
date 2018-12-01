import CreateVideo as createVideo
import AnalyzeVideo as analyzeVideo
import GetPictures as getPictures
from TwitterDBConnector import MyDB


#Changeable constants
USERNAME = "NASA"
NUM_IMAGES = 10
FRAME_DURATION = "2"



try:
    myDB = MyDB()
    
    getPictures.getPictures(USERNAME, NUM_IMAGES)
    
    createVideo.createVideo(USERNAME, FRAME_DURATION)
    
    labels = analyzeVideo.analyzeVideo(USERNAME)
    
    sessionID = myDB.add_new_session(USERNAME, NUM_IMAGES, len(labels))
    
    for label in labels:
        myDB.add_new_label(sessionID, label)
except Exception as e:
    print(e)
    
myDB.close_connection()
