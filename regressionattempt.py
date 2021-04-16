import pandas as pd
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt

def read_pickle_file(file):
    pickle_data = pd.read_pickle(file)
    return pickle_data

sent9 = read_pickle_file("sentscore9.pkl") # reading scores from category 9
smallsent9=[]
for i in range(4):
    smallsent9.append(sent9[i])


# scores gotten from perspective api
api9 = [0.072357394, 0.20611122, 0.08454758, 0.050218694, 0.03261705, 0.006482082, 0.092388295, 0.1994972, 0.05561256, 0.40333822, 0.10592767, 0.056817662, 0.1075928, 0.35585478, 0.15181361, 0.054665696, 0.07345019, 0.9586997, 0.6626366, 0.31089434, 0.97111857, 0.9657786, 0.8606264, 0.18338452, 0.90180725, 0.59636176, 0.1289913, 0.31089434, 0.31089434, 0.2824503, 0.20378792, 0.26657316, 0.15642665, 0.061228257, 0.15544996, 0.038235612, 0.067240015, 0.46871042, 0.49371913, 0.88824683, 0.7203391, 0.31550348, 0.16465709, 0.24291468, 0.9194924, 0.06481319, 0.31089434, 0.11497382, 0.06290888, 0.26567507, 0.070089795, 0.31089434, 0.15629117, 0.2423853, 0.17011969, 0.24243608, 0.10049798, 0.13741107, 0.3338724, 0.1667411, 0.06354354, 0.21634768, 0.5602942, 0.6046365, 0.11146223, 0.26820934, 0.97037077, 0.9017438, 0.46302333, 0.82913435, 0.8606264, 0.18185681, 0.24067727, 0.04278995, 0.101416685, 0.4937289, 0.12440016, 0.2371996, 0.4207419, 0.08524489, 0.24101233, 0.6530753, 0.23970042, 0.28534624, 0.07914105, 0.107251644, 0.1243725, 0.29630482, 0.32494316, 0.15310538, 0.34969363, 0.074833535, 0.36497495, 0.55629796, 0.53490317, 0.7373566, 0.1511023, 0.11957156, 0.093952574, 0.052396554, 0.19331545, 0.15342833, 0.11468109, 0, 0, 0.33780602, 0.7410297, 0, 0.08134904, 0, 0, 0, 0, 0, 0, 0, 0.8273243, 0, 0.40337518, 0.69844526, 0, 0, 0, 0, 0, 0.13543096, 0, 0, 0, 0, 0, 0, 0, 0]

# scores from VADER and Hatebase analysis
smallsent99 = [0.4404, 0.765, 0.5106, 0.4549, 0.4019, 0.0, 0.4404, 0.7845, 0.0, 0.5095, 0.6199, 0.0, 0.0, -0.8602, 0.504, 0.0, 0.0, -0.2484, 0.4019, -0.5106, -0.5106, -0.7146, -0.1645, -0.802, -0.5423, 0.1132, 0.3818, 0.9068, 0.8805, 0.9216, -0.5574, 0.9413, -0.7783, 0.0, -0.5255, 0.0, 0.4404, -0.6249, 0.7463, -0.9205, -0.5413, -0.5574, -0.0772, 0.1027, -0.9286, 0.7579, -0.6901, 0.0, 0.0, -0.8681, -0.6486, 0.0, 0.0, -0.2755, -0.1027, -0.631, 0.6124, 0.5442, -0.0964, -0.6597, -0.2263, -0.4588, -0.5293, -0.967, 0.5093, -0.5302,
-0.8995, -0.8869, 0.0, -0.9333, -0.9881, -0.3182, -0.4678, -0.5574, 0.7388, 0.5983, -0.0516, -0.4689, -0.6113, -0.3612, -0.34, -0.4767, 0.8583, -0.5574, 0.0, 0.4278, 0.4677, -0.6836, -0.7351, 0.4215, -0.296, -0.308, -0.8126, 0.6474, 0.0, -0.2263, 0.4215, 0.7013, 0.0, 0.0, -0.2144, 0.0, 0.5267, 0.0, -0.8583, 0.0, -0.1027, 0.836, -0.4019, -0.7488, 0.0, 0.4404, 0.8258, 0.5106, 0.4404, -0.8481, -0.8824, 0.7184, 0.3612, -0.948, -0.4939, 0.1603, 0.4404, 0.6908, 0.3818, 0.5106, 0.0, -0.296, 0.6808, 0.1779, 0.4019, 0.3818, -0.5549, 0.8407]


bad_indicies = [] # as both toxicity detecction tools failed in some cases (score is 0.00) we eliminate those
for i in range(len(api9)): # Doesnt matter because len api9 is the same as smallsent99
    if api9[i] == 0:
        bad_indicies.append(i)
    elif smallsent99[i] == 0.0:
        bad_indicies.append(i)
    else:
        pass

for index in reversed(bad_indicies): # as if the scores failed (are 0) but we still have to keep the same lenght of both lists
    api9.pop(index) # we look for where the neither score is 0
    smallsent99.pop(index)

smallsent999 =[]


for i in smallsent99: # correcting the scores from VADER and Hatebase so it only looks at toxic ones
    if i < 0:
        smallsent999.append(i*(-1))
    else:
        smallsent999.append(0)


x = np.array(api9)
y = np.array(smallsent999)

# different correlation analysis

print(np.corrcoef(api9, smallsent999))

print(scipy.stats.pearsonr(api9, smallsent999))

print(scipy.stats.spearmanr(api9, smallsent999))

result = scipy.stats.linregress(api9, smallsent999)

print("check this", result.slope, result.intercept, result.rvalue, "p", result.pvalue, result.stderr)

plt.style.use('ggplot')
slope, intercept, r, p, stderr = scipy.stats.linregress(x, y)
line = f'Regression line: y={intercept:.2f}+{slope:.2f}x, r={r:.2f}'
line

fig, ax = plt.subplots()
ax.plot(x, y, linewidth=0, marker='s', label='Data points')
ax.plot(x, intercept + slope * x, label=line)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend(facecolor='white')
plt.show()