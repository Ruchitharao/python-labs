import csv
import boto3

def defect_labels(photo):
    with open('credentials.csv', 'r') as input:
        next(input)
        reader = csv.reader(input)
        for line in reader:
            access_key_id = line[2]
            secret_access_key = line[3]

    client = boto3.client('rekognition',region_name = 'us-west-1', aws_access_key_id = access_key_id, aws_secret_access_key=secret_access_key)

    #collect from local storage
    # with open(photo, 'rb') as source_image:
    #     source_bytes = source_image.read()

    # response = client.detect_labels(Image = {'Bytes': source_bytes}, MaxLabels=2,MinConfidence = 95)

    #collect from s3 storage
    response = client.detect_labels(Image = {'S3Object': {
    'Bucket': 'testingrekon',
    'Name': photo,
    }
    }, MaxLabels=2,MinConfidence = 95)

    print(response)


if __name__ == "__main__":
    photo = 'rose.jpg'
    labels = defect_labels(photo)