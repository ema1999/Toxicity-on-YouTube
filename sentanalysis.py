import pandas as pd
import pickle
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


analyser = SentimentIntensityAnalyzer()

def sentiment_analyzer_scores(sentence): # function that returns us a sentiment score based on VADER
    score = analyser.polarity_scores(sentence)
    return score



def read_pickle_file(file):
    pickle_data = pd.read_pickle(file)
    return pickle_data


cat1 = read_pickle_file("category1.vif")
cat2 = read_pickle_file("category2.vif")
cat3 = read_pickle_file("category3.vif")
cat4 = read_pickle_file("category4.vif")
cat5 = read_pickle_file("category5.vif")
cat6 = read_pickle_file("category6.vif")
cat7 = read_pickle_file("category7.vif")
cat8 = read_pickle_file("category8.vif")
cat9 = read_pickle_file("category9.vif")
cat10 = read_pickle_file("category10.vif")
cat11 = read_pickle_file("category11.vif")
cat12 = read_pickle_file("category12.vif")
cat13 = read_pickle_file("category13.vif")
cat14 = read_pickle_file("category14.vif")
cat15 = read_pickle_file("category15.vif")
cat16 = read_pickle_file("category16.vif")

sent4=[]

for i in cat4: # for loops that analyse Transcripts and comments from each category and return us scores
    sentscore_list = []
    sentscore_list.append(sentiment_analyzer_scores(i["Transcript"]))
    for j in i["Comments"]:
        sentscore_list.append(sentiment_analyzer_scores(j))
    sent4.append(sentscore_list)



sent1=[]
for i in cat1:
    sentscore_list = []
    sentscore_list.append(sentiment_analyzer_scores(i["Transcript"]))
    for j in i["Comments"]:
        sentscore_list.append(sentiment_analyzer_scores(j))
    sent1.append(sentscore_list)

sent2=[]
for i in cat2:
    sentscore_list = []
    sentscore_list.append(sentiment_analyzer_scores(i["Transcript"]))
    for j in i["Comments"]:
        sentscore_list.append(sentiment_analyzer_scores(j))
    sent2.append(sentscore_list)

sent3=[]
for i in cat3:
    sentscore_list = []
    sentscore_list.append(sentiment_analyzer_scores(i["Transcript"]))
    for j in i["Comments"]:
        sentscore_list.append(sentiment_analyzer_scores(j))
    sent3.append(sentscore_list)



sent5=[]
for i in cat5:
    sentscore_list = []
    sentscore_list.append(sentiment_analyzer_scores(i["Transcript"]))
    for j in i["Comments"]:
        sentscore_list.append(sentiment_analyzer_scores(j))
    sent5.append(sentscore_list)

sent6=[]
for i in cat6:
    sentscore_list = []
    sentscore_list.append(sentiment_analyzer_scores(i["Transcript"]))
    for j in i["Comments"]:
        sentscore_list.append(sentiment_analyzer_scores(j))
    sent6.append(sentscore_list)

sent7=[]
for i in cat7:
    sentscore_list = []
    sentscore_list.append(sentiment_analyzer_scores(i["Transcript"]))
    for j in i["Comments"]:
        sentscore_list.append(sentiment_analyzer_scores(j))
    sent7.append(sentscore_list)

sent8=[]
for i in cat8:
    sentscore_list = []
    sentscore_list.append(sentiment_analyzer_scores(i["Transcript"]))
    for j in i["Comments"]:
        sentscore_list.append(sentiment_analyzer_scores(j))
    sent8.append(sentscore_list)

sent9=[]
for i in cat9:
    sentscore_list = []
    sentscore_list.append(sentiment_analyzer_scores(i["Transcript"]))
    for j in i["Comments"]:
        sentscore_list.append(sentiment_analyzer_scores(j))
    sent9.append(sentscore_list)

sent10=[]
for i in cat10:
    sentscore_list = []
    sentscore_list.append(sentiment_analyzer_scores(i["Transcript"]))
    for j in i["Comments"]:
        sentscore_list.append(sentiment_analyzer_scores(j))
    sent10.append(sentscore_list)

sent11=[]
for i in cat11:
    sentscore_list = []
    sentscore_list.append(sentiment_analyzer_scores(i["Transcript"]))
    for j in i["Comments"]:
        sentscore_list.append(sentiment_analyzer_scores(j))
    sent11.append(sentscore_list)

sent12=[]
for i in cat12:
    sentscore_list = []
    sentscore_list.append(sentiment_analyzer_scores(i["Transcript"]))
    for j in i["Comments"]:
        sentscore_list.append(sentiment_analyzer_scores(j))
    sent12.append(sentscore_list)

sent13=[]
for i in cat13:
    sentscore_list = []
    sentscore_list.append(sentiment_analyzer_scores(i["Transcript"]))
    for j in i["Comments"]:
        sentscore_list.append(sentiment_analyzer_scores(j))
    sent13.append(sentscore_list)

