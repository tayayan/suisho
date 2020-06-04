#先手番局面のバックアップ用
import Bboard

b1a,b2a,b3a,b4a,b5a,b6a,b7a,b8a,b9a = '','','','','','','','',''
b1b,b2b,b3b,b4b,b5b,b6b,b7b,b8b,b9b = '','','','','','','','',''
b1c,b2c,b3c,b4c,b5c,b6c,b7c,b8c,b9c = '','','','','','','','',''
b1d,b2d,b3d,b4d,b5d,b6d,b7d,b8d,b9d = '','','','','','','','',''
b1e,b2e,b3e,b4e,b5e,b6e,b7e,b8e,b9e = '','','','','','','','',''
b1f,b2f,b3f,b4f,b5f,b6f,b7f,b8f,b9f = '','','','','','','','',''
b1g,b2g,b3g,b4g,b5g,b6g,b7g,b8g,b9g = 'P','P','P','P','P','P','P','P','P'
b1h,b2h,b3h,b4h,b5h,b6h,b7h,b8h,b9h = '','R','','','','','','B',''
b1i,b2i,b3i,b4i,b5i,b6i,b7i,b8i,b9i = 'L','N','S','G','','G','S','N','L'
P = 0
L = 0
N = 0
S = 0
G = 0
B = 0
R = 0
koma = ''

#現局面を記憶
def kioku():
    global b1a,b2a,b3a,b4a,b5a,b6a,b7a,b8a,b9a,\
           b1b,b2b,b3b,b4b,b5b,b6b,b7b,b8b,b9b,\
           b1c,b2c,b3c,b4c,b5c,b6c,b7c,b8c,b9c,\
           b1d,b2d,b3d,b4d,b5d,b6d,b7d,b8d,b9d,\
           b1e,b2e,b3e,b4e,b5e,b6e,b7e,b8e,b9e,\
           b1f,b2f,b3f,b4f,b5f,b6f,b7f,b8f,b9f,\
           b1g,b2g,b3g,b4g,b5g,b6g,b7g,b8g,b9g,\
           b1h,b2h,b3h,b4h,b5h,b6h,b7h,b8h,b9h,\
           b1i,b2i,b3i,b4i,b5i,b6i,b7i,b8i,b9i,\
           P,L,N,S,G,B,R,koma
    b1a,b2a,b3a,b4a,b5a,b6a,b7a,b8a,b9a = Bboard.b1a,Bboard.b2a,Bboard.b3a,Bboard.b4a,Bboard.b5a,Bboard.b6a,Bboard.b7a,Bboard.b8a,Bboard.b9a
    b1b,b2b,b3b,b4b,b5b,b6b,b7b,b8b,b9b = Bboard.b1b,Bboard.b2b,Bboard.b3b,Bboard.b4b,Bboard.b5b,Bboard.b6b,Bboard.b7b,Bboard.b8b,Bboard.b9b
    b1c,b2c,b3c,b4c,b5c,b6c,b7c,b8c,b9c = Bboard.b1c,Bboard.b2c,Bboard.b3c,Bboard.b4c,Bboard.b5c,Bboard.b6c,Bboard.b7c,Bboard.b8c,Bboard.b9c
    b1d,b2d,b3d,b4d,b5d,b6d,b7d,b8d,b9d = Bboard.b1d,Bboard.b2d,Bboard.b3d,Bboard.b4d,Bboard.b5d,Bboard.b6d,Bboard.b7d,Bboard.b8d,Bboard.b9d
    b1e,b2e,b3e,b4e,b5e,b6e,b7e,b8e,b9e = Bboard.b1e,Bboard.b2e,Bboard.b3e,Bboard.b4e,Bboard.b5e,Bboard.b6e,Bboard.b7e,Bboard.b8e,Bboard.b9e
    b1f,b2f,b3f,b4f,b5f,b6f,b7f,b8f,b9f = Bboard.b1f,Bboard.b2f,Bboard.b3f,Bboard.b4f,Bboard.b5f,Bboard.b6f,Bboard.b7f,Bboard.b8f,Bboard.b9f
    b1g,b2g,b3g,b4g,b5g,b6g,b7g,b8g,b9g = Bboard.b1g,Bboard.b2g,Bboard.b3g,Bboard.b4g,Bboard.b5g,Bboard.b6g,Bboard.b7g,Bboard.b8g,Bboard.b9g
    b1h,b2h,b3h,b4h,b5h,b6h,b7h,b8h,b9h = Bboard.b1h,Bboard.b2h,Bboard.b3h,Bboard.b4h,Bboard.b5h,Bboard.b6h,Bboard.b7h,Bboard.b8h,Bboard.b9h
    b1i,b2i,b3i,b4i,b5i,b6i,b7i,b8i,b9i = Bboard.b1i,Bboard.b2i,Bboard.b3i,Bboard.b4i,Bboard.b5i,Bboard.b6i,Bboard.b7i,Bboard.b8i,Bboard.b9i
    P = Bboard.P
    L = Bboard.L
    N = Bboard.N
    S = Bboard.S
    G = Bboard.G
    B = Bboard.B
    R = Bboard.R
    koma = Bboard.koma

