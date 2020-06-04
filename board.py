#先手番局面と後手番局面を合成した盤面
import re
import Bboard
import Wboard

s1a,s2a,s3a,s4a,s5a,s6a,s7a,s8a,s9a = '','','','','','','','',''
s1b,s2b,s3b,s4b,s5b,s6b,s7b,s8b,s9b = '','','','','','','','',''
s1c,s2c,s3c,s4c,s5c,s6c,s7c,s8c,s9c = '','','','','','','','',''
s1d,s2d,s3d,s4d,s5d,s6d,s7d,s8d,s9d = '','','','','','','','',''
s1e,s2e,s3e,s4e,s5e,s6e,s7e,s8e,s9e = '','','','','','','','',''
s1f,s2f,s3f,s4f,s5f,s6f,s7f,s8f,s9f = '','','','','','','','',''
s1g,s2g,s3g,s4g,s5g,s6g,s7g,s8g,s9g = '','','','','','','','',''
s1h,s2h,s3h,s4h,s5h,s6h,s7h,s8h,s9h = '','','','','','','','',''
s1i,s2i,s3i,s4i,s5i,s6i,s7i,s8i,s9i = '','','','','','','','',''
P = 0
L = 0
N = 0
S = 0
G = 0
B = 0
R = 0
p = 0
l = 0
n = 0
s = 0
g = 0
b = 0
r = 0

#先手番局面と後手番局面を合成
def synth():
    global s1a,s2a,s3a,s4a,s5a,s6a,s7a,s8a,s9a,\
           s1b,s2b,s3b,s4b,s5b,s6b,s7b,s8b,s9b,\
           s1c,s2c,s3c,s4c,s5c,s6c,s7c,s8c,s9c,\
           s1d,s2d,s3d,s4d,s5d,s6d,s7d,s8d,s9d,\
           s1e,s2e,s3e,s4e,s5e,s6e,s7e,s8e,s9e,\
           s1f,s2f,s3f,s4f,s5f,s6f,s7f,s8f,s9f,\
           s1g,s2g,s3g,s4g,s5g,s6g,s7g,s8g,s9g,\
           s1h,s2h,s3h,s4h,s5h,s6h,s7h,s8h,s9h,\
           s1i,s2i,s3i,s4i,s5i,s6i,s7i,s8i,s9i,\
           P,L,N,S,G,B,R,p,l,n,s,g,b,r
    
    s1a,s2a,s3a,s4a,s5a,s6a,s7a,s8a,s9a = Bboard.b1a+Wboard.w1a,\
                                          Bboard.b2a+Wboard.w2a,\
                                          Bboard.b3a+Wboard.w3a,\
                                          Bboard.b4a+Wboard.w4a,\
                                          Bboard.b5a+Wboard.w5a,\
                                          Bboard.b6a+Wboard.w6a,\
                                          Bboard.b7a+Wboard.w7a,\
                                          Bboard.b8a+Wboard.w8a,\
                                          Bboard.b9a+Wboard.w9a
                             
    s1b,s2b,s3b,s4b,s5b,s6b,s7b,s8b,s9b = Bboard.b1b+Wboard.w1b,\
                                          Bboard.b2b+Wboard.w2b,\
                                          Bboard.b3b+Wboard.w3b,\
                                          Bboard.b4b+Wboard.w4b,\
                                          Bboard.b5b+Wboard.w5b,\
                                          Bboard.b6b+Wboard.w6b,\
                                          Bboard.b7b+Wboard.w7b,\
                                          Bboard.b8b+Wboard.w8b,\
                                          Bboard.b9b+Wboard.w9b
                                 
    s1c,s2c,s3c,s4c,s5c,s6c,s7c,s8c,s9c = Bboard.b1c+Wboard.w1c,\
                                          Bboard.b2c+Wboard.w2c,\
                                          Bboard.b3c+Wboard.w3c,\
                                          Bboard.b4c+Wboard.w4c,\
                                          Bboard.b5c+Wboard.w5c,\
                                          Bboard.b6c+Wboard.w6c,\
                                          Bboard.b7c+Wboard.w7c,\
                                          Bboard.b8c+Wboard.w8c,\
                                          Bboard.b9c+Wboard.w9c
                                 
    s1d,s2d,s3d,s4d,s5d,s6d,s7d,s8d,s9d = Bboard.b1d+Wboard.w1d,\
                                          Bboard.b2d+Wboard.w2d,\
                                          Bboard.b3d+Wboard.w3d,\
                                          Bboard.b4d+Wboard.w4d,\
                                          Bboard.b5d+Wboard.w5d,\
                                          Bboard.b6d+Wboard.w6d,\
                                          Bboard.b7d+Wboard.w7d,\
                                          Bboard.b8d+Wboard.w8d,\
                                          Bboard.b9d+Wboard.w9d
                                 
    s1e,s2e,s3e,s4e,s5e,s6e,s7e,s8e,s9e = Bboard.b1e+Wboard.w1e,\
                                          Bboard.b2e+Wboard.w2e,\
                                          Bboard.b3e+Wboard.w3e,\
                                          Bboard.b4e+Wboard.w4e,\
                                          Bboard.b5e+Wboard.w5e,\
                                          Bboard.b6e+Wboard.w6e,\
                                          Bboard.b7e+Wboard.w7e,\
                                          Bboard.b8e+Wboard.w8e,\
                                          Bboard.b9e+Wboard.w9e
                                 
    s1f,s2f,s3f,s4f,s5f,s6f,s7f,s8f,s9f = Bboard.b1f+Wboard.w1f,\
                                          Bboard.b2f+Wboard.w2f,\
                                          Bboard.b3f+Wboard.w3f,\
                                          Bboard.b4f+Wboard.w4f,\
                                          Bboard.b5f+Wboard.w5f,\
                                          Bboard.b6f+Wboard.w6f,\
                                          Bboard.b7f+Wboard.w7f,\
                                          Bboard.b8f+Wboard.w8f,\
                                          Bboard.b9f+Wboard.w9f
                                 
    s1g,s2g,s3g,s4g,s5g,s6g,s7g,s8g,s9g = Bboard.b1g+Wboard.w1g,\
                                          Bboard.b2g+Wboard.w2g,\
                                          Bboard.b3g+Wboard.w3g,\
                                          Bboard.b4g+Wboard.w4g,\
                                          Bboard.b5g+Wboard.w5g,\
                                          Bboard.b6g+Wboard.w6g,\
                                          Bboard.b7g+Wboard.w7g,\
                                          Bboard.b8g+Wboard.w8g,\
                                          Bboard.b9g+Wboard.w9g
                                 
    s1h,s2h,s3h,s4h,s5h,s6h,s7h,s8h,s9h = Bboard.b1h+Wboard.w1h,\
                                          Bboard.b2h+Wboard.w2h,\
                                          Bboard.b3h+Wboard.w3h,\
                                          Bboard.b4h+Wboard.w4h,\
                                          Bboard.b5h+Wboard.w5h,\
                                          Bboard.b6h+Wboard.w6h,\
                                          Bboard.b7h+Wboard.w7h,\
                                          Bboard.b8h+Wboard.w8h,\
                                          Bboard.b9h+Wboard.w9h
                                          
    s1i,s2i,s3i,s4i,s5i,s6i,s7i,s8i,s9i = Bboard.b1i+Wboard.w1i,\
                                          Bboard.b2i+Wboard.w2i,\
                                          Bboard.b3i+Wboard.w3i,\
                                          Bboard.b4i+Wboard.w4i,\
                                          Bboard.b5i+Wboard.w5i,\
                                          Bboard.b6i+Wboard.w6i,\
                                          Bboard.b7i+Wboard.w7i,\
                                          Bboard.b8i+Wboard.w8i,\
                                          Bboard.b9i+Wboard.w9i
                                 
    P = Bboard.P
    L = Bboard.L
    N = Bboard.N
    S = Bboard.S
    G = Bboard.G
    B = Bboard.B
    R = Bboard.R
    p = Wboard.p
    l = Wboard.l
    n = Wboard.n
    s = Wboard.s
    g = Wboard.g
    b = Wboard.b
    r = Wboard.r

