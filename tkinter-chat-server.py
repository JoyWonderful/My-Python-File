import tkinter as tk
import socket
import time
import threading as th
root = tk.Tk()
sk = socket.socket()

def threadit(func,*args) :
    t = th.Thread(target = func,args = args)
    t.setDaemon(True)
    t.start()

def bind() :
    def yes() :
        conadd = str(add.get())
        conport = int(port.get())
        threadit(connect,conadd,conport)
    bind_win = tk.Toplevel()
    tk.Label(bind_win,text = "请输入您想绑定的IP地址: ").pack(padx = 1,pady = 1)
    tk.Label(bind_win,text = "建议您始用127.0.0.1",font = ("SimHei",5,"normal"),fg = "dodgerblue").pack()
    add = tk.Entry(bind_win)
    add.pack(padx = 1,pady = 1)
    tk.Label(bind_win,text = "请输入您想绑定的端口号: ").pack(padx = 1,pady = 1)
    port = tk.Entry(bind_win)
    port.pack(padx = 1,pady = 1)
    tk.Button(bind_win,text = "确定",command = yes).pack()
    bind_win.title("通讯-服务器_绑定")

def connect(address,port) :
    def send():
        sendstr = sendbox.get()
        conn.send(bytes,(sendstr,"utf-8"))
    con_win = tk.Toplevel()
    con_win.geometry("500x500")
    con_win.maxsize(1100,1150)
    con_win.minsize(400,350)
    con_win.title("通讯-服务器_"+address)
    
    info = tk.StringVar()
    show_info = tk.Label(con_win,textvariable = info,font = ("宋体",5,"normal"))
    show_info.pack(side = "bottom",pady = 2)
    
    info.set("为了避免GUI界面卡死,己开启线程。")
    time.sleep(1.5)
    sk.bind((address,port))
    sk.listen(5)
    info.set("等待连接...")
    
    sk.accept()
    info.set("对方己连接，准备环境...")
    
    message = tk.Text(con_win)
    message.pack(padx = 1,pady = 1,fill = "both")
    sendbox = tk.Entry(con_win)
    sendbox.pack(padx = 1,pady = 1)
    tk.Button(con_win,bg = "green",fg = "white",text = "发送",command = send).pack(padx = 1,pady = 1)
    tk.Button(con_win,bg = "red",fg = "white",text = "断开连接").pack(padx = 1,pady = 1)
    while True:
        conn,addr = sk.accept()
        info.set("连接至"+addr)
        while True:
            data = conn.recv(1024)
            if not data :
                info.set("退出连接")
                time.sleep(1.5)
                conn.close()
                break
        message.insert("end",str(data,"utf8"))
    

tk.Label(root,text = "通讯-服务器",font = ("SimHei",30,"normal")).pack(padx = 1,pady = 2)
tk.Label(root,text = "请注意：您使用的是服务器。\n请先绑定IP地址,然后打开客户端联接。",
                fg = "red",font = ("楷体",10,"normal")).pack(padx = 1,pady = 2)
tk.Button(root,text = "绑定...",command = bind).pack(padx = 1,pady = 1)

root.title("通讯-服务器_等待绑定")
root.geometry("300x150")
root.mainloop()