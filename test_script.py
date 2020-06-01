from getcover import get_cover, save_cover
import pandas as pd
import json


# client = boto3.client('rekognition')
# response = client.detect_labels(
#     Image={
#         'S3Object': {
#             'Bucket': 'judge-a-book',
#             'Name': '1934876569.png'
#         }
#     }
# )

#Save response to s3
# # print(type(response))
# res_bytes = json.dumps(response).encode('utf-8')
# # print(type(res_bytes))
# s3.Bucket('judge-a-book').put_object(Key='responses/1934876569.json', Body=res_bytes)

if __name__ == '__main__':
    f = open('isbn.json')
    isbns = json.load(f)
    for isbn in isbns:
        print(isbn)
        save_cover(get_cover(isbn), isbn, mode='s3')
