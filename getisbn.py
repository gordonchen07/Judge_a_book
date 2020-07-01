import pandas as pd
import json


def get_isbn(json_file):
    """Create list of isbn numbers and save to json"""
    df = pd.read_json(json_file, lines=True)
    isbns = df[df.isbn != ''].isbn.values.tolist()
    with open('isbn.json', 'w') as outfile:
        json.dump(isbns, outfile)


if __name__ == '__main__':
    get_isbn('goodreads_books_children.json')