#縦の線対称局面を生成
def mirror():
    global s1a,s2a,s3a,s4a,s5a,s6a,s7a,s8a,s9a,\
           s1b,s2b,s3b,s4b,s5b,s6b,s7b,s8b,s9b,\
           s1c,s2c,s3c,s4c,s5c,s6c,s7c,s8c,s9c,\
           s1d,s2d,s3d,s4d,s5d,s6d,s7d,s8d,s9d,\
           s1e,s2e,s3e,s4e,s5e,s6e,s7e,s8e,s9e,\
           s1f,s2f,s3f,s4f,s5f,s6f,s7f,s8f,s9f,\
           s1g,s2g,s3g,s4g,s5g,s6g,s7g,s8g,s9g,\
           s1h,s2h,s3h,s4h,s5h,s6h,s7h,s8h,s9h,\
           s1i,s2i,s3i,s4i,s5i,s6i,s7i,s8i,s9i,\
           P,L,N,S,G,B,R,p,l,n,s,g,b,r
    
    s1a,s2a,s3a,s4a,s5a,s6a,s7a,s8a,s9a = Bboard.b9a+Wboard.w9a,\
                                          Bboard.b8a+Wboard.w8a,\
                                          Bboard.b7a+Wboard.w7a,\
                                          Bboard.b6a+Wboard.w6a,\
                                          Bboard.b5a+Wboard.w5a,\
                                          Bboard.b4a+Wboard.w4a,\
                                          Bboard.b3a+Wboard.w3a,\
                                          Bboard.b2a+Wboard.w2a,\
                                          Bboard.b1a+Wboard.w1a
                             
    s1b,s2b,s3b,s4b,s5b,s6b,s7b,s8b,s9b = Bboard.b9b+Wboard.w9b,\
                                          Bboard.b8b+Wboard.w8b,\
                                          Bboard.b7b+Wboard.w7b,\
                                          Bboard.b6b+Wboard.w6b,\
                                          Bboard.b5b+Wboard.w5b,\
                                          Bboard.b4b+Wboard.w4b,\
                                          Bboard.b3b+Wboard.w3b,\
                                          Bboard.b2b+Wboard.w2b,\
                                          Bboard.b1b+Wboard.w1b
                                 
    s1c,s2c,s3c,s4c,s5c,s6c,s7c,s8c,s9c = Bboard.b9c+Wboard.w9c,\
                                          Bboard.b8c+Wboard.w8c,\
                                          Bboard.b7c+Wboard.w7c,\
                                          Bboard.b6c+Wboard.w6c,\
                                          Bboard.b5c+Wboard.w5c,\
                                          Bboard.b4c+Wboard.w4c,\
                                          Bboard.b3c+Wboard.w3c,\
                                          Bboard.b2c+Wboard.w2c,\
                                          Bboard.b1c+Wboard.w1c
                                 
    s1d,s2d,s3d,s4d,s5d,s6d,s7d,s8d,s9d = Bboard.b9d+Wboard.w9d,\
                                          Bboard.b8d+Wboard.w8d,\
                                          Bboard.b7d+Wboard.w7d,\
                                          Bboard.b6d+Wboard.w6d,\
                                          Bboard.b5d+Wboard.w5d,\
                                          Bboard.b4d+Wboard.w4d,\
                                          Bboard.b3d+Wboard.w3d,\
                                          Bboard.b2d+Wboard.w2d,\
                                          Bboard.b1d+Wboard.w1d
                                 
    s1e,s2e,s3e,s4e,s5e,s6e,s7e,s8e,s9e = Bboard.b9e+Wboard.w9e,\
                                          Bboard.b8e+Wboard.w8e,\
                                          Bboard.b7e+Wboard.w7e,\
                                          Bboard.b6e+Wboard.w6e,\
                                          Bboard.b5e+Wboard.w5e,\
                                          Bboard.b4e+Wboard.w4e,\
                                          Bboard.b3e+Wboard.w3e,\
                                          Bboard.b2e+Wboard.w2e,\
                                          Bboard.b1e+Wboard.w1e
                                 
    s1f,s2f,s3f,s4f,s5f,s6f,s7f,s8f,s9f = Bboard.b9f+Wboard.w9f,\
                                          Bboard.b8f+Wboard.w8f,\
                                          Bboard.b7f+Wboard.w7f,\
                                          Bboard.b6f+Wboard.w6f,\
                                          Bboard.b5f+Wboard.w5f,\
                                          Bboard.b4f+Wboard.w4f,\
                                          Bboard.b3f+Wboard.w3f,\
                                          Bboard.b2f+Wboard.w2f,\
                                          Bboard.b1f+Wboard.w1f
                                 
    s1g,s2g,s3g,s4g,s5g,s6g,s7g,s8g,s9g = Bboard.b9g+Wboard.w9g,\
                                          Bboard.b8g+Wboard.w8g,\
                                          Bboard.b7g+Wboard.w7g,\
                                          Bboard.b6g+Wboard.w6g,\
                                          Bboard.b5g+Wboard.w5g,\
                                          Bboard.b4g+Wboard.w4g,\
                                          Bboard.b3g+Wboard.w3g,\
                                          Bboard.b2g+Wboard.w2g,\
                                          Bboard.b1g+Wboard.w1g
                                 
    s1h,s2h,s3h,s4h,s5h,s6h,s7h,s8h,s9h = Bboard.b9h+Wboard.w9h,\
                                          Bboard.b8h+Wboard.w8h,\
                                          Bboard.b7h+Wboard.w7h,\
                                          Bboard.b6h+Wboard.w6h,\
                                          Bboard.b5h+Wboard.w5h,\
                                          Bboard.b4h+Wboard.w4h,\
                                          Bboard.b3h+Wboard.w3h,\
                                          Bboard.b2h+Wboard.w2h,\
                                          Bboard.b1h+Wboard.w1h
                                          
    s1i,s2i,s3i,s4i,s5i,s6i,s7i,s8i,s9i = Bboard.b9i+Wboard.w9i,\
                                          Bboard.b8i+Wboard.w8i,\
                                          Bboard.b7i+Wboard.w7i,\
                                          Bboard.b6i+Wboard.w6i,\
                                          Bboard.b5i+Wboard.w5i,\
                                          Bboard.b4i+Wboard.w4i,\
                                          Bboard.b3i+Wboard.w3i,\
                                          Bboard.b2i+Wboard.w2i,\
                                          Bboard.b1i+Wboard.w1i
                                 
    P = Bboard.P
    L = Bboard.L
    N = Bboard.N
    S = Bboard.S
    G = Bboard.G
    B = Bboard.B
    R = Bboard.R
    p = Wboard.p
    l = Wboard.l
    n = Wboard.n
    s = Wboard.s
    g = Wboard.g
    b = Wboard.b
    r = Wboard.r


