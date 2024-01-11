import pandas as pd
import random
import math
import numpy as np
import copy


#数据预处理
df = pd.read_excel(r'D:\Desktop\start.xls', sheet_name='Sheet4')
data = df.values
datatemp = []
for i in data:
    datatemp.append(i.tolist())
data = datatemp
Listlength = len(data)
Datalength = len(data[0])
adrdata = []
rawdata = []
cpadata = []
msgdata = []
rdatalength = int(Datalength/2-2)
groupdata = [0 for i in range(rdatalength+1)]
for i in range(len(groupdata)):
    groupdata[i] = []
for i in data:
    adrdata.append(i[0] - 1)
    rawdata.append(i[1:rdatalength + 1])
    cpadata.append(i[rdatalength + 1:Datalength-3])
    msgdata.append(i[Datalength-3:Datalength])
for i in range(Listlength - 1):
    groupdata[int(msgdata[i][0])].append(i)
listgrp = []
listmsg = []

max = msgdata[0][2]
maxtep = 0
for i in msgdata:
    if i[2] > maxtep:
        maxtep = i[2]

listgrp = [0 for i in range(maxtep)]
listmsg = [0 for i in range(maxtep)]
for i in range(maxtep):
    listgrp[i] = []
    listmsg[i] = []
for i in range(len(msgdata)):
    listgrp[msgdata[i][2] - 1].append(i)
    listmsg[msgdata[i][2]-1] = msgdata[i]

listarea = []
listarea = [0 for i in range(rdatalength + 1)]
for i in range(rdatalength + 1):
    listarea[i] = []
for i in listmsg:
    listarea[i[0]].append(i[2])

listzero = []
for i in range(len(listarea)):
    if len(listarea[i]) != 0:
        listzero.append(i)


# print(listgrp)
# print(listmsg)
# print(rawdata)
# print(listarea)
# print(listzero)
T = 1
AT = 0.6



templistgrp = copy.deepcopy(listgrp)
templistmsg = copy.deepcopy(listmsg)



def msglist(list):
    mylist = []
    num = len(list)
    for i in range(rdatalength):
        key = 1
        for j in range(num):
            if rawdata[list[j]][i] != rawdata[list[0]][i]:
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



def comparemessagelist(list1,list2):
    result = []
    for i in range(len(list1)):
        if list1[i] == 0 or list2[i] == 0:
            result.append(0)
        else:
            result.append(1)
    return result
def comparedatalist(list1,list2):
    mylist = []
    unequal = 0
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            mylist.append(0)
            unequal = unequal + 1
        else:
            mylist.append(1)
    mylist.append(unequal)
    return mylist

def comparedata(list1,list2):
    mylist = []
    unequal = 0
    for i in range(rdatalength):
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
def costfunction(list):
    result = 0
    for i in list:
        if i[0] == 0 or i[0] == 1:
            result += i[0] * i[1]
        else:
            result += rdatalength * i[1]
    return result

def changeway():
    SUM = 1000
    while True:
        on = 0
        tw = 0
        tt = 0
        re = []
        fi = []
        se = []
        th = []


        fi.append(listzero[random.randint(0, len(listzero) - 1)])
        fi.append(listarea[fi[0]][random.randint(0, len(listarea[fi[0]]) - 1)])
        fi.append(listgrp[fi[1] - 1][random.randint(0, len(listgrp[fi[1] - 1]) - 1)])

        se.append(listzero[random.randint(0, len(listzero) - 1)])
        while True:
            a = listarea[se[0]][random.randint(0, len(listarea[se[0]]) - 1)]
            if a != fi[1]:
                se.append(a)
                break
            if on > SUM:
                break
            on += 1
        if on > SUM:
            continue
        se.append(listgrp[se[1] - 1][random.randint(0, len(listgrp[se[1] - 1]) - 1)])



        while True:
            b = listzero[random.randint(0, len(listzero) - 1)]
            if (b == fi[0] and b == se[0]) == False:
                th.append(b)
                break
            if tw > SUM:
                break
            tw += 1
        if tw > SUM:
            continue
        while True:
            c = listarea[th[0]][random.randint(0, len(listarea[th[0]]) - 1)]
            if c != fi[1] and c != se [1]:
                th.append(c)
                break
            if tt > SUM:
                break
            tt += 1
        if tt > SUM:
            continue
        th.append(listgrp[th[1] - 1][random.randint(0, len(listgrp[th[1] - 1]) - 1)])

        re.append(fi)
        re.append(se)
        re.append(th)
        break
    return re

