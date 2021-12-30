from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
from datetime import datetime


db = pymysql.connect(host = "localhost", user = "root", 
                     password = "dudu!20010521!", database = "football", port = 3306, autocommit = True)
#创建游标对象
cursor = db.cursor()
  
def searchperson():
    otherFrame = Toplevel()
    otherFrame.geometry("1400x600+200+200")
    otherFrame.title("查询球员")
    handler = lambda:onCloseOtherFrame(otherFrame)
    btn = ttk.Button(otherFrame, text = '返回', command = handler)
    btn.pack(side = 'bottom', anchor = 'ne')
    l1 = Label(otherFrame, text = '请输入球队名称', font=('Arial', 18)).pack()
    e1 = StringVar()
    Entry(otherFrame, show='', textvariable = e1, font=('Arial', 14)).pack()
    l2 = Label(otherFrame, text = '请输入国家名称', font=('Arial', 18)).pack()
    e2 = StringVar()
    Entry(otherFrame, show='', textvariable = e2, font=('Arial', 14)).pack()
    l3 = Label(otherFrame, text = '请输入球员姓名', font=('Arial', 18)).pack()
    e3 = StringVar()
    Entry(otherFrame, show='', textvariable = e3, font=('Arial', 14)).pack()
    click = lambda:f(otherFrame, e1, e2, e3)
    s = ttk.Button(otherFrame, text = '查询', command = click).pack(side = 'bottom')
   


def f(otherFrame, e1, e2, e3):
    team = e1.get()
    country = e2.get()
    name = e3.get()
    tree = ttk.Treeview(otherFrame)
    ls = ["球队名称", "号码", "姓名", "出生日期", "国籍", "位置", "所属足协"]
    tree["columns"] = ("球队名称", "号码", "姓名", "出生日期", "国籍", "位置", "所属足协")
    tree.column("号码", width = 100)
    tree.column("国籍", width = 100)
    tree.column("所属足协", width = 100)
    for i in ls:
        tree.column(i, anchor = "center")
        tree.heading(i, text = i)  
    temp = 'select * from INFO '
    if team != '' and country != '' and name != '':
        temp = temp + "where 球队名称 = '" + str(team) + "' and 姓名 = '" + str(name) + "' and 国籍 = '" + str(country) + "';"
    elif team != '' and country != '':
        temp = temp + "where 球队名称 = '" + str(team) + "' and 国籍 = '" + str(country) + "';"
    elif team != '' and name != '':
        temp = temp + "where 球队名称 = '" + str(team) + "' and 姓名 = '" + str(name) + "';"
    elif country != '' and name != '':
        temp = temp + "where 姓名 = '" + str(name) + "' and 国籍 = '" + str(country) + "';"
    elif name != '':
        temp = temp + "where 姓名 = '" + str(name) + "';"
    elif team != '':
        temp = temp + "where 球队名称 = '" + str(team) + "';"
    elif country != '':
        temp = temp + "where 国籍 = '" + str(country) + "';"
    else:
        l = Label(OtherFrame, text = '查 询 失 败',  font = ('Arial', 30), width = 30, height = 2)
        l.pack()
        return
    cursor.execute(temp)
    result = cursor.fetchall()
    for i in range(len(result)):
        tree.insert("", i, values = result[i])
    tree['show'] = 'headings'
    tree.pack(anchor = "center")
    


def searchteam():
    otherFrame = Toplevel()
    otherFrame.geometry("1100x600+200+200")
    otherFrame.title("查询球队")
    handler = lambda:onCloseOtherFrame(otherFrame)
    Text(otherFrame, width=300, height=200, font=("微软雅黑", 50), )
    btn = ttk.Button(otherFrame, text = '返回', command = handler)
    btn.pack(side = 'bottom', anchor = 'ne')
    l1 = Label(otherFrame, text = '请输入球队名称', font=('Arial', 18)).pack()
    e1 = StringVar()
    Entry(otherFrame, show='', textvariable = e1, font=('Arial', 14)).pack()
    click = lambda:f1(otherFrame, e1)
    s = ttk.Button(otherFrame, text = '查询', command = click).pack(side = 'bottom')
    



def f1(otherFrame, e1):
    team = e1.get()
    temp = "select * from 球队 where 球队名称 = '" + team + "';"
    cursor.execute(temp)
    result = cursor.fetchall()
    tree = ttk.Treeview(otherFrame)
    ls = ["球队所属地", "球队名称", "所属足协", "主场", "成立日期", "教练", "进球数"]
    tree["columns"] = ("球队所属地", "球队名称", "所属足协", "主场", "成立日期", "教练", "进球数")
    for i in ls:
        tree.column(i, anchor = "center", width = 150)
        tree.heading(i, text = i)  
    for i in range(len(result)):
        tree.insert("", i, values = result[i])
    tree['show'] = 'headings'
    tree.pack(anchor = "center")
    if len(result) != 0:
        l1 = Label(otherFrame, text = '请输入进球数', font=('Arial', 18)).pack()
        e = StringVar()
        Entry(otherFrame, show='', textvariable = e, font=('Arial', 14)).pack()
        click = lambda:f2(otherFrame, e, team)
        s = ttk.Button(otherFrame, text = '更新', command = click).pack(side = 'bottom')
        
        
def f2(otherFrame, e, team):
    num = e.get()
    try:
        sql = "call update_score(" + num + ", " + "'" + team + "');"
        cursor.execute(sql)
        win = messagebox.showinfo(message='更新成功！')
    except Exception as m:
        win = messagebox.showerror('警告', m.args)
    
    
    

