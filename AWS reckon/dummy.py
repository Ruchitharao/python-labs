# with open(sourceFile, 'rb') as source_image:
#     source_bytes = source_image.read()
#
# with open(targetFile,'rb') as target_image:
#     target_bytes = target_image.read()


# source_bytes = open('recent_pic.jpg', 'rb')
# target_bytes = open('rose.jpg', 'rb')
#
# response = client.compare_faces(
#     SourceImage = {
#         'Bytes':source_bytes.read()
#     },
#     TargetImage = {
#         'Bytes':target_bytes.read()
#     },
#     SimilarityThreshold = 70
# )
# print(response)
# source_image.close()
# target_image.close()







# ------------------------------------------------------------------------------------------/


import boto3
import csv




if __name__ == "__main__":

    bucket='MyBucketName'
    sourceFile='Mamata_gc.png'
    targetFile='Mamata.png'


    with open('credentials.csv', 'r') as input:
        next(input)
        reader = csv.reader(input)
        for line in reader:
            access_key_id = line[2]
            secret_access_key = line[3]

    client = boto3.client('rekognition', region_name='us-west-1', aws_access_key_id=access_key_id,
                          aws_secret_access_key=secret_access_key)


    response=client.compare_faces(SimilarityThreshold=70,
                              SourceImage={'S3Object':{'Bucket':'testingrekon','Name':sourceFile}},
                              TargetImage={'S3Object':{'Bucket':'testingrekon','Name':targetFile}})
    print(response)
    for faceMatch in response['FaceMatches']:
        position = faceMatch['Face']['BoundingBox']
        confidence = str(faceMatch['Face']['Confidence'])
        print('The face at ' +
               str(position['Left']) + ' ' +
               str(position['Top']) +
               ' matches with ' + confidence + '% confidence')