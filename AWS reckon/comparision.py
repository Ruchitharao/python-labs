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
                                    SourceImage={'S3Object': {'Bucket': 'testingrekon', 'Name': sourceFile}},
                                    TargetImage={'S3Object': {'Bucket': 'testingrekon', 'Name': targetFile}})

    for faceMatch in response['FaceMatches']:
        position = faceMatch['Face']['BoundingBox']
        confidence = str(faceMatch['Face']['Confidence'])
        print('The face at ' +
              str(position['Left']) + ' ' +
              str(position['Top']) +
              ' matches with ' + confidence + '% confidence')

if __name__ == "__main__":
    sourceFile = 'Mamata_gc.png'
    targetFile = 'Mamata.png'
    compared = comparision(sourceFile,targetFile)
