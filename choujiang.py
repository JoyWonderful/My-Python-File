from tkinter import *
import tkinter.messagebox as messagebox
import pygame
import random
import os
import sys
import time
import turtle as t
s = t.Screen()
 
class MyApp(Frame):
 
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()
 
    def createWidgets(self):
        t.setup(width=250, height=250, startx=None, starty=None)
        self.helloLabel = Label(self,text="开始抽奖啦!快来抽奖!")
        self.helloLabel.pack()
        self.quitButton = Button(self,text="开始抽奖",command=self.start)
        self.quitButton.pack()
        self.qButton = Button(self,text="说明",command=self.show)
        self.qButton.pack()
    
    def show(self):
        messagebox.showinfo("帮助","一切都是运气,谢谢...   再见——不，永不再见!")
        messagebox.showwarning("哈哈","好吧,还是给你帮助吧。")
        messagebox.showinfo("真正的说明（哈哈）","一等奖100元，二等奖30元，三等奖5元，感谢参与啥也没有。。。")
 
    def start(self):
        t.title("马上开始")
        t.hideturtle()
        t.write("3", align = "center", font = ("楷体",30,"normal"))
        time.sleep(1)
        t.undo()
        t.write("2", align = "center", font = ("楷体",30,"normal"))
        time.sleep(1)
        t.undo()
        t.write("1", align = "center", font = ("楷体",30,"normal"))
        time.sleep(1)
        t.undo()
        t.write("START", align = "center", font = ("楷体",30,"normal"))
        time.sleep(1)
        s.bye()
        self.choujiang()
 
    def choujiang(self):
        IMAGEDIR = 'pic'
        SUPPORTEXTS = ['jpg', 'png', 'bmp']
        SCREENSIZE = (550, 400)
        WHITE = (255, 255, 255, 27)
        GRAY = (192, 192, 192)
 
 
        def readImageRandomly():
            filenames = os.listdir(IMAGEDIR)
            filenames = [f for f in filenames if f.split('.')[-1] in SUPPORTEXTS]
            imgpath = os.path.join(IMAGEDIR, random.choice(filenames))
            return pygame.transform.scale(pygame.image.load(imgpath), SCREENSIZE)
 
 
        def main():
            pygame.init()
            pygame.mixer.init()
            pygame.mouse.set_cursor(*pygame.cursors.diamond)
            screen = pygame.display.set_mode(SCREENSIZE)
            pygame.display.set_caption("刮奖啦")
            surface = pygame.Surface(SCREENSIZE).convert_alpha()
            surface.fill(GRAY)
            image_used = readImageRandomly()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit(-1)
                mouse_event_flags = pygame.mouse.get_pressed()
                if mouse_event_flags[0]:
                    pygame.draw.circle(surface, WHITE, pygame.mouse.get_pos(), 40)
                elif mouse_event_flags[-1]:
                    surface.fill(GRAY)
                    image_used = readImageRandomly()
                screen.blit(image_used, (0, 0))
                screen.blit(surface, (0, 0))
                pygame.display.update()
 
        if __name__ == '__main__':
            main()
 
myapp = MyApp()
myapp.master.title("抽奖")
myapp.mainloop()

#制作:权家乐  想法提供:权家乐
#版权所有 侵权必究