#点対称局面（先後入替局面）を生成
def rotate():
    global s1a,s2a,s3a,s4a,s5a,s6a,s7a,s8a,s9a,\
           s1b,s2b,s3b,s4b,s5b,s6b,s7b,s8b,s9b,\
           s1c,s2c,s3c,s4c,s5c,s6c,s7c,s8c,s9c,\
           s1d,s2d,s3d,s4d,s5d,s6d,s7d,s8d,s9d,\
           s1e,s2e,s3e,s4e,s5e,s6e,s7e,s8e,s9e,\
           s1f,s2f,s3f,s4f,s5f,s6f,s7f,s8f,s9f,\
           s1g,s2g,s3g,s4g,s5g,s6g,s7g,s8g,s9g,\
           s1h,s2h,s3h,s4h,s5h,s6h,s7h,s8h,s9h,\
           s1i,s2i,s3i,s4i,s5i,s6i,s7i,s8i,s9i,\
           P,L,N,S,G,B,R,p,l,n,s,g,b,r
    
    s1a,s2a,s3a,s4a,s5a,s6a,s7a,s8a,s9a = Bboard.b9i.lower()+Wboard.w9i.upper(),\
                                          Bboard.b8i.lower()+Wboard.w8i.upper(),\
                                          Bboard.b7i.lower()+Wboard.w7i.upper(),\
                                          Bboard.b6i.lower()+Wboard.w6i.upper(),\
                                          Bboard.b5i.lower()+Wboard.w5i.upper(),\
                                          Bboard.b4i.lower()+Wboard.w4i.upper(),\
                                          Bboard.b3i.lower()+Wboard.w3i.upper(),\
                                          Bboard.b2i.lower()+Wboard.w2i.upper(),\
                                          Bboard.b1i.lower()+Wboard.w1i.upper()
                             
    s1b,s2b,s3b,s4b,s5b,s6b,s7b,s8b,s9b = Bboard.b9h.lower()+Wboard.w9h.upper(),\
                                          Bboard.b8h.lower()+Wboard.w8h.upper(),\
                                          Bboard.b7h.lower()+Wboard.w7h.upper(),\
                                          Bboard.b6h.lower()+Wboard.w6h.upper(),\
                                          Bboard.b5h.lower()+Wboard.w5h.upper(),\
                                          Bboard.b4h.lower()+Wboard.w4h.upper(),\
                                          Bboard.b3h.lower()+Wboard.w3h.upper(),\
                                          Bboard.b2h.lower()+Wboard.w2h.upper(),\
                                          Bboard.b1h.lower()+Wboard.w1h.upper()
                                
    s1c,s2c,s3c,s4c,s5c,s6c,s7c,s8c,s9c = Bboard.b9g.lower()+Wboard.w9g.upper(),\
                                          Bboard.b8g.lower()+Wboard.w8g.upper(),\
                                          Bboard.b7g.lower()+Wboard.w7g.upper(),\
                                          Bboard.b6g.lower()+Wboard.w6g.upper(),\
                                          Bboard.b5g.lower()+Wboard.w5g.upper(),\
                                          Bboard.b4g.lower()+Wboard.w4g.upper(),\
                                          Bboard.b3g.lower()+Wboard.w3g.upper(),\
                                          Bboard.b2g.lower()+Wboard.w2g.upper(),\
                                          Bboard.b1g.lower()+Wboard.w1g.upper()
                                 
    s1d,s2d,s3d,s4d,s5d,s6d,s7d,s8d,s9d = Bboard.b9f.lower()+Wboard.w9f.upper(),\
                                          Bboard.b8f.lower()+Wboard.w8f.upper(),\
                                          Bboard.b7f.lower()+Wboard.w7f.upper(),\
                                          Bboard.b6f.lower()+Wboard.w6f.upper(),\
                                          Bboard.b5f.lower()+Wboard.w5f.upper(),\
                                          Bboard.b4f.lower()+Wboard.w4f.upper(),\
                                          Bboard.b3f.lower()+Wboard.w3f.upper(),\
                                          Bboard.b2f.lower()+Wboard.w2f.upper(),\
                                          Bboard.b1f.lower()+Wboard.w1f.upper()
                                 
    s1e,s2e,s3e,s4e,s5e,s6e,s7e,s8e,s9e = Bboard.b9e.lower()+Wboard.w9e.upper(),\
                                          Bboard.b8e.lower()+Wboard.w8e.upper(),\
                                          Bboard.b7e.lower()+Wboard.w7e.upper(),\
                                          Bboard.b6e.lower()+Wboard.w6e.upper(),\
                                          Bboard.b5e.lower()+Wboard.w5e.upper(),\
                                          Bboard.b4e.lower()+Wboard.w4e.upper(),\
                                          Bboard.b3e.lower()+Wboard.w3e.upper(),\
                                          Bboard.b2e.lower()+Wboard.w2e.upper(),\
                                          Bboard.b1e.lower()+Wboard.w1e.upper()
                                 
    s1f,s2f,s3f,s4f,s5f,s6f,s7f,s8f,s9f = Bboard.b9d.lower()+Wboard.w9d.upper(),\
                                          Bboard.b8d.lower()+Wboard.w8d.upper(),\
                                          Bboard.b7d.lower()+Wboard.w7d.upper(),\
                                          Bboard.b6d.lower()+Wboard.w6d.upper(),\
                                          Bboard.b5d.lower()+Wboard.w5d.upper(),\
                                          Bboard.b4d.lower()+Wboard.w4d.upper(),\
                                          Bboard.b3d.lower()+Wboard.w3d.upper(),\
                                          Bboard.b2d.lower()+Wboard.w2d.upper(),\
                                          Bboard.b1d.lower()+Wboard.w1d.upper()
                                 
    s1g,s2g,s3g,s4g,s5g,s6g,s7g,s8g,s9g = Bboard.b9c.lower()+Wboard.w9c.upper(),\
                                          Bboard.b8c.lower()+Wboard.w8c.upper(),\
                                          Bboard.b7c.lower()+Wboard.w7c.upper(),\
                                          Bboard.b6c.lower()+Wboard.w6c.upper(),\
                                          Bboard.b5c.lower()+Wboard.w5c.upper(),\
                                          Bboard.b4c.lower()+Wboard.w4c.upper(),\
                                          Bboard.b3c.lower()+Wboard.w3c.upper(),\
                                          Bboard.b2c.lower()+Wboard.w2c.upper(),\
                                          Bboard.b1c.lower()+Wboard.w1c.upper()
                                 
    s1h,s2h,s3h,s4h,s5h,s6h,s7h,s8h,s9h = Bboard.b9b.lower()+Wboard.w9b.upper(),\
                                          Bboard.b8b.lower()+Wboard.w8b.upper(),\
                                          Bboard.b7b.lower()+Wboard.w7b.upper(),\
                                          Bboard.b6b.lower()+Wboard.w6b.upper(),\
                                          Bboard.b5b.lower()+Wboard.w5b.upper(),\
                                          Bboard.b4b.lower()+Wboard.w4b.upper(),\
                                          Bboard.b3b.lower()+Wboard.w3b.upper(),\
                                          Bboard.b2b.lower()+Wboard.w2b.upper(),\
                                          Bboard.b1b.lower()+Wboard.w1b.upper()
                                    
    s1i,s2i,s3i,s4i,s5i,s6i,s7i,s8i,s9i = Bboard.b9a.lower()+Wboard.w9a.upper(),\
                                          Bboard.b8a.lower()+Wboard.w8a.upper(),\
                                          Bboard.b7a.lower()+Wboard.w7a.upper(),\
                                          Bboard.b6a.lower()+Wboard.w6a.upper(),\
                                          Bboard.b5a.lower()+Wboard.w5a.upper(),\
                                          Bboard.b4a.lower()+Wboard.w4a.upper(),\
                                          Bboard.b3a.lower()+Wboard.w3a.upper(),\
                                          Bboard.b2a.lower()+Wboard.w2a.upper(),\
                                          Bboard.b1a.lower()+Wboard.w1a.upper()
                                 
    P = Wboard.p
    L = Wboard.l
    N = Wboard.n
    S = Wboard.s
    G = Wboard.g
    B = Wboard.b
    R = Wboard.r
    p = Bboard.P
    l = Bboard.L
    n = Bboard.N
    s = Bboard.S
    g = Bboard.G
    b = Bboard.B
    r = Bboard.R

