import csv
import boto3


with open('credentials.csv', 'r') as input:
    next(input)
    reader = csv.reader(input)
    for line in reader:
        access_key_id = line[2]
        secret_access_key = line[3]

client = boto3.client('rekognition', region_name='us-west-1', aws_access_key_id=access_key_id,
                      aws_secret_access_key=secret_access_key)


# sourceFile = 'recent_pic.jpg'
# targetFile = 'recent_pic.jpg'

response=client.compare_faces(SimilarityThreshold=70,
                              SourceImage={'S3Object':{'Bucket':'rekonpic','Name':'recent_pic.jpg'}},
                              TargetImage={'S3Object':{'Bucket':'rekonpic','Name':'recent_pic.jpg'}})
print(response)
print(response['FaceMatches'])
# for faceMatch in response['FaceMatches']:
#     position = faceMatch['Face']['BoundingBox']
#     confidence = str(faceMatch['Face']['Confidence'])
#     print('The face at ' +
#            str(position['Left']) + ' ' +
#            str(position['Top']) +
#            ' matches with ' + confidence + '% confidence')



# ---------------------------------------




import csv
import boto3

def comparision(sourceFile,targetFile):
    with open('credentials.csv', 'r') as input:
        next(input)
        reader = csv.reader(input)
        for line in reader:
            access_key_id = line[2]
            secret_access_key = line[3]

    client = boto3.client('rekognition', region_name='us-west-1', aws_access_key_id=access_key_id,
                          aws_secret_access_key=secret_access_key)

    response = client.compare_faces(SimilarityThreshold=70,
                                    SourceImage={'S3Object': {'Bucket': 'rekonpic', 'Name': sourceFile}},
                                    TargetImage={'S3Object': {'Bucket': 'rekonpic', 'Name': targetFile}})

    for faceMatch in response['FaceMatches']:
        position = faceMatch['Face']['BoundingBox']
        confidence = str(faceMatch['Face']['Confidence'])
        print('The face at ' +
              str(position['Left']) + ' ' +
              str(position['Top']) +
              ' matches with ' + confidence + '% confidence')

if __name__ == "__main__":
    sourceFile = 'recent_pic.jpg'
    targetFile = 'recent_pic.jpg'
    compared = comparision(sourceFile,targetFile)


#     with open('credentials.csv', 'r') as input:
#         next(input)
#         reader = csv.reader(input)
#         for line in reader:
#             access_key_id = line[2]
#             secret_access_key = line[3]
#
#     client = boto3.client('rekognition', region_name='us-west-1', aws_access_key_id=access_key_id,
#                           aws_secret_access_key=secret_access_key)

# response=client.compare_faces(SimilarityThreshold=70,
#                               SourceImage={'S3Object':{'Bucket':'rekonpic','Name':'recent_pic.jpg'}},
#                               TargetImage={'S3Object':{'Bucket':'rekonpic','Name':'recent_pic.jpg'}})
# # print(response)
# # print(response['FaceMatches'])
# for faceMatch in response['FaceMatches']:
#     position = faceMatch['Face']['BoundingBox']
#     confidence = str(faceMatch['Face']['Confidence'])
#     print('The face at ' +
#            str(position['Left']) + ' ' +
#            str(position['Top']) +
#            ' matches with ' + confidence + '% confidence')




# -------------------------------------------------------------------------------

import csv
import boto3

with open('credentials.csv', 'r') as input:
    next(input)
    reader = csv.reader(input)
    for line in reader:
        access_key_id = line[2]
        secret_access_key = line[3]

client = boto3.client('rekognition',region_name = 'us-west-1', aws_access_key_id = access_key_id, aws_secret_access_key=secret_access_key)

# if __name__ == "__main__":
#
#     bucket='MyBucketName'
sourceFile='recent_pic.jpg'
targetFile='rose.jpg'


response=client.compare_faces(SimilarityThreshold=70,
                              SourceImage={'S3Object':{'Bucket':'testingrekon','Name':'recent_pic.jpg'}},
                              TargetImage={'S3Object':{'Bucket':'testingrekon','Name':'recent_pic.jpg'}})
print(response)
print(response['FaceMatches'])