
import scipy.stats
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def read_pickle_file(file):
    pickle_data = pd.read_pickle(file)
    return pickle_data


sent1 = read_pickle_file("sentscore1.pkl")  # reading all toxicity scores
sent2 = read_pickle_file("sentscore2.pkl")
sent3 = read_pickle_file("sentscore3.pkl")
sent4 = read_pickle_file("sentscore4.pkl")
sent5 = read_pickle_file("sentscore5.pkl")
sent6 = read_pickle_file("sentscore6.pkl")
sent7 = read_pickle_file("sentscore7.pkl")
sent8 = read_pickle_file("sentscore8.pkl")
sent9 = read_pickle_file("sentscore9.pkl")
sent10 = read_pickle_file("sentscore10.pkl")
sent11 = read_pickle_file("sentscore11.pkl")
sent12 = read_pickle_file("sentscore12.pkl")
sent13 = read_pickle_file("sentscore13.pkl")
sent14 = read_pickle_file("sentscore14.pkl")
sent15 = read_pickle_file("sentscore15.pkl")
sent16 = read_pickle_file("sentscore16.pkl")
cat9= read_pickle_file('category9.vif')
transcripts1=[]
comments1=[]
firstcomment=[]



for i in sent9: # splitting transcripts and the comments (we are going to do regression analysis comparing them)
    if len(i) > 1:
        transcripts1.append(i[0])
        comments1.append(i[1:])
    else:
        sent9.remove(i)

improved_trans=[]
for i in transcripts1: # we are interested only in toxic scores
    if i < 0:
        improved_trans.append(i*(-1))
    else:
        improved_trans.append(0)

improved_comments=[]

for i in comments1:
    interlist = []
    for j in i:

        if j < 0:
            interlist.append(j*(-1))
        else:
            interlist.append(0)
    improved_comments.append(interlist)

def gini1(list_of_values): # function for gini coefficient calculation
    sorted_list = sorted(list_of_values)
    height, area = 0, 0
    for value in sorted_list:
        height += value
        area += height - value / 2.
    fair_area = height * len(list_of_values) / 2.
    return (fair_area - area) / fair_area




ginis1=[]
for i in range(len(sent7)): # this is an example how to run this code to analyse category 7
    try:
        ginis1.append(gini1(sent7[i]))
    except:
        pass

ginis1correct =[]

for i in ginis1:
    if 0 < i <= 1:
        ginis1correct.append(i)
    else:
        pass




print(len(ginis1)) # gini coefficient analysis - looking at average, median, minimum, maximum and standard diviation
print(len(ginis1correct))
avg= np.average(ginis1correct)
median = np.median(ginis1correct)
min = np.min(ginis1correct)
max = np.max(ginis1correct)


std = np.std(ginis1correct)
print(avg, std, max, min, median)



avgsent=[] # regression analysis (similar to in the file analysing correlation between Perspective API scores and our toxicity detection tool
for i in improved_comments:
    avgsent.append(np.average(i))


bad_indicies = []
for i in range(len(improved_trans)): # Doesnt matter because len api9 is the same as smallsent99
    if improved_trans[i] == 0:
        bad_indicies.append(i)
    else:
        pass

for index in reversed(bad_indicies):
    avgsent.pop(index)
    improved_trans.pop(index)

print(improved_trans)
print(avgsent)


print(len(avgsent), len(improved_trans))


x = np.array(improved_trans)
y = np.array(avgsent)


print(np.corrcoef(improved_trans, avgsent))

print(scipy.stats.pearsonr(improved_trans, avgsent))

print(scipy.stats.spearmanr(improved_trans, avgsent))



#result = scipy.stats.linregress(transcripts1, firstcomment)

#print("check this", result.slope, result.intercept, result.rvalue, "p", result.pvalue, result.stderr)

#plt.style.use('ggplot')
#slope, intercept, r, p, stderr = scipy.stats.linregress(x, y)
#line = f'Regression line: y={intercept:.2f}+{slope:.2f}x, r={r:.2f}'
#line

#fig, ax = plt.subplots()
#ax.plot(x, y, linewidth=0, marker='s', label='Data points')
#ax.plot(x, intercept + slope * x) #label=line)
#ax.set_xlabel('Toxicity of transcripts')
#ax.set_ylabel('Average toxicity of comments')
#ax.legend(facecolor='white')
#plt.show()




