import re
import random
import Bboard
import Wboard
import board
import oute
import Bkikimoves2
import Wmoves
import Bkikiboard

def culc():
    global kiki2,kikilist1,kikilist2
    Bboard.P,Bboard.L,Bboard.N,Bboard.S,Bboard.G,Bboard.B,Bboard.R=0,0,0,0,0,0,0
    Bkikimoves2.move1()
    Bkikiboard.shoki()
    for i in range(len(Bkikimoves2.depth1)):
        exec('Bkikiboard.k{} += 1'.format(Bkikimoves2.depth1[i][2:4]))
    kikilist1 =[]
    kikilist2 =[]
    kikilist1 = [Bkikiboard.k1a,Bkikiboard.k2a,Bkikiboard.k3a,Bkikiboard.k4a,Bkikiboard.k5a,Bkikiboard.k6a,Bkikiboard.k7a,Bkikiboard.k8a,Bkikiboard.k9a,\
                 Bkikiboard.k1b,Bkikiboard.k2b,Bkikiboard.k3b,Bkikiboard.k4b,Bkikiboard.k5b,Bkikiboard.k6b,Bkikiboard.k7b,Bkikiboard.k8b,Bkikiboard.k9b,\
                 Bkikiboard.k1c,Bkikiboard.k2c,Bkikiboard.k3c,Bkikiboard.k4c,Bkikiboard.k5c,Bkikiboard.k6c,Bkikiboard.k7c,Bkikiboard.k8c,Bkikiboard.k9c,\
                 Bkikiboard.k1d,Bkikiboard.k2d,Bkikiboard.k3d,Bkikiboard.k4d,Bkikiboard.k5d,Bkikiboard.k6d,Bkikiboard.k7d,Bkikiboard.k8d,Bkikiboard.k9d,\
                 Bkikiboard.k1e,Bkikiboard.k2e,Bkikiboard.k3e,Bkikiboard.k4e,Bkikiboard.k5e,Bkikiboard.k6e,Bkikiboard.k7e,Bkikiboard.k8e,Bkikiboard.k9e,\
                 Bkikiboard.k1f,Bkikiboard.k2f,Bkikiboard.k3f,Bkikiboard.k4f,Bkikiboard.k5f,Bkikiboard.k6f,Bkikiboard.k7f,Bkikiboard.k8f,Bkikiboard.k9f,\
                 Bkikiboard.k1g,Bkikiboard.k2g,Bkikiboard.k3g,Bkikiboard.k4g,Bkikiboard.k5g,Bkikiboard.k6g,Bkikiboard.k7g,Bkikiboard.k8g,Bkikiboard.k9g,\
                 Bkikiboard.k1h,Bkikiboard.k2h,Bkikiboard.k3h,Bkikiboard.k4h,Bkikiboard.k5h,Bkikiboard.k6h,Bkikiboard.k7h,Bkikiboard.k8h,Bkikiboard.k9h,\
                 Bkikiboard.k1i,Bkikiboard.k2i,Bkikiboard.k3i,Bkikiboard.k4i,Bkikiboard.k5i,Bkikiboard.k6i,Bkikiboard.k7i,Bkikiboard.k8i,Bkikiboard.k9i]

    kikilist2 = [Bboard.b1a,Bboard.b2a,Bboard.b3a,Bboard.b4a,Bboard.b5a,Bboard.b6a,Bboard.b7a,Bboard.b8a,Bboard.b9a,\
                 Bboard.b1b,Bboard.b2b,Bboard.b3b,Bboard.b4b,Bboard.b5b,Bboard.b6b,Bboard.b7b,Bboard.b8b,Bboard.b9b,\
                 Bboard.b1c,Bboard.b2c,Bboard.b3c,Bboard.b4c,Bboard.b5c,Bboard.b6c,Bboard.b7c,Bboard.b8c,Bboard.b9c,\
                 Bboard.b1d,Bboard.b2d,Bboard.b3d,Bboard.b4d,Bboard.b5d,Bboard.b6d,Bboard.b7d,Bboard.b8d,Bboard.b9d,\
                 Bboard.b1e,Bboard.b2e,Bboard.b3e,Bboard.b4e,Bboard.b5e,Bboard.b6e,Bboard.b7e,Bboard.b8e,Bboard.b9e,\
                 Bboard.b1f,Bboard.b2f,Bboard.b3f,Bboard.b4f,Bboard.b5f,Bboard.b6f,Bboard.b7f,Bboard.b8f,Bboard.b9f,\
                 Bboard.b1g,Bboard.b2g,Bboard.b3g,Bboard.b4g,Bboard.b5g,Bboard.b6g,Bboard.b7g,Bboard.b8g,Bboard.b9g,\
                 Bboard.b1h,Bboard.b2h,Bboard.b3h,Bboard.b4h,Bboard.b5h,Bboard.b6h,Bboard.b7h,Bboard.b8h,Bboard.b9h,\
                 Bboard.b1i,Bboard.b2i,Bboard.b3i,Bboard.b4i,Bboard.b5i,Bboard.b6i,Bboard.b7i,Bboard.b8i,Bboard.b9i]
    kiki2 = 0
    for j in range(len(kikilist1)):
        if kikilist2[j] != '':
            kiki2 += kikilist1[j]
