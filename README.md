# Toxicity-on-YouTube
This project contains the code for my dissertation which aims to look at the current state of toxicity on YouTube. Here is a brief description of what each file included does:
- GetVideoIDs was run first to extract 50 video ids from 20 channel ids per category (16 categories)
- GetTranscripts takes the video ids and gets English transcripts for those videos that do not have disabled captions
- GetComments takes video ids and gets comments from those videos (but max 50 due to the Google API limit)
- DataCombiner combines the data that was scraped into files that have a video id, its English transcript and all available comments in English
- Sentanalysis deploys VADER sentiment analysis and stores sentiment scores into pickle files
- Hatebase assesses whether there are any hateful words from the Hatebase dictionary and combines the results with the sentiment scores
- Ginicoefs includes the function used for calculating the Gini coefficients, the code used for correlation analyis and Lorentz curve 
- Regressionattempt has the code used for regression analysis