#先手後手入替局面の縦線対称局面を生成
def romirror():
    global s1a,s2a,s3a,s4a,s5a,s6a,s7a,s8a,s9a,\
           s1b,s2b,s3b,s4b,s5b,s6b,s7b,s8b,s9b,\
           s1c,s2c,s3c,s4c,s5c,s6c,s7c,s8c,s9c,\
           s1d,s2d,s3d,s4d,s5d,s6d,s7d,s8d,s9d,\
           s1e,s2e,s3e,s4e,s5e,s6e,s7e,s8e,s9e,\
           s1f,s2f,s3f,s4f,s5f,s6f,s7f,s8f,s9f,\
           s1g,s2g,s3g,s4g,s5g,s6g,s7g,s8g,s9g,\
           s1h,s2h,s3h,s4h,s5h,s6h,s7h,s8h,s9h,\
           s1i,s2i,s3i,s4i,s5i,s6i,s7i,s8i,s9i,\
           P,L,N,S,G,B,R,p,l,n,s,g,b,r
    
    s1a,s2a,s3a,s4a,s5a,s6a,s7a,s8a,s9a = Bboard.b1i.lower()+Wboard.w1i.upper(),\
                                          Bboard.b2i.lower()+Wboard.w2i.upper(),\
                                          Bboard.b3i.lower()+Wboard.w3i.upper(),\
                                          Bboard.b4i.lower()+Wboard.w4i.upper(),\
                                          Bboard.b5i.lower()+Wboard.w5i.upper(),\
                                          Bboard.b6i.lower()+Wboard.w6i.upper(),\
                                          Bboard.b7i.lower()+Wboard.w7i.upper(),\
                                          Bboard.b8i.lower()+Wboard.w8i.upper(),\
                                          Bboard.b9i.lower()+Wboard.w9i.upper()
                             
    s1b,s2b,s3b,s4b,s5b,s6b,s7b,s8b,s9b = Bboard.b1h.lower()+Wboard.w1h.upper(),\
                                          Bboard.b2h.lower()+Wboard.w2h.upper(),\
                                          Bboard.b3h.lower()+Wboard.w3h.upper(),\
                                          Bboard.b4h.lower()+Wboard.w4h.upper(),\
                                          Bboard.b5h.lower()+Wboard.w5h.upper(),\
                                          Bboard.b6h.lower()+Wboard.w6h.upper(),\
                                          Bboard.b7h.lower()+Wboard.w7h.upper(),\
                                          Bboard.b8h.lower()+Wboard.w8h.upper(),\
                                          Bboard.b9h.lower()+Wboard.w9h.upper()
                                
    s1c,s2c,s3c,s4c,s5c,s6c,s7c,s8c,s9c = Bboard.b1g.lower()+Wboard.w1g.upper(),\
                                          Bboard.b2g.lower()+Wboard.w2g.upper(),\
                                          Bboard.b3g.lower()+Wboard.w3g.upper(),\
                                          Bboard.b4g.lower()+Wboard.w4g.upper(),\
                                          Bboard.b5g.lower()+Wboard.w5g.upper(),\
                                          Bboard.b6g.lower()+Wboard.w6g.upper(),\
                                          Bboard.b7g.lower()+Wboard.w7g.upper(),\
                                          Bboard.b8g.lower()+Wboard.w8g.upper(),\
                                          Bboard.b9g.lower()+Wboard.w9g.upper()
                                 
    s1d,s2d,s3d,s4d,s5d,s6d,s7d,s8d,s9d = Bboard.b1f.lower()+Wboard.w1f.upper(),\
                                          Bboard.b2f.lower()+Wboard.w2f.upper(),\
                                          Bboard.b3f.lower()+Wboard.w3f.upper(),\
                                          Bboard.b4f.lower()+Wboard.w4f.upper(),\
                                          Bboard.b5f.lower()+Wboard.w5f.upper(),\
                                          Bboard.b6f.lower()+Wboard.w6f.upper(),\
                                          Bboard.b7f.lower()+Wboard.w7f.upper(),\
                                          Bboard.b8f.lower()+Wboard.w8f.upper(),\
                                          Bboard.b9f.lower()+Wboard.w9f.upper()
                                 
    s1e,s2e,s3e,s4e,s5e,s6e,s7e,s8e,s9e = Bboard.b1e.lower()+Wboard.w1e.upper(),\
                                          Bboard.b2e.lower()+Wboard.w2e.upper(),\
                                          Bboard.b3e.lower()+Wboard.w3e.upper(),\
                                          Bboard.b4e.lower()+Wboard.w4e.upper(),\
                                          Bboard.b5e.lower()+Wboard.w5e.upper(),\
                                          Bboard.b6e.lower()+Wboard.w6e.upper(),\
                                          Bboard.b7e.lower()+Wboard.w7e.upper(),\
                                          Bboard.b8e.lower()+Wboard.w8e.upper(),\
                                          Bboard.b9e.lower()+Wboard.w9e.upper()
                                 
    s1f,s2f,s3f,s4f,s5f,s6f,s7f,s8f,s9f = Bboard.b1d.lower()+Wboard.w1d.upper(),\
                                          Bboard.b2d.lower()+Wboard.w2d.upper(),\
                                          Bboard.b3d.lower()+Wboard.w3d.upper(),\
                                          Bboard.b4d.lower()+Wboard.w4d.upper(),\
                                          Bboard.b5d.lower()+Wboard.w5d.upper(),\
                                          Bboard.b6d.lower()+Wboard.w6d.upper(),\
                                          Bboard.b7d.lower()+Wboard.w7d.upper(),\
                                          Bboard.b8d.lower()+Wboard.w8d.upper(),\
                                          Bboard.b9d.lower()+Wboard.w9d.upper()
                                 
    s1g,s2g,s3g,s4g,s5g,s6g,s7g,s8g,s9g = Bboard.b1c.lower()+Wboard.w1c.upper(),\
                                          Bboard.b2c.lower()+Wboard.w2c.upper(),\
                                          Bboard.b3c.lower()+Wboard.w3c.upper(),\
                                          Bboard.b4c.lower()+Wboard.w4c.upper(),\
                                          Bboard.b5c.lower()+Wboard.w5c.upper(),\
                                          Bboard.b6c.lower()+Wboard.w6c.upper(),\
                                          Bboard.b7c.lower()+Wboard.w7c.upper(),\
                                          Bboard.b8c.lower()+Wboard.w8c.upper(),\
                                          Bboard.b9c.lower()+Wboard.w9c.upper()
                                 
    s1h,s2h,s3h,s4h,s5h,s6h,s7h,s8h,s9h = Bboard.b1b.lower()+Wboard.w1b.upper(),\
                                          Bboard.b2b.lower()+Wboard.w2b.upper(),\
                                          Bboard.b3b.lower()+Wboard.w3b.upper(),\
                                          Bboard.b4b.lower()+Wboard.w4b.upper(),\
                                          Bboard.b5b.lower()+Wboard.w5b.upper(),\
                                          Bboard.b6b.lower()+Wboard.w6b.upper(),\
                                          Bboard.b7b.lower()+Wboard.w7b.upper(),\
                                          Bboard.b8b.lower()+Wboard.w8b.upper(),\
                                          Bboard.b9b.lower()+Wboard.w9b.upper()
                                
    s1i,s2i,s3i,s4i,s5i,s6i,s7i,s8i,s9i = Bboard.b1a.lower()+Wboard.w1a.upper(),\
                                          Bboard.b2a.lower()+Wboard.w2a.upper(),\
                                          Bboard.b3a.lower()+Wboard.w3a.upper(),\
                                          Bboard.b4a.lower()+Wboard.w4a.upper(),\
                                          Bboard.b5a.lower()+Wboard.w5a.upper(),\
                                          Bboard.b6a.lower()+Wboard.w6a.upper(),\
                                          Bboard.b7a.lower()+Wboard.w7a.upper(),\
                                          Bboard.b8a.lower()+Wboard.w8a.upper(),\
                                          Bboard.b9a.lower()+Wboard.w9a.upper()
                                 
    P = Wboard.p
    L = Wboard.l
    N = Wboard.n
    S = Wboard.s
    G = Wboard.g
    B = Wboard.b
    R = Wboard.r
    p = Bboard.P
    l = Bboard.L
    n = Bboard.N
    s = Bboard.S
    g = Bboard.G
    b = Bboard.B
    r = Bboard.R