#現局面を呼び出し
def yobidashi():
    global b1a,b2a,b3a,b4a,b5a,b6a,b7a,b8a,b9a,\
           b1b,b2b,b3b,b4b,b5b,b6b,b7b,b8b,b9b,\
           b1c,b2c,b3c,b4c,b5c,b6c,b7c,b8c,b9c,\
           b1d,b2d,b3d,b4d,b5d,b6d,b7d,b8d,b9d,\
           b1e,b2e,b3e,b4e,b5e,b6e,b7e,b8e,b9e,\
           b1f,b2f,b3f,b4f,b5f,b6f,b7f,b8f,b9f,\
           b1g,b2g,b3g,b4g,b5g,b6g,b7g,b8g,b9g,\
           b1h,b2h,b3h,b4h,b5h,b6h,b7h,b8h,b9h,\
           b1i,b2i,b3i,b4i,b5i,b6i,b7i,b8i,b9i,\
           P,L,N,S,G,B,R,koma
    Bboard.b1a,Bboard.b2a,Bboard.b3a,Bboard.b4a,Bboard.b5a,Bboard.b6a,Bboard.b7a,Bboard.b8a,Bboard.b9a = b1a,b2a,b3a,b4a,b5a,b6a,b7a,b8a,b9a
    Bboard.b1b,Bboard.b2b,Bboard.b3b,Bboard.b4b,Bboard.b5b,Bboard.b6b,Bboard.b7b,Bboard.b8b,Bboard.b9b = b1b,b2b,b3b,b4b,b5b,b6b,b7b,b8b,b9b
    Bboard.b1c,Bboard.b2c,Bboard.b3c,Bboard.b4c,Bboard.b5c,Bboard.b6c,Bboard.b7c,Bboard.b8c,Bboard.b9c = b1c,b2c,b3c,b4c,b5c,b6c,b7c,b8c,b9c 
    Bboard.b1d,Bboard.b2d,Bboard.b3d,Bboard.b4d,Bboard.b5d,Bboard.b6d,Bboard.b7d,Bboard.b8d,Bboard.b9d = b1d,b2d,b3d,b4d,b5d,b6d,b7d,b8d,b9d 
    Bboard.b1e,Bboard.b2e,Bboard.b3e,Bboard.b4e,Bboard.b5e,Bboard.b6e,Bboard.b7e,Bboard.b8e,Bboard.b9e = b1e,b2e,b3e,b4e,b5e,b6e,b7e,b8e,b9e
    Bboard.b1f,Bboard.b2f,Bboard.b3f,Bboard.b4f,Bboard.b5f,Bboard.b6f,Bboard.b7f,Bboard.b8f,Bboard.b9f = b1f,b2f,b3f,b4f,b5f,b6f,b7f,b8f,b9f 
    Bboard.b1g,Bboard.b2g,Bboard.b3g,Bboard.b4g,Bboard.b5g,Bboard.b6g,Bboard.b7g,Bboard.b8g,Bboard.b9g = b1g,b2g,b3g,b4g,b5g,b6g,b7g,b8g,b9g 
    Bboard.b1h,Bboard.b2h,Bboard.b3h,Bboard.b4h,Bboard.b5h,Bboard.b6h,Bboard.b7h,Bboard.b8h,Bboard.b9h = b1h,b2h,b3h,b4h,b5h,b6h,b7h,b8h,b9h 
    Bboard.b1i,Bboard.b2i,Bboard.b3i,Bboard.b4i,Bboard.b5i,Bboard.b6i,Bboard.b7i,Bboard.b8i,Bboard.b9i = b1i,b2i,b3i,b4i,b5i,b6i,b7i,b8i,b9i 
    Bboard.P = P
    Bboard.L = L
    Bboard.N = N
    Bboard.S = S
    Bboard.G = G
    Bboard.B = B
    Bboard.R = R
    Bboard.koma = koma
