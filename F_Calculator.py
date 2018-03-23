import pickle
import numpy as np
from Functions import Calculator
import datetime

num_files = 898

with open('labels.pkl', 'rb') as F:
    labels = pickle.load(F)

def toDateTime(S):
    return datetime.datetime.strptime(S[0:10], "%Y/%m/%d")

def get_safety(crime_pkl_name):
    with open(crime_pkl_name, 'rb') as F:
        crimes = pickle.load(F)

    res = 0
    Cal = Calculator(labels)

    cnt = 0
    num_data = len(crimes)
    for crime in crimes:
        cnt+=1
        res+=Cal.f(crime)
        #if cnt%100 == 0: print(str(cnt)+" data processed")
    first_time = toDateTime(crimes[0][0])
    last_time = toDateTime(crimes[num_data-1][0])
    delta_time = last_time - first_time
    #print(delta_time)
    data_time_length = delta_time.total_seconds()//(3600*7)
    res/=data_time_length
    res*=Cal.g(crimes)
    return res

F = open('result.txt', 'w')
F.close()

for i in range(1, num_files+1):
    safety = get_safety('./data-all-week/crimes-'+str(i)+'.pkl')
    print("Safety of dataset "+str(i)+" : "+str(safety))
    F = open('result.txt', 'a')
    F.write(str(i)+" "+str(safety)+"\n")

#print(crimes)
#print(labels)
