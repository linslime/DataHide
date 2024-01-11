import pandas as pd
#数据预处理
df = pd.read_excel(r'D:\Desktop\one.xls', sheet_name='多元2')
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

def listchange(list1,list2,list3):
    mylist = []
    for i in list1:
        key = 1
        for j in list2:
            if i == j:
                key = 0
                break
        for j in list3:
            if i == j:
                key = 0
                break
        if key == 1:
            mylist.append(i)
    return mylist
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

def ifdataequal(list1,list2):
    for i in range(Datalength):
        if list[i] != list2[i]:
            return 0
    return 1

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
    max = comparedata(data[listfindmax[0]],data[listfindmax[1]])
    max1 = listfindmax[0]
    max2 = listfindmax[1]
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

def findmin(min,listfindmin):
    mylist = []
    templist = []
    resultlist = []
    for key in range(Datalength + 1):
        mylist = []
        templist = []
        for i in listfindmin:
            if i == min:
                mylist.append(i)
                continue
            resultlist = comparedatalist(data[i], data[min])
            if resultlist[-1] == key and (templist == [] or resultlist == templist):
                templist = resultlist
                mylist.append(i)


        if len(mylist) >= Plimit:
            break
    return mylist


def messagelist(list):
    result = []
    gro = 1
    # print("haah")
    for i in list:
        resultlist = comparedatalist(data[i[0]],data[i[0]])[:-1]
        for j in range(1,len(i)):
            li1 = comparedatalist(data[i[0]],data[i[j]])[:-1]
            resultlist = comparemessagelist(li1,resultlist)

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
    thrlist = []
    key = 0
    datalist = []
    while key < 200 :
        datalist = groupdata[0]
        groupdata = groupdata[1:]

        one = datalist[0]

        onelist = []
        twolist = []
        thrlist = []
        onelist = findmin(one, datalist)

        # print(type(onelist))
        thrlist = list(set(datalist) - set(onelist))
        # print(datalist)
        # print(groupdata)
        # print(one)
        #
        # print(onelist)
        # print(twolist)
        # print(thrlist)
        if len(onelist) >= Plimit and len(thrlist) >= Plimit:
            temllist = []
            temllist.append(thrlist)
            groupdata = temllist + groupdata
            groupdata.append(onelist)
        else:

            groupdata.append(datalist)
        # print(groupdata)
        key = key + 1
        lii = []
        lii = messagelist(groupdata)
        aa = 0
        bb = 0
        for i in lii:
            aa += i[-2] * i[-3]
            bb += i[-2]
        # print(groupdata)
        # print(lii)
        print(aa)
        # print(bb)