#-------------------Lorentz curve----------------------


lorentz1= [0.8885, 0.6369, 0.7184, 0.6486, 0.8288, 0.9153, -0.7506, 0.8625, 0.5574, 0.0, 0.4754, 0.0, 0.4019, 0.4404, 0.0, 0.4404, -0.5, 0.296, 0.0, 0.0, 0.0, 0.5003, 0.25, 0.0, -0.7156, 0.0, 0.0, 0.0, -0.7351, 0.4404, -0.9504, 0.5129, 0.3612, 0.6041, 0.639, -0.5574, 0.0, 0.7845, 0.0, 0.5574, -0.3527, 0.0, 0.5267, -0.4939, 0.7717, -0.5106, 0.0, -0.631, -0.8942]
improvedlorentz1=[]
lorentz2=[-0.937, -0.8074, 0.4939, 0.9081, 0.0066, 0.0, -0.5362, 0.2023, 0.0, 0.91, 0.5341, -0.0258, 0.0, 0.3089, -0.6808, 0.7178, 0.25, 0.0, 0.8534, 0.0, 0.0, -0.2023, 0.2382, -0.5574, 0.6705, -0.5574, -0.296, 0.743, -0.891, 0.5106, 0.4023, 0.431, 0.2023, 0.5574, 0.3612, 0.4588, -0.8271, 0.8625, 0.891, 0.0, 0.1531, 0.538, 0.7964, 0.2846, 0.0, -0.7003, 0.0762, -0.3612, -0.92, -0.6022, -0.296, 0.0772, 0.6286, 0.0, 0.0, 0.7297, -0.7964]
improvedlorentz2=[]

for i in lorentz1: # we are interested only in toxic scores
    if i < 0:
        improvedlorentz1.append(i*(-1))
    else:
        improvedlorentz1.append(0)

X=np.array(sorted(improvedlorentz1, reverse=True))

def lorenz(arr):
    # this divides the prefix sum by the total sum
    # this ensures all the values are between 0 and 1.0
    scaled_prefix_sum = arr.cumsum() / arr.sum()
    # this prepends the 0 value (because 0% of all people have 0% of all wealth)
    return np.insert(scaled_prefix_sum, 0, 0)

# show the gini index!


lorenz_curve = lorenz(X)

# we need the X values to be between 0.0 to 1.0
plt.plot(np.linspace(0.0, 1.0, lorenz_curve.size), lorenz_curve)
# plot the straight line perfect equality curve
plt.plot([0,1], [0,1])
plt.show()




X_lorenz = X.cumsum() / X.sum()
X_lorenz = np.insert(X_lorenz, 0, 0)
X_lorenz[0], X_lorenz[-1]
fig, ax = plt.subplots(figsize=[6,6])
## scatter plot of Lorenz curve
ax.scatter(np.arange(X_lorenz.size)/(X_lorenz.size-1), X_lorenz,
           marker='x', color='darkgreen', s=100)
## line plot of equality
ax.plot([0,1], [0,1], color='k')


def lorenz_curve(X):
    X_lorenz = X.cumsum() / X.sum()
    X_lorenz = np.insert(X_lorenz, 0, 0)
    #X_lorenz[0], X_lorenz[-1]
    fig, ax = plt.subplots(figsize=[6,6])
    ## scatter plot of Lorenz curve
    ax.scatter(np.arange(X_lorenz.size)/(X_lorenz.size-1), X_lorenz,
               marker='x', color='darkgreen', s=100)
    ## line plot of equality
    ax.plot([0,1], [0,1], color='k')


lorenz_curve(X)





ginis1=[]
for i in range(len(sent16)):
    try:
        ginis1.append(gini1(sent16[i]))
    except:
        pass

ginis1correct =[]

for i in ginis1:
    if 0 < i <= 1:
        ginis1correct.append(i)
    else:
        pass




print(len(ginis1))
print(len(ginis1correct))
avg= np.average(ginis1correct)
median = np.median(ginis1correct)
max = np.min(ginis1correct)
lol = np.max(ginis1correct)


std = np.std(ginis1correct)
print(avg, std, max, lol, median)

