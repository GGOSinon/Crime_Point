import pandas as pd
import pickle
import numpy as np
from operator import itemgetter
import datetime

def toDateTime(S):
    return datetime.datetime.strptime(S[0:10], "%Y/%m/%d")

def save_pkl(filename, X):
    F = open(filename, 'wb')
    pickle.dump(X, F)

dataset = 'Edited-Crimes-2014.csv'

full_data = pd.read_csv(dataset)
total_length = len(full_data)
#print(data)
print("Load complete")
Crimes = []

with open('labels.pkl', 'rb') as F:
    Labels = pickle.load(F)

dict_label = []
for i in range(7):
    dict_label.append({})    
    for j in range(len(Labels[i])):
        dict_label[i][Labels[i][j]]=j

data_pos = [2, 5, 6, 7, 8, 9, 10] 
#data_pos = [1, 2, 3, 4, 5, 6, 7]

cnt = 0

print ("Stored "+str(total_length)+" crime datas")
chk = True
full_data = full_data.sort_values(by='Date')
#values = data.values
#print(values.shape)

#num_data = values.shape[0]

#data = pd.read_csv(dataset, chunksize = 2)
#values = data.values
deltatime = datetime.timedelta(days = 7)
deltatime_leap = datetime.timedelta(days = 7)
data = full_data[0:1]
values = data.values
next_time = toDateTime(values[0][2]) + deltatime
file_num = 1
mb_size = 1000

#for i in range(num_data-1, -1, -1):
for l in range(0, total_length, mb_size):
    #data = pd.read_csv(dataset, skiprows=l, nrows=mb_size)
    size_batch = min(total_length-l, mb_size)
    data = full_data[l:l+size_batch]
    #data = full_data[total_length-1-(l+size_batch): total_length-1-l]
    values = data.values
    for i in range(size_batch):
    #for i in range(size_batch-1, -1, -1):
        #print(values[i][2])
        cnt+=1
        if np.isnan(values[i][0]): break
        cur_time = toDateTime(values[i][2])
        if cur_time>=next_time:
            if cur_time.year%4==0: next_time = cur_time + deltatime_leap
            else: next_time = cur_time + deltatime
            save_pkl('./data/crimes-'+str(file_num)+'.pkl', Crimes)
            file_num += 1
            Crimes = []
        X = []
        for j in range(7):
            V = values[i][data_pos[j]]
            if j==0 or j==2: X.append(V)
            elif j==4:
                #print(V)
                if V==True: X.append(0)
                elif V==False: X.append(1)
            elif j==5: 
                if V==True: X.append(0)
                elif V==False: X.append(1) 
            elif V not in dict_label[j].keys(): X.append(-1)
            else: X.append(dict_label[j][V])
    #print(X[0], X[2])
        Crimes.append(X)
        if cnt%100 == 0:
            print("Step "+str(cnt)+" processed, Time = "+str(cur_time)+","+str(next_time))

#for i in range(100):
#    print(Crimes[i])

save_pkl('./data/crimes-'+str(file_num)+'.pkl', Crimes)
