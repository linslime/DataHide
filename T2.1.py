import numpy as np
from scipy.fftpack import fft
from matplotlib.pylab import mpl
import pandas as pd
from xlutils.copy import copy
import xlrd as xr
import random

#数据预处理
df = pd.read_excel(r'D:\Desktop\one.xls', sheet_name='二元1')
data = df.values
datatemp = []
for i in data:
    datatemp.append(i.tolist())
data = datatemp
Datalength = len(data[0])
Listlength = len(data)
Plimit = 2
groupdata = [i for i in range(Listlength)]
templist = groupdata
groupdata = []
groupdata.append(templist)
# print(data)

def comparedatalist(list1,list2):
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

def comparemessagelist(list1,list2):
    result = []
    for i in range(len(list1)):
        if list1[i] == 0 or list2[i] == 0:
            result.append(0)
        else:
            result.append(1)
    return result
def comparedata(list1,list2):
    unequal = 0
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            unequal = unequal + 1
    return unequal

def findmax(listfindmax):
    max = 0
    max1 = 0
    max2 = 0
    for i in range(0,len(listfindmax) - 1):
        if max == Datalength:
            break
        for j in range(i + 1, len(listfindmax)):
            if max == Datalength:
                break
            result = comparedata(data[listfindmax[i]],data[listfindmax[j]])
            if result > max:
                max1 = listfindmax[i]
                max2 = listfindmax[j]
                max = result
    resultlist = []
    resultlist.append(max)
    resultlist.append(max1)
    resultlist.append(max2)
    return resultlist

def messagelist(list):
    result = []
    gro = 1
    print("haah")
    for i in list:
        resultlist = comparedatalist(data[i[0]],data[i[0]])[:-1]
        for j in range(1,len(i)):
            li1 = comparedatalist(data[i[0]],data[i[j]])[:-1]
            resultlist = comparemessagelist(li1,resultlist)
            print(resultlist)
        num = 0
        for j in resultlist:
            if j == 0:
                num += 1
        resultlist.append(num)
        resultlist.append(len(i))
        resultlist.append(gro)
        gro += 1
        result.append(resultlist)
    return result

if __name__ == "__main__":
    onelist = []
    twolist = []
    key = 0
    datalist = []
    while key < 200000 :
        datalist = groupdata[0]
        groupdata = groupdata[1:]
        if len(datalist) >= 2 * Plimit:
            result = findmax(datalist)
            one = result[-1]
            two = result[-2]
            onelist = []
            twolist = []
            l = len(datalist)
            for i in range(l):
                index = datalist[i]
                if comparedata(data[index], data[one]) < comparedata(data[index], data[two]):
                    onelist.append(index)
                else:
                    twolist.append(index)
            if len(onelist) >= Plimit and len(twolist) >= Plimit:
                groupdata.append(onelist)
                groupdata.append(twolist)
            else:
                groupdata.append(datalist)
        else:
            groupdata.append(datalist)
        key = key + 1
        # print(groupdata)
    lii = []
    lii = messagelist(groupdata)
    aa = 0
    bb = 0
    for i in lii:
        aa += i[-2] * i[-3]
        bb += i[-2]
    print(groupdata)
    print(lii)
    print(aa)
    print(bb)