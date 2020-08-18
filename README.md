# Judge a Book - An Analysis of Book Covers
SharpestMinds project analyzing children book's bookcovers data. 

Includes series of scripts to:
1) Extract book identification numbers from [UCSD Book Graph - Goodreads Children](https://sites.google.com/eng.ucsd.edu/ucsdbookgraph/home).
2) Collect book cover images from Google Books API.
3) Save images to Amazon Web Services S3 storage.
4) Format Amazon Web Services Boto3 Rekognition image labeling data into .json files.

Also, includes:
* Color composition extraction using OpenCV in the form of color histograms and formatting into dataframes in .pkl files. 
* Analysis of image label data and color histograms, with distributions and statistical significance testing of features in relation to book ratings.