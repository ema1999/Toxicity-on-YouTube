import pickle
import json
from langdetect import detect  # If english, keep else throw away
import time

f2 = pickle.load(open("topic1comments.lst", "rb"))
f = pickle.load(open("transcripts1.lst", "rb"))


def parse_comments(comment_data, video_ID): # as the format we got comments in is quite complicated, a lot of if statements and for loops are required
    data = comment_data
    comments_list = []
    for video in range(len(data)):
        if data[video]["kind"] == "youtube#commentThreadListResponse":
            for comment_thread in range(len(data[video]["items"])):
                if data[video]["items"][comment_thread]["kind"] == "youtube#commentThread":
                    if "replies" in data[video]["items"][comment_thread]:
                        for comment in range(len(data[video]["items"][comment_thread]["replies"]["comments"])):
                            if data[video]["items"][comment_thread]["replies"]["comments"][comment][
                                "kind"] == "youtube#comment" \
                                    and data[video]["items"][comment_thread]["replies"]["comments"][comment]["snippet"][
                                "videoId"] == video_ID:
                                langstatus = False
                                try:
                                    langstatus = detect(
                                        data[video]["items"][comment_thread]["replies"]["comments"][comment]["snippet"][
                                            "textOriginal"]) == "en"
                                except:
                                    pass
                                if langstatus:
                                    comments_list.append(
                                        data[video]["items"][comment_thread]["replies"]["comments"][comment]["snippet"][
                                            "textOriginal"])
                            else:
                                pass
                    else:
                        pass
                else:
                    pass
                print("\rProcessing comments |", end="", flush=False)
                print("\rProcessing comments \\", end="", flush=False)
                print("\rProcessing comments -", end="", flush=False)
                print("\rProcessing comments /", end="", flush=False)
        else:
            pass
    return comments_list


# Video Information Packet or VIP has the following structure.
# typedef struct vif { "vidID":id_string, "Transcript": transcript_string, "Comments": list_of_comments[] }
# Each category will be stored in its own VIF file (Video Information Format), a list of VIPs.
def create_vif_list(comment_file_index):
    fcomments = open("topic" + str(comment_file_index) + "comments.lst", "rb")
    ftrans = open("transcripts" + str(comment_file_index) + ".lst", "rb")
    comment_data = pickle.load(fcomments)
    trans_data = pickle.load(ftrans)  # Transcripts are called comments in these files, silly me
    ftrans.close()
    fcomments.close()
    ret_list = []
    for i in range(len(trans_data)):
        comments_list = parse_comments(comment_data, trans_data[i]["id"])
        vif = {"vidID": trans_data[i]["id"], "Transcript": trans_data[i]["comments"], "Comments": comments_list}
        ret_list.append(vif)
    return ret_list


def create_vif_files():
    stamp = time.time()
    for i in range(16):
        inner_stamp = time.time()
        i += 1  # Files start at one so our counter does too
        print("Processing files of index: " + str(i))
        vif_list = create_vif_list(i)
        filename = "category" + str(i) + ".vif"
        print("Creating file: " + filename)
        fhandle = open(filename, "wb")
        pickle.dump(vif_list, fhandle)
        fhandle.close()
        print("Dataset " + str(i) + " processed and saved in: " + str(time.time() - inner_stamp) + " seconds.")
    print("Total running time: "  + str(time.time() - stamp) + " seconds.")

create_vif_files()
