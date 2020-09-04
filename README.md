# Judge a Book - An Analysis of Book Covers
SharpestMinds project analyzing children book bookcovers data. The motivation for this project is to identify what visual features influence consumers to consider picking up a book when they enter a bookstore. In this project, I tried to identify labels(features) on children book bookcovers that may yield high popularity. I found that bookcovers with labels associated with astronomy, pets, animals, and covers with a high red color value are statistically significant to the rating of the book. Below details the Jupyter Notebooks and Python Scripts I used for this project.

Jupyter Notebooks:
1) [1_Data_Wrangling.ipynb](https://github.com/gordonchen07/Judge_a_book/blob/scale_image_collector/1_Data_Wrangling.ipynb) - Details the steps I used to collect all the data for this project and how I compiled them into a final DataFrame for analysis.
2) [2_Data_Exploration.ipynb](https://github.com/gordonchen07/Judge_a_book/blob/scale_image_collector/2_Data_Exploration.ipynb) - Contains the Data Exploration and Data Analysis of the bookcover image label data collected and color histograms from [1_Data_Wrangling](https://github.com/gordonchen07/Judge_a_book/blob/scale_image_collector/1_Data_Wrangling.ipynb) with distributions and statistical significance testing.

Python Scripts:
1) [1_get_isbn.py](https://github.com/gordonchen07/Judge_a_book/blob/scale_image_collector/Scripts/1_get_isbn.py) - Extract book identification numbers from [UCSD Book Graph - Goodreads Children](https://sites.google.com/eng.ucsd.edu/ucsdbookgraph/home).
2) [2_getcover.py](https://github.com/gordonchen07/Judge_a_book/blob/scale_image_collector/Scripts/2_get_bookcover.py) - Collect book cover images from [Google Books API](https://developers.google.com/books).
3) [3_analyzeimage.py](https://github.com/gordonchen07/Judge_a_book/blob/scale_image_collector/Scripts/3_analyzeimage.py) - Save images to [Amazon Web Services S3 storage](https://aws.amazon.com/s3/).
4) Format [Amazon Web Services Boto3 Rekognition](https://aws.amazon.com/rekognition/) image labeling data into .json files.

Next Steps:
Explore [goodreads_interactions_children.json](https://sites.google.com/eng.ucsd.edu/ucsdbookgraph/home) dataset to determine if certain features yields greater initial engagement as consumers enter a bookstore.