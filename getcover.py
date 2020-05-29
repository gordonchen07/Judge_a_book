#Import libraries
import boto3
import os
import json
from urllib.request import urlopen
import pandas as pd

#Defining a function to get the book cover image with in input ISBN
def get_cover(isbn):
    APIKEY = os.getenv("BOOKAPIKEY")
    BASE_GBOOKS_API_URL = "https://www.googleapis.com/books/v1/volumes?q="
    #Navigate to webpage of the Google Books Volume that contains the link to the book cover image

    url = BASE_GBOOKS_API_URL + str(isbn) + '&key={}'.format(APIKEY)

    #Saves all texts from webpage into a json file
    response = urlopen(url)
    book_json = json.load(response)

    #Locate link to book cover image from json file
    try:
        image_url = book_json['items'][0]['volumeInfo']['imageLinks']['thumbnail']
        image_req = urlopen(image_url)
        return image_req
    #Returns a message with ISBN number and No image if a book cover image is not found in the json file
    except KeyError:
        return None


def save_cover(image_req,
               isbn,
               new_directory='BookCovers',
               parent_directory=None,
               mode='local'):
    if parent_directory is None:
        parent_directory = os.getcwd()
    path = os.path.join(parent_directory, new_directory)
    if not os.path.exists(path):
        os.makedirs(path)
    s3 = boto3.resource('s3')

    if image_req is None:
        print('No image found')
    elif mode == 'local':
        image_file = open(os.path.join(path, str(isbn) + '.png'), 'wb')
        image_file.write(image_req.read())
        image_file.close()
    elif mode == 's3':
        data = image_req.read()
        s3.Bucket('judge-a-book').put_object(Key='BookCovers/'+str(isbn)+'.png', Body=data)
    else:
        raise ValueError('Save mode not acceptable.')
