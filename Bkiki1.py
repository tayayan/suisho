import re
import random
import Bboard
import Wboard
import board
import oute
import Bkikimoves1
import Wmoves
import Bkikiboard

def culc():
    global kiki1
    Bboard.P,Bboard.L,Bboard.N,Bboard.S,Bboard.G,Bboard.B,Bboard.R=0,0,0,0,0,0,0
    Bkikimoves1.move1()
    Bkikiboard.shoki()
    for i in range(len(Bkikimoves1.depth1)):
        exec('Bkikiboard.k{} += 1'.format(Bkikimoves1.depth1[i][2:4]))
    kiki1=0
    kiki1=  Bkikiboard.k1a*2+Bkikiboard.k2a*2+Bkikiboard.k3a*2+Bkikiboard.k4a*2+Bkikiboard.k5a*2+Bkikiboard.k6a*2+Bkikiboard.k7a*2+Bkikiboard.k8a*2+Bkikiboard.k9a*2\
           +Bkikiboard.k1b*2+Bkikiboard.k2b*2+Bkikiboard.k3b*2+Bkikiboard.k4b*2+Bkikiboard.k5b*2+Bkikiboard.k6b*2+Bkikiboard.k7b*2+Bkikiboard.k8b*2+Bkikiboard.k9b*2\
           +Bkikiboard.k1c*2+Bkikiboard.k2c*2+Bkikiboard.k3c*2+Bkikiboard.k4c*2+Bkikiboard.k5c*2+Bkikiboard.k6c*2+Bkikiboard.k7c*2+Bkikiboard.k8c*2+Bkikiboard.k9c*2\
           +Bkikiboard.k1d+Bkikiboard.k2d+Bkikiboard.k3d+Bkikiboard.k4d+Bkikiboard.k5d+Bkikiboard.k6d+Bkikiboard.k7d+Bkikiboard.k8d+Bkikiboard.k9d\
           +Bkikiboard.k1e+Bkikiboard.k2e+Bkikiboard.k3e+Bkikiboard.k4e+Bkikiboard.k5e+Bkikiboard.k6e+Bkikiboard.k7e+Bkikiboard.k8e+Bkikiboard.k9e\
           +Bkikiboard.k1f+Bkikiboard.k2f+Bkikiboard.k3f+Bkikiboard.k4f+Bkikiboard.k5f+Bkikiboard.k6f+Bkikiboard.k7f+Bkikiboard.k8f+Bkikiboard.k9f\
           +Bkikiboard.k1g+Bkikiboard.k2g+Bkikiboard.k3g+Bkikiboard.k4g+Bkikiboard.k5g+Bkikiboard.k6g+Bkikiboard.k7g+Bkikiboard.k8g+Bkikiboard.k9g\
           +Bkikiboard.k1h+Bkikiboard.k2h+Bkikiboard.k3h+Bkikiboard.k4h+Bkikiboard.k5h+Bkikiboard.k6h+Bkikiboard.k7h+Bkikiboard.k8h+Bkikiboard.k9h\
           +Bkikiboard.k1i+Bkikiboard.k2i+Bkikiboard.k3i+Bkikiboard.k4i+Bkikiboard.k5i+Bkikiboard.k6i+Bkikiboard.k7i+Bkikiboard.k8i+Bkikiboard.k9i
