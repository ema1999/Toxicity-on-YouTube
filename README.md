# Toxicity-on-YouTube
This project contains the code for my dissertation which aims to look at the current state of toxicity on YouTube. 
- GetVideoIDs was run first to extract 50 video ids from 20 channel ids per category (16 categories)
- GetTranscripts takes the video ids and gets English transcripts for those videos that do not have disabled captions
- GetComments takes video ids and gets comments from those videos (but max 50 due to the Google API limit)
- DataCombiner combines the data that was scraped into files that have a video id, its English transcript and all available comments in English
