import re
import random
import Bboard
import Wboard
import board
import oute
import Wkikimoves1
import Wmoves
import Wkikiboard

def culc():
    global kiki1
    Wboard.p,Wboard.l,Wboard.n,Wboard.s,Wboard.g,Wboard.b,Wboard.r=0,0,0,0,0,0,0
    Wkikimoves1.move1()
    Wkikiboard.shoki()
    for i in range(len(Wkikimoves1.depth1)):
        exec('Wkikiboard.k{} += 1'.format(Wkikimoves1.depth1[i][2:4]))
    kiki1=0
    kiki1=  Wkikiboard.k1a+Wkikiboard.k2a+Wkikiboard.k3a+Wkikiboard.k4a+Wkikiboard.k5a+Wkikiboard.k6a+Wkikiboard.k7a+Wkikiboard.k8a+Wkikiboard.k9a\
           +Wkikiboard.k1b+Wkikiboard.k2b+Wkikiboard.k3b+Wkikiboard.k4b+Wkikiboard.k5b+Wkikiboard.k6b+Wkikiboard.k7b+Wkikiboard.k8b+Wkikiboard.k9b\
           +Wkikiboard.k1c+Wkikiboard.k2c+Wkikiboard.k3c+Wkikiboard.k4c+Wkikiboard.k5c+Wkikiboard.k6c+Wkikiboard.k7c+Wkikiboard.k8c+Wkikiboard.k9c\
           +Wkikiboard.k1d+Wkikiboard.k2d+Wkikiboard.k3d+Wkikiboard.k4d+Wkikiboard.k5d+Wkikiboard.k6d+Wkikiboard.k7d+Wkikiboard.k8d+Wkikiboard.k9d\
           +Wkikiboard.k1e+Wkikiboard.k2e+Wkikiboard.k3e+Wkikiboard.k4e+Wkikiboard.k5e+Wkikiboard.k6e+Wkikiboard.k7e+Wkikiboard.k8e+Wkikiboard.k9e\
           +Wkikiboard.k1f+Wkikiboard.k2f+Wkikiboard.k3f+Wkikiboard.k4f+Wkikiboard.k5f+Wkikiboard.k6f+Wkikiboard.k7f+Wkikiboard.k8f+Wkikiboard.k9f\
           +Wkikiboard.k1g*5+Wkikiboard.k2g*5+Wkikiboard.k3g*5+Wkikiboard.k4g*5+Wkikiboard.k5g*5+Wkikiboard.k6g*5+Wkikiboard.k7g*5+Wkikiboard.k8g*5+Wkikiboard.k9g*5\
           +Wkikiboard.k1h*5+Wkikiboard.k2h*5+Wkikiboard.k3h*5+Wkikiboard.k4h*5+Wkikiboard.k5h*5+Wkikiboard.k6h*5+Wkikiboard.k7h*5+Wkikiboard.k8h*5+Wkikiboard.k9h*5\
           +Wkikiboard.k1i*5+Wkikiboard.k2i*5+Wkikiboard.k3i*5+Wkikiboard.k4i*5+Wkikiboard.k5i*5+Wkikiboard.k6i*5+Wkikiboard.k7i*5+Wkikiboard.k8i*5+Wkikiboard.k9i*5
