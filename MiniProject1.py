import CreateVideo as createVideo
import AnalyzeVideo as analyzeVideo
import GetPictures as getPictures

TWITTER = "test"
FRAME_DURATION = ".25"

getPictures.getPictures(TWITTER)
    
createVideo.createVideo(TWITTER, FRAME_DURATION)

analyzeVideo.analyzeVideo(TWITTER)
