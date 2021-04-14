from youtube_transcript_api import YouTubeTranscriptApi
import pickle


def make_string_from_video(videoid): #this function gets only English transcripts from the video ids we extracted - as it takes quite a long time, I decided to put in prints just so we know its working
    print("Processing video id: " + str(videoid))
    out_string = ""
    try:
        string_data = YouTubeTranscriptApi.get_transcript(videoid, languages=["en"])
        print("Success!")
        for section in string_data:
            out_string += (section["text"])
            out_string += " "
        return {"id":videoid, "comments":out_string}
    except Exception as err:
        print("Non Fatal Error: " + type(err).__name__+ ". Proceeding...")    # Ignore videos with transcripts disabled
        return {"id":videoid, "comments":0}
def get_string_files():
    i = 0  # Filename counter
    for j in range(4):
        filename = "videoids"+str(i)+".lst"
        print("-------- Processing file: " + filename+" --------")
        fhandle = open(filename, "rb")
        topic_group = pickle.load(fhandle)
        fhandle.close()
        for topic in topic_group:
            print("------------ Processing sublist: " + str(i) + " -------------")
            save_list = []  #New list per video topic
            for vidID in topic:
                return_dictionary = make_string_from_video(vidID) #Make a string or error code
                if return_dictionary["comments"] != 0:
                    save_list.append(return_dictionary) #If not error code, add it to list
            handle = open("transcripts"+str(i)+".lst", "wb") # again saving everything into new pickle files
            pickle.dump(save_list, handle)
            handle.close()
            i += 1

get_string_files()