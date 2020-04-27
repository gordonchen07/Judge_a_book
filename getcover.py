def get_cover(isbn):
    if not os.path.exists(path):
        os.makedirs(path)
    url = BASE_GBOOKS_API_URL + str(isbn) + '&key={}'.format(APIKEY)
    response = urlopen(url)
    book_json = json.load(response)
    try:
        image_url = book_json['items'][0]['volumeInfo']['imageLinks']['thumbnail']
        image_req = urlopen(image_url)
        image_file = open(os.path.join(path, str(isbn_number) + '.png'), 'wb')
        image_file.write(image_req.read())
        image_file.close()
    except:
        print(str(isbn) + ' No image')
        
