# import requests 
# import numpy as np 
# from pandas import DataFrame, Series
# import json


# url = 'https://www.dongqiudi.com/player/50025255.html'
# r = requests.get(url + '1')
# s = Series(r.json())
# data = DataFrame(columns = s.index)
# for i in range(100000):
#     r = requests.get(url + str(i + 1))
#     if r.json():
#         sp = Series(r.json())
#         sp['read_card'] = ' '
#         data.loc[i] = sp.values
#         print(i, '    ', data.loc[i]['name']) 
# data.to_csv("球员.csv")


from bs4 import BeautifulSoup
import numpy 
import requests
t = open("/Users/zhuhaoze/Desktop/球员.txt", "w")
url = 'http://www.niumou.com.cn/detail/308.html'
html = requests.get(url=url)
soup = BeautifulSoup(html.text, 'lxml')
a = soup.find_all('tr', align = 'center')
for i in range(len(a)):
    if i != 0 and i != 1:
        number = a[i].contents[0].string
        name = a[i].contents[1].string
        date = a[i].contents[3].string
        pos = a[i].contents[6].string
        nation = a[i].contents[7].string
        print(number, name, date, pos, nation)
        if number != None and number != 'None' and name != None and date != None and pos != None and nation != None:
            s = "INSERT INTO 球员 VALUES('巴塞罗那'" + "," + number + ",'" + name + "','" + date + "','" + nation + "','" + pos + "');"
            t.write(s)
            t.write('\n')





# #将txt文件逐行变成插入数据库的语句
# f = open("/Users/zhuhaoze/Desktop/Poems.txt", "r")
# t = open("/Users/zhuhaoze/Desktop/参赛.txt", "w")
# line = f.readline()
# while line:
#     temp = line.replace(' ', "','")
#     temp1 = "INSERT INTO 参赛 VALUES('"+ temp + "');"
#     t.write(temp1)
#     t.write('\n')
#     line = f.readline()