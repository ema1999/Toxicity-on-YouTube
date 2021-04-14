# -*- coding: utf-8 -*-

# Sample Python code for youtube.commentThreads.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os
import pickle

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors


######### Equates, do not change unless you know what you are doing!!##########
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
client_secrets_file = # insert your own secret file / api key
scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
api_service_name = "youtube"
api_version = "v3"
###############################################################################

    # Get credentials and create an API client
flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
credentials = flow.run_console()

youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)


def get_comments_for_topic(video_ids):  # Pass ids for a SINGLE TOPIC
    return_list = []
    for video_id in video_ids:
        request = youtube.commentThreads().list(
            part="snippet,replies",
            order="relevance",
            textFormat="plainText",
            videoId=video_id
        )
        try:    # Catches if we couldnt retrieve data for a specific video
            response = request.execute()
        except googleapiclient.errors.HttpError:
            response = {"kind":"Failed to get comments for video id: " + video_id}
        return_list.append(response)
        print(response)
    return return_list


#infile0 = open("videoids.lst",'rb')
#ids0 = pickle.load(infile0)
#infile0.close()

infile11 = open("videoids0.lst",'rb')
ids11 = pickle.load(infile11)
infile11.close()

infile2 = open("videoids5.lst",'rb')
ids2 = pickle.load(infile2)
infile2.close()

infile3 = open("videoids10.lst",'rb')
ids3 = pickle.load(infile3)
infile3.close()

infile4 = open("videoids15.lst",'rb')
ids4 = pickle.load(infile4)
infile4.close()

i = 0  # File name counter
#for topic_video_ids in ids11:
#    filename = "topic"+str(i)+"comments.lst"
#    comments = get_comments_for_topic(topic_video_ids)  # Gives comments per video topic from original list
 #   fhandle = open(filename, "wb")
 #   pickle.dump(comments, fhandle)
 #   fhandle.close()
 #   i += 1
