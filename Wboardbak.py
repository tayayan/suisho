#後手番局面のバックアップ用
import Wboard

w1a,w2a,w3a,w4a,w5a,w6a,w7a,w8a,w9a = 'K','','s','g','k','g','s','n','l'
w1b,w2b,w3b,w4b,w5b,w6b,w7b,w8b,w9b = '','n','','','','','','r',''
w1c,w2c,w3c,w4c,w5c,w6c,w7c,w8c,w9c = 'p','p','','p','p','p','p','p','p'
w1d,w2d,w3d,w4d,w5d,w6d,w7d,w8d,w9d = '','','','','','','','',''
w1e,w2e,w3e,w4e,w5e,w6e,w7e,w8e,w9e = '','','','','b','','','',''
w1f,w2f,w3f,w4f,w5f,w6f,w7f,w8f,w9f = '','','','','','','','',''
w1g,w2g,w3g,w4g,w5g,w6g,w7g,w8g,w9g = '','','','','','','','',''
w1h,w2h,w3h,w4h,w5h,w6h,w7h,w8h,w9h = '','','','','','','','',''
w1i,w2i,w3i,w4i,w5i,w6i,w7i,w8i,w9i = '','','','','','','','',''
p = 0
l = 0
n = 0
s = 0
g = 0
b = 0
r = 0
koma =''

#現局面を記憶
def kioku():
    global w1a,w2a,w3a,w4a,w5a,w6a,w7a,w8a,w9a,\
           w1b,w2b,w3b,w4b,w5b,w6b,w7b,w8b,w9b,\
           w1c,w2c,w3c,w4c,w5c,w6c,w7c,w8c,w9c,\
           w1d,w2d,w3d,w4d,w5d,w6d,w7d,w8d,w9d,\
           w1e,w2e,w3e,w4e,w5e,w6e,w7e,w8e,w9e,\
           w1f,w2f,w3f,w4f,w5f,w6f,w7f,w8f,w9f,\
           w1g,w2g,w3g,w4g,w5g,w6g,w7g,w8g,w9g,\
           w1h,w2h,w3h,w4h,w5h,w6h,w7h,w8h,w9h,\
           w1i,w2i,w3i,w4i,w5i,w6i,w7i,w8i,w9i,\
           p,l,n,s,g,b,r,koma
    w1a,w2a,w3a,w4a,w5a,w6a,w7a,w8a,w9a = Wboard.w1a,Wboard.w2a,Wboard.w3a,Wboard.w4a,Wboard.w5a,Wboard.w6a,Wboard.w7a,Wboard.w8a,Wboard.w9a
    w1b,w2b,w3b,w4b,w5b,w6b,w7b,w8b,w9b = Wboard.w1b,Wboard.w2b,Wboard.w3b,Wboard.w4b,Wboard.w5b,Wboard.w6b,Wboard.w7b,Wboard.w8b,Wboard.w9b
    w1c,w2c,w3c,w4c,w5c,w6c,w7c,w8c,w9c = Wboard.w1c,Wboard.w2c,Wboard.w3c,Wboard.w4c,Wboard.w5c,Wboard.w6c,Wboard.w7c,Wboard.w8c,Wboard.w9c
    w1d,w2d,w3d,w4d,w5d,w6d,w7d,w8d,w9d = Wboard.w1d,Wboard.w2d,Wboard.w3d,Wboard.w4d,Wboard.w5d,Wboard.w6d,Wboard.w7d,Wboard.w8d,Wboard.w9d
    w1e,w2e,w3e,w4e,w5e,w6e,w7e,w8e,w9e = Wboard.w1e,Wboard.w2e,Wboard.w3e,Wboard.w4e,Wboard.w5e,Wboard.w6e,Wboard.w7e,Wboard.w8e,Wboard.w9e
    w1f,w2f,w3f,w4f,w5f,w6f,w7f,w8f,w9f = Wboard.w1f,Wboard.w2f,Wboard.w3f,Wboard.w4f,Wboard.w5f,Wboard.w6f,Wboard.w7f,Wboard.w8f,Wboard.w9f
    w1g,w2g,w3g,w4g,w5g,w6g,w7g,w8g,w9g = Wboard.w1g,Wboard.w2g,Wboard.w3g,Wboard.w4g,Wboard.w5g,Wboard.w6g,Wboard.w7g,Wboard.w8g,Wboard.w9g
    w1h,w2h,w3h,w4h,w5h,w6h,w7h,w8h,w9h = Wboard.w1h,Wboard.w2h,Wboard.w3h,Wboard.w4h,Wboard.w5h,Wboard.w6h,Wboard.w7h,Wboard.w8h,Wboard.w9h
    w1i,w2i,w3i,w4i,w5i,w6i,w7i,w8i,w9i = Wboard.w1i,Wboard.w2i,Wboard.w3i,Wboard.w4i,Wboard.w5i,Wboard.w6i,Wboard.w7i,Wboard.w8i,Wboard.w9i
    p = Wboard.p
    l = Wboard.l
    n = Wboard.n
    s = Wboard.s
    g = Wboard.g
    b = Wboard.b
    r = Wboard.r
    koma = Wboard.koma

