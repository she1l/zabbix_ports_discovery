#!/usr/bin/python
# coding: utf-8
import commands

_, result = commands.getstatusoutput('netstat -lntp')
result = result.split('\n')
del result[0:2]

newList = []
newList2 = []

for i in result:
    name = i.split('/')[-1].strip()
    port = i.split()[3].split(':')[-1]
    newList.append([port, name])

for i in newList:
    if i not in newList2:
        newList2.append(i)

json_data = "{\n" + "\t" + '"data":[' + "\n"

for net in newList2:
    if net != newList2[-1]:
        json_data = json_data + "\t\t" + "{" + "\n" + "\t\t\t" + '"{#PPORT}":"' + str(
            net[0]) + "\",\n" + "\t\t\t" + '"{#PNAME}":"' + str(net[1]) + "\"},\n"
    else:
        json_data = json_data + "\t\t" + "{" + "\n" + "\t\t\t" + '"{#PPORT}":"' + str(
            net[0]) + "\",\n" + "\t\t\t" + '"{#PNAME}":"' + str(net[1]) + "\"}]}"

print json_data
