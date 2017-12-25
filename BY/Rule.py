import Data
class PeopleMove():
    def PeopleMove(p,direction):
        if direction==1:
            p.x=p.x-1
            p.y=p.y-1
        elif direction==2:
            p.x=p.x-1
        elif direction==3:
            p.x=p.x-1
            p.y=p.y+1
        elif direction==4:
            p.y=p.y-1
        elif direction==5:
            p.x=p.x
            p.y=p.y
        elif direction==6:
            p.y=p.y+1
        elif direction==7:
            p.x=p.x+1
            p.y=p.y-1
        elif direction==8:
            p.x=p.x+1
        elif direction==9:
            p.x=p.x+1
            p.y=p.y+1

def chickOverAround(p,allPeople):       #移除出系统
    if p.x==0 and (p.y>=0 and p.y<=4):
        # p.logo=Data.BasicData.LOGO_NULL
        allPeople.remove(p)
        a=[]