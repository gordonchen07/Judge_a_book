# Judge a Book - An Analysis of Book Covers
SharpestMinds project analyzing children book's bookcovers data. Includes series of scripts to extract book identification numbers from [UCSD Book Graph - Goodreads Children](https://sites.google.com/eng.ucsd.edu/ucsdbookgraph/home), collect book cover images from Google Books API, save images to Amazon Web Services S3 storage, and format Amazon Web Services Boto3 Rekognition image labeling data into .json files. Also, includes color composition extraction using OpenCV in the form of color histograms and formatting into dataframes in .pkl files. Additionally, includes analysis of image label data and color histograms, with distributions and statistical significance testing of features in relation to book ratings.