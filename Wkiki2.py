import re
import random
import Bboard
import Wboard
import board
import oute
import Wkikimoves2
import Wmoves
import Wkikiboard

def culc():
    global kiki2,kikilist2,kikilist1
    Wboard.p,Wboard.l,Wboard.n,Wboard.s,Wboard.g,Wboard.b,Wboard.r=0,0,0,0,0,0,0
    Wkikimoves2.move1()
    Wkikiboard.shoki()
    for i in range(len(Wkikimoves2.depth1)):
        exec('Wkikiboard.k{} += 1'.format(Wkikimoves2.depth1[i][2:4]))

    kikilist1=[]
    kikilist2=[]
    kikilist1 = [Wkikiboard.k1a,Wkikiboard.k2a,Wkikiboard.k3a,Wkikiboard.k4a,Wkikiboard.k5a,Wkikiboard.k6a,Wkikiboard.k7a,Wkikiboard.k8a,Wkikiboard.k9a,\
                 Wkikiboard.k1b,Wkikiboard.k2b,Wkikiboard.k3b,Wkikiboard.k4b,Wkikiboard.k5b,Wkikiboard.k6b,Wkikiboard.k7b,Wkikiboard.k8b,Wkikiboard.k9b,\
                 Wkikiboard.k1c,Wkikiboard.k2c,Wkikiboard.k3c,Wkikiboard.k4c,Wkikiboard.k5c,Wkikiboard.k6c,Wkikiboard.k7c,Wkikiboard.k8c,Wkikiboard.k9c,\
                 Wkikiboard.k1d,Wkikiboard.k2d,Wkikiboard.k3d,Wkikiboard.k4d,Wkikiboard.k5d,Wkikiboard.k6d,Wkikiboard.k7d,Wkikiboard.k8d,Wkikiboard.k9d,\
                 Wkikiboard.k1e,Wkikiboard.k2e,Wkikiboard.k3e,Wkikiboard.k4e,Wkikiboard.k5e,Wkikiboard.k6e,Wkikiboard.k7e,Wkikiboard.k8e,Wkikiboard.k9e,\
                 Wkikiboard.k1f,Wkikiboard.k2f,Wkikiboard.k3f,Wkikiboard.k4f,Wkikiboard.k5f,Wkikiboard.k6f,Wkikiboard.k7f,Wkikiboard.k8f,Wkikiboard.k9f,\
                 Wkikiboard.k1g,Wkikiboard.k2g,Wkikiboard.k3g,Wkikiboard.k4g,Wkikiboard.k5g,Wkikiboard.k6g,Wkikiboard.k7g,Wkikiboard.k8g,Wkikiboard.k9g,\
                 Wkikiboard.k1h,Wkikiboard.k2h,Wkikiboard.k3h,Wkikiboard.k4h,Wkikiboard.k5h,Wkikiboard.k6h,Wkikiboard.k7h,Wkikiboard.k8h,Wkikiboard.k9h,\
                 Wkikiboard.k1i,Wkikiboard.k2i,Wkikiboard.k3i,Wkikiboard.k4i,Wkikiboard.k5i,Wkikiboard.k6i,Wkikiboard.k7i,Wkikiboard.k8i,Wkikiboard.k9i]

    kikilist2 = [Wboard.w1a,Wboard.w2a,Wboard.w3a,Wboard.w4a,Wboard.w5a,Wboard.w6a,Wboard.w7a,Wboard.w8a,Wboard.w9a,\
                 Wboard.w1b,Wboard.w2b,Wboard.w3b,Wboard.w4b,Wboard.w5b,Wboard.w6b,Wboard.w7b,Wboard.w8b,Wboard.w9b,\
                 Wboard.w1c,Wboard.w2c,Wboard.w3c,Wboard.w4c,Wboard.w5c,Wboard.w6c,Wboard.w7c,Wboard.w8c,Wboard.w9c,\
                 Wboard.w1d,Wboard.w2d,Wboard.w3d,Wboard.w4d,Wboard.w5d,Wboard.w6d,Wboard.w7d,Wboard.w8d,Wboard.w9d,\
                 Wboard.w1e,Wboard.w2e,Wboard.w3e,Wboard.w4e,Wboard.w5e,Wboard.w6e,Wboard.w7e,Wboard.w8e,Wboard.w9e,\
                 Wboard.w1f,Wboard.w2f,Wboard.w3f,Wboard.w4f,Wboard.w5f,Wboard.w6f,Wboard.w7f,Wboard.w8f,Wboard.w9f,\
                 Wboard.w1g,Wboard.w2g,Wboard.w3g,Wboard.w4g,Wboard.w5g,Wboard.w6g,Wboard.w7g,Wboard.w8g,Wboard.w9g,\
                 Wboard.w1h,Wboard.w2h,Wboard.w3h,Wboard.w4h,Wboard.w5h,Wboard.w6h,Wboard.w7h,Wboard.w8h,Wboard.w9h,\
                 Wboard.w1i,Wboard.w2i,Wboard.w3i,Wboard.w4i,Wboard.w5i,Wboard.w6i,Wboard.w7i,Wboard.w8i,Wboard.w9i]

    kiki2 = 0
    for j in range(len(kikilist1)):
        if kikilist2[j] != '':
            kiki2 += kikilist1[j]
