import os
import json
from urllib.request import urlopen

APIKEY = os.getenv("BOOKAPIKEY")
BASE_GBOOKS_API_URL = "https://www.googleapis.com/books/v1/volumes?q="
NEW_DIRECTORY = 'BookCovers'
PARENT_DIRECTORY = os.getcwd()
path = os.path.join(PARENT_DIRECTORY, NEW_DIRECTORY)

def get_cover(isbn):
    if not os.path.exists(path):
        os.makedirs(path)
    url = BASE_GBOOKS_API_URL + str(isbn) + '&key={}'.format(APIKEY)
    response = urlopen(url)
    book_json = json.load(response)
    try:
        image_url = book_json['items'][0]['volumeInfo']['imageLinks']['thumbnail']
        image_req = urlopen(image_url)
        image_file = open(os.path.join(path, str(isbn) + '.png'), 'wb')
        image_file.write(image_req.read())
        image_file.close()
    except KeyError:
        print(str(isbn) + ' No image')

if __name__ == '__main__':
    get_cover(1934876569)