def changestate(list):
    #改变listgrp
    global listmsg
    global listgrp
    global listzero
    global listarea
    global templistgrp
    global templistmsg
    templistgrp[list[0][1] - 1].append(list[1][2])
    templistgrp[list[0][1] - 1].remove(list[0][2])

    templistgrp[list[1][1] - 1].append(list[2][2])
    templistgrp[list[1][1] - 1].remove(list[1][2])

    templistgrp[list[2][1] - 1].append(list[0][2])
    templistgrp[list[2][1] - 1].remove(list[2][2])

    #改变msg
    templistmsg[list[0][1] - 1][0] = msglist(templistgrp[list[0][1] - 1])[-1]
    templistmsg[list[1][1] - 1][0] = msglist(templistgrp[list[1][1] - 1])[-1]
    templistmsg[list[2][1] - 1][0] = msglist(templistgrp[list[2][1] - 1])[-1]

    return costfunction(templistmsg) - costfunction(listmsg)
def acceptrule(cost):
    if cost < 0:
        # print(1)
        return 1
    else:
        one = math.exp((0 - cost) / T)
        two = random.randint(0, 100000000) / 100000000

        if one >= two:
            # print(1,one, two)
            return 1
        else:
            # print(2,one, two)
            return 0

def acceptstate(ifcost):
    # 改变listgrp
    global listmsg
    global listgrp
    global listzero
    global listarea
    global templistgrp
    global templistmsg
    global T
    # print(T)

    if ifcost == 1:
        listgrp = []
        listmsg = []
        listmsg = copy.deepcopy(templistmsg)

        listgrp = copy.deepcopy(templistgrp)

        listarea = []
        listarea = [0 for i in range(rdatalength + 1)]
        for i in range(rdatalength + 1):
            listarea[i] = []
        for i in listmsg:
            listarea[i[0]].append(i[2])

        listzero = []
        for i in range(len(listarea)):
            if len(listarea[i]) != 0:
                listzero.append(i)

        # print(listgrp)
        # print(listmsg)
        # print(listarea)
        # print(listzero)
    else:
        templistgrp = copy.deepcopy(listgrp)
        templistmsg = copy.deepcopy(listmsg)
    T = T * AT


if __name__ == "__main__":
    # a = changeway()
    # print(a)
    # print(changestate(a))
    # print(templistgrp)
    # print(listgrp)
    # print(templistmsg)
    # print(listmsg)
    # print(msglist([13,30]))
    # print(T < np.power(10.0,-100))
    listre = []
    listre.append(costfunction(listmsg))
    tt = 0
    while T > np.power(10.0,-100):
        changelist = changeway()

        # print(changelist)
        cost = changestate(changelist)
        acrule = acceptrule(cost)

        acceptstate(acrule)
        tt = costfunction(listmsg)
        listre.append(tt)
        print(tt)

    print(listgrp)
    print(listmsg)

    from xlutils.copy import copy
    import xlrd as xr
    n = 4
    listans = [[0,listre[0]]]
    key = 0
    for i in listre:
        if listans[key][1] == i:
            listans[key][0] += 1
        else :
            tli = []
            tli.append(1)
            tli.append(i)
            listans.append(tli)
            key += 1





    file = "D:\\Desktop\\ans.xls"
    oldwb = xr.open_workbook(file)
    newwb = copy(oldwb)
    newws = newwb.get_sheet(-1 + n)
    for i in range(len(listans)):
        for j in range(len(listans[i])):
            newws.write(i + 1, j + 1, listans[i][j])  # 行，列，数据
    newwb.save(file)

    file = "D:\\Desktop\\listmsg.xls"
    oldwb = xr.open_workbook(file)
    newwb = copy(oldwb)
    newws = newwb.get_sheet(-1 + n)
    for i in range(len(listmsg)):
        for j in range(len(listmsg[i])):
            newws.write(i + 1, j + 1, listmsg[i][j])  # 行，列，数据
    newwb.save(file)

    file = "D:\\Desktop\\listgrp.xls"
    oldwb = xr.open_workbook(file)
    newwb = copy(oldwb)
    newws = newwb.get_sheet(-1 + n)
    for i in range(len(listgrp)):
        for j in range(len(listgrp[i])):
            newws.write(i + 1, j + 1, listgrp[i][j])  # 行，列，数据
    newwb.save(file)
