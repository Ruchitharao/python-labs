import json
import boto3
import csv

s3 = boto3.resource('s3')


def lambda_handler(event, context):
    # TODO implement

    bucket = 'MyBucketName'
    sourceFile = 'recent_pic.jpg'
    targetFile = 'friend.jpg'

    # with open('credentials.csv', 'r') as input:
    #     next(input)
    #     reader = csv.reader(input)
    #     for line in reader:
    #         access_key_id = line[2]
    #         secret_access_key = line[3]

    client = boto3.client('rekognition')

    response = client.compare_faces(SimilarityThreshold=70,
                                    SourceImage={'S3Object': {'Bucket': 'testingrekon', 'Name': sourceFile}},
                                    TargetImage={'S3Object': {'Bucket': 'testingrekon', 'Name': targetFile}})

    for faceMatch in response['FaceMatches']:
        position = faceMatch['Face']['BoundingBox']
        confidence = str(faceMatch['Face']['Confidence'])
        print('The face at ' +
              str(position['Left']) + ' ' +
              str(position['Top']) +
              ' matches with ' + confidence + '% confidence')

    if response['FaceMatches'] == []:

        return {
            'statusCode': 200,
            'body': "Unmatched Faces"
        }
    else:
        return {
            'statusCode': 200,
            'body': "Face matched with " + confidence + " " + "confidence"
        }


