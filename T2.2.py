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


def comparedata(list1,list2):
    unequal = 0
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            unequal = unequal + 1
    return unequal

def findmax(list):
    max = 0
    max1 = 0
    max2 = 0
    for i in range(0,len(list) - 1):
        if max == Datalength:
            break
        for j in range(i + 1, len(list)):
            if max == Datalength:
                break
            result = comparedata(data[i],data[j])
            if result > max:
                max1 = i
                max2 = j
                max = result
    resultlist = []
    resultlist.append(max)
    resultlist.append(max1)
    resultlist.append(max2)
    return resultlist

if __name__ == "__main__":
    onelist = []
    twolist = []
    telist = []
    while i < 100:
        i += 1
        telist = groupdata[0]
        groupdata = groupdata[1:]
        res = findmax(telist)
        one = res[-1]
        two = res[-2]
        for i in telist:
            if comparedata(data[i],data[one]) < comparedata(data[i],data[two]):
                onelist.append(i)
            else :
                twolist.append(i)
    groupdata.append(onelist)
    groupdata.append(telist)

    # onelist = []
    # twolist = []
    #  telist = []
    #  while i < 100:
    #
    #      telist = groupdata[0]
    #         groupdata = groupdata[1:]
    #      res = findmax(telist)
    #      one = res[-1]
    #     two = res[-2]
    #     for i in telist:
    #
    #         if comparedata(data[i],data[one]) < comparedata(data[i],data[two]):
    #             onelist.append(i)
    #         else:
    #             twolist.append(i)
    #     groupdata.append(onelist)
    #     groupdata.append(twolist)
    #




