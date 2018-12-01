import os
import io

from google.cloud import videointelligence

#location of Google Credentials.json file
GOOGLE_KEY_JSON_FILE = "C:/Users/Sean/Desktop/601 Keys/key.json"

#Analyzes video from given location
def analyzeVideo(username):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_KEY_JSON_FILE
    print("Videos/" + username + ".mp4")
    
    with io.open("Videos/" + username + ".mp4", 'rb') as movie:
        input_content = movie.read()
    labels = analyzeLabels(input_content)
    return labels


#Analyzes video and outputs labels to console
def analyzeLabels(input_content):
    videoClient = videointelligence.VideoIntelligenceServiceClient()
    features = [videointelligence.enums.Feature.LABEL_DETECTION]
    operation = videoClient.annotate_video(input_content = input_content, features=features)
   
    print('\nProcessing video for label annotations:')

    result = operation.result(timeout=90)
    print('\nFinished processing.')
    
    labels = []

    shotLabels = result.annotation_results[0].shot_label_annotations
    for i, shot_label in enumerate(shotLabels):
        print('Shot label description: {}'.format(
            shot_label.entity.description))
        for category_entity in shot_label.category_entities:
            print('\tLabel category description: {}'.format(
                category_entity.description))
            labels.append(category_entity.description)
    
        for i, shot in enumerate(shot_label.segments):
            startTime = (shot.segment.start_time_offset.seconds +
                          shot.segment.start_time_offset.nanos / 1e9)
            endTime = (shot.segment.end_time_offset.seconds +
                        shot.segment.end_time_offset.nanos / 1e9)
            positions = '{}s to {}s'.format(startTime, endTime)
            confidence = shot.confidence
            print('\tSegment {}: {}'.format(i, positions))
            print('\tConfidence: {}'.format(confidence))
        print('\n')
    return labels