sent14=[]
for i in cat14:
    sentscore_list = []
    sentscore_list.append(sentiment_analyzer_scores(i["Transcript"]))
    for j in i["Comments"]:
        sentscore_list.append(sentiment_analyzer_scores(j))
    sent14.append(sentscore_list)

sent15=[]
for i in cat15:
    sentscore_list = []
    sentscore_list.append(sentiment_analyzer_scores(i["Transcript"]))
    for j in i["Comments"]:
        sentscore_list.append(sentiment_analyzer_scores(j))
    sent15.append(sentscore_list)

sent16=[]
for i in cat16:
    sentscore_list = []
    sentscore_list.append(sentiment_analyzer_scores(i["Transcript"]))
    for j in i["Comments"]:
        sentscore_list.append(sentiment_analyzer_scores(j))
    sent16.append(sentscore_list)



#----------------------Getting only meaningful numbers out-------

sentscore1=[]
for i in sent1:
    intermidiatelist=[]
    for j in i:
        intermidiatelist.append(j["compound"])
    sentscore1.append(intermidiatelist)

sentscore2=[]
for i in sent2:
    intermidiatelist=[]
    for j in i:
        intermidiatelist.append(j["compound"])
    sentscore2.append(intermidiatelist)

sentscore3=[]
for i in sent3:
    intermidiatelist=[]
    for j in i:
        intermidiatelist.append(j["compound"])
    sentscore3.append(intermidiatelist)


sentscore5=[]
for i in sent5:
    intermidiatelist=[]
    for j in i:
        intermidiatelist.append(j["compound"])
    sentscore5.append(intermidiatelist)

sentscore6=[]
for i in sent6:
    intermidiatelist=[]
    for j in i:
        intermidiatelist.append(j["compound"])
    sentscore6.append(intermidiatelist)


sentscore7=[]
for i in sent7:
    intermidiatelist=[]
    for j in i:
        intermidiatelist.append(j["compound"])
    sentscore7.append(intermidiatelist)

sentscore8=[]
for i in sent8:
    intermidiatelist=[]
    for j in i:
        intermidiatelist.append(j["compound"])
    sentscore8.append(intermidiatelist)

sentscore9=[]
for i in sent9:
    intermidiatelist=[]
    for j in i:
        intermidiatelist.append(j["compound"])
    sentscore9.append(intermidiatelist)

sentscore10=[]
for i in sent10:
    intermidiatelist=[]
    for j in i:
        intermidiatelist.append(j["compound"])
    sentscore10.append(intermidiatelist)

sentscore11=[]
for i in sent11:
    intermidiatelist=[]
    for j in i:
        intermidiatelist.append(j["compound"])
    sentscore11.append(intermidiatelist)

sentscore12=[]
for i in sent12:
    intermidiatelist=[]
    for j in i:
        intermidiatelist.append(j["compound"])
    sentscore12.append(intermidiatelist)

sentscore13=[]
for i in sent13:
    intermidiatelist=[]
    for j in i:
        intermidiatelist.append(j["compound"])
    sentscore13.append(intermidiatelist)

sentscore14=[]
for i in sent14:
    intermidiatelist=[]
    for j in i:
        intermidiatelist.append(j["compound"])
    sentscore14.append(intermidiatelist)

sentscore15=[]
for i in sent15:
    intermidiatelist=[]
    for j in i:
        intermidiatelist.append(j["compound"])
    sentscore15.append(intermidiatelist)

sentscore16=[]
for i in sent16:
    intermidiatelist=[]
    for j in i:
        intermidiatelist.append(j["compound"])
    sentscore16.append(intermidiatelist)

sentscore4=[]
for i in sent4:
    intermidiatelist=[]
    for j in i:
        intermidiatelist.append(j["compound"])
    sentscore4.append(intermidiatelist)



#--------------------Pickleing----------------------------------


pickle.dump(sentscore1, open( "sentscore1.pkl", "wb" ))
pickle.dump(sentscore2, open( "sentscore2.pkl", "wb" ))
pickle.dump(sentscore3, open( "sentscore3.pkl", "wb" ))
pickle.dump(sentscore4, open( "sentscore4.pkl", "wb" ))
pickle.dump(sentscore5, open( "sentscore5.pkl", "wb" ))
pickle.dump(sentscore6, open( "sentscore6.pkl", "wb" ))
pickle.dump(sentscore7, open( "sentscore7.pkl", "wb" ))
pickle.dump(sentscore8, open( "sentscore8.pkl", "wb" ))
pickle.dump(sentscore9, open( "sentscore9.pkl", "wb" ))
pickle.dump(sentscore10, open( "sentscore10.pkl", "wb" ))
pickle.dump(sentscore11, open( "sentscore11.pkl", "wb" ))
pickle.dump(sentscore12, open( "sentscore12.pkl", "wb" ))
pickle.dump(sentscore13, open( "sentscore13.pkl", "wb" ))
pickle.dump(sentscore14, open( "sentscore14.pkl", "wb" ))
pickle.dump(sentscore15, open( "sentscore15.pkl", "wb" ))
pickle.dump(sentscore16, open( "sentscore16.pkl", "wb" ))

