from tkinter import *
from math import *

#-------massive coordinates of object------#

#objectx=[0, 1, 0, -1]
#objecty=[1, 0, -1, 0]

#---------------********------------------#



#-------coordinates of circle object------#
objectx=[]
objecty=[]

numpoint=100
alpha0=2*3.14/numpoint
radius=0.03
for pcr in range(numpoint):
    alpha=alpha0*pcr
    objectx.append(radius*cos(alpha)+0.1)
    objecty.append(radius*sin(alpha)+0.1)
##
##radius=0.02
##for pcr in range(numpoint):
##    alpha=alpha0*pcr
##    objectx.append(radius*cos(alpha)+0.04)
##    objecty.append(radius*sin(alpha)+0.04)    
#------------------********----------------#



objectx=[]
objecty=[]
numberline=80
numberpoint=80
for ln in range(numberline):
    for point in range(numberpoint):
        #objectx.append((ln-10.2)/19)
        objectx.append((ln*4/numberline-2))
        objecty.append((point*4/numberpoint-2))
print(objectx)
print(objecty)




#-------double lense------#

##lensposx=[0.2, -0.2]
##lensposy=[0.01, 0.01]

#--------********---------#

#-------single lense------#

lensposx=[0.001]
lensposy=[0]
   
#--------********---------#





#---------------------------------------------------------Calculation angle of deflaction----------------------------------------------#


def mvec(x, y):                       #modul of vector  
    return (x**2 + y**2)**0.5   

def theta(m, p):                      #function of deflection angle
    return -0.01*m/p

vsumx=0.0
vsumy=0.0


vecsumx=[]
vecsumy=[]

for objects in range(len(objectx)):
    for lens in range(len(lensposx)):
        if lens==1:
            m=4
        else: m=2
        vecx=(lensposx[lens]-objectx[objects])/mvec((lensposx[lens]-objectx[objects]),(lensposy[lens]-objecty[objects]))*theta(m, mvec((lensposx[lens]-objectx[objects]),(lensposy[lens]-objecty[objects])))
        vecy=(lensposy[lens]-objecty[objects])/mvec((lensposx[lens]-objectx[objects]),(lensposy[lens]-objecty[objects]))*theta(m, mvec((lensposx[lens]-objectx[objects]),(lensposy[lens]-objecty[objects])))

        vsumx=vsumx+vecx
        vsumy=vsumy+vecy


    vecsumx.append(vsumx+objectx[objects])
    vecsumy.append(vsumy+objecty[objects])
    vsumx=0.0
    vsumy=0.0
#---------------------------------------------------------*********************************---------------------------------------------#

#----------------------------setcollor----------------------
##    colormarker=[]
##    colormarker2=[]
##    color0=16
##    coldist=256/(len(objectx)+16)
##    for col in range(len(objectx)):
##        color0+=coldist
##        new0=hex(int(color0))
##        colormarker.append("#"+new0[2:]+"00ff")
##        colormarker2.append("#ff"+new0[2:]+"00")
##        
#------------------------***************-------------------




#---------------------------------------------------------DRAWING----------------------------------------------#

    

size=800                                                        #size canvas
root = Tk()                                                     #create window
canvas = Canvas(root, bg="black", width=size, height=size)      #create canvas
canvas.pack()                                                   #to place canvas into window



zoom=220                                                        #mashtab                                             

#-------------------------------------Drawing image---------------------------------------#

for image in range(len(vecsumx)):
    d=10
    x0=vecsumx[image]*zoom+size/2
    y0=vecsumy[image]*zoom+size/2
    #colm=(colormarker[image])
    colm='red'
    canvas.create_oval(x0, y0, x0+d/2, y0+d/2, fill=colm)        #draw ellips
    root.update()
#-------------------------------------Drawing lenses--------------------------------------#
for lens in range(len(lensposx)):
    d=8
    x0=lensposx[lens]*zoom+size/2
    y0=lensposy[lens]*zoom+size/2
    print(lensposx[lens])
    canvas.create_oval(x0, y0, x0+d/2, y0+d/2, fill="white")        #draw ellips
    root.update()

#-------------------------------------Drawing objects-------------------------------------#
for objects in range(len(objectx)):
    d=7
    x0=objectx[objects]*zoom+size/2
    y0=objecty[objects]*zoom+size/2
    #colm=(colormarker2[objects])
    colm='green'
    canvas.create_oval(x0, y0, x0+d/2, y0+d/2, fill=colm)        #draw ellips
    root.update()

#-----------------------------------********************************--------------------------------------------#    






#a=input()
