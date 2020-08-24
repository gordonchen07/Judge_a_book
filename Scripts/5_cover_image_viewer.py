from boto3 import client
from matplotlib import pyplot as plt, image as mpimg
from io import BytesIO

bucket = 'judge-a-book'
folder = 'BookCovers/'
conn = client('s3')


def get_image(isbn):
    image_file = folder+str(isbn)+'.png'
    response = conn.get_object(Key=image_file, Bucket=bucket)
    image = mpimg.imread(BytesIO(response['Body'].read()), 'jp2')
    return plt.imshow(image)
