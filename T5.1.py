import numpy as np
from scipy.fftpack import fft
from matplotlib.pylab import mpl
import pandas as pd
from xlutils.copy import copy
import xlrd as xr
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
Plimit = 2
Group = 1
groupdata = []
tempgrupdata = []
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
if __name__ == "__main__":
    for key in range(Datalength + 1):
        # tempgrupdata = []
        for i in range(Listlength - 1):
            if len(data[i]) > Datalength:
                continue
            adrlist = []
            templist = []
            resultlist = []
            mylist = data[i]
            adrlist.append(i)
            for j in range(i + 1, Listlength):
                if len(data[j]) > Datalength:
                    continue

                templist = copy.deepcopy(adrlist)
                templist.append(j)
                resultlist = msglist(templist)
                if resultlist[-1] <= key :
                    adrlist.append(j)

            if len(adrlist) >= Plimit:
                resultlist.append(len(adrlist))
                resultlist.append(Group)
                Group = Group + 1
                for j in adrlist:
                    data[j] = data[j] + resultlist
                # tempgrupdata.append(adrlist)
        # groupdata.append(tempgrupdata)


    from xlutils.copy import copy
    import xlrd as xr
    num = 0
    for i in data:
        num = num + i[-3]
    print(num)
    file = "D:\Desktop\T3.3.xls"
    oldwb = xr.open_workbook(file)
    newwb = copy(oldwb)
    newws = newwb.get_sheet(-1 + 1)
    for i in range(len(data)):
        for j in range(len(data[i])):
            newws.write(i + 1, j + 1, data[i][j])  #行，列，数据
    newwb.save(file)