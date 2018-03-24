import math
from datetime import datetime
class Calculator:
    # Constants
    c1 = [30, 40, 35, 38, 40, 40, 35, 38, 42, 38, 15, 52, 38, 48, 90, 10, 93, 25, 82, 87, 10, 100, 88, 30, 25, 12, 35]
    c2 = []
    c3_metro = [6, 1, 6, 1, 3, 1, 4, 2, 1, 1, 2, 5, 1, 8, 5, 2, 1, 1, 3,10, 2, 1, 3, 1, 4, 8, 8, 3, 1, 1, 3, 1, 1, 3, 1, 7, 3, 1, 1, 7, 1, 3, 
6, 1] + [3]*49
    c3_local = [6, 9, 6, 9, 3, 8, 2, 2, 7, 1, 4, 5, 7, 8, 5, 4, 5, 1, 4, 2, 2, 10, 3, 3, 1, 8, 8, 5, 1, 7, 4, 9, 9, 7, 6, 7, 1, 3, 10, 3, 2, 3, 6, 1] + [3]*49 
    c3_danger = [3, 6, 3, 6, 3, 5, 4, 8, 6, 6, 2, 2, 2, 2, 3, 6, 2, 4, 5, 5, 2, 5, 2, 2, 5, 8, 7, 10, 10, 2, 3, 9, 1, 2, 5, 2, 6, 2, 4, 4, 8, 3, 4, 8] + [3]*49   
    c4 = [1, 1.2]
    c5 = []
    w_night = 1.2
    w_day = 1
    w_agg = 1.5

    crimes = []
    labels = []
    #print(len(c3_public))
    #print(c3_danger)
    pop_local = 2800000.0
    pop_metro = 6000000.0*4/7

    rat_local = pop_local / (pop_local + pop_metro)
    rat_metro = pop_metro / (pop_metro + pop_local)
    def check_time(self, cur_time):
        cur_time = datetime.strptime(cur_time, '%Y/%m/%d %I:%M:%S %p')
        if cur_time.hour*60+cur_time.minute>=1230: return 1
        if cur_time.hour*60+cur_time.minute<=330: return 1
        return 0

    def is_agg(self, S):
        if 'AGG' in S and 'NON' not in S:
            #print(S)
            return True
        return False

    def __init__(self, labels):
        self.labels = labels
        #print(labels[2]) 
        #print(self.c3_metro)
        #print(self.c3_local)
        for i in range(len(labels[3])):
            S = self.c3_metro[i] + self.c3_local[i]
            self.c3_metro[i]=float(self.c3_metro[i])/S
            self.c3_local[i]=float(self.c3_local[i])/S
        #print(self.c3_metro)
        #print(self.c3_local)

    def f(self, crime):
        if crime[1]==-1: w_crime1 = 25
        else: w_crime1 = self.c1[crime[1]]
        if self.is_agg(crime[2]): w_crime2 = 1.5
        else: w_crime2 = 1
        if crime[3]==-1:
            w_loc_local = 0.5
            w_loc_danger = 2
            w_loc_metro = 0.5
        else:
            w_loc_local = self.c3_local[crime[3]] 
            w_loc_danger = self.c3_danger[crime[3]]
            w_loc_metro = self.c3_metro[crime[3]] 
        w_domestic = self.c4[crime[5]]
        if self.check_time(crime[0]): w_time = self.w_night
        else: w_time = self.w_day
        w = w_crime1/100.0 * w_crime2 * w_loc_danger * (w_loc_local * self.rat_local + w_loc_metro * self.rat_metro) * w_domestic * w_time
        #print(w)
        return w

    def g(self, crimes):
        arrest_rate = 0.0
        for crime in crimes:
            if crime[4]==1: arrest_rate+=1
        arrest_rate/=len(crimes)
        epsilon = 0.0001
        res = 1.0/(1+arrest_rate)
        #print(res)
        return res
