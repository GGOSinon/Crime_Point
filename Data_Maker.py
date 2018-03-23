import openpyxl
import pickle
from operator import itemgetter

wb = openpyxl.load_workbook('My_City_Crime_Data.xlsx')
ws = wb.get_sheet_by_name("Sheet1")

Crimes = []
Labels = []

def add(dict_num, key):
    if key in dict_num: dict_num[key]+=1
    else: dict_num[key]=1

for i in range(8): Labels.append([])

chk = True
cnt = 0

dict_label = []
dict_num = []
for i in range(8): dict_label.append({})
for i in range(8): dict_num.append({})

for r in ws.rows:
    if chk: 
        chk=False
        continue
    cnt += 1
    if r[0].value==None: break
    X = []
    for i in range(1, 8):
        V = r[i].value
        add(dict_num[i-1], V)

for i in range(0,7):
    X = []
    #print(dict_num[i])
    for key, values in dict_num[i].items():
        X.append((key, values))
    X_sorted = sorted(X, key=itemgetter(1), reverse=True)
    for j in range(len(X_sorted)):
        dict_label[i][X_sorted[j][0]] = j
        Labels[i].append(X_sorted[j][0])

print ("Stored "+str(cnt)+" crime datas")
chk = True

for r in ws.rows:
    if chk:
        chk = False
        continue
    if r[0].value==None: break
    X = []
    for i in range(1,8):
        V = r[i].value
        if i==1 or i==3: X.append(V)
        else: X.append(dict_label[i-1][V])
    Crimes.append(X)

for x in Labels[1]:
    print(x)
with open('crimes.pkl', 'wb') as f:
    pickle.dump(Crimes, f)

with open('labels.pkl', 'wb') as f:
    pickle.dump(Labels, f)
