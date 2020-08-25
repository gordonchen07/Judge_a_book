import pandas as pd
import json


def get_isbn(json_file):
    """Create list of isbn numbers and save to json"""

    # Read dataset into a DataFrame
    df = pd.read_json(json_file, lines=True)

    # Extract ISBN numbers from DataFrame and compile into list.
    isbns = df[df.isbn != ''].isbn.values.tolist()

    # Write ISBN numbers list into a .json file.
    with open('isbn.json', 'w') as outfile:
        json.dump(isbns, outfile)


if __name__ == '__main__':
    get_isbn('goodreads_books_children.json')