#現局面をプログラム上に書き出す関数
def kyokumen():
    linea = '  9   8   7   6   5   4   3   2   1'
    lineb = '-------------------------------------'
    linec = '|   '
    line1 =  linec[0:2-int(len(s9a)/2)]+s9a+linec[1+int(len(s9a)/2+0.6):3]\
            +linec[0:2-int(len(s8a)/2)]+s8a+linec[1+int(len(s8a)/2+0.6):3]\
            +linec[0:2-int(len(s7a)/2)]+s7a+linec[1+int(len(s7a)/2+0.6):3]\
            +linec[0:2-int(len(s6a)/2)]+s6a+linec[1+int(len(s6a)/2+0.6):3]\
            +linec[0:2-int(len(s5a)/2)]+s5a+linec[1+int(len(s5a)/2+0.6):3]\
            +linec[0:2-int(len(s4a)/2)]+s4a+linec[1+int(len(s4a)/2+0.6):3]\
            +linec[0:2-int(len(s3a)/2)]+s3a+linec[1+int(len(s3a)/2+0.6):3]\
            +linec[0:2-int(len(s2a)/2)]+s2a+linec[1+int(len(s2a)/2+0.6):3]\
            +linec[0:2-int(len(s1a)/2)]+s1a+linec[1+int(len(s1a)/2+0.6):3]+'|   a'

    line2 =  linec[0:2-int(len(s9b)/2)]+s9b+linec[1+int(len(s9b)/2+0.6):3]\
            +linec[0:2-int(len(s8b)/2)]+s8b+linec[1+int(len(s8b)/2+0.6):3]\
            +linec[0:2-int(len(s7b)/2)]+s7b+linec[1+int(len(s7b)/2+0.6):3]\
            +linec[0:2-int(len(s6b)/2)]+s6b+linec[1+int(len(s6b)/2+0.6):3]\
            +linec[0:2-int(len(s5b)/2)]+s5b+linec[1+int(len(s5b)/2+0.6):3]\
            +linec[0:2-int(len(s4b)/2)]+s4b+linec[1+int(len(s4b)/2+0.6):3]\
            +linec[0:2-int(len(s3b)/2)]+s3b+linec[1+int(len(s3b)/2+0.6):3]\
            +linec[0:2-int(len(s2b)/2)]+s2b+linec[1+int(len(s2b)/2+0.6):3]\
            +linec[0:2-int(len(s1b)/2)]+s1b+linec[1+int(len(s1b)/2+0.6):3]+'|   b'
    
    line3 =  linec[0:2-int(len(s9c)/2)]+s9c+linec[1+int(len(s9c)/2+0.6):3]\
            +linec[0:2-int(len(s8c)/2)]+s8c+linec[1+int(len(s8c)/2+0.6):3]\
            +linec[0:2-int(len(s7c)/2)]+s7c+linec[1+int(len(s7c)/2+0.6):3]\
            +linec[0:2-int(len(s6c)/2)]+s6c+linec[1+int(len(s6c)/2+0.6):3]\
            +linec[0:2-int(len(s5c)/2)]+s5c+linec[1+int(len(s5c)/2+0.6):3]\
            +linec[0:2-int(len(s4c)/2)]+s4c+linec[1+int(len(s4c)/2+0.6):3]\
            +linec[0:2-int(len(s3c)/2)]+s3c+linec[1+int(len(s3c)/2+0.6):3]\
            +linec[0:2-int(len(s2c)/2)]+s2c+linec[1+int(len(s2c)/2+0.6):3]\
            +linec[0:2-int(len(s1c)/2)]+s1c+linec[1+int(len(s1c)/2+0.6):3]+'|   c'
    
    line4 =  linec[0:2-int(len(s9d)/2)]+s9d+linec[1+int(len(s9d)/2+0.6):3]\
            +linec[0:2-int(len(s8d)/2)]+s8d+linec[1+int(len(s8d)/2+0.6):3]\
            +linec[0:2-int(len(s7d)/2)]+s7d+linec[1+int(len(s7d)/2+0.6):3]\
            +linec[0:2-int(len(s6d)/2)]+s6d+linec[1+int(len(s6d)/2+0.6):3]\
            +linec[0:2-int(len(s5d)/2)]+s5d+linec[1+int(len(s5d)/2+0.6):3]\
            +linec[0:2-int(len(s4d)/2)]+s4d+linec[1+int(len(s4d)/2+0.6):3]\
            +linec[0:2-int(len(s3d)/2)]+s3d+linec[1+int(len(s3d)/2+0.6):3]\
            +linec[0:2-int(len(s2d)/2)]+s2d+linec[1+int(len(s2d)/2+0.6):3]\
            +linec[0:2-int(len(s1d)/2)]+s1d+linec[1+int(len(s1d)/2+0.6):3]+'|   d'

    line5 =  linec[0:2-int(len(s9e)/2)]+s9e+linec[1+int(len(s9e)/2+0.6):3]\
            +linec[0:2-int(len(s8e)/2)]+s8e+linec[1+int(len(s8e)/2+0.6):3]\
            +linec[0:2-int(len(s7e)/2)]+s7e+linec[1+int(len(s7e)/2+0.6):3]\
            +linec[0:2-int(len(s6e)/2)]+s6e+linec[1+int(len(s6e)/2+0.6):3]\
            +linec[0:2-int(len(s5e)/2)]+s5e+linec[1+int(len(s5e)/2+0.6):3]\
            +linec[0:2-int(len(s4e)/2)]+s4e+linec[1+int(len(s4e)/2+0.6):3]\
            +linec[0:2-int(len(s3e)/2)]+s3e+linec[1+int(len(s3e)/2+0.6):3]\
            +linec[0:2-int(len(s2e)/2)]+s2e+linec[1+int(len(s2e)/2+0.6):3]\
            +linec[0:2-int(len(s1e)/2)]+s1e+linec[1+int(len(s1e)/2+0.6):3]+'|   e'
    
    line6 =  linec[0:2-int(len(s9f)/2)]+s9f+linec[1+int(len(s9f)/2+0.6):3]\
            +linec[0:2-int(len(s8f)/2)]+s8f+linec[1+int(len(s8f)/2+0.6):3]\
            +linec[0:2-int(len(s7f)/2)]+s7f+linec[1+int(len(s7f)/2+0.6):3]\
            +linec[0:2-int(len(s6f)/2)]+s6f+linec[1+int(len(s6f)/2+0.6):3]\
            +linec[0:2-int(len(s5f)/2)]+s5f+linec[1+int(len(s5f)/2+0.6):3]\
            +linec[0:2-int(len(s4f)/2)]+s4f+linec[1+int(len(s4f)/2+0.6):3]\
            +linec[0:2-int(len(s3f)/2)]+s3f+linec[1+int(len(s3f)/2+0.6):3]\
            +linec[0:2-int(len(s2f)/2)]+s2f+linec[1+int(len(s2f)/2+0.6):3]\
            +linec[0:2-int(len(s1f)/2)]+s1f+linec[1+int(len(s1f)/2+0.6):3]+'|   f'
    
    line7 =  linec[0:2-int(len(s9g)/2)]+s9g+linec[1+int(len(s9g)/2+0.6):3]\
            +linec[0:2-int(len(s8g)/2)]+s8g+linec[1+int(len(s8g)/2+0.6):3]\
            +linec[0:2-int(len(s7g)/2)]+s7g+linec[1+int(len(s7g)/2+0.6):3]\
            +linec[0:2-int(len(s6g)/2)]+s6g+linec[1+int(len(s6g)/2+0.6):3]\
            +linec[0:2-int(len(s5g)/2)]+s5g+linec[1+int(len(s5g)/2+0.6):3]\
            +linec[0:2-int(len(s4g)/2)]+s4g+linec[1+int(len(s4g)/2+0.6):3]\
            +linec[0:2-int(len(s3g)/2)]+s3g+linec[1+int(len(s3g)/2+0.6):3]\
            +linec[0:2-int(len(s2g)/2)]+s2g+linec[1+int(len(s2g)/2+0.6):3]\
            +linec[0:2-int(len(s1g)/2)]+s1g+linec[1+int(len(s1g)/2+0.6):3]+'|   g'

    line8 =  linec[0:2-int(len(s9h)/2)]+s9h+linec[1+int(len(s9h)/2+0.6):3]\
            +linec[0:2-int(len(s8h)/2)]+s8h+linec[1+int(len(s8h)/2+0.6):3]\
            +linec[0:2-int(len(s7h)/2)]+s7h+linec[1+int(len(s7h)/2+0.6):3]\
            +linec[0:2-int(len(s6h)/2)]+s6h+linec[1+int(len(s6h)/2+0.6):3]\
            +linec[0:2-int(len(s5h)/2)]+s5h+linec[1+int(len(s5h)/2+0.6):3]\
            +linec[0:2-int(len(s4h)/2)]+s4h+linec[1+int(len(s4h)/2+0.6):3]\
            +linec[0:2-int(len(s3h)/2)]+s3h+linec[1+int(len(s3h)/2+0.6):3]\
            +linec[0:2-int(len(s2h)/2)]+s2h+linec[1+int(len(s2h)/2+0.6):3]\
            +linec[0:2-int(len(s1h)/2)]+s1h+linec[1+int(len(s1h)/2+0.6):3]+'|   h'

    line9 =  linec[0:2-int(len(s9i)/2)]+s9i+linec[1+int(len(s9i)/2+0.6):3]\
            +linec[0:2-int(len(s8i)/2)]+s8i+linec[1+int(len(s8i)/2+0.6):3]\
            +linec[0:2-int(len(s7i)/2)]+s7i+linec[1+int(len(s7i)/2+0.6):3]\
            +linec[0:2-int(len(s6i)/2)]+s6i+linec[1+int(len(s6i)/2+0.6):3]\
            +linec[0:2-int(len(s5i)/2)]+s5i+linec[1+int(len(s5i)/2+0.6):3]\
            +linec[0:2-int(len(s4i)/2)]+s4i+linec[1+int(len(s4i)/2+0.6):3]\
            +linec[0:2-int(len(s3i)/2)]+s3i+linec[1+int(len(s3i)/2+0.6):3]\
            +linec[0:2-int(len(s2i)/2)]+s2i+linec[1+int(len(s2i)/2+0.6):3]\
            +linec[0:2-int(len(s1i)/2)]+s1i+linec[1+int(len(s1i)/2+0.6):3]+'|   i'
    
    print('\n' + linea + '\n')
    print(lineb)
    print(line1)
    print(lineb)
    print(line2)
    print(lineb)
    print(line3)
    print(lineb)
    print(line4)
    print(lineb)
    print(line5)
    print(lineb)
    print(line6)
    print(lineb)
    print(line7)
    print(lineb)
    print(line8)
    print(lineb)
    print(line9)
    print(lineb + '\n')
    print(f'{P=} {L=} {N=} {S=} {G=} {B=} {R=}')
    print(f'{p=} {l=} {n=} {s=} {g=} {b=} {r=}' + '\n')


