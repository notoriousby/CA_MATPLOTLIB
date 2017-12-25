import Block,Data
import random
class InitPeoples():
    def creatPeople(self):
        allBlock=[]#用于存放格子
        allPeople=[]#用于存放行人
        for i in range(1,Data.ROOM_M):
            for j in range(1,Data.ROOM_N):
                b=Block.Block(1)
                b.x=i
                b.y=j
                allBlock.append(b)
        '''随机排序'''
        random.shuffle(allBlock)
        '''取前N个'''
        '''可有效防止无限产生随机数'''
        allPeople=allBlock[:100]
        return allPeople

    def creatForemostPeo(self):
        allPeople=[]
        b1 = Block.Block(1)
        typenumber=random.random()
        if typenumber>=0.5:
            b1.type=1
        else:
            b1.type=2
        b1.x = 10
        b1.y = 10
        allPeople.append(b1)

    def creatWall(self):
        allWall=[]
        for i in range(19):
            D=[i,19]
            U=[i,0]
            L=[0,i]
            R=[19,i]
            allWall.append(D)
            allWall.append(U)
            allWall.append(L)
            allWall.append(R)
        return allWall

    '''产生出口'''
    def creatExit(self):
        allExit=[]
        for i in range(8,12):
            E=[0,i]
            allExit.append(E)
        return allExit

