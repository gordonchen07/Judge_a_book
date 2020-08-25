import boto3
from boto3 import client
import cv2
import pandas as pd


def color_histogram(images, file_name):
    """Extract color histograms from book cover image using OpenCV.
    Compile histograms into Pandas DataFrame
    Save DataFrame to csv file."""

    # Create empty DataFrame.
    final_df = pd.DataFrame()

    # Iterate all bookcover images to be analyzed by OpenCV.
    for image in images[:]:
        # Access image file in S3 Bucket.
        object = s3.Bucket(bucket).Object(image)
        with open('image.png', 'wb') as f:
            object.download_fileobj(f)

        # Read in image to OpenCV.
        img = cv2.imread('image.png')

        # Extract color histograms using OpenCV.
        blue_hist = cv2.calcHist([img], [0], None, [32], [0, 256])
        green_hist = cv2.calcHist([img], [1], None, [32], [0, 256])
        red_hist = cv2.calcHist([img], [2], None, [32], [0, 256])

        # Compile color histogram values into a DataFrame.
        df_hists = pd.DataFrame({'blue': blue_hist[:, 0],
                                 'green': green_hist[:, 0],
                                 'red': red_hist[:, 0]}).stack()

        # Transpose DataFrameto a single row.
        df_hists.index = df_hists.index.map('{0[1]}_{0[0]}'.format)
        temp_df = df_hists.to_frame().T
        temp_df.insert(0, 'isbn', image[11:-4])

        # Save row to final_df
        final_df = final_df.append(temp_df, ignore_index=True)

    # Save DataFrame to .csv file.
    final_df.to_csv(str(file_name))


def color_average(images, file_name):
    """Aggregate average color value for each book cover image using OpenCV.
    Compile average color values into Pandas DataFrame.
    Save DataFrame to csv file."""

    # Create empty DataFrame.
    average_rbg = pd.DataFrame()

    # Iterate all bookcover images to be analyzed by OpenCV.
    for image in images[:]:
        # Access image file in S3 Bucket.
        object = s3.Bucket(bucket).Object(image)
        with open('image.png', 'wb') as f:
            object.download_fileobj(f)

        # Read in image to OpenCV.
        img = cv2.imread('image.png')

        # Aggregate the mean value of red, blue, and green.
        red = [img[:, :, 2].mean()]
        blue = [img[:, :, 0].mean()]
        green = [img[:, :, 1].mean()]

        # Compile mean color values into a DataFrame.
        df_hists = pd.DataFrame({'blue': blue[:],
                                 'green': green[:],
                                 'red': red[:]}).stack()

        # Transpose DataFrame to a single row.
        df_hists.index = df_hists.index.map('{0[1]}'.format)
        temp_df = df_hists.to_frame().T
        temp_df.insert(0, 'isbn', image[11:-4])

        # Save row to final_df
        average_rbg = average_rbg.append(temp_df, ignore_index=True)

    # Save DataFrame to .csv file.
    average_rbg.to_csv(str(file_name))


if __name__ == '__main__':
    """Access the book covers stored in the AWS S3 bucket"""
    bucket = 'judge-a-book'
    folder = 'BookCovers/'
    conn = client('s3')
    s3 = boto3.resource('s3')

    # Access image files in the S3 Bucket.
    files_in_bucket = list(s3.Bucket('judge-a-book').objects.all())

    # Identify and list bookcover images that have not been analyzed by Boto3
    # Rekognition to avoid duplicates.
    coversisbn = [file.key[11:-4] for file in files_in_bucket
                  if file.key.startswith('BookCovers')]
    histogramsisbn = [file.key[10:-5] for file in files_in_bucket
                      if file.key.startswith('histograms')]
    leftover = list(set(coversisbn) - set(histogramsisbn))
    leftoverpngs = ['BookCovers/'+str(isbn)+'.png' for isbn in leftover]

    # Create csv of color histograms of the book cover images.
    color_histogram(leftoverpngs, 'histograms.csv')

    # Create csv of color averages of the book cover images.
    color_average(leftoverpngs, 'average_rbg.csv')
