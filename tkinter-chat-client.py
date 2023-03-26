import tkinter as tk
import tkinter.messagebox as msg
import socket
import time
import threading as th
root = tk.Tk()
sk = socket.socket()

def threadit(func,*args):
    t = th.Thread(target = func,args = args)
    t.setDaemon(True)
    t.start()

def connecting():
    def yes() :
        conadd = str(add.get())
        conport = int(port.get())
        threadit(connect,conadd,conport)
    connect_win = tk.Toplevel()
    tk.Label(connect_win,text = "请输入你想连接的IP地址:").pack(padx = 1,pady = 1)
    add = tk.Entry(connect_win)
    add.pack(padx = 1)
    tk.Label(connect_win,text = "请输入你想连接的端口号:").pack(padx = 1,pady = 1)
    port = tk.Entry(connect_win)
    port.pack(padx = 1)
    tk.Button(connect_win,text = "确定",command = yes).pack()

def connect(address,port):
    def send():
        sendstr = sendbox.get()
        sk.send(bytes(sendstr,"utf8"))
    con_win = tk.Toplevel()
    con_win.geometry("500x500")
    con_win.maxsize(1100,1150)
    con_win.minsize(400,350)
    con_win.title("通讯_客户端_"+address)

    info = tk.StringVar()
    show_info = tk.Label(con_win,textvariable = info,font = ("宋体",5,"normal"))
    show_info.pack(padx = 1,pady = 1,side = "bottom")

    info.set("为避免GUI界面卡死,已开启线程...")
    time.sleep(1.5)
    try:
        sk.connect((address,port))
    except Exception as e:
        msg.showerror(e,"请重试,发生了%s的错误"%(e))
    message = tk.Text(con_win)
    message.pack(padx = 1,pady = 1,fill = "both")
    sendbox = tk.Entry(con_win)
    sendbox.pack(padx = 1,pady = 1)
    tk.Button(con_win,bg = "green",fg = "white",text = "发送",command = send).pack(padx = 1,pady = 1)
    tk.Button(con_win,bg = "red",fg = "white",text = "断开连接").pack(padx = 1,pady = 1)
    
    while True:
        data = sk.recv(1024)
        message.insert("end",str(data,"utf8"))

tk.Label(root,text = "通讯-客户端",font = ("SimHei",30,"normal")).pack(padx = 1,pady = 1)
tk.Label(root,text = "注意:此程序为客户端。\n请先启动服务端,再启动此程序!",
                fg = "red",font = ("楷体",10,"normal")).pack()
tk.Button(root,text = "连接...",command = connecting).pack(padx = 1,pady = 2)

root.title("通讯-客户端_准备连接")
root.geometry("300x150")
root.mainloop()