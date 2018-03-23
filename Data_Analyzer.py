import pickle
import numpy as np
from operator import itemgetter
with open('crimes.pkl', 'rb') as F:
    crimes = pickle.load(F)

with open('labels.pkl', 'rb') as F:
    labels = pickle.load(F)

c = np.zeros((10,1000))
for i in range(1,7):
    for x in crimes:
        #print(x)
        c[i][x[i]]+=1

for i in range(1,7):
    #print(i, len(labels[i]))
    X = []
    for j in range(len(labels[i])):
        X.append((str(labels[i][j]), c[i][j]))
    #X_sorted = sorted(X, key=itemgetter(1), reverse=True)
    X_sorted = X
    #res=0
    for j in range(min(1000,len(X_sorted))):
        label, cnt = X_sorted[j]
        #res+=cnt
        print(label+": "+str(cnt))
    print("")
    print(len(X_sorted))

#print(crimes)
#print(labels)