#現局面を呼び出し
def yobidashi():
    global w1a,w2a,w3a,w4a,w5a,w6a,w7a,w8a,w9a,\
           w1b,w2b,w3b,w4b,w5b,w6b,w7b,w8b,w9b,\
           w1c,w2c,w3c,w4c,w5c,w6c,w7c,w8c,w9c,\
           w1d,w2d,w3d,w4d,w5d,w6d,w7d,w8d,w9d,\
           w1e,w2e,w3e,w4e,w5e,w6e,w7e,w8e,w9e,\
           w1f,w2f,w3f,w4f,w5f,w6f,w7f,w8f,w9f,\
           w1g,w2g,w3g,w4g,w5g,w6g,w7g,w8g,w9g,\
           w1h,w2h,w3h,w4h,w5h,w6h,w7h,w8h,w9h,\
           w1i,w2i,w3i,w4i,w5i,w6i,w7i,w8i,w9i,\
           p,l,n,s,g,b,r,koma
    Wboard.w1a,Wboard.w2a,Wboard.w3a,Wboard.w4a,Wboard.w5a,Wboard.w6a,Wboard.w7a,Wboard.w8a,Wboard.w9a = w1a,w2a,w3a,w4a,w5a,w6a,w7a,w8a,w9a
    Wboard.w1b,Wboard.w2b,Wboard.w3b,Wboard.w4b,Wboard.w5b,Wboard.w6b,Wboard.w7b,Wboard.w8b,Wboard.w9b = w1b,w2b,w3b,w4b,w5b,w6b,w7b,w8b,w9b
    Wboard.w1c,Wboard.w2c,Wboard.w3c,Wboard.w4c,Wboard.w5c,Wboard.w6c,Wboard.w7c,Wboard.w8c,Wboard.w9c = w1c,w2c,w3c,w4c,w5c,w6c,w7c,w8c,w9c 
    Wboard.w1d,Wboard.w2d,Wboard.w3d,Wboard.w4d,Wboard.w5d,Wboard.w6d,Wboard.w7d,Wboard.w8d,Wboard.w9d = w1d,w2d,w3d,w4d,w5d,w6d,w7d,w8d,w9d 
    Wboard.w1e,Wboard.w2e,Wboard.w3e,Wboard.w4e,Wboard.w5e,Wboard.w6e,Wboard.w7e,Wboard.w8e,Wboard.w9e = w1e,w2e,w3e,w4e,w5e,w6e,w7e,w8e,w9e
    Wboard.w1f,Wboard.w2f,Wboard.w3f,Wboard.w4f,Wboard.w5f,Wboard.w6f,Wboard.w7f,Wboard.w8f,Wboard.w9f = w1f,w2f,w3f,w4f,w5f,w6f,w7f,w8f,w9f 
    Wboard.w1g,Wboard.w2g,Wboard.w3g,Wboard.w4g,Wboard.w5g,Wboard.w6g,Wboard.w7g,Wboard.w8g,Wboard.w9g = w1g,w2g,w3g,w4g,w5g,w6g,w7g,w8g,w9g 
    Wboard.w1h,Wboard.w2h,Wboard.w3h,Wboard.w4h,Wboard.w5h,Wboard.w6h,Wboard.w7h,Wboard.w8h,Wboard.w9h = w1h,w2h,w3h,w4h,w5h,w6h,w7h,w8h,w9h 
    Wboard.w1i,Wboard.w2i,Wboard.w3i,Wboard.w4i,Wboard.w5i,Wboard.w6i,Wboard.w7i,Wboard.w8i,Wboard.w9i = w1i,w2i,w3i,w4i,w5i,w6i,w7i,w8i,w9i 
    Wboard.p = p
    Wboard.l = l
    Wboard.n = n
    Wboard.s = s
    Wboard.g = g
    Wboard.b = b
    Wboard.r = r
    Wboard.koma = koma
