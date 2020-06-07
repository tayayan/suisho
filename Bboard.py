#先手番の局面
b1a,b2a,b3a,b4a,b5a,b6a,b7a,b8a,b9a = '','','','','','','','',''
b1b,b2b,b3b,b4b,b5b,b6b,b7b,b8b,b9b = '','','','','','','','',''
b1c,b2c,b3c,b4c,b5c,b6c,b7c,b8c,b9c = '','','','','','','','',''
b1d,b2d,b3d,b4d,b5d,b6d,b7d,b8d,b9d = '','','','','','','','',''
b1e,b2e,b3e,b4e,b5e,b6e,b7e,b8e,b9e = '','','','','','','','',''
b1f,b2f,b3f,b4f,b5f,b6f,b7f,b8f,b9f = '','','','','','','','',''
b1g,b2g,b3g,b4g,b5g,b6g,b7g,b8g,b9g = 'P','P','P','P','P','P','P','P','P'
b1h,b2h,b3h,b4h,b5h,b6h,b7h,b8h,b9h = '','R','','','','','','B',''
b1i,b2i,b3i,b4i,b5i,b6i,b7i,b8i,b9i = 'L','N','S','G','K','G','S','N','L'
P = 0
L = 0
N = 0
S = 0
G = 0
B = 0
R = 0
koma = ''

#初期配置
def shoki():
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
    b1a,b2a,b3a,b4a,b5a,b6a,b7a,b8a,b9a = '','','','','','','','',''
    b1b,b2b,b3b,b4b,b5b,b6b,b7b,b8b,b9b = '','','','','','','','',''
    b1c,b2c,b3c,b4c,b5c,b6c,b7c,b8c,b9c = '','','','','','','','',''
    b1d,b2d,b3d,b4d,b5d,b6d,b7d,b8d,b9d = '','','','','','','','',''
    b1e,b2e,b3e,b4e,b5e,b6e,b7e,b8e,b9e = '','','','','','','','',''
    b1f,b2f,b3f,b4f,b5f,b6f,b7f,b8f,b9f = '','','','','','','','',''
    b1g,b2g,b3g,b4g,b5g,b6g,b7g,b8g,b9g = 'P','P','P','P','P','P','P','P','P'
    b1h,b2h,b3h,b4h,b5h,b6h,b7h,b8h,b9h = '','R','','','','','','B',''
    b1i,b2i,b3i,b4i,b5i,b6i,b7i,b8i,b9i = 'L','N','S','G','K','G','S','N','L'
    P = 0
    L = 0
    N = 0
    S = 0
    G = 0
    B = 0
    R = 0
    koma = ''
