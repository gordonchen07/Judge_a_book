import cv2
import boto3
from boto3 import client
import pandas as pd
from io import StringIO
import tempfile


def gethist(image):
    """Defining a function to get color histogram of an image"""
    object = s3.Bucket(bucket).Object(image)
    with open('image.png', 'wb') as f:
        object.download_fileobj(f)
    img = cv2.imread('image.png')

    blue_hist = cv2.calcHist([img], [0], None, [32], [0, 256])
    green_hist = cv2.calcHist([img], [1], None, [32], [0, 256])
    red_hist = cv2.calcHist([img], [2], None, [32], [0, 256])
    df_blue = pd.DataFrame(data=blue_hist, columns=['blue'])
    df_green = pd.DataFrame(data=green_hist, columns=['green'])
    df_red = pd.DataFrame(data=red_hist, columns=['red'])
    result = pd.concat([df_blue, df_green, df_red], axis=1, sort=False)
    df_out = result.stack()
    df_out.index = df_out.index.map('{0[1]}_{0[0]}'.format)
    trans_df = df_out.to_frame().T
    trans_df.insert(0, 'isbn', image[:-4])

    # csv_buffer = StringIO()
    # trans_df.to_csv(csv_buffer)
    # df_bytes = csv_buffer.getvalue()
    # Key = 'histograms/' + image[12:-4] + '.csv'
    # s3.Bucket('judge-a-book').put_object(Key=Key, Body=df_bytes)


if __name__ == '__main__':
    bucket = 'judge-a-book'
    folder = 'BookCovers/'
    conn = client('s3')
    s3 = boto3.resource('s3')
    files_in_bucket = list(s3.Bucket('judge-a-book').objects.all())
    coversisbn = [file.key[11:-4] for file in files_in_bucket
                  if file.key.startswith('BookCovers')]
    histogramsisbn = [file.key[10:-5] for file in files_in_bucket
                      if file.key.startswith('histograms')]
    leftover = list(set(coversisbn) - set(histogramsisbn))
    leftoverpngs = ['BookCovers/'+str(isbn)+'.png' for isbn in leftover]

    for image in leftoverpngs[:10]:
        print(image)
        gethist(image)
