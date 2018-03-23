import pandas as pd
import pickle
import numpy as np
from operator import itemgetter
import datetime

def modify(S):
    return S[6:10]+"/"+S[0:5]+" "+S[11:]

def demodify(S):
    return S[5:10]+"/"+S[0:4]+" "+S[10:]

dataset = 'My_City_Crime_Data.csv'

full_data = pd.read_csv(dataset)
total_length = len(full_data)
#print(data)
print("Load complete")
mb_size = 1000
cnt = 0
for l in range(0, total_length, mb_size):
    size_batch = min(total_length-l, mb_size)
    data = full_data[l:l+size_batch]
    values = data.values
    for i in range(size_batch):
        cnt+=1
        #if np.isnan(values[i][0]): break
        cur_time = values[i][2]
        full_data.set_value(l+i, 'Date', modify(cur_time))
        if cnt%100 == 0:
            print("Step "+str(cnt)+" processed")

full_data = full_data.sort_values(by=['Date'])
print(full_data)
'''
mb_size = 1000
cnt = 0
for l in range(0, total_length, mb_size):
    size_batch = min(total_length-l, mb_size)
    data = full_data[l:l+size_batch]
    values = data.values
    for i in range(size_batch):
        cnt+=1
        if np.isnan(values[i][0]): break
        cur_time = values[i][2]
        full_data.set_value(l+i, 'Date', demodify(cur_time))
        if cnt%100 == 0:
            print("Step "+str(cnt)+" processed")
'''
full_data.to_csv('Edited-'+dataset, index=False)
