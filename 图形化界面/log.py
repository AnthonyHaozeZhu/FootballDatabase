import tkinter as tk
import pickle
import tkinter.messagebox
window = tk.Tk()
window.title('Welcome To Myapp!')
##窗口尺寸
window.geometry('450x300')
# welcome image
canvas = tk.Canvas(window, height=200, width=500)#创建画布
#image_file = tk.PhotoImage(file='welcome.gif')#加载图片文件
#image = canvas.create_image(0,0, anchor='nw', image=image_file)#将图片置于画布上
canvas.pack(side='top')#放置画布(为上端)
# user information
tk.Label(window, text='用户名: ').place(x=50, y= 150)#创建一个`label`名为`User name: `置于坐标(50,150)
tk.Label(window, text='密码: ').place(x=50, y= 190)
#用户名输入框
var_usr_name = tk.StringVar()#定义变量
var_usr_name.set('example@python.com')#变量赋值'example@python.com'
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)#创建一个`entry`，显示为变量`var_usr_name`即图中的`example@python.com`
entry_usr_name.place(x=160, y=150)
#密码输入框
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')#`show`这个参数将输入的密码变为`***`的形式
entry_usr_pwd.place(x=160, y=190)
#登录事件
def usr_login():
    ##这两行代码就是获取用户输入的`usr_name`和`usr_pwd`
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
##这里设置异常捕获，当我们第一次访问用户信息文件时是不存在的，所以这里设置异常捕获。
##中间的两行就是我们的匹配，即程序将输入的信息和文件中的信息匹配。
    try:
        with open('usrs_info.pickle', 'rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except EOFError:
 ##这里就是我们在没有读取到`usr_file`的时候，程序会创建一个`usr_file`这个文件，并将管理员
 ##的用户和密码写入，即用户名为`admin`密码为`admin`。
        with open('usrs_info.pickle', 'wb') as usr_file:
            usrs_info = {'admin': 'admin'}
            pickle.dump(usrs_info, usr_file)
#如果用户名和密码与文件中的匹配成功，则会登录成功，并跳出弹窗`how are you?`加上你的用户名。
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            tk.messagebox.showinfo(title='欢迎', message='你好' + usr_name)
    ##如果用户名匹配成功，而密码输入错误，则会弹出'Error, your password is wrong, try again.'
        else:
            tk.messagebox.showerror(message='错误，你的密码有问题，请重新输入')
    else:   # 如果发现用户名不存在
        is_sign_up = tk.messagebox.askyesno('Welcome',
                           '你还没有注册，现在注册？')
    # 提示需不需要注册新用户
    if is_sign_up:
        usr_sign_up()
#注册事件
def usr_sign_up():
    def sign_to_app():
         ##以下三行就是获取我们注册时所输入的信息
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()
         ##这里是打开我们记录数据的文件，将注册信息读出
        with open('usrs_info.pickle', 'rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)
 
        ##这里就是判断，如果两次密码输入不一致，则提示`'Error', 'Password and confirm password must be the same!'`
        if np != npf:
            tk.messagebox.showerror('Error', '两次密码输入不一致哦！')
 
        ##如果用户名已经在我们的数据文件中，则提示`'Error', 'The user has already signed up!'`
        elif nn in exist_usr_info:
            tk.messagebox.showerror('Error', '这个用户名已经注册了！')
 
        ##最后如果输入无以上错误，则将注册输入的信息记录到文件当中，并提示注册成功`'Welcome', 'You have successfully signed up!'`
        ##然后销毁窗口。
        else:
            exist_usr_info[nn] = np
            with open('usrs_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            tk.messagebox.showinfo('Welcome', '你成功注册了!')
            ##然后销毁窗口。
            window_sign_up.destroy()
 
    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('350x200')
    window_sign_up.title('用户注册')
    #新用户名
    new_name = tk.StringVar()#将输入的注册名赋值给变量
    new_name.set('example@python.com')#将最初显示定为'example@python.com'
    tk.Label(window_sign_up, text='用户名: ').place(x=10, y= 10)#将`User name:`放置在坐标(10,10)。
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)#创建一个注册名的`entry`，变量为`new_name`
    entry_new_name.place(x=150, y=10)#`entry`放置在坐标(150,10).
    #新密码
    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='密码: ').place(x=10, y=50)
    entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_usr_pwd.place(x=150, y=50)
    #防止密码填错
    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='重复密码: ').place(x=10, y= 90)
    entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_usr_pwd_confirm.place(x=150, y=90)
    # 下面的 sign_to_app 
    btn_comfirm_sign_up = tk.Button(window_sign_up, text='注册', command=sign_to_app)
    btn_comfirm_sign_up.place(x=150, y=130)
 
 
 
 
# 登录和注册按钮
btn_login = tk.Button(window, text='登录', command=usr_login)#定义一个`button`按钮，名为`Login`,触发命令为`usr_login`
btn_login.place(x=170, y=230)
btn_sign_up = tk.Button(window, text='注册', command=usr_sign_up)
btn_sign_up.place(x=270, y=230)
 
##显示出来
window.mainloop()


