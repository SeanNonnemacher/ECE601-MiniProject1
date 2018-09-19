import CreateVideo as createVideo
import AnalyzeVideo as analyzeVideo
import GetPictures as getPictures

#Changeable constants
USERNAME = "NASA"
NUM_IMAGES = 10
FRAME_DURATION = ".25"

getPictures.getPictures(USERNAME, NUM_IMAGES)
    
createVideo.createVideo(USERNAME, FRAME_DURATION)

analyzeVideo.analyzeVideo(USERNAME)
