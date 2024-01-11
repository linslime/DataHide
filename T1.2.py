import pandas as pd

#数据预处理
df = pd.read_excel(r'D:\Desktop\start.xls', sheet_name='Sheet1')
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
print(groupdata)

groupdata = groupdata[:1]
# for i in range(Listlength - 1):
#     templist = []
#     templist.append(i)
#     for j in range(i + 1, Listlength):
#         if msgdata[i][2] == msgdata[j][2]:
#             templist.append(j)
#
#     groupdata[msgdata[templist[0]][0]].append(templist)

# print(adrdata)
# print(rawdata)
# print(cpadata)
# print(msgdata)
# print(groupdata)
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
# if __name__ == "__main__":
    # for key in range(1,rdatalength + 1):
    #     for i in range(rdatalength):
    #         if len(groupdata[rdatalength - 1 - i]) == 0:
    #             continue

