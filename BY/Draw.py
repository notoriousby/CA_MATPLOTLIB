import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
import numpy as np
import Data
import matplotlib.cm as cm

class Draw():
    def DrawPeople(self,P=[]):
        plt.clf()
        One_x=[]
        One_y=[]
        Two_x=[]
        Two_y=[]
        Three_x=[]
        Three_y=[]
        # North_x=[]
        # Northwest_x=[]
        # Northeast_x=[]
        # West_x=[]
        # East_x=[]
        # Southwest_x=[]
        # South_x=[]
        # Southeast_x=[]
        # North_y=[]
        # Northwest_y=[]
        # Northeast_y=[]
        # West_y=[]
        # East_y=[]
        # Southwest_y=[]
        # South_y=[]
        # Southeast_y=[]
        for p in P:
            if p.logo==Data.REASONABLE_PEOPLE:
                One_x.append(p.x)
                One_y.append(p.y)
            elif p.logo==Data.REASONABLE_PEOPLE:
                Two_x.append(p.x)
                Two_y.append(p.y)
            elif p.logo==Data.CROWD_PEOPLE:
                Three_x.append(p.x)
                Three_y.append(p.y)

        plt.subplot(1,1,1)#绘图板布局  不知道怎么取消这一行
        plt.scatter(One_x,One_y,c='k')
        plt.scatter(Two_x,Two_y,c='r')#绘制行人--散点图
        plt.scatter(Three_x,Three_y,c='b')

        draw.drawWallAndExit(self)#绘制墙壁和出口
        # plt.show()
        '''由于无法右上角关闭 加了个关闭按钮'''
        closeFig = plt.axes([0.8, 0.025, 0.1, 0.04])#关闭按钮
        closeFigbutton = Button(closeFig, 'close', hovercolor='0.5')#按钮样式
        closeFigbutton.on_clicked(draw.closeFigure)#按钮按下去的动作
        plt.pause(1)#暂停1s
    '''关闭按钮动作'''
    def closeFigure(event):
        plt.close()#将窗口关闭
        Data.flag=False#循环标记为Fasle

    def drawWallAndExit(self):
        '''墙壁为实线'''
        plt.plot([0,Data.ROOM_M],[0,0],'b-')# down
        plt.plot([0,Data.ROOM_M],[Data.ROOM_N,Data.ROOM_N],'b-')# up
        '''出口为虚线'''
        plt.plot([0,0],[0,Data.ROOM_N],'y--')#left and right
        plt.plot([Data.ROOM_M,Data.ROOM_M],[0,Data.ROOM_N],'y--')
        # plt.show()






