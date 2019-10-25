from tkinter import *

# -------massive coordinates of object------#

# objectx=[0, 1, 0, -1]
# objecty=[1, 0, -1, 0]

# ---------------********------------------#


# -------coordinates of circle object------#
# objectx=[]
# objecty=[]
#
# numpoint=100
# alpha0=2*3.14/numpoint
# radius=0.3
# for pcr in range(numpoint):
#    alpha=alpha0*pcr
#    objectx.append(radius*cos(alpha)-0.4)
#    objecty.append(radius*sin(alpha)+0.4)
#
# radius=0.02
# for pcr in range(numpoint):
#    alpha=alpha0*pcr
#    objectx.append(radius*cos(alpha)+0.04)
#    objecty.append(radius*sin(alpha)+0.04)
# ------------------********----------------#


objectx = []
objecty = []
numberline = 30
numberpoint = 180
for ln in range(numberline):
    for point in range(numberpoint):
        # objectx.append((ln-10.2)/19)
        objectx.append((ln * 4 / numberline - 2))
        objecty.append((point * 4 / numberpoint - 2))
print(objectx)
print(objecty)

# -------double lense------#

# lensposx=[0.2, -0.2]
# lensposy=[0.01, 0.01]

# --------********---------#

# -------single lense------#

lensposx = [0.001]
lensposy = [0]


# --------********---------#


# -------- Calculation angle of deflection  -------------------#


def mvec(x, y):  # module of vector
    return (x ** 2 + y ** 2) ** 0.5


def theta(m, p):  # function of deflection angle
    return (1 / 2 + (1 / 4 + 1 / (p ** 2)) ** 0.5) * p


def theta2(m, p):  # function of deflection angle
    return -(-1 / 2 + (1 / 4 + 1 / (p ** 2)) ** 0.5) * p


vsumx = 0.0
vsumy = 0.0

vsumx2 = 0.0
vsumy2 = 0.0

vecsumx = []
vecsumy = []

vecsumx2 = []
vecsumy2 = []

for objects in range(len(objectx)):
    for lens in range(len(lensposx)):
        if lens == 1:
            m = 1
        else:
            m = 1
        vecx = (lensposx[lens] - objectx[objects]) / mvec((lensposx[lens] - objectx[objects]),
                                                          (lensposy[lens] - objecty[objects])) * theta(m, mvec(
            (lensposx[lens] - objectx[objects]), (lensposy[lens] - objecty[objects])))
        vecy = (lensposy[lens] - objecty[objects]) / mvec((lensposx[lens] - objectx[objects]),
                                                          (lensposy[lens] - objecty[objects])) * theta(m, mvec(
            (lensposx[lens] - objectx[objects]), (lensposy[lens] - objecty[objects])))

        vecx2 = (lensposx[lens] - objectx[objects]) / mvec((lensposx[lens] - objectx[objects]),
                                                           (lensposy[lens] - objecty[objects])) * theta2(m, mvec(
            (lensposx[lens] - objectx[objects]), (lensposy[lens] - objecty[objects])))
        vecy2 = (lensposy[lens] - objecty[objects]) / mvec((lensposx[lens] - objectx[objects]),
                                                           (lensposy[lens] - objecty[objects])) * theta2(m, mvec(
            (lensposx[lens] - objectx[objects]), (lensposy[lens] - objecty[objects])))

        vsumx = vsumx + vecx
        vsumy = vsumy + vecy

        vsumx2 = vsumx2 + vecx2
        vsumy2 = vsumy2 + vecy2

    vecsumx.append(vsumx + objectx[objects])
    vecsumy.append(vsumy + objecty[objects])

    vecsumx2.append(vsumx2 + objectx[objects])
    vecsumy2.append(vsumy2 + objecty[objects])

    vsumx = 0.0
    vsumy = 0.0

    vsumx2 = 0.0
    vsumy2 = 0.0
# ---------------------------------------------------------*********************************---------------------------------------------#

# ----------------------------setcollor----------------------
#    colormarker=[]
#    colormarker2=[]
#    color0=16
#    coldist=256/(len(objectx)+16)
#    for col in range(len(objectx)):
#        color0+=coldist
#        new0=hex(int(color0))
#        colormarker.append("#"+new0[2:]+"00ff")
#        colormarker2.append("#ff"+new0[2:]+"00")
#
# ------------------------***************-------------------


# ---------------------------------------------------------DRAWING----------------------------------------------#


size = 800  # size canvas
root = Tk()  # create window
canvas = Canvas(root, bg="black", width=size, height=size)  # create canvas
canvas.pack()  # to place canvas into window

zoom = 120  # mashtab

# -------------------------------------Drawing image---------------------------------------#

for image in range(len(vecsumx)):
    d = 9
    x0 = vecsumx[image] * zoom + size / 2
    y0 = vecsumy[image] * zoom + size / 2
    # colm = (colormarker[image])
    colm = 'red'
    canvas.create_oval(x0, y0, x0 + d / 2, y0 + d / 2, fill=colm)  # draw ellips
    root.update()

# -------------------------------------Drawing image---------------------------------------#

for image in range(len(vecsumx)):
    d = 9
    x0 = vecsumx2[image] * zoom + size / 2
    y0 = vecsumy2[image] * zoom + size / 2
    # colm=(colormarker[image])
    colm = 'blue'
    canvas.create_oval(x0, y0, x0 + d / 2, y0 + d / 2, fill=colm)  # draw ellips
    root.update()
# -------------------------------------Drawing lenses--------------------------------------#
for lens in range(len(lensposx)):
    d = 30
    x0 = lensposx[lens] * zoom + size / 2
    y0 = lensposy[lens] * zoom + size / 2
    print(lensposx[lens])
    canvas.create_oval(x0, y0, x0 + d / 2, y0 + d / 2, fill="white")  # draw ellips
    root.update()

# -------------------------------------Drawing objects-------------------------------------#
for objects in range(len(objectx)):
    d = 9
    x0 = objectx[objects] * zoom + size / 2
    y0 = objecty[objects] * zoom + size / 2
    # colm=(colormarker2[objects])
    colm = 'green'
    # canvas.create_oval(x0, y0, x0+d/2, y0+d/2, fill=colm)        #draw ellips
    root.update()

# -----------------------------------********************************--------------------------------------------#


# a = input()
