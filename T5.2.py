import numpy as np
from scipy.fftpack import fft
from matplotlib.pylab import mpl
import pandas as pd

import random
import copy
#数据预处理
df = pd.read_excel(r'D:\Desktop\one.xls', sheet_name='多元1')
data = df.values
datatemp = []
for i in data:
    datatemp.append(i.tolist())
data = datatemp


Datalength = len(data[0])
Listlength = len(data)
templist = []
adrlist = []
Plimit = 3
Group = 1
groupdata = []
tempgrupdata = []
def msglist(list):
    mylist = []
    num = len(list)
    for i in range(Datalength):
        key = 1
        for j in range(num):
            if data[list[j]][i] != data[list[0]][i]:
                key = 0
                mylist.append(0)
                break
        if key == 1:
            mylist.append(1)
    num = 0
    for i in mylist:
        if i == 0:
            num += 1
    mylist.append(num)
    return mylist
def comparedata(list1,list2):
    mylist = []
    unequal = 0
    for i in range(Datalength):
        if list1[i] != list2[i]:
            mylist.append(0)
            unequal = unequal + 1
        else:
            mylist.append(1)
    mylist.append(unequal)
    return mylist

def ifdataequal(list1,list2):
    for i in range(Datalength):
        if list[i] != list2[i]:
            return 0
    return 1

def datanum():
    num = 0
    for i in data:
        if len(i) == Datalength:
            num += 1
    # print(num)
    return num
def dan():
    mylist = []
    for i in range(len(data)):
        if len(data[i]) == Datalength:
            mylist.append(i)
    return mylist
if __name__ == "__main__":
    for key in range(Datalength + 1):
        print(key)
        # tempgrupdata = []
        for i in range(Listlength - 1):
            print(i)
            if len(data[i]) > Datalength:
                continue
            adrlist = []
            templist = []
            mylist = data[i]
            adrlist.append(i)
            kkke = 0
            for j in range(i + 1, Listlength):
                if len(data[j]) > Datalength:
                    continue
                resultlist = comparedata(mylist, data[j])
                tt = copy.deepcopy(adrlist)
                tt.append(j)
                iftt = msglist(tt)
                if iftt[-1] <= key:
                    templist = resultlist
                    adrlist.append(j)
                if datanum() - len(adrlist) <= Plimit:
                    kkke = 1
                    break
            if kkke == 1:
                adrlist = dan()
            if len(adrlist) >= Plimit:
                templist.append(len(adrlist))
                templist.append(Group)
                Group = Group + 1
                for j in adrlist:
                    data[j] = data[j] + templist


                # tempgrupdata.append(adrlist)
        # groupdata.append(tempgrupdata)

    num = 0
    for i in data:
        num = num + i[-3]
    print(num)


    from xlutils.copy import copy
    import xlrd as xr
    file = "D:\Desktop\T3.3.xls"
    oldwb = xr.open_workbook(file)
    newwb = copy(oldwb)
    newws = newwb.get_sheet(-1 + 3)
    for i in range(len(data)):
        # print(len(data))
        for j in range(len(data[i])):
            # print(data[i])
            newws.write(i + 1, j + 1, data[i][j])  #行，列，数据
    newwb.save(file)