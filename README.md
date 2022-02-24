# Japanese Sentiment Analysis
This repository contains the script for the Japanese sentiment analysis project.


## Method
We follow Universal Language Model Fine-tuning (ULMFiT), an effective transfer learning method.
Language and classifier models are fine-tuned and trained on the Amazon data, respectively.
Transfer learning is a state-of-art technique which reuses a pre-trained model and fine-tunes it using another data.


## Pretrained Models
Pretrained models (sentencepiece model and language model) for Japanese,
which was trained on Wikipedia data, are obtained from the following repo: 
https://github.com/tsurushun/ulmfit-multilingual/tree/japanese


## Libraries
- torch: 1.10.0+cu111
- fastai: 1.0.61


## Data
This project utilizes the reviews from Amazon music in Japanese language.
Users' reviews have been categorized into either positive or negative reviews based on rating.
For example, reviews with 1 or 2 stars rating are classified as negative reviews while those with
rating of 4 stars and above as positive reviews. 

Raw data (in .review format) has been converted to csv files using `xml_to_csv.py`.

Data consists of Train, Test, and Unlabeled data. For this project, we intend to use 20000 positive and 20000 negative reviews
to finetune the language model and train the classifier model. Therefore, we randomly choose
those reviews from Unlabeled data since Train and Test contains only 2000 reviews each.
Unlabeled data contains information about users' comment and rating, which can be used to 
construct the sample data for this project.


## Result
Based on the result, using Amazon data, we are able to classify 90% of the reviews in Japanese correctly. 
This accuracy rate is significantly high, but we expect that we can achieve higher accuracy rate by injecting more data
into the fine-tuning and training processes.
