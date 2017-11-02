#!/usr/bin/python
# coding: utf-8
import commands

_, result = commands.getstatusoutput('netstat -lntp')
result = result.split('\n')
del result[0:2]

newList = []
newList2 = []

for i in result:
    val = i.split()
    del val[1:3]
    del val[2:4]

    if val[0] == 'tcp':
        valTmp = val[1].split(':')
        val[0] = valTmp[1]

        valTmp = val[2].split('/')
        val[1] = valTmp[1]
        del val[2]

        newList.append(val)

    elif val[0] == 'tcp6':
        valTmp = val[1].split(':')
        val[0] = valTmp[-1]

        valTmp = val[2].split('/')
        val[1] = valTmp[1]
        del val[2]

        newList.append(val)


for i in newList:
    if i not in newList2:
        newList2.append(i)


json_data = ""{\n"" + ""\t"" + '""data"":[' + ""\n""

for net in newList2:
    if net != newList2[-1]:
        json_data = json_data + ""\t\t"" + ""{"" + ""\n"" + ""\t\t\t"" + '""{#PPORT}"":""' + str(
            net[0]) + ""\"",\n"" + ""\t\t\t"" + '""{#PNAME}"":""' + str(net[1]) + ""\""},\n""
    else:
        json_data = json_data + ""\t\t"" + ""{"" + ""\n"" + ""\t\t\t"" + '""{#PPORT}"":""' + str(
            net[0]) + ""\"",\n"" + ""\t\t\t"" + '""{#PNAME}"":""' + str(net[1]) + ""\""}]}""


print json_data
