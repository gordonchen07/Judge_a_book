import json
import boto3
from boto3 import client
from tqdm import tqdm

s3 = boto3.resource('s3')


def analyze_image(photo, bucket, folder):
    """Analyze book cover image with Boto3 Rekognition"""
    client = boto3.client('rekognition')
    response = client.detect_labels(
        Image={'S3Object': {'Bucket': bucket, 'Name': (folder+photo)}},
        MaxLabels=10)

    # Save response to responses folder in S3
    res_bytes = json.dumps(response).encode('utf-8')
    Key = 'responses/' + photo[:-4] + '.json'
    s3.Bucket('judge-a-book').put_object(Key=Key, Body=res_bytes)


if __name__ == '__main__':
    bucket = 'judge-a-book'
    folder = 'BookCovers/'
    conn = client('s3')
    files_in_bucket = list(s3.Bucket('judge-a-book').objects.all())
    coversisbn = [file.key[11:-4] for file in files_in_bucket
                  if file.key.startswith('BookCovers')]
    responsesisbn = [file.key[10:-5] for file in files_in_bucket
                     if file.key.startswith('responses')]
    leftover = list(set(coversisbn) - set(responsesisbn))
    leftoverpngs = [str(isbn)+'.png' for isbn in leftover]

    for photo in tqdm(leftoverpngs):
        analyze_image(photo, bucket, folder)