#局面を動かす関数（startposから始まるものしか対応していない）
def position(sfen):
    global turn
    turn = 1
    m = re.search('moves',sfen)
    if not re.search('moves',sfen):
        return
    sfen = sfen[m.end()+1:]
    sfen =sfen.replace(' ', '')
    mae = sfen[0:2]
    ushiro = sfen[2:4]
    nari = sfen[4:5]

    while mae != '':
        if nari != '+':
            nari = ''
        if mae[1:2]=='*':
            exec('Bboard.{}-=1'.format(mae[0:1]))
            exec('Bboard.b{}="{}"'.format(ushiro,mae[0:1]))
        else:
            exec('Bboard.b{}=Bboard.b{}'.format(ushiro,mae))
            if nari == '+':
                exec("Bboard.b{}= '+'+Bboard.b{}".format(ushiro,ushiro))
            exec('Bboard.koma=Wboard.w{}'.format(ushiro))
            if Bboard.koma != '':
                exec('Bboard.{}+=1'.format(Bboard.koma[-1:].upper()))
            exec("Bboard.b{}=''".format(mae))
            exec("Wboard.w{}=''".format(ushiro))
        sfen = sfen[4+len(nari):]
        mae = sfen[0:2]
        ushiro = sfen[2:4]
        nari = sfen[4:5]
        turn *= -1
        if mae == '':
            break
        if nari != '+':
            nari = ''
        if mae[1:2]=='*':
            exec('Wboard.{}-=1'.format(mae[0:1].lower()))
            exec('Wboard.w{}="{}"'.format(ushiro,mae[0:1].lower()))
        else:
            exec('Wboard.w{}=Wboard.w{}'.format(ushiro,mae))
            if nari == '+':
                exec("Wboard.w{}= '+'+Wboard.w{}".format(ushiro,ushiro))
            exec('Wboard.koma=Bboard.b{}'.format(ushiro))
            if Wboard.koma != '':
                exec('Wboard.{}+=1'.format(Wboard.koma[-1:].lower()))
            exec("Wboard.w{}=''".format(mae))
            exec("Bboard.b{}=''".format(ushiro))
        sfen = sfen[4+len(nari):]
        mae = sfen[0:2]
        ushiro = sfen[2:4]
        nari = sfen[4:5]
        turn *= -1
