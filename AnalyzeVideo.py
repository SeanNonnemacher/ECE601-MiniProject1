import os
import io

from google.cloud import videointelligence


def analyzeVideo(username):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r"C:\Users\Sean\Downloads\key.json"
    print("Videos/" + username + ".mp4")
    with io.open("Videos/" + username + ".mp4", 'rb') as movie:
        input_content = movie.read()
        
    analyze_labels(input_content)





def analyze_labels(input_content):
    video_client = videointelligence.VideoIntelligenceServiceClient()
    features = [videointelligence.enums.Feature.LABEL_DETECTION]
    operation = video_client.annotate_video(input_content = input_content, features=features)
   
    print('\nProcessing video for label annotations:')

    result = operation.result(timeout=90)
    print('\nFinished processing.')

    shot_labels = result.annotation_results[0].shot_label_annotations
    for i, shot_label in enumerate(shot_labels):
        print('Shot label description: {}'.format(
            shot_label.entity.description))
        for category_entity in shot_label.category_entities:
            print('\tLabel category description: {}'.format(
                category_entity.description))
    
        for i, shot in enumerate(shot_label.segments):
            start_time = (shot.segment.start_time_offset.seconds +
                          shot.segment.start_time_offset.nanos / 1e9)
            end_time = (shot.segment.end_time_offset.seconds +
                        shot.segment.end_time_offset.nanos / 1e9)
            positions = '{}s to {}s'.format(start_time, end_time)
            confidence = shot.confidence
            print('\tSegment {}: {}'.format(i, positions))
            print('\tConfidence: {}'.format(confidence))
        print('\n')