def changedata():
    otherFrame = Toplevel()
    otherFrame.geometry("600x700+200+200")
    otherFrame.title("修改球员")
    handler = lambda:onCloseOtherFrame(otherFrame)
    Text(otherFrame, width=300, height=200, font=("微软雅黑", 50), )
    btn = ttk.Button(otherFrame, text = "返回", command = handler)
    btn.pack(side = 'bottom', anchor = 'ne')
    l1 = Label(otherFrame, text = '请输入球队名称', font=('Arial', 18)).pack()
    e1 = StringVar()
    Entry(otherFrame, show='', textvariable = e1, font=('Arial', 14)).pack()
    l2 = Label(otherFrame, text = '请输入号码', font=('Arial', 18)).pack()
    e2 = StringVar()
    Entry(otherFrame, show='', textvariable = e2, font=('Arial', 14)).pack()
    l3 = Label(otherFrame, text = '请输入球员姓名', font=('Arial', 18)).pack()
    e3 = StringVar()
    Entry(otherFrame, show='', textvariable = e3, font=('Arial', 14)).pack()
    l4 = Label(otherFrame, text = '请输入出生日期', font=('Arial', 18)).pack()
    e4 = StringVar()
    Entry(otherFrame, show='', textvariable = e4, font=('Arial', 14)).pack()
    l5 = Label(otherFrame, text = '请输入国籍', font=('Arial', 18)).pack()
    e5 = StringVar()
    Entry(otherFrame, show='', textvariable = e5, font=('Arial', 14)).pack()
    l6 = Label(otherFrame, text = '请输入位置', font=('Arial', 18)).pack()
    e6 = StringVar()
    Entry(otherFrame, show='', textvariable = e6, font=('Arial', 14)).pack()
    click = lambda:f3(otherFrame, e1, e2, e3, e4, e5, e6)
    s = ttk.Button(otherFrame, text = '插入', command = click).pack(side = 'bottom')



def f3(otherFrame, e1, e2, e3, e4, e5, e6):
    team = e1.get()
    num = e2.get()
    name = e3.get()
    date = e4.get()
    nation = e5.get()
    position = e6.get()
    sql = "INSERT INTO 球员 values('" + team + "', " + num + ", '" + name + "', '" + date + "', '" + nation + "', '" + position + "');"
    try:
        cursor.execute(sql)
        win = messagebox.showinfo(message='插入成功！')
    except Exception as m:
        win = messagebox.showerror('警告', m.args)


def delete():
    otherFrame = Toplevel()
    otherFrame.geometry("600x700+200+200")
    otherFrame.title("删除比赛")
    handler = lambda:onCloseOtherFrame(otherFrame)
    Text(otherFrame, width=300, height=200, font=("微软雅黑", 50), )
    btn = ttk.Button(otherFrame, text = '返回', command = handler)
    btn.pack(side = 'bottom', anchor = 'ne')
    l1 = Label(otherFrame, text = '请输入球队名称', font=('Arial', 18)).pack()
    e1 = StringVar()
    Entry(otherFrame, show='', textvariable = e1, font=('Arial', 14)).pack()
    l2 = Label(otherFrame, text = '请输入足协名称', font=('Arial', 18)).pack()
    e2 = StringVar()
    Entry(otherFrame, show='', textvariable = e2, font=('Arial', 14)).pack()
    click = lambda:f4(otherFrame, e1, e2)
    s = ttk.Button(otherFrame, text = '删除', command = click).pack(side = 'bottom')



def f4(otherFrame, e1, e2):
    team = e1.get()
    assic = e2.get()
    sql = "DELETE FROM 参赛 WHERE 球队名称 = '" + team + "' and 比赛名称 = (SELECT 比赛名称 from 比赛 where 所属足协 = '" + assic + "');"  
    tree = ttk.Treeview(otherFrame)
    ls = ["球队名称", "比赛名称"]
    tree["columns"] = ("球队名称", "比赛名称")
    for i in ls:
        tree.column(i, anchor = "center")
        tree.heading(i, text = i)  
    temp = "SELECT * FROM 参赛 WHERE 球队名称 = '" + team + "' and 比赛名称 = (SELECT 比赛名称 from 比赛 where 所属足协 = '" + assic + "');"  
    cursor.execute(temp)
    result = cursor.fetchall()
    for i in range(len(result)):
        tree.insert("", i, values = result[i])
    tree['show'] = 'headings'
    tree.pack(anchor = "center")
    click = lambda:f5(otherFrame, sql)
    s = ttk.Button(otherFrame, text = '取消', command = click).pack(side = 'bottom')
    click = lambda:f6(otherFrame, sql)
    s = ttk.Button(otherFrame, text = '确定', command = click).pack(side = 'bottom')

def f5(otherFrame, sql):
    cursor.execute("START TRANSACTION")
    cursor.execute(sql)
    cursor.execute("ROLLBACK")
    win = messagebox.showinfo(message = '已取消')


def f6(otherFrame, sql):
    cursor.execute("START TRANSACTION")
    cursor.execute(sql)
    cursor.execute("COMMIT")
    win = messagebox.showinfo(message = '已删除')



def onCloseOtherFrame(otherFrame):
    """"""
    otherFrame.destroy()
    show()
 
def show():
    """
    shows main frame
    """
    root.update()
    root.deiconify()
 
 
root = Tk()
root.geometry('400x300+200+200')

l = Label(root, text = '足 球 数 据 库 查 询 系 统',  font = ('Arial', 30), width = 30, height = 2)
l.pack()
 
 
ttk.Button(root, text = '查询球员', width=10, command = searchperson,).pack(anchor = 'center')
ttk.Button(root, text ='查询球队', width=10, command = searchteam,).pack(anchor = 'center')
ttk.Button(root, text = '添加球员', width=10, command = changedata,).pack(anchor = 'center')
ttk.Button(root, text = '删除比赛', width=10, command = delete,).pack(anchor = 'center')   

 
 
root.mainloop()
 
 

