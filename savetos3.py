"""Script to download and books for isbns"""
from getcover import get_cover, save_cover
import json
from tqdm import tqdm


if __name__ == '__main__':
    f = open('isbn.json')
    isbns = json.load(f)
    for isbn in tqdm(isbns[:10000]):
        save_cover(get_cover(isbn), isbn, mode='s3')
