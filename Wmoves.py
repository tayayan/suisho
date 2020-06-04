#後手番合法手生成
import re
import Bboard
import Bboardbak
import Wboard
import Wboardbak
import board
import oute


#動かした後に後手玉に王手がかかっていないか判定
def kaihimore(sfen):
    mae = sfen[0:2]
    ushiro = sfen[2:4]
    nari = sfen[4:5]
    if mae[1:2]=='*':
        exec('Wboard.w{}="{}"'.format(ushiro,mae[0:1]))
    else:
        exec('Wboard.w{}=Wboard.w{}'.format(ushiro,mae))
        if nari == '+':
            exec("Wboard.w{}= '+'+Wboard.w{}".format(ushiro,ushiro))
        exec("Wboard.w{}=''".format(mae))
        exec("Bboard.b{}=''".format(ushiro))
    oute.woute()
    Bboardbak.yobidashi()
    Wboardbak.yobidashi()
    board.synth()

#以下合法手生成コード
def move1():
    global depth1
    Bboardbak.kioku()
    Wboardbak.kioku()
    board.synth()
    depth1 = []
    if Wboard.w1i !='':
        if re.match(r'[gk+]',Wboard.w1i)and Wboard.w2i=='':
            moves = '1i2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',Wboard.w1i)and Wboard.w1h=='':
            moves = '1i1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w1i)and Wboard.w2h=='':
            moves = '1i2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',Wboard.w1i)and Wboard.w2i=='':
            moves = '1i2i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',Wboard.w1i)and Wboard.w1h=='':
            moves = '1i1h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',Wboard.w1i)and Wboard.w1h=='':
            moves = '1i2h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w1i)and Wboard.w1g==''\
           and board.s1h=='':
            moves = '1i1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w1i)and Wboard.w1g==''\
           and board.s1h=='':
            moves = '1i1g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w1i)and Wboard.w1f==''\
           and board.s1h+board.s1g=='':
            moves = '1i1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w1i)and Wboard.w1f==''\
           and board.s1h+board.s1g=='':
            moves = '1i1f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w1i)and Wboard.w1e==''\
           and board.s1h+board.s1g+board.s1f=='':
            moves = '1i1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w1i)and Wboard.w1e==''\
           and board.s1h+board.s1g+board.s1f=='':
            moves = '1i1e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w1i)and Wboard.w1d==''\
           and board.s1h+board.s1g+board.s1f+board.s1e=='':
            moves = '1i1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w1i)and Wboard.w1d==''\
           and board.s1h+board.s1g+board.s1f+board.s1e=='':
            moves = '1i1d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w1i)and Wboard.w1c==''\
           and board.s1h+board.s1g+board.s1f+board.s1e+board.s1d=='':
            moves = '1i1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w1i)and Wboard.w1c==''\
           and board.s1h+board.s1g+board.s1f+board.s1e+board.s1d=='':
            moves = '1i1c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w1i)and Wboard.w1b==''\
           and board.s1h+board.s1g+board.s1f+board.s1e+board.s1d+board.s1c=='':
            moves = '1i1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w1i)and Wboard.w1b==''\
           and board.s1h+board.s1g+board.s1f+board.s1e+board.s1d+board.s1c=='':
            moves = '1i1b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w1i)and Wboard.w1a==''\
           and board.s1h+board.s1g+board.s1f+board.s1e+board.s1d+board.s1c+board.s1b=='':
            moves = '1i1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w1i)and Wboard.w1a==''\
           and board.s1h+board.s1g+board.s1f+board.s1e+board.s1d+board.s1c+board.s1b=='':
            moves = '1i1a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w1i)and Wboard.w3i==''\
           and board.s2i=='':
            moves = '1i3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w1i)and Wboard.w3i==''\
           and board.s2i=='':
            moves = '1i3i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w1i)and Wboard.w4i==''\
           and board.s2i+board.s3i=='':
            moves = '1i4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w1i)and Wboard.w4i==''\
           and board.s2i+board.s3i=='':
            moves = '1i4i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w1i)and Wboard.w5i==''\
           and board.s2i+board.s3i+board.s4i=='':
            moves = '1i5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w1i)and Wboard.w5i==''\
           and board.s2i+board.s3i+board.s4i=='':
            moves = '1i5i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w1i)and Wboard.w6i==''\
           and board.s2i+board.s3i+board.s4i+board.s5i=='':
            moves = '1i6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w1i)and Wboard.w6i==''\
           and board.s2i+board.s3i+board.s4i+board.s5i=='':
            moves = '1i6i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w1i)and Wboard.w7i==''\
           and board.s2i+board.s3i+board.s4i+board.s5i+board.s6i=='':
            moves = '1i7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w1i)and Wboard.w7i==''\
           and board.s2i+board.s3i+board.s4i+board.s5i+board.s6i=='':
            moves = '1i7i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w1i)and Wboard.w8i==''\
           and board.s2i+board.s3i+board.s4i+board.s5i+board.s6i+board.s7i=='':
            moves = '1i8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w1i)and Wboard.w8i==''\
           and board.s2i+board.s3i+board.s4i+board.s5i+board.s6i+board.s7i=='':
            moves = '1i8i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w1i)and Wboard.w9i==''\
           and board.s2i+board.s3i+board.s4i+board.s5i+board.s6i+board.s7i+board.s8i=='':
            moves = '1i9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w1i)and Wboard.w9i==''\
           and board.s2i+board.s3i+board.s4i+board.s5i+board.s6i+board.s7i+board.s8i=='':
            moves = '1i9i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w1i)and Wboard.w3g==''\
           and board.s2h=='':
            moves = '1i3g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w1i)and Wboard.w4f==''\
           and board.s2h+board.s3g=='':
            moves = '1i4f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w1i)and Wboard.w5e==''\
           and board.s2h+board.s3g+board.s4f=='':
            moves = '1i5e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w1i)and Wboard.w6d==''\
           and board.s2h+board.s3g+board.s4f+board.s5e=='':
            moves = '1i6d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w1i)and Wboard.w7c==''\
           and board.s2h+board.s3g+board.s4f+board.s5e+board.s6d=='':
            moves = '1i7c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w1i)and Wboard.w8b==''\
           and board.s2h+board.s3g+board.s4f+board.s5e+board.s6d+board.s7c=='':
            moves = '1i8b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w1i)and Wboard.w9a==''\
           and board.s2h+board.s3g+board.s4f+board.s5e+board.s6d+board.s7c+board.s8b=='':
            moves = '1i9a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w1i)and Wboard.w3g==''\
           and board.s2h=='':
            moves = '1i3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w1i)and Wboard.w4f==''\
           and board.s2h+board.s3g=='':
            moves = '1i4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w1i)and Wboard.w5e==''\
           and board.s2h+board.s3g+board.s4f=='':
            moves = '1i5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w1i)and Wboard.w6d==''\
           and board.s2h+board.s3g+board.s4f+board.s5e=='':
            moves = '1i6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w1i)and Wboard.w7c==''\
           and board.s2h+board.s3g+board.s4f+board.s5e+board.s6d=='':
            moves = '1i7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w1i)and Wboard.w8b==''\
           and board.s2h+board.s3g+board.s4f+board.s5e+board.s6d+board.s7c=='':
            moves = '1i8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w1i)and Wboard.w9a==''\
           and board.s2h+board.s3g+board.s4f+board.s5e+board.s6d+board.s7c+board.s8b=='':
            moves = '1i9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w2i !='':
        if re.match(r'[gk+]',Wboard.w2i)and Wboard.w1i=='':
            moves = '2i1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',Wboard.w2i)and Wboard.w3i=='':
            moves = '2i3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',Wboard.w2i)and Wboard.w2h=='':
            moves = '2i2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w2i)and Wboard.w1h=='':
            moves = '2i1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'\+r|\+b|s|k',Wboard.w2i)and Wboard.w3h=='':
            moves = '2i3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',Wboard.w2i)and Wboard.w1i=='':
            moves = '2i1i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',Wboard.w2i)and Wboard.w3i=='':
            moves = '2i3i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',Wboard.w2i)and Wboard.w2h=='':
            moves = '2i2h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',Wboard.w2i)and Wboard.w1h=='':
            moves = '2i1h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',Wboard.w2i)and Wboard.w3h=='':
            moves = '2i3h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w2i)and Wboard.w2g==''\
           and board.s2h=='':
            moves = '2i2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w2i)and Wboard.w2g==''\
           and board.s2h=='':
            moves = '2i2g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w2i)and Wboard.w2f==''\
           and board.s2h+board.s2g=='':
            moves = '2i2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w2i)and Wboard.w2f==''\
           and board.s2h+board.s2g=='':
            moves = '2i2f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w2i)and Wboard.w2e==''\
           and board.s2h+board.s2g+board.s2f=='':
            moves = '2i2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w2i)and Wboard.w2e==''\
           and board.s2h+board.s2g+board.s2f=='':
            moves = '2i2e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w2i)and Wboard.w2d==''\
           and board.s2h+board.s2g+board.s2f+board.s2e=='':
            moves = '2i2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w2i)and Wboard.w2d==''\
           and board.s2h+board.s2g+board.s2f+board.s2e=='':
            moves = '2i2d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w2i)and Wboard.w2c==''\
           and board.s2h+board.s2g+board.s2f+board.s2e+board.s2d=='':
            moves = '2i2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w2i)and Wboard.w2c==''\
           and board.s2h+board.s2g+board.s2f+board.s2e+board.s2d=='':
            moves = '2i2c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w2i)and Wboard.w2b==''\
           and board.s2h+board.s2g+board.s2f+board.s2e+board.s2d+board.s2c=='':
            moves = '2i2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w2i)and Wboard.w2b==''\
           and board.s2h+board.s2g+board.s2f+board.s2e+board.s2d+board.s2c=='':
            moves = '2i2b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w2i)and Wboard.w2a==''\
           and board.s2h+board.s2g+board.s2f+board.s2e+board.s2d+board.s2c+board.s2b=='':
            moves = '2i2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w2i)and Wboard.w2a==''\
           and board.s2h+board.s2g+board.s2f+board.s2e+board.s2d+board.s2c+board.s2b=='':
            moves = '2i2a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w2i)and Wboard.w4i==''\
           and board.s3i=='':
            moves = '2i4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w2i)and Wboard.w4i==''\
           and board.s3i=='':
            moves = '2i4i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w2i)and Wboard.w5i==''\
           and board.s3i+board.s4i=='':
            moves = '2i5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w2i)and Wboard.w5i==''\
           and board.s3i+board.s4i=='':
            moves = '2i5i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w2i)and Wboard.w6i==''\
           and board.s3i+board.s4i+board.s5i=='':
            moves = '2i6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w2i)and Wboard.w6i==''\
           and board.s3i+board.s4i+board.s5i=='':
            moves = '2i6i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w2i)and Wboard.w7i==''\
           and board.s3i+board.s4i+board.s5i+board.s6i=='':
            moves = '2i7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w2i)and Wboard.w7i==''\
           and board.s3i+board.s4i+board.s5i+board.s6i=='':
            moves = '2i7i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w2i)and Wboard.w8i==''\
           and board.s3i+board.s4i+board.s5i+board.s6i+board.s7i=='':
            moves = '2i8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w2i)and Wboard.w8i==''\
           and board.s3i+board.s4i+board.s5i+board.s6i+board.s7i=='':
            moves = '2i8i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w2i)and Wboard.w9i==''\
           and board.s3i+board.s4i+board.s5i+board.s6i+board.s7i+board.s8i=='':
            moves = '2i9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w2i)and Wboard.w9i==''\
           and board.s3i+board.s4i+board.s5i+board.s6i+board.s7i+board.s8i=='':
            moves = '2i9i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w2i)and Wboard.w4g==''\
           and board.s3h=='':
            moves = '2i4g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w2i)and Wboard.w5f==''\
           and board.s3h+board.s4g=='':
            moves = '2i5f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w2i)and Wboard.w6e==''\
           and board.s3h+board.s4g+board.s5f=='':
            moves = '2i6e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w2i)and Wboard.w7d==''\
           and board.s3h+board.s4g+board.s5f+board.s6e=='':
            moves = '2i7d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w2i)and Wboard.w8c==''\
           and board.s3h+board.s4g+board.s5f+board.s6e+board.s7d=='':
            moves = '2i8c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w2i)and Wboard.w9b==''\
           and board.s3h+board.s4g+board.s5f+board.s6e+board.s7d+board.s8c=='':
            moves = '2i9b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w2i)and Wboard.w4g==''\
           and board.s3h=='':
            moves = '2i4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w2i)and Wboard.w5f==''\
           and board.s3h+board.s4g=='':
            moves = '2i5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w2i)and Wboard.w6e==''\
           and board.s3h+board.s4g+board.s5f=='':
            moves = '2i6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w2i)and Wboard.w7d==''\
           and board.s3h+board.s4g+board.s5f+board.s6e=='':
            moves = '2i7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w2i)and Wboard.w8c==''\
           and board.s3h+board.s4g+board.s5f+board.s6e+board.s7d=='':
            moves = '2i8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w2i)and Wboard.w9b==''\
           and board.s3h+board.s4g+board.s5f+board.s6e+board.s7d+board.s8c=='':
            moves = '2i9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w3i !='':
        if re.match(r'[gk+]',Wboard.w3i)and Wboard.w2i=='':
            moves = '3i2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',Wboard.w3i)and Wboard.w4i=='':
            moves = '3i4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',Wboard.w3i)and Wboard.w3h=='':
            moves = '3i3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w3i)and Wboard.w2h=='':
            moves = '3i2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'\+r|\+b|s|k',Wboard.w3i)and Wboard.w4h=='':
            moves = '3i4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',Wboard.w3i)and Wboard.w2i=='':
            moves = '3i2i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',Wboard.w3i)and Wboard.w4i=='':
            moves = '3i4i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',Wboard.w3i)and Wboard.w3h=='':
            moves = '3i3h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',Wboard.w3i)and Wboard.w2h=='':
            moves = '3i2h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',Wboard.w3i)and Wboard.w4h=='':
            moves = '3i4h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w3i)and Wboard.w3g==''\
           and board.s3h=='':
            moves = '3i3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w3i)and Wboard.w3g==''\
           and board.s3h=='':
            moves = '3i3g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w3i)and Wboard.w3f==''\
           and board.s3h+board.s3g=='':
            moves = '3i3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w3i)and Wboard.w3f==''\
           and board.s3h+board.s3g=='':
            moves = '3i3f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w3i)and Wboard.w3e==''\
           and board.s3h+board.s3g+board.s3f=='':
            moves = '3i3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w3i)and Wboard.w3e==''\
           and board.s3h+board.s3g+board.s3f=='':
            moves = '3i3e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w3i)and Wboard.w3d==''\
           and board.s3h+board.s3g+board.s3f+board.s3e=='':
            moves = '3i3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w3i)and Wboard.w3d==''\
           and board.s3h+board.s3g+board.s3f+board.s3e=='':
            moves = '3i3d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w3i)and Wboard.w3c==''\
           and board.s3h+board.s3g+board.s3f+board.s3e+board.s3d=='':
            moves = '3i3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w3i)and Wboard.w3c==''\
           and board.s3h+board.s3g+board.s3f+board.s3e+board.s3d=='':
            moves = '3i3c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w3i)and Wboard.w3b==''\
           and board.s3h+board.s3g+board.s3f+board.s3e+board.s3d+board.s3c=='':
            moves = '3i3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w3i)and Wboard.w3b==''\
           and board.s3h+board.s3g+board.s3f+board.s3e+board.s3d+board.s3c=='':
            moves = '3i3b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w3i)and Wboard.w3a==''\
           and board.s3h+board.s3g+board.s3f+board.s3e+board.s3d+board.s3c+board.s3b=='':
            moves = '3i3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w3i)and Wboard.w3a==''\
           and board.s3h+board.s3g+board.s3f+board.s3e+board.s3d+board.s3c+board.s3b=='':
            moves = '3i3a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w3i)and Wboard.w1i==''\
           and board.s2i=='':
            moves = '3i1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w3i)and Wboard.w1i==''\
           and board.s2i=='':
            moves = '3i1i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w3i)and Wboard.w5i==''\
           and board.s4i=='':
            moves = '3i5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w3i)and Wboard.w5i==''\
           and board.s4i=='':
            moves = '3i5i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w3i)and Wboard.w6i==''\
           and board.s4i+board.s5i=='':
            moves = '3i6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w3i)and Wboard.w6i==''\
           and board.s4i+board.s5i=='':
            moves = '3i6i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w3i)and Wboard.w7i==''\
           and board.s4i+board.s5i+board.s6i=='':
            moves = '3i7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w3i)and Wboard.w7i==''\
           and board.s4i+board.s5i+board.s6i=='':
            moves = '3i7i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w3i)and Wboard.w8i==''\
           and board.s4i+board.s5i+board.s6i+board.s7i=='':
            moves = '3i8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w3i)and Wboard.w8i==''\
           and board.s4i+board.s5i+board.s6i+board.s7i=='':
            moves = '3i8i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w3i)and Wboard.w9i==''\
           and board.s4i+board.s5i+board.s6i+board.s7i+board.s8i=='':
            moves = '3i9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w3i)and Wboard.w9i==''\
           and board.s4i+board.s5i+board.s6i+board.s7i+board.s8i=='':
            moves = '3i9i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w3i)and Wboard.w1g==''\
           and board.s2h=='':
            moves = '3i1g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w3i)and Wboard.w5g==''\
           and board.s4h=='':
            moves = '3i5g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w3i)and Wboard.w6f==''\
           and board.s4h+board.s5g=='':
            moves = '3i6f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w3i)and Wboard.w6e==''\
           and board.s4h+board.s5g+board.s6f=='':
            moves = '3i7e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w3i)and Wboard.w7d==''\
           and board.s4h+board.s5g+board.s6f+board.s7e=='':
            moves = '3i8d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w3i)and Wboard.w9c==''\
           and board.s4h+board.s5g+board.s6f+board.s7e+board.s8d=='':
            moves = '3i9c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w3i)and Wboard.w1g==''\
           and board.s2h=='':
            moves = '3i1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w3i)and Wboard.w5g==''\
           and board.s4h=='':
            moves = '3i5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w3i)and Wboard.w6f==''\
           and board.s4h+board.s5g=='':
            moves = '3i6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w3i)and Wboard.w6e==''\
           and board.s4h+board.s5g+board.s6f=='':
            moves = '3i7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w3i)and Wboard.w7d==''\
           and board.s4h+board.s5g+board.s6f+board.s7e=='':
            moves = '3i8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w3i)and Wboard.w9c==''\
           and board.s4h+board.s5g+board.s6f+board.s7e+board.s8d=='':
            moves = '3i9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w4i !='':
        if re.match(r'[gk+]',Wboard.w4i)and Wboard.w3i=='':
            moves = '4i3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',Wboard.w4i)and Wboard.w5i=='':
            moves = '4i5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',Wboard.w4i)and Wboard.w4h=='':
            moves = '4i4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w4i)and Wboard.w3h=='':
            moves = '4i3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'\+r|\+b|s|k',Wboard.w4i)and Wboard.w5h=='':
            moves = '4i5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',Wboard.w4i)and Wboard.w3i=='':
            moves = '4i3i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',Wboard.w4i)and Wboard.w5i=='':
            moves = '4i5i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',Wboard.w4i)and Wboard.w4h=='':
            moves = '4i4h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',Wboard.w4i)and Wboard.w3h=='':
            moves = '4i3h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',Wboard.w4i)and Wboard.w5h=='':
            moves = '4i5h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w4i)and Wboard.w4g==''\
           and board.s4h=='':
            moves = '4i4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w4i)and Wboard.w4g==''\
           and board.s4h=='':
            moves = '4i4g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w4i)and Wboard.w4f==''\
           and board.s4h+board.s4g=='':
            moves = '4i4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w4i)and Wboard.w4f==''\
           and board.s4h+board.s4g=='':
            moves = '4i4f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w4i)and Wboard.w4e==''\
           and board.s4h+board.s4g+board.s4f=='':
            moves = '4i4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w4i)and Wboard.w4e==''\
           and board.s4h+board.s4g+board.s4f=='':
            moves = '4i4e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w4i)and Wboard.w4d==''\
           and board.s4h+board.s4g+board.s4f+board.s4e=='':
            moves = '4i4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w4i)and Wboard.w4d==''\
           and board.s4h+board.s4g+board.s4f+board.s4e=='':
            moves = '4i4d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w4i)and Wboard.w4c==''\
           and board.s4h+board.s4g+board.s4f+board.s4e+board.s4d=='':
            moves = '4i4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w4i)and Wboard.w4c==''\
           and board.s4h+board.s4g+board.s4f+board.s4e+board.s4d=='':
            moves = '4i4c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w4i)and Wboard.w4b==''\
           and board.s4h+board.s4g+board.s4f+board.s4e+board.s4d+board.s4c=='':
            moves = '4i4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w4i)and Wboard.w4b==''\
           and board.s4h+board.s4g+board.s4f+board.s4e+board.s4d+board.s4c=='':
            moves = '4i4b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w4i)and Wboard.w4a==''\
           and board.s4h+board.s4g+board.s4f+board.s4e+board.s4d+board.s4c+board.s4b=='':
            moves = '4i4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w4i)and Wboard.w4a==''\
           and board.s4h+board.s4g+board.s4f+board.s4e+board.s4d+board.s4c+board.s4b=='':
            moves = '4i4a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w4i)and Wboard.w1i==''\
           and board.s2i+board.s3i=='':
            moves = '4i1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w4i)and Wboard.w1i==''\
           and board.s2i+board.s3i=='':
            moves = '4i1i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w4i)and Wboard.w2i==''\
           and board.s3i=='':
            moves = '4i2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w4i)and Wboard.w2i==''\
           and board.s3i=='':
            moves = '4i2i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w4i)and Wboard.w6i==''\
           and board.s5i=='':
            moves = '4i6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w4i)and Wboard.w6i==''\
           and board.s5i=='':
            moves = '4i6i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w4i)and Wboard.w7i==''\
           and board.s5i+board.s6i=='':
            moves = '4i7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w4i)and Wboard.w7i==''\
           and board.s5i+board.s6i=='':
            moves = '4i7i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w4i)and Wboard.w8i==''\
           and board.s5i+board.s6i+board.s7i=='':
            moves = '4i8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w4i)and Wboard.w8i==''\
           and board.s5i+board.s6i+board.s7i=='':
            moves = '4i8i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w4i)and Wboard.w9i==''\
           and board.s5i+board.s6i+board.s7i+board.s8i=='':
            moves = '4i9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w4i)and Wboard.w9i==''\
           and board.s5i+board.s6i+board.s7i+board.s8i=='':
            moves = '4i9i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w4i)and Wboard.w6g==''\
           and board.s5h=='':
            moves = '4i6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w4i)and Wboard.w7f==''\
           and board.s5h+board.s6g=='':
            moves = '4i7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w4i)and Wboard.w8e==''\
           and board.s5h+board.s6g+board.s7f=='':
            moves = '4i8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w4i)and Wboard.w9d==''\
           and board.s5h+board.s6g+board.s7f+board.s8e=='':
            moves = '4i9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Wboard.w4i)and Wboard.w6g==''\
           and board.s5h=='':
            moves = '4i6g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w4i)and Wboard.w7f==''\
           and board.s5h+board.s6g=='':
            moves = '4i7f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w4i)and Wboard.w8e==''\
           and board.s5h+board.s6g+board.s7f=='':
            moves = '4i8e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w4i)and Wboard.w9d==''\
           and board.s5h+board.s6g+board.s7f+board.s8e=='':
            moves = '4i9d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w4i)and Wboard.w1f==''\
           and board.s2g+board.s3h=='':
            moves = '4i1f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w4i)and Wboard.w2g==''\
           and board.s3h=='':
            moves = '4i2g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w4i)and Wboard.w1f==''\
           and board.s2g+board.s3h=='':
            moves = '4i1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w4i)and Wboard.w2g==''\
           and board.s3h=='':
            moves = '4i2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w5i !='':
        if re.match(r'[gk+]',Wboard.w5i)and Wboard.w4i=='':
            moves = '5i4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',Wboard.w5i)and Wboard.w6i=='':
            moves = '5i6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',Wboard.w5i)and Wboard.w5h=='':
            moves = '5i5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w5i)and Wboard.w4h=='':
            moves = '5i4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'\+r|\+b|s|k',Wboard.w5i)and Wboard.w6h=='':
            moves = '5i6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',Wboard.w5i)and Wboard.w4i=='':
            moves = '5i4i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',Wboard.w5i)and Wboard.w6i=='':
            moves = '5i6i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',Wboard.w5i)and Wboard.w5h=='':
            moves = '5i5h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',Wboard.w5i)and Wboard.w4h=='':
            moves = '5i4h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',Wboard.w5i)and Wboard.w6h=='':
            moves = '5i6h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w5i)and Wboard.w5g==''\
           and board.s5h=='':
            moves = '5i5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w5i)and Wboard.w5g==''\
           and board.s5h=='':
            moves = '5i5g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w5i)and Wboard.w5f==''\
           and board.s5h+board.s5g=='':
            moves = '5i5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w5i)and Wboard.w5f==''\
           and board.s5h+board.s5g=='':
            moves = '5i5f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w5i)and Wboard.w5e==''\
           and board.s5h+board.s5g+board.s5f=='':
            moves = '5i5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w5i)and Wboard.w5e==''\
           and board.s5h+board.s5g+board.s5f=='':
            moves = '5i5e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w5i)and Wboard.w5d==''\
           and board.s5h+board.s5g+board.s5f+board.s5e=='':
            moves = '5i5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w5i)and Wboard.w5d==''\
           and board.s5h+board.s5g+board.s5f+board.s5e=='':
            moves = '5i5d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w5i)and Wboard.w5c==''\
           and board.s5h+board.s5g+board.s5f+board.s5e+board.s5d=='':
            moves = '5i5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w5i)and Wboard.w5c==''\
           and board.s5h+board.s5g+board.s5f+board.s5e+board.s5d=='':
            moves = '5i5c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w5i)and Wboard.w5b==''\
           and board.s5h+board.s5g+board.s5f+board.s5e+board.s5d+board.s5c=='':
            moves = '5i5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w5i)and Wboard.w5b==''\
           and board.s5h+board.s5g+board.s5f+board.s5e+board.s5d+board.s5c=='':
            moves = '5i5b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w5i)and Wboard.w5a==''\
           and board.s5h+board.s5g+board.s5f+board.s5e+board.s5d+board.s5c+board.s5b=='':
            moves = '5i5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w5i)and Wboard.w5a==''\
           and board.s5h+board.s5g+board.s5f+board.s5e+board.s5d+board.s5c+board.s5b=='':
            moves = '5i5a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w5i)and Wboard.w1i==''\
           and board.s2i+board.s3i+board.s4i=='':
            moves = '5i1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w5i)and Wboard.w1i==''\
           and board.s2i+board.s3i+board.s4i=='':
            moves = '5i1i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w5i)and Wboard.w2i==''\
           and board.s3i+board.s4i=='':
            moves = '5i2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w5i)and Wboard.w2i==''\
           and board.s3i+board.s4i=='':
            moves = '5i2i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w5i)and Wboard.w3i==''\
           and board.s4i=='':
            moves = '5i3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w5i)and Wboard.w3i==''\
           and board.s4i=='':
            moves = '5i3i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w5i)and Wboard.w7i==''\
           and board.s6i=='':
            moves = '5i7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w5i)and Wboard.w7i==''\
           and board.s6i=='':
            moves = '5i7i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w5i)and Wboard.w8i==''\
           and board.s6i+board.s7i=='':
            moves = '5i8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w5i)and Wboard.w8i==''\
           and board.s6i+board.s7i=='':
            moves = '5i8i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w5i)and Wboard.w9i==''\
           and board.s6i+board.s7i+board.s8i=='':
            moves = '5i9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w5i)and Wboard.w9i==''\
           and board.s6i+board.s7i+board.s8i=='':
            moves = '5i9i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w5i)and Wboard.w7g==''\
           and board.s6h=='':
            moves = '5i7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w5i)and Wboard.w8f==''\
           and board.s6h+board.s7g=='':
            moves = '5i8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w5i)and Wboard.w9e==''\
           and board.s6h+board.s7g+board.s8f=='':
            moves = '5i9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Wboard.w5i)and Wboard.w7g==''\
           and board.s6h=='':
            moves = '5i7g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w5i)and Wboard.w8f==''\
           and board.s6h+board.s7g=='':
            moves = '5i8f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w5i)and Wboard.w9e==''\
           and board.s6h+board.s7g+board.s8f=='':
            moves = '5i9e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w5i)and Wboard.w2f==''\
           and board.s3g+board.s4h=='':
            moves = '5i2f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w5i)and Wboard.w3g==''\
           and board.s4h=='':
            moves = '5i3g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w5i)and Wboard.w2f==''\
           and board.s3g+board.s4h=='':
            moves = '5i2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w5i)and Wboard.w3g==''\
           and board.s4h=='':
            moves = '5i3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w5i)and Wboard.w1e==''\
           and board.s4h+board.s3g+board.s2f=='':
            moves = '5i1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w5i)and Wboard.w1e==''\
           and board.s4h+board.s3g+board.s2f=='':
            moves = '5i1e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w6i !='':
        if re.match(r'[gk+]',Wboard.w6i)and Wboard.w5i=='':
            moves = '6i5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',Wboard.w6i)and Wboard.w7i=='':
            moves = '6i7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',Wboard.w6i)and Wboard.w6h=='':
            moves = '6i6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w6i)and Wboard.w5h=='':
            moves = '6i5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'\+r|\+b|s|k',Wboard.w6i)and Wboard.w7h=='':
            moves = '6i7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',Wboard.w6i)and Wboard.w5i=='':
            moves = '6i5i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',Wboard.w6i)and Wboard.w7i=='':
            moves = '6i7i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',Wboard.w6i)and Wboard.w6h=='':
            moves = '6i6h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',Wboard.w6i)and Wboard.w5h=='':
            moves = '6i5h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',Wboard.w6i)and Wboard.w7h=='':
            moves = '6i7h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w6i)and Wboard.w6g==''\
           and board.s6h=='':
            moves = '6i6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w6i)and Wboard.w6g==''\
           and board.s6h=='':
            moves = '6i6g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w6i)and Wboard.w6f==''\
           and board.s6h+board.s6g=='':
            moves = '6i6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w6i)and Wboard.w6f==''\
           and board.s6h+board.s6g=='':
            moves = '6i6f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w6i)and Wboard.w6e==''\
           and board.s6h+board.s6g+board.s6f=='':
            moves = '6i6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w6i)and Wboard.w6e==''\
           and board.s6h+board.s6g+board.s6f=='':
            moves = '6i6e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w6i)and Wboard.w6d==''\
           and board.s6h+board.s6g+board.s6f+board.s6e=='':
            moves = '6i6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w6i)and Wboard.w6d==''\
           and board.s6h+board.s6g+board.s6f+board.s6e=='':
            moves = '6i6d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w6i)and Wboard.w6c==''\
           and board.s6h+board.s6g+board.s6f+board.s6e+board.s6d=='':
            moves = '6i6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w6i)and Wboard.w6c==''\
           and board.s6h+board.s6g+board.s6f+board.s6e+board.s6d=='':
            moves = '6i6c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w6i)and Wboard.w6b==''\
           and board.s6h+board.s6g+board.s6f+board.s6e+board.s6d+board.s6c=='':
            moves = '6i6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w6i)and Wboard.w6b==''\
           and board.s6h+board.s6g+board.s6f+board.s6e+board.s6d+board.s6c=='':
            moves = '6i6b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w6i)and Wboard.w6a==''\
           and board.s6h+board.s6g+board.s6f+board.s6e+board.s6d+board.s6c+board.s6b=='':
            moves = '6i6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w6i)and Wboard.w6a==''\
           and board.s6h+board.s6g+board.s6f+board.s6e+board.s6d+board.s6c+board.s6b=='':
            moves = '6i6a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w6i)and Wboard.w9i==''\
           and board.s8i+board.s7i=='':
            moves = '6i9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w6i)and Wboard.w9i==''\
           and board.s8i+board.s7i=='':
            moves = '6i9i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w6i)and Wboard.w8i==''\
           and board.s7i=='':
            moves = '6i8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w6i)and Wboard.w8i==''\
           and board.s7i=='':
            moves = '6i8i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w6i)and Wboard.w4i==''\
           and board.s5i=='':
            moves = '6i4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w6i)and Wboard.w4i==''\
           and board.s5i=='':
            moves = '6i4i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w6i)and Wboard.w3i==''\
           and board.s5i+board.s4i=='':
            moves = '6i3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w6i)and Wboard.w3i==''\
           and board.s5i+board.s4i=='':
            moves = '6i3i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w6i)and Wboard.w2i==''\
           and board.s5i+board.s4i+board.s3i=='':
            moves = '6i2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w6i)and Wboard.w2i==''\
           and board.s5i+board.s4i+board.s3i=='':
            moves = '6i2i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w6i)and Wboard.w1i==''\
           and board.s5i+board.s4i+board.s3i+board.s2i=='':
            moves = '6i1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w6i)and Wboard.w1i==''\
           and board.s5i+board.s4i+board.s3i+board.s2i=='':
            moves = '6i1i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w6i)and Wboard.w4g==''\
           and board.s5h=='':
            moves = '6i4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w6i)and Wboard.w3f==''\
           and board.s5h+board.s4g=='':
            moves = '6i3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w6i)and Wboard.w2e==''\
           and board.s5h+board.s4g+board.s3f=='':
            moves = '6i2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w6i)and Wboard.w1d==''\
           and board.s5h+board.s4g+board.s3f+board.s2e=='':
            moves = '6i1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Wboard.w6i)and Wboard.w4g==''\
           and board.s5h=='':
            moves = '6i4g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w6i)and Wboard.w3f==''\
           and board.s5h+board.s4g=='':
            moves = '6i3f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w6i)and Wboard.w2e==''\
           and board.s5h+board.s4g+board.s3f=='':
            moves = '6i2e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w6i)and Wboard.w1d==''\
           and board.s5h+board.s4g+board.s3f+board.s2e=='':
            moves = '6i1d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w6i)and Wboard.w9f==''\
           and board.s8g+board.s7h=='':
            moves = '6i9f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w6i)and Wboard.w8g==''\
           and board.s7h=='':
            moves = '6i8g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w6i)and Wboard.w9f==''\
           and board.s8g+board.s7h=='':
            moves = '6i9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w6i)and Wboard.w8g==''\
           and board.s7h=='':
            moves = '6i8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w7i !='':
        if re.match(r'[gk+]',Wboard.w7i)and Wboard.w6i=='':
            moves = '7i6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',Wboard.w7i)and Wboard.w8i=='':
            moves = '7i8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',Wboard.w7i)and Wboard.w7h=='':
            moves = '7i7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w7i)and Wboard.w6h=='':
            moves = '7i6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'\+r|\+b|s|k',Wboard.w7i)and Wboard.w8h=='':
            moves = '7i8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',Wboard.w7i)and Wboard.w6i=='':
            moves = '7i6i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',Wboard.w7i)and Wboard.w8i=='':
            moves = '7i8i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',Wboard.w7i)and Wboard.w7h=='':
            moves = '7i7h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',Wboard.w7i)and Wboard.w6h=='':
            moves = '7i6h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',Wboard.w7i)and Wboard.w8h=='':
            moves = '7i8h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w7i)and Wboard.w7g==''\
           and board.s7h=='':
            moves = '7i7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w7i)and Wboard.w7g==''\
           and board.s7h=='':
            moves = '7i7g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w7i)and Wboard.w7f==''\
           and board.s7h+board.s7g=='':
            moves = '7i7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w7i)and Wboard.w7f==''\
           and board.s7h+board.s7g=='':
            moves = '7i7f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w7i)and Wboard.w7e==''\
           and board.s7h+board.s7g+board.s7f=='':
            moves = '7i7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w7i)and Wboard.w7e==''\
           and board.s7h+board.s7g+board.s7f=='':
            moves = '7i7e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w7i)and Wboard.w7d==''\
           and board.s7h+board.s7g+board.s7f+board.s7e=='':
            moves = '7i7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w7i)and Wboard.w7d==''\
           and board.s7h+board.s7g+board.s7f+board.s7e=='':
            moves = '7i7d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w7i)and Wboard.w7c==''\
           and board.s7h+board.s7g+board.s7f+board.s7e+board.s7d=='':
            moves = '7i7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w7i)and Wboard.w7c==''\
           and board.s7h+board.s7g+board.s7f+board.s7e+board.s7d=='':
            moves = '7i7c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w7i)and Wboard.w7b==''\
           and board.s7h+board.s7g+board.s7f+board.s7e+board.s7d+board.s7c=='':
            moves = '7i7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w7i)and Wboard.w7b==''\
           and board.s7h+board.s7g+board.s7f+board.s7e+board.s7d+board.s7c=='':
            moves = '7i7b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w7i)and Wboard.w7a==''\
           and board.s7h+board.s7g+board.s7f+board.s7e+board.s7d+board.s7c+board.s7b=='':
            moves = '7i7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w7i)and Wboard.w7a==''\
           and board.s7h+board.s7g+board.s7f+board.s7e+board.s7d+board.s7c+board.s7b=='':
            moves = '7i7a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w7i)and Wboard.w9i==''\
           and board.s8i=='':
            moves = '7i9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w7i)and Wboard.w9i==''\
           and board.s8i=='':
            moves = '7i9i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w7i)and Wboard.w5i==''\
           and board.s6i=='':
            moves = '7i5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w7i)and Wboard.w5i==''\
           and board.s6i=='':
            moves = '7i5i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w7i)and Wboard.w4i==''\
           and board.s6i+board.s5i=='':
            moves = '7i4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w7i)and Wboard.w4i==''\
           and board.s6i+board.s5i=='':
            moves = '7i4i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w7i)and Wboard.w3i==''\
           and board.s6i+board.s5i+board.s4i=='':
            moves = '7i3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w7i)and Wboard.w3i==''\
           and board.s6i+board.s5i+board.s4i=='':
            moves = '7i3i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w7i)and Wboard.w2i==''\
           and board.s6i+board.s5i+board.s4i+board.s3i=='':
            moves = '7i2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w7i)and Wboard.w2i==''\
           and board.s6i+board.s5i+board.s4i+board.s3i=='':
            moves = '7i2i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w7i)and Wboard.w1i==''\
           and board.s6i+board.s5i+board.s4i+board.s3i+board.s2i=='':
            moves = '7i1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w7i)and Wboard.w1i==''\
           and board.s6i+board.s5i+board.s4i+board.s3i+board.s2i=='':
            moves = '7i1i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w7i)and Wboard.w9g==''\
           and board.s8h=='':
            moves = '7i9g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w7i)and Wboard.w5g==''\
           and board.s6h=='':
            moves = '7i5g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w7i)and Wboard.w4f==''\
           and board.s6h+board.s5g=='':
            moves = '7i4f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w7i)and Wboard.w4e==''\
           and board.s6h+board.s5g+board.s4f=='':
            moves = '7i3e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w7i)and Wboard.w3d==''\
           and board.s6h+board.s5g+board.s4f+board.s3e=='':
            moves = '7i2d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w7i)and Wboard.w1c==''\
           and board.s6h+board.s5g+board.s4f+board.s3e+board.s2d=='':
            moves = '7i1c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w7i)and Wboard.w9g==''\
           and board.s8h=='':
            moves = '7i9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w7i)and Wboard.w5g==''\
           and board.s6h=='':
            moves = '7i5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w7i)and Wboard.w4f==''\
           and board.s6h+board.s5g=='':
            moves = '7i4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w7i)and Wboard.w4e==''\
           and board.s6h+board.s5g+board.s4f=='':
            moves = '7i3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w7i)and Wboard.w3d==''\
           and board.s6h+board.s5g+board.s4f+board.s3e=='':
            moves = '7i2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w7i)and Wboard.w1c==''\
           and board.s6h+board.s5g+board.s4f+board.s3e+board.s2d=='':
            moves = '7i1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w8i !='':
        if re.match(r'[gk+]',Wboard.w8i)and Wboard.w7i=='':
            moves = '8i7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',Wboard.w8i)and Wboard.w9i=='':
            moves = '8i9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',Wboard.w8i)and Wboard.w8h=='':
            moves = '8i8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w8i)and Wboard.w7h=='':
            moves = '8i7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'\+r|\+b|s|k',Wboard.w8i)and Wboard.w9h=='':
            moves = '8i9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',Wboard.w8i)and Wboard.w7i=='':
            moves = '8i7i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',Wboard.w8i)and Wboard.w9i=='':
            moves = '8i9i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',Wboard.w8i)and Wboard.w8h=='':
            moves = '8i8h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',Wboard.w8i)and Wboard.w7h=='':
            moves = '8i7h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',Wboard.w8i)and Wboard.w9h=='':
            moves = '8i9h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w8i)and Wboard.w8g==''\
           and board.s8h=='':
            moves = '8i8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w8i)and Wboard.w8g==''\
           and board.s8h=='':
            moves = '8i8g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w8i)and Wboard.w8f==''\
           and board.s8h+board.s8g=='':
            moves = '8i8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w8i)and Wboard.w8f==''\
           and board.s8h+board.s8g=='':
            moves = '8i8f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w8i)and Wboard.w8e==''\
           and board.s8h+board.s8g+board.s8f=='':
            moves = '8i8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w8i)and Wboard.w8e==''\
           and board.s8h+board.s8g+board.s8f=='':
            moves = '8i8e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w8i)and Wboard.w8d==''\
           and board.s8h+board.s8g+board.s8f+board.s8e=='':
            moves = '8i8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w8i)and Wboard.w8d==''\
           and board.s8h+board.s8g+board.s8f+board.s8e=='':
            moves = '8i8d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w8i)and Wboard.w8c==''\
           and board.s8h+board.s8g+board.s8f+board.s8e+board.s8d=='':
            moves = '8i8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w8i)and Wboard.w8c==''\
           and board.s8h+board.s8g+board.s8f+board.s8e+board.s8d=='':
            moves = '8i8c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w8i)and Wboard.w8b==''\
           and board.s8h+board.s8g+board.s8f+board.s8e+board.s8d+board.s8c=='':
            moves = '8i8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w8i)and Wboard.w8b==''\
           and board.s8h+board.s8g+board.s8f+board.s8e+board.s8d+board.s8c=='':
            moves = '8i8b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w8i)and Wboard.w8a==''\
           and board.s8h+board.s8g+board.s8f+board.s8e+board.s8d+board.s8c+board.s8b=='':
            moves = '8i8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w8i)and Wboard.w8a==''\
           and board.s8h+board.s8g+board.s8f+board.s8e+board.s8d+board.s8c+board.s8b=='':
            moves = '8i8a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w8i)and Wboard.w6i==''\
           and board.s7i=='':
            moves = '8i6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w8i)and Wboard.w6i==''\
           and board.s7i=='':
            moves = '8i6i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w8i)and Wboard.w5i==''\
           and board.s7i+board.s6i=='':
            moves = '8i5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w8i)and Wboard.w5i==''\
           and board.s7i+board.s6i=='':
            moves = '8i5i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w8i)and Wboard.w4i==''\
           and board.s7i+board.s6i+board.s5i=='':
            moves = '8i4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w8i)and Wboard.w4i==''\
           and board.s7i+board.s6i+board.s5i=='':
            moves = '8i4i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w8i)and Wboard.w3i==''\
           and board.s7i+board.s6i+board.s5i+board.s4i=='':
            moves = '8i3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w8i)and Wboard.w3i==''\
           and board.s7i+board.s6i+board.s5i+board.s4i=='':
            moves = '8i3i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w8i)and Wboard.w2i==''\
           and board.s7i+board.s6i+board.s5i+board.s4i+board.s3i=='':
            moves = '8i2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w8i)and Wboard.w2i==''\
           and board.s7i+board.s6i+board.s5i+board.s4i+board.s3i=='':
            moves = '8i2i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w8i)and Wboard.w1i==''\
           and board.s7i+board.s6i+board.s5i+board.s4i+board.s3i+board.s2i=='':
            moves = '8i1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w8i)and Wboard.w1i==''\
           and board.s7i+board.s6i+board.s5i+board.s4i+board.s3i+board.s2i=='':
            moves = '8i1i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w8i)and Wboard.w6g==''\
           and board.s7h=='':
            moves = '8i6g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w8i)and Wboard.w5f==''\
           and board.s7h+board.s6g=='':
            moves = '8i5f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w8i)and Wboard.w4e==''\
           and board.s7h+board.s6g+board.s5f=='':
            moves = '8i4e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w8i)and Wboard.w3d==''\
           and board.s7h+board.s6g+board.s5f+board.s4e=='':
            moves = '8i3d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w8i)and Wboard.w2c==''\
           and board.s7h+board.s6g+board.s5f+board.s4e+board.s3d=='':
            moves = '8i2c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w8i)and Wboard.w1b==''\
           and board.s7h+board.s6g+board.s5f+board.s4e+board.s3d+board.s2c=='':
            moves = '8i1b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w8i)and Wboard.w6g==''\
           and board.s7h=='':
            moves = '8i6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w8i)and Wboard.w5f==''\
           and board.s7h+board.s6g=='':
            moves = '8i5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w8i)and Wboard.w4e==''\
           and board.s7h+board.s6g+board.s5f=='':
            moves = '8i4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w8i)and Wboard.w3d==''\
           and board.s7h+board.s6g+board.s5f+board.s4e=='':
            moves = '8i3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w8i)and Wboard.w2c==''\
           and board.s7h+board.s6g+board.s5f+board.s4e+board.s3d=='':
            moves = '8i2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w8i)and Wboard.w1b==''\
           and board.s7h+board.s6g+board.s5f+board.s4e+board.s3d+board.s2c=='':
            moves = '8i1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w9i !='':
        if re.match(r'[gk+]',Wboard.w9i)and Wboard.w8i=='':
            moves = '9i8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',Wboard.w9i)and Wboard.w9h=='':
            moves = '9i9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w9i)and Wboard.w8h=='':
            moves = '9i8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('r',Wboard.w9i)and Wboard.w8i=='':
            moves = '9i8i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',Wboard.w9i)and Wboard.w9h=='':
            moves = '9i9h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',Wboard.w9i)and Wboard.w8h=='':
            moves = '9i8h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w9i)and Wboard.w9g==''\
           and board.s9h=='':
            moves = '9i9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w9i)and Wboard.w9g==''\
           and board.s9h=='':
            moves = '9i9g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w9i)and Wboard.w9f==''\
           and board.s9h+board.s9g=='':
            moves = '9i9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w9i)and Wboard.w9f==''\
           and board.s9h+board.s9g=='':
            moves = '9i9f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w9i)and Wboard.w9e==''\
           and board.s9h+board.s9g+board.s9f=='':
            moves = '9i9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w9i)and Wboard.w9e==''\
           and board.s9h+board.s9g+board.s9f=='':
            moves = '9i9e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w9i)and Wboard.w9d==''\
           and board.s9h+board.s9g+board.s9f+board.s9e=='':
            moves = '9i9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w9i)and Wboard.w9d==''\
           and board.s9h+board.s9g+board.s9f+board.s9e=='':
            moves = '9i9d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w9i)and Wboard.w9c==''\
           and board.s9h+board.s9g+board.s9f+board.s9e+board.s9d=='':
            moves = '9i9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w9i)and Wboard.w9c==''\
           and board.s9h+board.s9g+board.s9f+board.s9e+board.s9d=='':
            moves = '9i9c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w9i)and Wboard.w9b==''\
           and board.s9h+board.s9g+board.s9f+board.s9e+board.s9d+board.s9c=='':
            moves = '9i9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w9i)and Wboard.w9b==''\
           and board.s9h+board.s9g+board.s9f+board.s9e+board.s9d+board.s9c=='':
            moves = '9i9b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w9i)and Wboard.w9a==''\
           and board.s9h+board.s9g+board.s9f+board.s9e+board.s9d+board.s9c+board.s9b=='':
            moves = '9i9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w9i)and Wboard.w9a==''\
           and board.s9h+board.s9g+board.s9f+board.s9e+board.s9d+board.s9c+board.s9b=='':
            moves = '9i9a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w9i)and Wboard.w7i==''\
           and board.s8i=='':
            moves = '9i7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w9i)and Wboard.w7i==''\
           and board.s8i=='':
            moves = '9i7i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w9i)and Wboard.w6i==''\
           and board.s8i+board.s7i=='':
            moves = '9i6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w9i)and Wboard.w6i==''\
           and board.s8i+board.s7i=='':
            moves = '9i6i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w9i)and Wboard.w5i==''\
           and board.s8i+board.s7i+board.s6i=='':
            moves = '9i5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w9i)and Wboard.w5i==''\
           and board.s8i+board.s7i+board.s6i=='':
            moves = '9i5i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w9i)and Wboard.w4i==''\
           and board.s8i+board.s7i+board.s6i+board.s5i=='':
            moves = '9i4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w9i)and Wboard.w4i==''\
           and board.s8i+board.s7i+board.s6i+board.s5i=='':
            moves = '9i4i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w9i)and Wboard.w3i==''\
           and board.s8i+board.s7i+board.s6i+board.s5i+board.s4i=='':
            moves = '9i3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w9i)and Wboard.w3i==''\
           and board.s8i+board.s7i+board.s6i+board.s5i+board.s4i=='':
            moves = '9i3i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w9i)and Wboard.w2i==''\
           and board.s8i+board.s7i+board.s6i+board.s5i+board.s4i+board.s3i=='':
            moves = '9i2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w9i)and Wboard.w2i==''\
           and board.s8i+board.s7i+board.s6i+board.s5i+board.s4i+board.s3i=='':
            moves = '9i2i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w9i)and Wboard.w1i==''\
           and board.s8i+board.s7i+board.s6i+board.s5i+board.s4i+board.s3i+board.s2i=='':
            moves = '9i1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w9i)and Wboard.w1i==''\
           and board.s8i+board.s7i+board.s6i+board.s5i+board.s4i+board.s3i+board.s2i=='':
            moves = '9i1i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w9i)and Wboard.w7g==''\
           and board.s8h=='':
            moves = '9i7g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w9i)and Wboard.w6f==''\
           and board.s8h+board.s7g=='':
            moves = '9i6f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w9i)and Wboard.w5e==''\
           and board.s8h+board.s7g+board.s6f=='':
            moves = '9i5e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w9i)and Wboard.w4d==''\
           and board.s8h+board.s7g+board.s6f+board.s5e=='':
            moves = '9i4d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w9i)and Wboard.w3c==''\
           and board.s8h+board.s7g+board.s6f+board.s5e+board.s4d=='':
            moves = '9i3c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w9i)and Wboard.w2b==''\
           and board.s8h+board.s7g+board.s6f+board.s5e+board.s4d+board.s3c=='':
            moves = '9i2b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w9i)and Wboard.w1a==''\
           and board.s8h+board.s7g+board.s6f+board.s5e+board.s4d+board.s3c+board.s2b=='':
            moves = '9i1a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w9i)and Wboard.w7g==''\
           and board.s8h=='':
            moves = '9i7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w9i)and Wboard.w6f==''\
           and board.s8h+board.s7g=='':
            moves = '9i6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w9i)and Wboard.w5e==''\
           and board.s8h+board.s7g+board.s6f=='':
            moves = '9i5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w9i)and Wboard.w4d==''\
           and board.s8h+board.s7g+board.s6f+board.s5e=='':
            moves = '9i4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w9i)and Wboard.w3c==''\
           and board.s8h+board.s7g+board.s6f+board.s5e+board.s4d=='':
            moves = '9i3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w9i)and Wboard.w2b==''\
           and board.s8h+board.s7g+board.s6f+board.s5e+board.s4d+board.s3c=='':
            moves = '9i2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w9i)and Wboard.w1a==''\
           and board.s8h+board.s7g+board.s6f+board.s5e+board.s4d+board.s3c+board.s2b=='':
            moves = '9i1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w1h !='':
        if re.match(r'[sgk+]',Wboard.w1h)and Wboard.w1i=='':
            moves = '1h1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgk+]',Wboard.w1h)and Wboard.w2i=='':
            moves = '1h2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',Wboard.w1h)and Wboard.w2h=='':
            moves = '1h2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',Wboard.w1h)and Wboard.w1g=='':
            moves = '1h1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w1h)and Wboard.w2g=='':
            moves = '1h2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[plsr]',Wboard.w1h)and Wboard.w1i=='':
            moves = '1h1i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',Wboard.w1h)and Wboard.w2i=='':
            moves = '1h2i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('r',Wboard.w1h)and Wboard.w2h=='':
            moves = '1h2h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',Wboard.w1h)and Wboard.w1g=='':
            moves = '1h1g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',Wboard.w1h)and Wboard.w2g=='':
            moves = '1h2g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w1h)and Wboard.w1f==''\
           and board.s1e=='':
            moves = '1h1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w1h)and Wboard.w1f==''\
           and board.s1e=='':
            moves = '1h1f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w1h)and Wboard.w1e==''\
           and board.s1g+board.s1f=='':
            moves = '1h1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w1h)and Wboard.w1e==''\
           and board.s1g+board.s1f=='':
            moves = '1h1e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w1h)and Wboard.w1d==''\
           and board.s1g+board.s1f+board.s1e=='':
            moves = '1h1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w1h)and Wboard.w1d==''\
           and board.s1g+board.s1f+board.s1e=='':
            moves = '1h1d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w1h)and Wboard.w1c==''\
           and board.s1g+board.s1f+board.s1e+board.s1d=='':
            moves = '1h1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w1h)and Wboard.w1c==''\
           and board.s1g+board.s1f+board.s1e+board.s1d=='':
            moves = '1h1c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w1h)and Wboard.w1b==''\
           and board.s1g+board.s1f+board.s1e+board.s1d+board.s1c=='':
            moves = '1h1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w1h)and Wboard.w1b==''\
           and board.s1g+board.s1f+board.s1e+board.s1d+board.s1c=='':
            moves = '1h1b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w1h)and Wboard.w1a==''\
           and board.s1g+board.s1f+board.s1e+board.s1d+board.s1c+board.s1b=='':
            moves = '1h1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w1h)and Wboard.w1a==''\
           and board.s1g+board.s1f+board.s1e+board.s1d+board.s1c+board.s1b=='':
            moves = '1h1a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w1h)and Wboard.w3h==''\
           and board.s2h=='':
            moves = '1h3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w1h)and Wboard.w3h==''\
           and board.s2h=='':
            moves = '1h3h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w1h)and Wboard.w4h==''\
           and board.s2h+board.s3h=='':
            moves = '1h4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w1h)and Wboard.w4h==''\
           and board.s2h+board.s3h=='':
            moves = '1h4h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w1h)and Wboard.w5h==''\
           and board.s2h+board.s3h+board.s4h=='':
            moves = '1h5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w1h)and Wboard.w5h==''\
           and board.s2h+board.s3h+board.s4h=='':
            moves = '1h5h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w1h)and Wboard.w6h==''\
           and board.s2h+board.s3h+board.s4h+board.s5h=='':
            moves = '1h6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w1h)and Wboard.w6h==''\
           and board.s2h+board.s3h+board.s4h+board.s5h=='':
            moves = '1h6h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w1h)and Wboard.w7h==''\
           and board.s2h+board.s3h+board.s4h+board.s5h+board.s6h=='':
            moves = '1h7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w1h)and Wboard.w7h==''\
           and board.s2h+board.s3h+board.s4h+board.s5h+board.s6h=='':
            moves = '1h7h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w1h)and Wboard.w8h==''\
           and board.s2h+board.s3h+board.s4h+board.s5h+board.s6h+board.s7h=='':
            moves = '1h8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w1h)and Wboard.w8h==''\
           and board.s2h+board.s3h+board.s4h+board.s5h+board.s6h+board.s7h=='':
            moves = '1h8h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w1h)and Wboard.w9h==''\
           and board.s2h+board.s3h+board.s4h+board.s5h+board.s6h+board.s7h+board.s8h=='':
            moves = '1h9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w1h)and Wboard.w9h==''\
           and board.s2h+board.s3h+board.s4h+board.s5h+board.s6h+board.s7h+board.s8h=='':
            moves = '1h9h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w1h)and Wboard.w3f==''\
           and board.s2g=='':
            moves = '1h3f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w1h)and Wboard.w4e==''\
           and board.s2g+board.s3f=='':
            moves = '1h4e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w1h)and Wboard.w5d==''\
           and board.s2g+board.s3f+board.s4e=='':
            moves = '1h5d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w1h)and Wboard.w6c==''\
           and board.s2g+board.s3f+board.s4e+board.s5d=='':
            moves = '1h6c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w1h)and Wboard.w7b==''\
           and board.s2g+board.s3f+board.s4e+board.s5d+board.s6c=='':
            moves = '1h7b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w1h)and Wboard.w8a==''\
           and board.s2g+board.s3f+board.s4e+board.s5d+board.s6c+board.s7b=='':
            moves = '1h8a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w1h)and Wboard.w3f==''\
           and board.s2g=='':
            moves = '1h3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w1h)and Wboard.w4e==''\
           and board.s2g+board.s3f=='':
            moves = '1h4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w1h)and Wboard.w5d==''\
           and board.s2g+board.s3f+board.s4e=='':
            moves = '1h5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w1h)and Wboard.w6c==''\
           and board.s2g+board.s3f+board.s4e+board.s5d=='':
            moves = '1h6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w1h)and Wboard.w7b==''\
           and board.s2g+board.s3f+board.s4e+board.s5d+board.s6c=='':
            moves = '1h7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w1h)and Wboard.w8a==''\
           and board.s2g+board.s3f+board.s4e+board.s5d+board.s6c+board.s7b=='':
            moves = '1h8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w2h !='':
        if re.match(r'[sgk+]',Wboard.w2h)and Wboard.w2i=='':
            moves = '2h2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgk+]',Wboard.w2h)and Wboard.w1i=='':
            moves = '2h1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgk+]',Wboard.w2h)and Wboard.w3i=='':
            moves = '2h3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',Wboard.w2h)and Wboard.w1h=='':
            moves = '2h1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',Wboard.w2h)and Wboard.w3h=='':
            moves = '2h3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',Wboard.w2h)and Wboard.w2g=='':
            moves = '2h2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w2h)and Wboard.w1g=='':
            moves = '2h1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w2h)and Wboard.w3g=='':
            moves = '2h3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[plsr]',Wboard.w2h)and Wboard.w2i=='':
            moves = '2h2i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',Wboard.w2h)and Wboard.w1i=='':
            moves = '2h1i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'[bs]',Wboard.w2h)and Wboard.w3i=='':
            moves = '2h3i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('r',Wboard.w2h)and Wboard.w1h=='':
            moves = '2h1h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',Wboard.w2h)and Wboard.w3h=='':
            moves = '2h3h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',Wboard.w2h)and Wboard.w2g=='':
            moves = '2h2g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',Wboard.w2h)and Wboard.w1g=='':
            moves = '2h1g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',Wboard.w2h)and Wboard.w3g=='':
            moves = '2h3g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w2h)and Wboard.w2f==''\
           and board.s2e=='':
            moves = '2h2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w2h)and Wboard.w2f==''\
           and board.s2e=='':
            moves = '2h2f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w2h)and Wboard.w2e==''\
           and board.s2g+board.s2f=='':
            moves = '2h2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w2h)and Wboard.w2e==''\
           and board.s2g+board.s2f=='':
            moves = '2h2e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w2h)and Wboard.w2d==''\
           and board.s2g+board.s2f+board.s2e=='':
            moves = '2h2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w2h)and Wboard.w2d==''\
           and board.s2g+board.s2f+board.s2e=='':
            moves = '2h2d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w2h)and Wboard.w2c==''\
           and board.s2g+board.s2f+board.s2e+board.s2d=='':
            moves = '2h2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w2h)and Wboard.w2c==''\
           and board.s2g+board.s2f+board.s2e+board.s2d=='':
            moves = '2h2c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w2h)and Wboard.w2b==''\
           and board.s2g+board.s2f+board.s2e+board.s2d+board.s2c=='':
            moves = '2h2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w2h)and Wboard.w2b==''\
           and board.s2g+board.s2f+board.s2e+board.s2d+board.s2c=='':
            moves = '2h2b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w2h)and Wboard.w2a==''\
           and board.s2g+board.s2f+board.s2e+board.s2d+board.s2c+board.s2b=='':
            moves = '2h2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w2h)and Wboard.w2a==''\
           and board.s2g+board.s2f+board.s2e+board.s2d+board.s2c+board.s2b=='':
            moves = '2h2a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w2h)and Wboard.w4h==''\
           and board.s3h=='':
            moves = '2h4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w2h)and Wboard.w4h==''\
           and board.s3h=='':
            moves = '2h4h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w2h)and Wboard.w5h==''\
           and board.s3h+board.s4h=='':
            moves = '2h5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w2h)and Wboard.w5h==''\
           and board.s3h+board.s4h=='':
            moves = '2h5h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w2h)and Wboard.w6h==''\
           and board.s3h+board.s4h+board.s5h=='':
            moves = '2h6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w2h)and Wboard.w6h==''\
           and board.s3h+board.s4h+board.s5h=='':
            moves = '2h6h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w2h)and Wboard.w7h==''\
           and board.s3h+board.s4h+board.s5h+board.s6h=='':
            moves = '2h7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w2h)and Wboard.w7h==''\
           and board.s3h+board.s4h+board.s5h+board.s6h=='':
            moves = '2h7h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w2h)and Wboard.w8h==''\
           and board.s3h+board.s4h+board.s5h+board.s6h+board.s7h=='':
            moves = '2h8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w2h)and Wboard.w8h==''\
           and board.s3h+board.s4h+board.s5h+board.s6h+board.s7h=='':
            moves = '2h8h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w2h)and Wboard.w9h==''\
           and board.s3h+board.s4h+board.s5h+board.s6h+board.s7h+board.s8h=='':
            moves = '2h9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w2h)and Wboard.w9h==''\
           and board.s3h+board.s4h+board.s5h+board.s6h+board.s7h+board.s8h=='':
            moves = '2h9h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w2h)and Wboard.w4f==''\
           and board.s3g=='':
            moves = '2h4f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w2h)and Wboard.w5e==''\
           and board.s3g+board.s4f=='':
            moves = '2h5e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w2h)and Wboard.w6d==''\
           and board.s3g+board.s4f+board.s5e=='':
            moves = '2h6d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w2h)and Wboard.w7c==''\
           and board.s3g+board.s4f+board.s5e+board.s6d=='':
            moves = '2h7c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w2h)and Wboard.w8b==''\
           and board.s3g+board.s4f+board.s5e+board.s6d+board.s7c=='':
            moves = '2h8b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w2h)and Wboard.w9a==''\
           and board.s3g+board.s4f+board.s5e+board.s6d+board.s7c+board.s8b=='':
            moves = '2h9a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w2h)and Wboard.w4f==''\
           and board.s3g=='':
            moves = '2h4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w2h)and Wboard.w5e==''\
           and board.s3g+board.s4f=='':
            moves = '2h5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w2h)and Wboard.w6d==''\
           and board.s3g+board.s4f+board.s5e=='':
            moves = '2h6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w2h)and Wboard.w7c==''\
           and board.s3g+board.s4f+board.s5e+board.s6d=='':
            moves = '2h7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w2h)and Wboard.w8b==''\
           and board.s3g+board.s4f+board.s5e+board.s6d+board.s7c=='':
            moves = '2h8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w2h)and Wboard.w9a==''\
           and board.s3g+board.s4f+board.s5e+board.s6d+board.s7c+board.s8b=='':
            moves = '2h9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w3h !='':
        if re.match(r'[sgk+]',Wboard.w3h)and Wboard.w3i=='':
            moves = '3h3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgk+]',Wboard.w3h)and Wboard.w2i=='':
            moves = '3h2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgk+]',Wboard.w3h)and Wboard.w4i=='':
            moves = '3h4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',Wboard.w3h)and Wboard.w2h=='':
            moves = '3h2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',Wboard.w3h)and Wboard.w4h=='':
            moves = '3h4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',Wboard.w3h)and Wboard.w3g=='':
            moves = '3h3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w3h)and Wboard.w2g=='':
            moves = '3h2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w3h)and Wboard.w4g=='':
            moves = '3h4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[plsr]',Wboard.w3h)and Wboard.w3i=='':
            moves = '3h3i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',Wboard.w3h)and Wboard.w2i=='':
            moves = '3h2i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'[bs]',Wboard.w3h)and Wboard.w4i=='':
            moves = '3h4i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('r',Wboard.w3h)and Wboard.w2h=='':
            moves = '3h2h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',Wboard.w3h)and Wboard.w4h=='':
            moves = '3h4h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',Wboard.w3h)and Wboard.w3g=='':
            moves = '3h3g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',Wboard.w3h)and Wboard.w2g=='':
            moves = '3h2g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',Wboard.w3h)and Wboard.w4g=='':
            moves = '3h4g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w3h)and Wboard.w3f==''\
           and board.s3e=='':
            moves = '3h3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w3h)and Wboard.w3f==''\
           and board.s3e=='':
            moves = '3h3f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w3h)and Wboard.w3e==''\
           and board.s3g+board.s3f=='':
            moves = '3h3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w3h)and Wboard.w3e==''\
           and board.s3g+board.s3f=='':
            moves = '3h3e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w3h)and Wboard.w3d==''\
           and board.s3g+board.s3f+board.s3e=='':
            moves = '3h3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w3h)and Wboard.w3d==''\
           and board.s3g+board.s3f+board.s3e=='':
            moves = '3h3d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w3h)and Wboard.w3c==''\
           and board.s3g+board.s3f+board.s3e+board.s3d=='':
            moves = '3h3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w3h)and Wboard.w3c==''\
           and board.s3g+board.s3f+board.s3e+board.s3d=='':
            moves = '3h3c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w3h)and Wboard.w3b==''\
           and board.s3g+board.s3f+board.s3e+board.s3d+board.s3c=='':
            moves = '3h3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w3h)and Wboard.w3b==''\
           and board.s3g+board.s3f+board.s3e+board.s3d+board.s3c=='':
            moves = '3h3b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w3h)and Wboard.w3a==''\
           and board.s3g+board.s3f+board.s3e+board.s3d+board.s3c+board.s3b=='':
            moves = '3h3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w3h)and Wboard.w3a==''\
           and board.s3g+board.s3f+board.s3e+board.s3d+board.s3c+board.s3b=='':
            moves = '3h3a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w3h)and Wboard.w1h==''\
           and board.s2h=='':
            moves = '3h1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w3h)and Wboard.w1h==''\
           and board.s2h=='':
            moves = '3h1h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w3h)and Wboard.w5h==''\
           and board.s4h=='':
            moves = '3h5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w3h)and Wboard.w5h==''\
           and board.s4h=='':
            moves = '3h5h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w3h)and Wboard.w6h==''\
           and board.s4h+board.s5h=='':
            moves = '3h6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w3h)and Wboard.w6h==''\
           and board.s4h+board.s5h=='':
            moves = '3h6h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w3h)and Wboard.w7h==''\
           and board.s4h+board.s5h+board.s6h=='':
            moves = '3h7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w3h)and Wboard.w7h==''\
           and board.s4h+board.s5h+board.s6h=='':
            moves = '3h7h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w3h)and Wboard.w8h==''\
           and board.s4h+board.s5h+board.s6h+board.s7h=='':
            moves = '3h8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w3h)and Wboard.w8h==''\
           and board.s4h+board.s5h+board.s6h+board.s7h=='':
            moves = '3h8h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w3h)and Wboard.w9h==''\
           and board.s4h+board.s5h+board.s6h+board.s7h+board.s8h=='':
            moves = '3h9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w3h)and Wboard.w9h==''\
           and board.s4h+board.s5h+board.s6h+board.s7h+board.s8h=='':
            moves = '3h9h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w3h)and Wboard.w5f==''\
           and board.s4g=='':
            moves = '3h5f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w3h)and Wboard.w6e==''\
           and board.s4g+board.s5f=='':
            moves = '3h6e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w3h)and Wboard.w7d==''\
           and board.s4g+board.s5f+board.s6e=='':
            moves = '3h7d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w3h)and Wboard.w8c==''\
           and board.s4g+board.s5f+board.s6e+board.s7d=='':
            moves = '3h8c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w3h)and Wboard.w9b==''\
           and board.s4g+board.s5f+board.s6e+board.s7d+board.s8c=='':
            moves = '3h9b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w3h)and Wboard.w5f==''\
           and board.s4g=='':
            moves = '3h5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w3h)and Wboard.w6e==''\
           and board.s4g+board.s5f=='':
            moves = '3h6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w3h)and Wboard.w7d==''\
           and board.s4g+board.s5f+board.s6e=='':
            moves = '3h7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w3h)and Wboard.w8c==''\
           and board.s4g+board.s5f+board.s6e+board.s7d=='':
            moves = '3h8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w3h)and Wboard.w9b==''\
           and board.s4g+board.s5f+board.s6e+board.s7d+board.s8c=='':
            moves = '3h9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w3h)and Wboard.w1f==''\
           and board.s2g=='':
            moves = '3h1f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w3h)and Wboard.w1f==''\
           and board.s2g=='':
            moves = '3h1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w4h !='':
        if re.match(r'[sgk+]',    Wboard.w4h)and Wboard.w4i=='':
            moves = '4h4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgk+]',    Wboard.w4h)and Wboard.w3i=='':
            moves = '4h3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgk+]',    Wboard.w4h)and Wboard.w5i=='':
            moves = '4h5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w4h)and Wboard.w3h=='':
            moves = '4h3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w4h)and Wboard.w5h=='':
            moves = '4h5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w4h)and Wboard.w4g=='':
            moves = '4h4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w4h)and Wboard.w3g=='':
            moves = '4h3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w4h)and Wboard.w5g=='':
            moves = '4h5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[plsr]',   Wboard.w4h)and Wboard.w4i=='':
            moves = '4h4i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',     Wboard.w4h)and Wboard.w3i=='':
            moves = '4h3i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'[bs]',     Wboard.w4h)and Wboard.w5i=='':
            moves = '4h5i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('r',         Wboard.w4h)and Wboard.w3h=='':
            moves = '4h3h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',         Wboard.w4h)and Wboard.w5h=='':
            moves = '4h5h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',         Wboard.w4h)and Wboard.w4g=='':
            moves = '4h4g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',     Wboard.w4h)and Wboard.w3g=='':
            moves = '4h3g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',     Wboard.w4h)and Wboard.w5g=='':
            moves = '4h5g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w4h)and Wboard.w4f==''\
           and board.s4e=='':
            moves = '4h4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w4h)and Wboard.w4f==''\
           and board.s4e=='':
            moves = '4h4f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w4h)and Wboard.w4e==''\
           and board.s4g+board.s4f=='':
            moves = '4h4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w4h)and Wboard.w4e==''\
           and board.s4g+board.s4f=='':
            moves = '4h4e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w4h)and Wboard.w4d==''\
           and board.s4g+board.s4f+board.s4e=='':
            moves = '4h4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w4h)and Wboard.w4d==''\
           and board.s4g+board.s4f+board.s4e=='':
            moves = '4h4d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w4h)and Wboard.w4c==''\
           and board.s4g+board.s4f+board.s4e+board.s4d=='':
            moves = '4h4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w4h)and Wboard.w4c==''\
           and board.s4g+board.s4f+board.s4e+board.s4d=='':
            moves = '4h4c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w4h)and Wboard.w4b==''\
           and board.s4g+board.s4f+board.s4e+board.s4d+board.s4c=='':
            moves = '4h4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w4h)and Wboard.w4b==''\
           and board.s4g+board.s4f+board.s4e+board.s4d+board.s4c=='':
            moves = '4h4b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w4h)and Wboard.w4a==''\
           and board.s4g+board.s4f+board.s4e+board.s4d+board.s4c+board.s4b=='':
            moves = '4h4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w4h)and Wboard.w4a==''\
           and board.s4g+board.s4f+board.s4e+board.s4d+board.s4c+board.s4b=='':
            moves = '4h4a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w4h)and Wboard.w1h==''\
           and board.s2h+board.s3h=='':
            moves = '4h1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w4h)and Wboard.w1h==''\
           and board.s2h+board.s3h=='':
            moves = '4h1h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w4h)and Wboard.w5h==''\
           and board.s3h=='':
            moves = '4h2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w4h)and Wboard.w5h==''\
           and board.s3h=='':
            moves = '4h2h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w4h)and Wboard.w6h==''\
           and board.s5h=='':
            moves = '4h6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w4h)and Wboard.w6h==''\
           and board.s5h=='':
            moves = '4h6h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w4h)and Wboard.w7h==''\
           and board.s5h+board.s6h=='':
            moves = '4h7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w4h)and Wboard.w7h==''\
           and board.s5h+board.s6h=='':
            moves = '4h7h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w4h)and Wboard.w8h==''\
           and board.s5h+board.s6h+board.s7h=='':
            moves = '4h8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w4h)and Wboard.w8h==''\
           and board.s5h+board.s6h+board.s7h=='':
            moves = '4h8h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w4h)and Wboard.w9h==''\
           and board.s5h+board.s6h+board.s7h+board.s8h=='':
            moves = '4h9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w4h)and Wboard.w9h==''\
           and board.s5h+board.s6h+board.s7h+board.s8h=='':
            moves = '4h9h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w4h)and Wboard.w6f==''\
           and board.s5g=='':
            moves = '4h6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w4h)and Wboard.w7e==''\
           and board.s5g+board.s6f=='':
            moves = '4h7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w4h)and Wboard.w8d==''\
           and board.s5g+board.s6f+board.s7e=='':
            moves = '4h8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w4h)and Wboard.w9c==''\
           and board.s5g+board.s6f+board.s7e+board.s8d=='':
            moves = '4h9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Wboard.w4h)and Wboard.w6f==''\
           and board.s5g=='':
            moves = '4h6f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w4h)and Wboard.w7e==''\
           and board.s5g+board.s6f=='':
            moves = '4h7e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w4h)and Wboard.w8d==''\
           and board.s5g+board.s6f+board.s7e=='':
            moves = '4h8d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w4h)and Wboard.w9c==''\
           and board.s5g+board.s6f+board.s7e+board.s8d=='':
            moves = '4h9c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w4h)and Wboard.w1e==''\
           and board.s2f+board.s3g=='':
            moves = '4h1e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w4h)and Wboard.w2f==''\
           and board.s3g=='':
            moves = '4h2f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w4h)and Wboard.w1e==''\
           and board.s2f+board.s3g=='':
            moves = '4h1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w4h)and Wboard.w2f==''\
           and board.s3g=='':
            moves = '4h2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w5h !='':
        if re.match(r'[sgk+]',    Wboard.w5h)and Wboard.w5i=='':
            moves = '5h5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgk+]',    Wboard.w5h)and Wboard.w4i=='':
            moves = '5h4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgk+]',    Wboard.w5h)and Wboard.w6i=='':
            moves = '5h6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w5h)and Wboard.w4h=='':
            moves = '5h4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w5h)and Wboard.w6h=='':
            moves = '5h6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w5h)and Wboard.w5g=='':
            moves = '5h5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w5h)and Wboard.w4g=='':
            moves = '5h4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w5h)and Wboard.w6g=='':
            moves = '5h6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[plsr]',   Wboard.w5h)and Wboard.w5i=='':
            moves = '5h5i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',     Wboard.w5h)and Wboard.w4i=='':
            moves = '5h4i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'[bs]',     Wboard.w5h)and Wboard.w6i=='':
            moves = '5h6i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('r',         Wboard.w5h)and Wboard.w4h=='':
            moves = '5h4h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',         Wboard.w5h)and Wboard.w6h=='':
            moves = '5h6h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',         Wboard.w5h)and Wboard.w5g=='':
            moves = '5h5g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',     Wboard.w5h)and Wboard.w4g=='':
            moves = '5h4g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',     Wboard.w5h)and Wboard.w6g=='':
            moves = '5h6g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w5h)and Wboard.w5f==''\
           and board.s5e=='':
            moves = '5h5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w5h)and Wboard.w5f==''\
           and board.s5e=='':
            moves = '5h5f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w5h)and Wboard.w5e==''\
           and board.s5g+board.s5f=='':
            moves = '5h5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w5h)and Wboard.w5e==''\
           and board.s5g+board.s5f=='':
            moves = '5h5e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w5h)and Wboard.w5d==''\
           and board.s5g+board.s5f+board.s5e=='':
            moves = '5h5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w5h)and Wboard.w5d==''\
           and board.s5g+board.s5f+board.s5e=='':
            moves = '5h5d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w5h)and Wboard.w5c==''\
           and board.s5g+board.s5f+board.s5e+board.s5d=='':
            moves = '5h5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w5h)and Wboard.w5c==''\
           and board.s5g+board.s5f+board.s5e+board.s5d=='':
            moves = '5h5c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w5h)and Wboard.w5b==''\
           and board.s5g+board.s5f+board.s5e+board.s5d+board.s5c=='':
            moves = '5h5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w5h)and Wboard.w5b==''\
           and board.s5g+board.s5f+board.s5e+board.s5d+board.s5c=='':
            moves = '5h5b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w5h)and Wboard.w5a==''\
           and board.s5g+board.s5f+board.s5e+board.s5d+board.s5c+board.s5b=='':
            moves = '5h5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w5h)and Wboard.w5a==''\
           and board.s5g+board.s5f+board.s5e+board.s5d+board.s5c+board.s5b=='':
            moves = '5h5a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w5h)and Wboard.w1h==''\
           and board.s2h+board.s3h+board.s4h=='':
            moves = '5h1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w5h)and Wboard.w1h==''\
           and board.s2h+board.s3h+board.s4h=='':
            moves = '5h1h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w5h)and Wboard.w2h==''\
           and board.s3h+board.s4h=='':
            moves = '5h2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w5h)and Wboard.w2h==''\
           and board.s3h+board.s4h=='':
            moves = '5h2h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w5h)and Wboard.w3h==''\
           and board.s4h=='':
            moves = '5h3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w5h)and Wboard.w3h==''\
           and board.s4h=='':
            moves = '5h3h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w5h)and Wboard.w7h==''\
           and board.s6h=='':
            moves = '5h7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w5h)and Wboard.w7h==''\
           and board.s6h=='':
            moves = '5h7h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w5h)and Wboard.w8h==''\
           and board.s6h+board.s7h=='':
            moves = '5h8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w5h)and Wboard.w8h==''\
           and board.s6h+board.s7h=='':
            moves = '5h8h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w5h)and Wboard.w9h==''\
           and board.s6h+board.s7h+board.s8h=='':
            moves = '5h9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w5h)and Wboard.w9h==''\
           and board.s6h+board.s7h+board.s8h=='':
            moves = '5h9h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w5h)and Wboard.w7f==''\
           and board.s6g=='':
            moves = '5h7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w5h)and Wboard.w8e==''\
           and board.s6g+board.s7f=='':
            moves = '5h8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w5h)and Wboard.w9d==''\
           and board.s6g+board.s7f+board.s8e=='':
            moves = '5h9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Wboard.w5h)and Wboard.w7f==''\
           and board.s6g=='':
            moves = '5h7f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w5h)and Wboard.w8e==''\
           and board.s6g+board.s7f=='':
            moves = '5h8e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w5h)and Wboard.w9d==''\
           and board.s6g+board.s7f+board.s8e=='':
            moves = '5h9d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w5h)and Wboard.w2e==''\
           and board.s3f+board.s4g=='':
            moves = '5h2e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w5h)and Wboard.w3f==''\
           and board.s4g=='':
            moves = '5h3f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w5h)and Wboard.w2e==''\
           and board.s3f+board.s4g=='':
            moves = '5h2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w5h)and Wboard.w3f==''\
           and board.s4g=='':
            moves = '5h3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w5h)and Wboard.w1d==''\
           and board.s4g+board.s3f+board.s2e=='':
            moves = '5h1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w5h)and Wboard.w1d==''\
           and board.s4g+board.s3f+board.s2e=='':
            moves = '5h1d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w6h !='':
        if re.match(r'[sgk+]',    Wboard.w6h)and Wboard.w6i=='':
            moves = '6h6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgk+]',    Wboard.w6h)and Wboard.w5i=='':
            moves = '6h5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgk+]',    Wboard.w6h)and Wboard.w7i=='':
            moves = '6h7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w6h)and Wboard.w5h=='':
            moves = '6h5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w6h)and Wboard.w7h=='':
            moves = '6h7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w6h)and Wboard.w6g=='':
            moves = '6h6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w6h)and Wboard.w5g=='':
            moves = '6h5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w6h)and Wboard.w7g=='':
            moves = '6h7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[plsr]',   Wboard.w6h)and Wboard.w6i=='':
            moves = '6h6i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',     Wboard.w6h)and Wboard.w5i=='':
            moves = '6h5i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'[bs]',     Wboard.w6h)and Wboard.w7i=='':
            moves = '6h7i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('r',         Wboard.w6h)and Wboard.w5h=='':
            moves = '6h5h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',         Wboard.w6h)and Wboard.w7h=='':
            moves = '6h7h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',         Wboard.w6h)and Wboard.w6g=='':
            moves = '6h6g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',     Wboard.w6h)and Wboard.w5g=='':
            moves = '6h5g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',     Wboard.w6h)and Wboard.w7g=='':
            moves = '6h7g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w6h)and Wboard.w6f==''\
           and board.s6e=='':
            moves = '6h6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w6h)and Wboard.w6f==''\
           and board.s6e=='':
            moves = '6h6f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w6h)and Wboard.w6e==''\
           and board.s6g+board.s6f=='':
            moves = '6h6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w6h)and Wboard.w6e==''\
           and board.s6g+board.s6f=='':
            moves = '6h6e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w6h)and Wboard.w6d==''\
           and board.s6g+board.s6f+board.s6e=='':
            moves = '6h6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w6h)and Wboard.w6d==''\
           and board.s6g+board.s6f+board.s6e=='':
            moves = '6h6d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w6h)and Wboard.w6c==''\
           and board.s6g+board.s6f+board.s6e+board.s6d=='':
            moves = '6h6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w6h)and Wboard.w6c==''\
           and board.s6g+board.s6f+board.s6e+board.s6d=='':
            moves = '6h6c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w6h)and Wboard.w6b==''\
           and board.s6g+board.s6f+board.s6e+board.s6d+board.s6c=='':
            moves = '6h6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w6h)and Wboard.w6b==''\
           and board.s6g+board.s6f+board.s6e+board.s6d+board.s6c=='':
            moves = '6h6b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w6h)and Wboard.w6a==''\
           and board.s6g+board.s6f+board.s6e+board.s6d+board.s6c+board.s6b=='':
            moves = '6h6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w6h)and Wboard.w6a==''\
           and board.s6g+board.s6f+board.s6e+board.s6d+board.s6c+board.s6b=='':
            moves = '6h6a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w6h)and Wboard.w9h==''\
           and board.s8h+board.s7h=='':
            moves = '6h9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w6h)and Wboard.w9h==''\
           and board.s8h+board.s7h=='':
            moves = '6h9h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w6h)and Wboard.w5h==''\
           and board.s7h=='':
            moves = '6h8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w6h)and Wboard.w5h==''\
           and board.s7h=='':
            moves = '6h8h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w6h)and Wboard.w4h==''\
           and board.s5h=='':
            moves = '6h4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w6h)and Wboard.w4h==''\
           and board.s5h=='':
            moves = '6h4h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w6h)and Wboard.w3h==''\
           and board.s5h+board.s4h=='':
            moves = '6h3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w6h)and Wboard.w3h==''\
           and board.s5h+board.s4h=='':
            moves = '6h3h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w6h)and Wboard.w2h==''\
           and board.s5h+board.s4h+board.s3h=='':
            moves = '6h2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w6h)and Wboard.w2h==''\
           and board.s5h+board.s4h+board.s3h=='':
            moves = '6h2h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w6h)and Wboard.w1h==''\
           and board.s5h+board.s4h+board.s3h+board.s2h=='':
            moves = '6h1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w6h)and Wboard.w1h==''\
           and board.s5h+board.s4h+board.s3h+board.s2h=='':
            moves = '6h1h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w6h)and Wboard.w4f==''\
           and board.s5g=='':
            moves = '6h4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w6h)and Wboard.w3e==''\
           and board.s5g+board.s4f=='':
            moves = '6h3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w6h)and Wboard.w2d==''\
           and board.s5g+board.s4f+board.s3e=='':
            moves = '6h2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w6h)and Wboard.w1c==''\
           and board.s5g+board.s4f+board.s3e+board.s2d=='':
            moves = '6h1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Wboard.w6h)and Wboard.w4f==''\
           and board.s5g=='':
            moves = '6h4f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w6h)and Wboard.w3e==''\
           and board.s5g+board.s4f=='':
            moves = '6h3e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w6h)and Wboard.w2d==''\
           and board.s5g+board.s4f+board.s3e=='':
            moves = '6h2d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w6h)and Wboard.w1c==''\
           and board.s5g+board.s4f+board.s3e+board.s2d=='':
            moves = '6h1c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w6h)and Wboard.w9e==''\
           and board.s8f+board.s7g=='':
            moves = '6h9e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w6h)and Wboard.w8f==''\
           and board.s7g=='':
            moves = '6h8f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w6h)and Wboard.w9e==''\
           and board.s8f+board.s7g=='':
            moves = '6h9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w6h)and Wboard.w8f==''\
           and board.s7g=='':
            moves = '6h8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w7h !='':
        if re.match(r'[sgk+]',    Wboard.w7h)and Wboard.w7i=='':
            moves = '7h7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgk+]',    Wboard.w7h)and Wboard.w6i=='':
            moves = '7h6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgk+]',    Wboard.w7h)and Wboard.w8i=='':
            moves = '7h8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w7h)and Wboard.w6h=='':
            moves = '7h6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w7h)and Wboard.w8h=='':
            moves = '7h8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w7h)and Wboard.w7g=='':
            moves = '7h7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w7h)and Wboard.w6g=='':
            moves = '7h6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w7h)and Wboard.w8g=='':
            moves = '7h8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[plsr]',   Wboard.w7h)and Wboard.w7i=='':
            moves = '7h7i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',     Wboard.w7h)and Wboard.w6i=='':
            moves = '7h6i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'[bs]',     Wboard.w7h)and Wboard.w8i=='':
            moves = '7h8i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('r',         Wboard.w7h)and Wboard.w6h=='':
            moves = '7h6h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',         Wboard.w7h)and Wboard.w8h=='':
            moves = '7h8h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',         Wboard.w7h)and Wboard.w7g=='':
            moves = '7h7g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',     Wboard.w7h)and Wboard.w6g=='':
            moves = '7h6g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',     Wboard.w7h)and Wboard.w8g=='':
            moves = '7h8g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w7h)and Wboard.w7f==''\
           and board.s7e=='':
            moves = '7h7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w7h)and Wboard.w7f==''\
           and board.s7e=='':
            moves = '7h7f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w7h)and Wboard.w7e==''\
           and board.s7g+board.s7f=='':
            moves = '7h7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w7h)and Wboard.w7e==''\
           and board.s7g+board.s7f=='':
            moves = '7h7e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w7h)and Wboard.w7d==''\
           and board.s7g+board.s7f+board.s7e=='':
            moves = '7h7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w7h)and Wboard.w7d==''\
           and board.s7g+board.s7f+board.s7e=='':
            moves = '7h7d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w7h)and Wboard.w7c==''\
           and board.s7g+board.s7f+board.s7e+board.s7d=='':
            moves = '7h7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w7h)and Wboard.w7c==''\
           and board.s7g+board.s7f+board.s7e+board.s7d=='':
            moves = '7h7c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w7h)and Wboard.w7b==''\
           and board.s7g+board.s7f+board.s7e+board.s7d+board.s7c=='':
            moves = '7h7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w7h)and Wboard.w7b==''\
           and board.s7g+board.s7f+board.s7e+board.s7d+board.s7c=='':
            moves = '7h7b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w7h)and Wboard.w7a==''\
           and board.s7g+board.s7f+board.s7e+board.s7d+board.s7c+board.s7b=='':
            moves = '7h7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w7h)and Wboard.w7a==''\
           and board.s7g+board.s7f+board.s7e+board.s7d+board.s7c+board.s7b=='':
            moves = '7h7a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w7h)and Wboard.w9h==''\
           and board.s8h=='':
            moves = '7h9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w7h)and Wboard.w9h==''\
           and board.s8h=='':
            moves = '7h9h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w7h)and Wboard.w5h==''\
           and board.s6h=='':
            moves = '7h5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w7h)and Wboard.w5h==''\
           and board.s6h=='':
            moves = '7h5h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w7h)and Wboard.w4h==''\
           and board.s6h+board.s5h=='':
            moves = '7h4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w7h)and Wboard.w4h==''\
           and board.s6h+board.s5h=='':
            moves = '7h4h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w7h)and Wboard.w3h==''\
           and board.s6h+board.s5h+board.s4h=='':
            moves = '7h3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w7h)and Wboard.w3h==''\
           and board.s6h+board.s5h+board.s4h=='':
            moves = '7h3h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w7h)and Wboard.w2h==''\
           and board.s6h+board.s5h+board.s4h+board.s3h=='':
            moves = '7h2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w7h)and Wboard.w2h==''\
           and board.s6h+board.s5h+board.s4h+board.s3h=='':
            moves = '7h2h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w7h)and Wboard.w1h==''\
           and board.s6h+board.s5h+board.s4h+board.s3h+board.s2h=='':
            moves = '7h1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w7h)and Wboard.w1h==''\
           and board.s6h+board.s5h+board.s4h+board.s3h+board.s2h=='':
            moves = '7h1h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w7h)and Wboard.w5f==''\
           and board.s6g=='':
            moves = '7h5f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w7h)and Wboard.w4e==''\
           and board.s6g+board.s5f=='':
            moves = '7h4e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w7h)and Wboard.w3d==''\
           and board.s6g+board.s5f+board.s4e=='':
            moves = '7h3d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w7h)and Wboard.w2c==''\
           and board.s6g+board.s5f+board.s4e+board.s3d=='':
            moves = '7h2c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w7h)and Wboard.w1b==''\
           and board.s6g+board.s5f+board.s4e+board.s3d+board.s2c=='':
            moves = '7h1b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w7h)and Wboard.w5f==''\
           and board.s6g=='':
            moves = '7h5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w7h)and Wboard.w4e==''\
           and board.s6g+board.s5f=='':
            moves = '7h4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w7h)and Wboard.w3d==''\
           and board.s6g+board.s5f+board.s4e=='':
            moves = '7h3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w7h)and Wboard.w2c==''\
           and board.s6g+board.s5f+board.s4e+board.s3d=='':
            moves = '7h2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w7h)and Wboard.w1b==''\
           and board.s6g+board.s5f+board.s4e+board.s3d+board.s2c=='':
            moves = '7h1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w7h)and Wboard.w9f==''\
           and board.s8g=='':
            moves = '7h9f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w7h)and Wboard.w9f==''\
           and board.s8g=='':
            moves = '7h9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w8h !='':
        if re.match(r'[sgk+]',    Wboard.w8h)and Wboard.w8i=='':
            moves = '8h8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgk+]',    Wboard.w8h)and Wboard.w7i=='':
            moves = '8h7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgk+]',    Wboard.w8h)and Wboard.w9i=='':
            moves = '8h9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w8h)and Wboard.w7h=='':
            moves = '8h7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w8h)and Wboard.w9h=='':
            moves = '8h9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w8h)and Wboard.w8g=='':
            moves = '8h8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w8h)and Wboard.w7g=='':
            moves = '8h7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w8h)and Wboard.w9g=='':
            moves = '8h9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[plsr]',   Wboard.w8h)and Wboard.w8i=='':
            moves = '8h8i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',     Wboard.w8h)and Wboard.w7i=='':
            moves = '8h7i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'[bs]',     Wboard.w8h)and Wboard.w9i=='':
            moves = '8h9i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('r',         Wboard.w8h)and Wboard.w7h=='':
            moves = '8h7h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',         Wboard.w8h)and Wboard.w9h=='':
            moves = '8h9h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',         Wboard.w8h)and Wboard.w8g=='':
            moves = '8h8g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',     Wboard.w8h)and Wboard.w7g=='':
            moves = '8h7g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',     Wboard.w8h)and Wboard.w9g=='':
            moves = '8h9g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w8h)and Wboard.w8f==''\
           and board.s8e=='':
            moves = '8h8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w8h)and Wboard.w8f==''\
           and board.s8e=='':
            moves = '8h8f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w8h)and Wboard.w8e==''\
           and board.s8g+board.s8f=='':
            moves = '8h8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w8h)and Wboard.w8e==''\
           and board.s8g+board.s8f=='':
            moves = '8h8e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w8h)and Wboard.w8d==''\
           and board.s8g+board.s8f+board.s8e=='':
            moves = '8h8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w8h)and Wboard.w8d==''\
           and board.s8g+board.s8f+board.s8e=='':
            moves = '8h8d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w8h)and Wboard.w8c==''\
           and board.s8g+board.s8f+board.s8e+board.s8d=='':
            moves = '8h8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w8h)and Wboard.w8c==''\
           and board.s8g+board.s8f+board.s8e+board.s8d=='':
            moves = '8h8c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w8h)and Wboard.w8b==''\
           and board.s8g+board.s8f+board.s8e+board.s8d+board.s8c=='':
            moves = '8h8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w8h)and Wboard.w8b==''\
           and board.s8g+board.s8f+board.s8e+board.s8d+board.s8c=='':
            moves = '8h8b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w8h)and Wboard.w8a==''\
           and board.s8g+board.s8f+board.s8e+board.s8d+board.s8c+board.s8b=='':
            moves = '8h8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w8h)and Wboard.w8a==''\
           and board.s8g+board.s8f+board.s8e+board.s8d+board.s8c+board.s8b=='':
            moves = '8h8a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w8h)and Wboard.w6h==''\
           and board.s7h=='':
            moves = '8h6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w8h)and Wboard.w6h==''\
           and board.s7h=='':
            moves = '8h6h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w8h)and Wboard.w5h==''\
           and board.s7h+board.s6h=='':
            moves = '8h5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w8h)and Wboard.w5h==''\
           and board.s7h+board.s6h=='':
            moves = '8h5h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w8h)and Wboard.w4h==''\
           and board.s7h+board.s6h+board.s5h=='':
            moves = '8h4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w8h)and Wboard.w4h==''\
           and board.s7h+board.s6h+board.s5h=='':
            moves = '8h4h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w8h)and Wboard.w3h==''\
           and board.s7h+board.s6h+board.s5h+board.s4h=='':
            moves = '8h3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w8h)and Wboard.w3h==''\
           and board.s7h+board.s6h+board.s5h+board.s4h=='':
            moves = '8h3h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w8h)and Wboard.w2h==''\
           and board.s7h+board.s6h+board.s5h+board.s4h+board.s3h=='':
            moves = '8h2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w8h)and Wboard.w2h==''\
           and board.s7h+board.s6h+board.s5h+board.s4h+board.s3h=='':
            moves = '8h2h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w8h)and Wboard.w1h==''\
           and board.s7h+board.s6h+board.s5h+board.s4h+board.s3h+board.s2h=='':
            moves = '8h1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w8h)and Wboard.w1h==''\
           and board.s7h+board.s6h+board.s5h+board.s4h+board.s3h+board.s2h=='':
            moves = '8h1h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w8h)and Wboard.w6f==''\
           and board.s7g=='':
            moves = '8h6f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w8h)and Wboard.w5e==''\
           and board.s7g+board.s6f=='':
            moves = '8h5e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w8h)and Wboard.w4d==''\
           and board.s7g+board.s6f+board.s5e=='':
            moves = '8h4d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w8h)and Wboard.w3c==''\
           and board.s7g+board.s6f+board.s5e+board.s4d=='':
            moves = '8h3c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w8h)and Wboard.w2b==''\
           and board.s7g+board.s6f+board.s5e+board.s4d+board.s3c=='':
            moves = '8h2b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w8h)and Wboard.w1a==''\
           and board.s7g+board.s6f+board.s5e+board.s4d+board.s3c+board.s2b=='':
            moves = '8h1a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w8h)and Wboard.w6f==''\
           and board.s7g=='':
            moves = '8h6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w8h)and Wboard.w5e==''\
           and board.s7g+board.s6f=='':
            moves = '8h5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w8h)and Wboard.w4d==''\
           and board.s7g+board.s6f+board.s5e=='':
            moves = '8h4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w8h)and Wboard.w3c==''\
           and board.s7g+board.s6f+board.s5e+board.s4d=='':
            moves = '8h3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w8h)and Wboard.w2b==''\
           and board.s7g+board.s6f+board.s5e+board.s4d+board.s3c=='':
            moves = '8h2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w8h)and Wboard.w1a==''\
           and board.s7g+board.s6f+board.s5e+board.s4d+board.s3c+board.s2b=='':
            moves = '8h1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w9h !='':
        if re.match(r'[sgk+]',    Wboard.w9h)and Wboard.w9i=='':
            moves = '9h9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgk+]',    Wboard.w9h)and Wboard.w8i=='':
            moves = '9h8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w9h)and Wboard.w8h=='':
            moves = '9h8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w9h)and Wboard.w9g=='':
            moves = '9h9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w9h)and Wboard.w8g=='':
            moves = '9h8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[plsr]',   Wboard.w9h)and Wboard.w9i=='':
            moves = '9h9i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',     Wboard.w9h)and Wboard.w8i=='':
            moves = '9h8i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('r',         Wboard.w9h)and Wboard.w8h=='':
            moves = '9h8h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',         Wboard.w9h)and Wboard.w9g=='':
            moves = '9h9g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',     Wboard.w9h)and Wboard.w8g=='':
            moves = '9h8g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w9h)and Wboard.w9f==''\
           and board.s9e=='':
            moves = '9h9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w9h)and Wboard.w9f==''\
           and board.s9e=='':
            moves = '9h9f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w9h)and Wboard.w9e==''\
           and board.s9g+board.s9f=='':
            moves = '9h9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w9h)and Wboard.w9e==''\
           and board.s9g+board.s9f=='':
            moves = '9h9e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w9h)and Wboard.w9d==''\
           and board.s9g+board.s9f+board.s9e=='':
            moves = '9h9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w9h)and Wboard.w9d==''\
           and board.s9g+board.s9f+board.s9e=='':
            moves = '9h9d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w9h)and Wboard.w9c==''\
           and board.s9g+board.s9f+board.s9e+board.s9d=='':
            moves = '9h9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w9h)and Wboard.w9c==''\
           and board.s9g+board.s9f+board.s9e+board.s9d=='':
            moves = '9h9c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w9h)and Wboard.w9b==''\
           and board.s9g+board.s9f+board.s9e+board.s9d+board.s9c=='':
            moves = '9h9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w9h)and Wboard.w9b==''\
           and board.s9g+board.s9f+board.s9e+board.s9d+board.s9c=='':
            moves = '9h9b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w9h)and Wboard.w9a==''\
           and board.s9g+board.s9f+board.s9e+board.s9d+board.s9c+board.s9b=='':
            moves = '9h9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w9h)and Wboard.w9a==''\
           and board.s9g+board.s9f+board.s9e+board.s9d+board.s9c+board.s9b=='':
            moves = '9h9a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w9h)and Wboard.w7h==''\
           and board.s8h=='':
            moves = '9h7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w9h)and Wboard.w7h==''\
           and board.s8h=='':
            moves = '9h7h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w9h)and Wboard.w6h==''\
           and board.s8h+board.s7h=='':
            moves = '9h6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w9h)and Wboard.w6h==''\
           and board.s8h+board.s7h=='':
            moves = '9h6h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w9h)and Wboard.w5h==''\
           and board.s8h+board.s7h+board.s6h=='':
            moves = '9h5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w9h)and Wboard.w5h==''\
           and board.s8h+board.s7h+board.s6h=='':
            moves = '9h5h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w9h)and Wboard.w4h==''\
           and board.s8h+board.s7h+board.s6h+board.s5h=='':
            moves = '9h4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w9h)and Wboard.w4h==''\
           and board.s8h+board.s7h+board.s6h+board.s5h=='':
            moves = '9h4h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w9h)and Wboard.w3h==''\
           and board.s8h+board.s7h+board.s6h+board.s5h+board.s4h=='':
            moves = '9h3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w9h)and Wboard.w3h==''\
           and board.s8h+board.s7h+board.s6h+board.s5h+board.s4h=='':
            moves = '9h3h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w9h)and Wboard.w2h==''\
           and board.s8h+board.s7h+board.s6h+board.s5h+board.s4h+board.s3h=='':
            moves = '9h2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w9h)and Wboard.w2h==''\
           and board.s8h+board.s7h+board.s6h+board.s5h+board.s4h+board.s3h=='':
            moves = '9h2h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w9h)and Wboard.w1h==''\
           and board.s8h+board.s7h+board.s6h+board.s5h+board.s4h+board.s3h+board.s2h=='':
            moves = '9h1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w9h)and Wboard.w1h==''\
           and board.s8h+board.s7h+board.s6h+board.s5h+board.s4h+board.s3h+board.s2h=='':
            moves = '9h1h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w9h)and Wboard.w7f==''\
           and board.s8g=='':
            moves = '9h7f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w9h)and Wboard.w6e==''\
           and board.s8g+board.s7f=='':
            moves = '9h6e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w9h)and Wboard.w5d==''\
           and board.s8g+board.s7f+board.s6e=='':
            moves = '9h5d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w9h)and Wboard.w4c==''\
           and board.s8g+board.s7f+board.s6e+board.s5d=='':
            moves = '9h4c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w9h)and Wboard.w3b==''\
           and board.s8g+board.s7f+board.s6e+board.s5d+board.s4c=='':
            moves = '9h3b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w9h)and Wboard.w2a==''\
           and board.s8g+board.s7f+board.s6e+board.s5d+board.s4c+board.s3b=='':
            moves = '9h2a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w9h)and Wboard.w7f==''\
           and board.s8g=='':
            moves = '9h7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w9h)and Wboard.w6e==''\
           and board.s8g+board.s7f=='':
            moves = '9h6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w9h)and Wboard.w5d==''\
           and board.s8g+board.s7f+board.s6e=='':
            moves = '9h5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w9h)and Wboard.w4c==''\
           and board.s8g+board.s7f+board.s6e+board.s5d=='':
            moves = '9h4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w9h)and Wboard.w3b==''\
           and board.s8g+board.s7f+board.s6e+board.s5d+board.s4c=='':
            moves = '9h3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w9h)and Wboard.w2a==''\
           and board.s8g+board.s7f+board.s6e+board.s5d+board.s4c+board.s3b=='':
            moves = '9h2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w1g !='':
        if re.match(r'[sgk+]',    Wboard.w1g)and Wboard.w1h=='':
            moves = '1g1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgk+]',    Wboard.w1g)and Wboard.w2h=='':
            moves = '1g2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w1g)and Wboard.w2g=='':
            moves = '1g2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w1g)and Wboard.w1f=='':
            moves = '1g1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w1g)and Wboard.w2f=='':
            moves = '1g2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[plsr]',   Wboard.w1g)and Wboard.w1h=='':
            moves = '1g1h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',     Wboard.w1g)and Wboard.w2h=='':
            moves = '1g2h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('r',         Wboard.w1g)and Wboard.w2g=='':
            moves = '1g2g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',         Wboard.w1g)and Wboard.w1f=='':
            moves = '1g1f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',     Wboard.w1g)and Wboard.w2f=='':
            moves = '1g2f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w1g)and Wboard.w2i=='':
            moves = '1g2i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w1g)and Wboard.w1i==''\
           and board.s1h=='':
            moves = '1g1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w1g)and Wboard.w1i==''\
           and board.s1h=='':
            moves = '1g1i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w1g)and Wboard.w1e==''\
           and board.s1f=='':
            moves = '1g1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w1g)and Wboard.w1e==''\
           and board.s1f=='':
            moves = '1g1e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w1g)and Wboard.w1d==''\
           and board.s1f+board.s1e=='':
            moves = '1g1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w1g)and Wboard.w1d==''\
           and board.s1f+board.s1e=='':
            moves = '1g1d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w1g)and Wboard.w1c==''\
           and board.s1f+board.s1e+board.s1d=='':
            moves = '1g1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w1g)and Wboard.w1c==''\
           and board.s1f+board.s1e+board.s1d=='':
            moves = '1g1c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w1g)and Wboard.w1b==''\
           and board.s1f+board.s1e+board.s1d+board.s1c=='':
            moves = '1g1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w1g)and Wboard.w1b==''\
           and board.s1f+board.s1e+board.s1d+board.s1c=='':
            moves = '1g1b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w1g)and Wboard.w1a==''\
           and board.s1f+board.s1e+board.s1d+board.s1c+board.s1b=='':
            moves = '1g1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w1g)and Wboard.w1a==''\
           and board.s1f+board.s1e+board.s1d+board.s1c+board.s1b=='':
            moves = '1g1a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w1g)and Wboard.w3g==''\
           and board.s2g=='':
            moves = '1g3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w1g)and Wboard.w3g==''\
           and board.s2g=='':
            moves = '1g3g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w1g)and Wboard.w4g==''\
           and board.s2g+board.s3g=='':
            moves = '1g4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w1g)and Wboard.w4g==''\
           and board.s2g+board.s3g=='':
            moves = '1g4g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w1g)and Wboard.w5g==''\
           and board.s2g+board.s3g+board.s4g=='':
            moves = '1g5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w1g)and Wboard.w5g==''\
           and board.s2g+board.s3g+board.s4g=='':
            moves = '1g5g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w1g)and Wboard.w6g==''\
           and board.s2g+board.s3g+board.s4g+board.s5g=='':
            moves = '1g6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w1g)and Wboard.w6g==''\
           and board.s2g+board.s3g+board.s4g+board.s5g=='':
            moves = '1g6g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w1g)and Wboard.w7g==''\
           and board.s2g+board.s3g+board.s4g+board.s5g+board.s6g=='':
            moves = '1g7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w1g)and Wboard.w7g==''\
           and board.s2g+board.s3g+board.s4g+board.s5g+board.s6g=='':
            moves = '1g7g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w1g)and Wboard.w8g==''\
           and board.s2g+board.s3g+board.s4g+board.s5g+board.s6g+board.s7g=='':
            moves = '1g8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w1g)and Wboard.w8g==''\
           and board.s2g+board.s3g+board.s4g+board.s5g+board.s6g+board.s7g=='':
            moves = '1g8g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w1g)and Wboard.w9g==''\
           and board.s2g+board.s3g+board.s4g+board.s5g+board.s6g+board.s7g+board.s8g=='':
            moves = '1g9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w1g)and Wboard.w9g==''\
           and board.s2g+board.s3g+board.s4g+board.s5g+board.s6g+board.s7g+board.s8g=='':
            moves = '1g9g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w1g)and Wboard.w3i==''\
           and board.s2h=='':
            moves = '1g3i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w1g)and Wboard.w3e==''\
           and board.s2f=='':
            moves = '1g3e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w1g)and Wboard.w4d==''\
           and board.s2f+board.s3e=='':
            moves = '1g4d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w1g)and Wboard.w5c==''\
           and board.s2f+board.s3e+board.s4d=='':
            moves = '1g5c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w1g)and Wboard.w6b==''\
           and board.s2f+board.s3e+board.s4d+board.s5c=='':
            moves = '1g6b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w1g)and Wboard.w7a==''\
           and board.s2f+board.s3e+board.s4d+board.s5c+board.s6b=='':
            moves = '1g7a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w1g)and Wboard.w3i==''\
           and board.s2h=='':
            moves = '1g3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w1g)and Wboard.w3e==''\
           and board.s2f=='':
            moves = '1g3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w1g)and Wboard.w4d==''\
           and board.s2f+board.s3e=='':
            moves = '1g4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w1g)and Wboard.w5c==''\
           and board.s2f+board.s3e+board.s4d=='':
            moves = '1g5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w1g)and Wboard.w6b==''\
           and board.s2f+board.s3e+board.s4d+board.s5c=='':
            moves = '1g6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w1g)and Wboard.w7a==''\
           and board.s2f+board.s3e+board.s4d+board.s5c+board.s6b=='':
            moves = '1g7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w2g !='':
        if re.match(r'[sgk+]',    Wboard.w2g)and Wboard.w2h=='':
            moves = '2g2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgk+]',    Wboard.w2g)and Wboard.w1h=='':
            moves = '2g1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgk+]',    Wboard.w2g)and Wboard.w3h=='':
            moves = '2g3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w2g)and Wboard.w1g=='':
            moves = '2g1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w2g)and Wboard.w3g=='':
            moves = '2g3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w2g)and Wboard.w2f=='':
            moves = '2g2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w2g)and Wboard.w1f=='':
            moves = '2g1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w2g)and Wboard.w3f=='':
            moves = '2g3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[plsr]',   Wboard.w2g)and Wboard.w2h=='':
            moves = '2g2h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',     Wboard.w2g)and Wboard.w1h=='':
            moves = '2g1h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'[bs]',     Wboard.w2g)and Wboard.w3h=='':
            moves = '2g3h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('r',         Wboard.w2g)and Wboard.w1g=='':
            moves = '2g1g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',         Wboard.w2g)and Wboard.w3g=='':
            moves = '2g3g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',         Wboard.w2g)and Wboard.w2f=='':
            moves = '2g2f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',     Wboard.w2g)and Wboard.w1f=='':
            moves = '2g1f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',     Wboard.w2g)and Wboard.w3f=='':
            moves = '2g3f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w2g)and Wboard.w1i=='':
            moves = '2g1i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w2g)and Wboard.w3i=='':
            moves = '2g3i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w2g)and Wboard.w2i==''\
           and board.s2h=='':
            moves = '2g2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w2g)and Wboard.w2i==''\
           and board.s2h=='':
            moves = '2g2i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w2g)and Wboard.w2e==''\
           and board.s2f=='':
            moves = '2g2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w2g)and Wboard.w2e==''\
           and board.s2f=='':
            moves = '2g2e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w2g)and Wboard.w2d==''\
           and board.s2f+board.s2e=='':
            moves = '2g2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w2g)and Wboard.w2d==''\
           and board.s2f+board.s2e=='':
            moves = '2g2d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w2g)and Wboard.w2c==''\
           and board.s2f+board.s2e+board.s2d=='':
            moves = '2g2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w2g)and Wboard.w2c==''\
           and board.s2f+board.s2e+board.s2d=='':
            moves = '2g2c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w2g)and Wboard.w2b==''\
           and board.s2f+board.s2e+board.s2d+board.s2c=='':
            moves = '2g2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w2g)and Wboard.w2b==''\
           and board.s2f+board.s2e+board.s2d+board.s2c=='':
            moves = '2g2b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w2g)and Wboard.w2a==''\
           and board.s2f+board.s2e+board.s2d+board.s2c+board.s2b=='':
            moves = '2g2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w2g)and Wboard.w2a==''\
           and board.s2f+board.s2e+board.s2d+board.s2c+board.s2b=='':
            moves = '2g2a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w2g)and Wboard.w4g==''\
           and board.s3g=='':
            moves = '2g4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w2g)and Wboard.w4g==''\
           and board.s3g=='':
            moves = '2g4g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w2g)and Wboard.w5g==''\
           and board.s3g+board.s4g=='':
            moves = '2g5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w2g)and Wboard.w5g==''\
           and board.s3g+board.s4g=='':
            moves = '2g5g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w2g)and Wboard.w6g==''\
           and board.s3g+board.s4g+board.s5g=='':
            moves = '2g6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w2g)and Wboard.w6g==''\
           and board.s3g+board.s4g+board.s5g=='':
            moves = '2g6g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w2g)and Wboard.w7g==''\
           and board.s3g+board.s4g+board.s5g+board.s6g=='':
            moves = '2g7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w2g)and Wboard.w7g==''\
           and board.s3g+board.s4g+board.s5g+board.s6g=='':
            moves = '2g7g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w2g)and Wboard.w8g==''\
           and board.s3g+board.s4g+board.s5g+board.s6g+board.s7g=='':
            moves = '2g8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w2g)and Wboard.w8g==''\
           and board.s3g+board.s4g+board.s5g+board.s6g+board.s7g=='':
            moves = '2g8g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w2g)and Wboard.w9g==''\
           and board.s3g+board.s4g+board.s5g+board.s6g+board.s7g+board.s8g=='':
            moves = '2g9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w2g)and Wboard.w9g==''\
           and board.s3g+board.s4g+board.s5g+board.s6g+board.s7g+board.s8g=='':
            moves = '2g9g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w2g)and Wboard.w4e==''\
           and board.s3f=='':
            moves = '2g4e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w2g)and Wboard.w5d==''\
           and board.s3f+board.s4e=='':
            moves = '2g5d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w2g)and Wboard.w6c==''\
           and board.s3f+board.s4e+board.s5d=='':
            moves = '2g6c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w2g)and Wboard.w7b==''\
           and board.s3f+board.s4e+board.s5d+board.s6c=='':
            moves = '2g7b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w2g)and Wboard.w8a==''\
           and board.s3f+board.s4e+board.s5d+board.s6c+board.s7b=='':
            moves = '2g8a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w2g)and Wboard.w4e==''\
           and board.s3f=='':
            moves = '2g4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w2g)and Wboard.w5d==''\
           and board.s3f+board.s4e=='':
            moves = '2g5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w2g)and Wboard.w6c==''\
           and board.s3f+board.s4e+board.s5d=='':
            moves = '2g6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w2g)and Wboard.w7b==''\
           and board.s3f+board.s4e+board.s5d+board.s6c=='':
            moves = '2g7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w2g)and Wboard.w8a==''\
           and board.s3f+board.s4e+board.s5d+board.s6c+board.s7b=='':
            moves = '2g8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w2g)and Wboard.w4i==''\
           and board.s3h=='':
            moves = '2g4i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w2g)and Wboard.w4i==''\
           and board.s3h=='':
            moves = '2g4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w3g !='':
        if re.match(r'[sgk+]',    Wboard.w3g)and Wboard.w3h=='':
            moves = '3g3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgk+]',    Wboard.w3g)and Wboard.w2h=='':
            moves = '3g2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgk+]',    Wboard.w3g)and Wboard.w4h=='':
            moves = '3g4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w3g)and Wboard.w2g=='':
            moves = '3g2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w3g)and Wboard.w4g=='':
            moves = '3g4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w3g)and Wboard.w3f=='':
            moves = '3g3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w3g)and Wboard.w2f=='':
            moves = '3g2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w3g)and Wboard.w4f=='':
            moves = '3g4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[plsr]',   Wboard.w3g)and Wboard.w3h=='':
            moves = '3g3h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',     Wboard.w3g)and Wboard.w2h=='':
            moves = '3g2h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'[bs]',     Wboard.w3g)and Wboard.w4h=='':
            moves = '3g4h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('r',         Wboard.w3g)and Wboard.w2g=='':
            moves = '3g2g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',         Wboard.w3g)and Wboard.w4g=='':
            moves = '3g4g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',         Wboard.w3g)and Wboard.w3f=='':
            moves = '3g3f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',     Wboard.w3g)and Wboard.w2f=='':
            moves = '3g2f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',     Wboard.w3g)and Wboard.w4f=='':
            moves = '3g4f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w3g)and Wboard.w2i=='':
            moves = '3g2i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w3g)and Wboard.w4i=='':
            moves = '3g4i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w3g)and Wboard.w3i==''\
           and board.s3h=='':
            moves = '3g3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w3g)and Wboard.w3i==''\
           and board.s3h=='':
            moves = '3g3i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w3g)and Wboard.w3e==''\
           and board.s3f=='':
            moves = '3g3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w3g)and Wboard.w3e==''\
           and board.s3f=='':
            moves = '3g3e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w3g)and Wboard.w3d==''\
           and board.s3f+board.s3e=='':
            moves = '3g3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w3g)and Wboard.w3d==''\
           and board.s3f+board.s3e=='':
            moves = '3g3d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w3g)and Wboard.w3c==''\
           and board.s3f+board.s3e+board.s3d=='':
            moves = '3g3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w3g)and Wboard.w3c==''\
           and board.s3f+board.s3e+board.s3d=='':
            moves = '3g3c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w3g)and Wboard.w3b==''\
           and board.s3f+board.s3e+board.s3d+board.s3c=='':
            moves = '3g3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w3g)and Wboard.w3b==''\
           and board.s3f+board.s3e+board.s3d+board.s3c=='':
            moves = '3g3b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w3g)and Wboard.w3a==''\
           and board.s3f+board.s3e+board.s3d+board.s3c+board.s3b=='':
            moves = '3g3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w3g)and Wboard.w3a==''\
           and board.s3f+board.s3e+board.s3d+board.s3c+board.s3b=='':
            moves = '3g3a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w3g)and Wboard.w1g==''\
           and board.s2g=='':
            moves = '3g1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w3g)and Wboard.w1g==''\
           and board.s2g=='':
            moves = '3g1g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w3g)and Wboard.w5g==''\
           and board.s4g=='':
            moves = '3g5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w3g)and Wboard.w5g==''\
           and board.s4g=='':
            moves = '3g5g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w3g)and Wboard.w6g==''\
           and board.s4g+board.s5g=='':
            moves = '3g6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w3g)and Wboard.w6g==''\
           and board.s4g+board.s5g=='':
            moves = '3g6g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w3g)and Wboard.w7g==''\
           and board.s4g+board.s5g+board.s6g=='':
            moves = '3g7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w3g)and Wboard.w7g==''\
           and board.s4g+board.s5g+board.s6g=='':
            moves = '3g7g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w3g)and Wboard.w8g==''\
           and board.s4g+board.s5g+board.s6g+board.s7g=='':
            moves = '3g8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w3g)and Wboard.w8g==''\
           and board.s4g+board.s5g+board.s6g+board.s7g=='':
            moves = '3g8g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w3g)and Wboard.w9g==''\
           and board.s4g+board.s5g+board.s6g+board.s7g+board.s8g=='':
            moves = '3g9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w3g)and Wboard.w9g==''\
           and board.s4g+board.s5g+board.s6g+board.s7g+board.s8g=='':
            moves = '3g9g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w3g)and Wboard.w1i==''\
           and board.s2h=='':
            moves = '3g1i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w3g)and Wboard.w5e==''\
           and board.s4f=='':
            moves = '3g5e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w3g)and Wboard.w6d==''\
           and board.s4f+board.s5e=='':
            moves = '3g6d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w3g)and Wboard.w7c==''\
           and board.s4f+board.s5e+board.s6d=='':
            moves = '3g7c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w3g)and Wboard.w8b==''\
           and board.s4f+board.s5e+board.s6d+board.s7c=='':
            moves = '3g8b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w3g)and Wboard.w9a==''\
           and board.s4f+board.s5e+board.s6d+board.s7c+board.s8b=='':
            moves = '3g9a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w3g)and Wboard.w1i==''\
           and board.s2h=='':
            moves = '3g1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w3g)and Wboard.w5e==''\
           and board.s4f=='':
            moves = '3g5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w3g)and Wboard.w6d==''\
           and board.s4f+board.s5e=='':
            moves = '3g6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w3g)and Wboard.w7c==''\
           and board.s4f+board.s5e+board.s6d=='':
            moves = '3g7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w3g)and Wboard.w8b==''\
           and board.s4f+board.s5e+board.s6d+board.s7c=='':
            moves = '3g8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w3g)and Wboard.w9a==''\
           and board.s4f+board.s5e+board.s6d+board.s7c+board.s8b=='':
            moves = '3g9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w3g)and Wboard.w5i==''\
           and board.s4h=='':
            moves = '3g5i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w3g)and Wboard.w1e==''\
           and board.s2f=='':
            moves = '3g1e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w3g)and Wboard.w5i==''\
           and board.s4h=='':
            moves = '3g5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w3g)and Wboard.w1e==''\
           and board.s2f=='':
            moves = '3g1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w4g !='':
        if re.match(r'[sgk+]',    Wboard.w4g)and Wboard.w4h=='':
            moves = '4g4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgk+]',    Wboard.w4g)and Wboard.w3h=='':
            moves = '4g3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgk+]',    Wboard.w4g)and Wboard.w5h=='':
            moves = '4g5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w4g)and Wboard.w3g=='':
            moves = '4g3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w4g)and Wboard.w5g=='':
            moves = '4g5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w4g)and Wboard.w4f=='':
            moves = '4g4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w4g)and Wboard.w3f=='':
            moves = '4g3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w4g)and Wboard.w5f=='':
            moves = '4g5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[plsr]',   Wboard.w4g)and Wboard.w4h=='':
            moves = '4g4h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',     Wboard.w4g)and Wboard.w3h=='':
            moves = '4g3h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'[bs]',     Wboard.w4g)and Wboard.w5h=='':
            moves = '4g5h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('r',         Wboard.w4g)and Wboard.w3g=='':
            moves = '4g3g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',         Wboard.w4g)and Wboard.w5g=='':
            moves = '4g5g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',         Wboard.w4g)and Wboard.w4f=='':
            moves = '4g4f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',     Wboard.w4g)and Wboard.w3f=='':
            moves = '4g3f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',     Wboard.w4g)and Wboard.w5f=='':
            moves = '4g5f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w4g)and Wboard.w3i=='':
            moves = '4g3i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w4g)and Wboard.w5i=='':
            moves = '4g5i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w4g)and Wboard.w4i==''\
           and board.s4h=='':
            moves = '4g4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w4g)and Wboard.w4i==''\
           and board.s4h=='':
            moves = '4g4i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w4g)and Wboard.w4e==''\
           and board.s4f=='':
            moves = '4g4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w4g)and Wboard.w4e==''\
           and board.s4f=='':
            moves = '4g4e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w4g)and Wboard.w4d==''\
           and board.s4f+board.s4e=='':
            moves = '4g4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w4g)and Wboard.w4d==''\
           and board.s4f+board.s4e=='':
            moves = '4g4d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w4g)and Wboard.w4c==''\
           and board.s4f+board.s4e+board.s4d=='':
            moves = '4g4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w4g)and Wboard.w4c==''\
           and board.s4f+board.s4e+board.s4d=='':
            moves = '4g4c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w4g)and Wboard.w4b==''\
           and board.s4f+board.s4e+board.s4d+board.s4c=='':
            moves = '4g4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w4g)and Wboard.w4b==''\
           and board.s4f+board.s4e+board.s4d+board.s4c=='':
            moves = '4g4b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w4g)and Wboard.w4a==''\
           and board.s4f+board.s4e+board.s4d+board.s4c+board.s4b=='':
            moves = '4g4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w4g)and Wboard.w4a==''\
           and board.s4f+board.s4e+board.s4d+board.s4c+board.s4b=='':
            moves = '4g4a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w4g)and Wboard.w1g==''\
           and board.s2g+board.s3g=='':
            moves = '4g1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w4g)and Wboard.w1g==''\
           and board.s2g+board.s3g=='':
            moves = '4g1g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w4g)and Wboard.w5g==''\
           and board.s3g=='':
            moves = '4g2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w4g)and Wboard.w5g==''\
           and board.s3g=='':
            moves = '4g2g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w4g)and Wboard.w6g==''\
           and board.s5g=='':
            moves = '4g6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w4g)and Wboard.w6g==''\
           and board.s5g=='':
            moves = '4g6g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w4g)and Wboard.w7g==''\
           and board.s5g+board.s6g=='':
            moves = '4g7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w4g)and Wboard.w7g==''\
           and board.s5g+board.s6g=='':
            moves = '4g7g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w4g)and Wboard.w8g==''\
           and board.s5g+board.s6g+board.s7g=='':
            moves = '4g8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w4g)and Wboard.w8g==''\
           and board.s5g+board.s6g+board.s7g=='':
            moves = '4g8g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w4g)and Wboard.w9g==''\
           and board.s5g+board.s6g+board.s7g+board.s8g=='':
            moves = '4g9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w4g)and Wboard.w9g==''\
           and board.s5g+board.s6g+board.s7g+board.s8g=='':
            moves = '4g9g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w4g)and Wboard.w6e==''\
           and board.s5f=='':
            moves = '4g6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w4g)and Wboard.w7d==''\
           and board.s5f+board.s6e=='':
            moves = '4g7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w4g)and Wboard.w8c==''\
           and board.s5f+board.s6e+board.s7d=='':
            moves = '4g8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w4g)and Wboard.w9b==''\
           and board.s5f+board.s6e+board.s7d+board.s8c=='':
            moves = '4g9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Wboard.w4g)and Wboard.w6e==''\
           and board.s5f=='':
            moves = '4g6e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w4g)and Wboard.w7d==''\
           and board.s5f+board.s6e=='':
            moves = '4g7d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w4g)and Wboard.w8c==''\
           and board.s5f+board.s6e+board.s7d=='':
            moves = '4g8c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w4g)and Wboard.w9b==''\
           and board.s5f+board.s6e+board.s7d+board.s8c=='':
            moves = '4g9b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w4g)and Wboard.w1d==''\
           and board.s2e+board.s3f=='':
            moves = '4g1d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w4g)and Wboard.w2e==''\
           and board.s3f=='':
            moves = '4g2e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w4g)and Wboard.w1d==''\
           and board.s2e+board.s3f=='':
            moves = '4g1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w4g)and Wboard.w2e==''\
           and board.s3f=='':
            moves = '4g2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w4g)and Wboard.w2i==''\
           and board.s3h=='':
            moves = '4g2i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w4g)and Wboard.w2i==''\
           and board.s3h=='':
            moves = '4g2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w4g)and Wboard.w6i==''\
           and board.s5h=='':
            moves = '4g6i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w4g)and Wboard.w6i==''\
           and board.s5h=='':
            moves = '4g6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w5g !='':
        if re.match(r'[sgk+]',    Wboard.w5g)and Wboard.w5h=='':
            moves = '5g5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgk+]',    Wboard.w5g)and Wboard.w4h=='':
            moves = '5g4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgk+]',    Wboard.w5g)and Wboard.w6h=='':
            moves = '5g6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w5g)and Wboard.w4g=='':
            moves = '5g4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w5g)and Wboard.w6g=='':
            moves = '5g6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w5g)and Wboard.w5f=='':
            moves = '5g5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w5g)and Wboard.w4f=='':
            moves = '5g4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w5g)and Wboard.w6f=='':
            moves = '5g6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[plsr]',   Wboard.w5g)and Wboard.w5h=='':
            moves = '5g5h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',     Wboard.w5g)and Wboard.w4h=='':
            moves = '5g4h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'[bs]',     Wboard.w5g)and Wboard.w6h=='':
            moves = '5g6h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('r',         Wboard.w5g)and Wboard.w4g=='':
            moves = '5g4g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',         Wboard.w5g)and Wboard.w6g=='':
            moves = '5g6g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',         Wboard.w5g)and Wboard.w5f=='':
            moves = '5g5f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',     Wboard.w5g)and Wboard.w4f=='':
            moves = '5g4f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',     Wboard.w5g)and Wboard.w6f=='':
            moves = '5g6f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w5g)and Wboard.w4i=='':
            moves = '5g4i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w5g)and Wboard.w6i=='':
            moves = '5g6i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w5g)and Wboard.w5i==''\
           and board.s5h=='':
            moves = '5g5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w5g)and Wboard.w5i==''\
           and board.s5h=='':
            moves = '5g5i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w5g)and Wboard.w5e==''\
           and board.s5f=='':
            moves = '5g5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w5g)and Wboard.w5e==''\
           and board.s5f=='':
            moves = '5g5e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w5g)and Wboard.w5d==''\
           and board.s5f+board.s5e=='':
            moves = '5g5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w5g)and Wboard.w5d==''\
           and board.s5f+board.s5e=='':
            moves = '5g5d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w5g)and Wboard.w5c==''\
           and board.s5f+board.s5e+board.s5d=='':
            moves = '5g5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w5g)and Wboard.w5c==''\
           and board.s5f+board.s5e+board.s5d=='':
            moves = '5g5c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w5g)and Wboard.w5b==''\
           and board.s5f+board.s5e+board.s5d+board.s5c=='':
            moves = '5g5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w5g)and Wboard.w5b==''\
           and board.s5f+board.s5e+board.s5d+board.s5c=='':
            moves = '5g5b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w5g)and Wboard.w5a==''\
           and board.s5f+board.s5e+board.s5d+board.s5c+board.s5b=='':
            moves = '5g5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w5g)and Wboard.w5a==''\
           and board.s5f+board.s5e+board.s5d+board.s5c+board.s5b=='':
            moves = '5g5a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w5g)and Wboard.w1g==''\
           and board.s2g+board.s3g+board.s4g=='':
            moves = '5g1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w5g)and Wboard.w1g==''\
           and board.s2g+board.s3g+board.s4g=='':
            moves = '5g1g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w5g)and Wboard.w2g==''\
           and board.s3g+board.s4g=='':
            moves = '5g2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w5g)and Wboard.w2g==''\
           and board.s3g+board.s4g=='':
            moves = '5g2g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w5g)and Wboard.w3g==''\
           and board.s4g=='':
            moves = '5g3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w5g)and Wboard.w3g==''\
           and board.s4g=='':
            moves = '5g3g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w5g)and Wboard.w7g==''\
           and board.s6g=='':
            moves = '5g7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w5g)and Wboard.w7g==''\
           and board.s6g=='':
            moves = '5g7g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w5g)and Wboard.w8g==''\
           and board.s6g+board.s7g=='':
            moves = '5g8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w5g)and Wboard.w8g==''\
           and board.s6g+board.s7g=='':
            moves = '5g8g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w5g)and Wboard.w9g==''\
           and board.s6g+board.s7g+board.s8g=='':
            moves = '5g9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w5g)and Wboard.w9g==''\
           and board.s6g+board.s7g+board.s8g=='':
            moves = '5g9g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w5g)and Wboard.w7e==''\
           and board.s6f=='':
            moves = '5g7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w5g)and Wboard.w8d==''\
           and board.s6f+board.s7e=='':
            moves = '5g8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w5g)and Wboard.w9c==''\
           and board.s6f+board.s7e+board.s8d=='':
            moves = '5g9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Wboard.w5g)and Wboard.w7e==''\
           and board.s6f=='':
            moves = '5g7e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w5g)and Wboard.w8d==''\
           and board.s6f+board.s7e=='':
            moves = '5g8d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w5g)and Wboard.w9c==''\
           and board.s6f+board.s7e+board.s8d=='':
            moves = '5g9c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w5g)and Wboard.w2d==''\
           and board.s3e+board.s4f=='':
            moves = '5g2d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w5g)and Wboard.w3e==''\
           and board.s4f=='':
            moves = '5g3e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w5g)and Wboard.w2d==''\
           and board.s3e+board.s4f=='':
            moves = '5g2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w5g)and Wboard.w3e==''\
           and board.s4f=='':
            moves = '5g3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w5g)and Wboard.w1c==''\
           and board.s4f+board.s3e+board.s2d=='':
            moves = '5g1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w5g)and Wboard.w1c==''\
           and board.s4f+board.s3e+board.s2d=='':
            moves = '5g1c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w5g)and Wboard.w3i==''\
           and board.s4h=='':
            moves = '5g3i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w5g)and Wboard.w3i==''\
           and board.s4h=='':
            moves = '5g3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w5g)and Wboard.w7i==''\
           and board.s6h=='':
            moves = '5g7i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w5g)and Wboard.w7i==''\
           and board.s6h=='':
            moves = '5g7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w6g !='':
        if re.match(r'[sgk+]',    Wboard.w6g)and Wboard.w6h=='':
            moves = '6g6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgk+]',    Wboard.w6g)and Wboard.w5h=='':
            moves = '6g5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgk+]',    Wboard.w6g)and Wboard.w7h=='':
            moves = '6g7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w6g)and Wboard.w5g=='':
            moves = '6g5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w6g)and Wboard.w7g=='':
            moves = '6g7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w6g)and Wboard.w6f=='':
            moves = '6g6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w6g)and Wboard.w5f=='':
            moves = '6g5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w6g)and Wboard.w7f=='':
            moves = '6g7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[plsr]',   Wboard.w6g)and Wboard.w6h=='':
            moves = '6g6h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',     Wboard.w6g)and Wboard.w5h=='':
            moves = '6g5h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'[bs]',     Wboard.w6g)and Wboard.w7h=='':
            moves = '6g7h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('r',         Wboard.w6g)and Wboard.w5g=='':
            moves = '6g5g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',         Wboard.w6g)and Wboard.w7g=='':
            moves = '6g7g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',         Wboard.w6g)and Wboard.w6f=='':
            moves = '6g6f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',     Wboard.w6g)and Wboard.w5f=='':
            moves = '6g5f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',     Wboard.w6g)and Wboard.w7f=='':
            moves = '6g7f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w6g)and Wboard.w5i=='':
            moves = '6g5i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w6g)and Wboard.w7i=='':
            moves = '6g7i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w6g)and Wboard.w6i==''\
           and board.s6h=='':
            moves = '6g6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w6g)and Wboard.w6i==''\
           and board.s6h=='':
            moves = '6g6i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w6g)and Wboard.w6e==''\
           and board.s6f=='':
            moves = '6g6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w6g)and Wboard.w6e==''\
           and board.s6f=='':
            moves = '6g6e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w6g)and Wboard.w6d==''\
           and board.s6f+board.s6e=='':
            moves = '6g6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w6g)and Wboard.w6d==''\
           and board.s6f+board.s6e=='':
            moves = '6g6d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w6g)and Wboard.w6c==''\
           and board.s6f+board.s6e+board.s6d=='':
            moves = '6g6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w6g)and Wboard.w6c==''\
           and board.s6f+board.s6e+board.s6d=='':
            moves = '6g6c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w6g)and Wboard.w6b==''\
           and board.s6f+board.s6e+board.s6d+board.s6c=='':
            moves = '6g6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w6g)and Wboard.w6b==''\
           and board.s6f+board.s6e+board.s6d+board.s6c=='':
            moves = '6g6b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w6g)and Wboard.w6a==''\
           and board.s6f+board.s6e+board.s6d+board.s6c+board.s6b=='':
            moves = '6g6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w6g)and Wboard.w6a==''\
           and board.s6f+board.s6e+board.s6d+board.s6c+board.s6b=='':
            moves = '6g6a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w6g)and Wboard.w9g==''\
           and board.s8g+board.s7g=='':
            moves = '6g9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w6g)and Wboard.w9g==''\
           and board.s8g+board.s7g=='':
            moves = '6g9g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w6g)and Wboard.w5g==''\
           and board.s7g=='':
            moves = '6g8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w6g)and Wboard.w5g==''\
           and board.s7g=='':
            moves = '6g8g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w6g)and Wboard.w4g==''\
           and board.s5g=='':
            moves = '6g4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w6g)and Wboard.w4g==''\
           and board.s5g=='':
            moves = '6g4g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w6g)and Wboard.w3g==''\
           and board.s5g+board.s4g=='':
            moves = '6g3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w6g)and Wboard.w3g==''\
           and board.s5g+board.s4g=='':
            moves = '6g3g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w6g)and Wboard.w2g==''\
           and board.s5g+board.s4g+board.s3g=='':
            moves = '6g2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w6g)and Wboard.w2g==''\
           and board.s5g+board.s4g+board.s3g=='':
            moves = '6g2g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w6g)and Wboard.w1g==''\
           and board.s5g+board.s4g+board.s3g+board.s2g=='':
            moves = '6g1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w6g)and Wboard.w1g==''\
           and board.s5g+board.s4g+board.s3g+board.s2g=='':
            moves = '6g1g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w6g)and Wboard.w4e==''\
           and board.s5f=='':
            moves = '6g4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w6g)and Wboard.w3d==''\
           and board.s5f+board.s4e=='':
            moves = '6g3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w6g)and Wboard.w2c==''\
           and board.s5f+board.s4e+board.s3d=='':
            moves = '6g2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w6g)and Wboard.w1b==''\
           and board.s5f+board.s4e+board.s3d+board.s2c=='':
            moves = '6g1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Wboard.w6g)and Wboard.w4e==''\
           and board.s5f=='':
            moves = '6g4e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w6g)and Wboard.w3d==''\
           and board.s5f+board.s4e=='':
            moves = '6g3d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w6g)and Wboard.w2c==''\
           and board.s5f+board.s4e+board.s3d=='':
            moves = '6g2c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w6g)and Wboard.w1b==''\
           and board.s5f+board.s4e+board.s3d+board.s2c=='':
            moves = '6g1b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w6g)and Wboard.w9d==''\
           and board.s8e+board.s7f=='':
            moves = '6g9d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w6g)and Wboard.w8e==''\
           and board.s7f=='':
            moves = '6g8e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w6g)and Wboard.w9d==''\
           and board.s8e+board.s7f=='':
            moves = '6g9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w6g)and Wboard.w8e==''\
           and board.s7f=='':
            moves = '6g8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w6g)and Wboard.w8i==''\
           and board.s7h=='':
            moves = '6g8i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w6g)and Wboard.w8i==''\
           and board.s7h=='':
            moves = '6g8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w6g)and Wboard.w4i==''\
           and board.s5h=='':
            moves = '6g4i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w6g)and Wboard.w4i==''\
           and board.s5h=='':
            moves = '6g4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w7g !='':
        if re.match(r'[sgk+]',    Wboard.w7g)and Wboard.w7h=='':
            moves = '7g7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgk+]',    Wboard.w7g)and Wboard.w6h=='':
            moves = '7g6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgk+]',    Wboard.w7g)and Wboard.w8h=='':
            moves = '7g8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w7g)and Wboard.w6g=='':
            moves = '7g6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w7g)and Wboard.w8g=='':
            moves = '7g8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w7g)and Wboard.w7f=='':
            moves = '7g7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w7g)and Wboard.w6f=='':
            moves = '7g6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w7g)and Wboard.w8f=='':
            moves = '7g8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[plsr]',   Wboard.w7g)and Wboard.w7h=='':
            moves = '7g7h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',     Wboard.w7g)and Wboard.w6h=='':
            moves = '7g6h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'[bs]',     Wboard.w7g)and Wboard.w8h=='':
            moves = '7g8h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('r',         Wboard.w7g)and Wboard.w6g=='':
            moves = '7g6g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',         Wboard.w7g)and Wboard.w8g=='':
            moves = '7g8g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',         Wboard.w7g)and Wboard.w7f=='':
            moves = '7g7f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',     Wboard.w7g)and Wboard.w6f=='':
            moves = '7g6f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',     Wboard.w7g)and Wboard.w8f=='':
            moves = '7g8f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w7g)and Wboard.w6i=='':
            moves = '7g6i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w7g)and Wboard.w8i=='':
            moves = '7g8i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w7g)and Wboard.w7i==''\
           and board.s7h=='':
            moves = '7g7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w7g)and Wboard.w7i==''\
           and board.s7h=='':
            moves = '7g7i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w7g)and Wboard.w7e==''\
           and board.s7f=='':
            moves = '7g7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w7g)and Wboard.w7e==''\
           and board.s7f=='':
            moves = '7g7e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w7g)and Wboard.w7d==''\
           and board.s7f+board.s7e=='':
            moves = '7g7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w7g)and Wboard.w7d==''\
           and board.s7f+board.s7e=='':
            moves = '7g7d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w7g)and Wboard.w7c==''\
           and board.s7f+board.s7e+board.s7d=='':
            moves = '7g7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w7g)and Wboard.w7c==''\
           and board.s7f+board.s7e+board.s7d=='':
            moves = '7g7c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w7g)and Wboard.w7b==''\
           and board.s7f+board.s7e+board.s7d+board.s7c=='':
            moves = '7g7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w7g)and Wboard.w7b==''\
           and board.s7f+board.s7e+board.s7d+board.s7c=='':
            moves = '7g7b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w7g)and Wboard.w7a==''\
           and board.s7f+board.s7e+board.s7d+board.s7c+board.s7b=='':
            moves = '7g7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w7g)and Wboard.w7a==''\
           and board.s7f+board.s7e+board.s7d+board.s7c+board.s7b=='':
            moves = '7g7a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w7g)and Wboard.w9g==''\
           and board.s8g=='':
            moves = '7g9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w7g)and Wboard.w9g==''\
           and board.s8g=='':
            moves = '7g9g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w7g)and Wboard.w5g==''\
           and board.s6g=='':
            moves = '7g5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w7g)and Wboard.w5g==''\
           and board.s6g=='':
            moves = '7g5g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w7g)and Wboard.w4g==''\
           and board.s6g+board.s5g=='':
            moves = '7g4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w7g)and Wboard.w4g==''\
           and board.s6g+board.s5g=='':
            moves = '7g4g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w7g)and Wboard.w3g==''\
           and board.s6g+board.s5g+board.s4g=='':
            moves = '7g3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w7g)and Wboard.w3g==''\
           and board.s6g+board.s5g+board.s4g=='':
            moves = '7g3g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w7g)and Wboard.w2g==''\
           and board.s6g+board.s5g+board.s4g+board.s3g=='':
            moves = '7g2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w7g)and Wboard.w2g==''\
           and board.s6g+board.s5g+board.s4g+board.s3g=='':
            moves = '7g2g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w7g)and Wboard.w1g==''\
           and board.s6g+board.s5g+board.s4g+board.s3g+board.s2g=='':
            moves = '7g1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w7g)and Wboard.w1g==''\
           and board.s6g+board.s5g+board.s4g+board.s3g+board.s2g=='':
            moves = '7g1g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w7g)and Wboard.w9i==''\
           and board.s8h=='':
            moves = '7g9i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w7g)and Wboard.w5e==''\
           and board.s6f=='':
            moves = '7g5e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w7g)and Wboard.w4d==''\
           and board.s6f+board.s5e=='':
            moves = '7g4d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w7g)and Wboard.w3c==''\
           and board.s6f+board.s5e+board.s4d=='':
            moves = '7g3c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w7g)and Wboard.w2b==''\
           and board.s6f+board.s5e+board.s4d+board.s3c=='':
            moves = '7g2b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w7g)and Wboard.w1a==''\
           and board.s6f+board.s5e+board.s4d+board.s3c+board.s2b=='':
            moves = '7g1a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w7g)and Wboard.w9i==''\
           and board.s8h=='':
            moves = '7g9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w7g)and Wboard.w5e==''\
           and board.s6f=='':
            moves = '7g5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w7g)and Wboard.w4d==''\
           and board.s6f+board.s5e=='':
            moves = '7g4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w7g)and Wboard.w3c==''\
           and board.s6f+board.s5e+board.s4d=='':
            moves = '7g3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w7g)and Wboard.w2b==''\
           and board.s6f+board.s5e+board.s4d+board.s3c=='':
            moves = '7g2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w7g)and Wboard.w1a==''\
           and board.s6f+board.s5e+board.s4d+board.s3c+board.s2b=='':
            moves = '7g1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w7g)and Wboard.w5i==''\
           and board.s6h=='':
            moves = '7g5i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w7g)and Wboard.w9e==''\
           and board.s8f=='':
            moves = '7g9e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w7g)and Wboard.w5i==''\
           and board.s6h=='':
            moves = '7g5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w7g)and Wboard.w9e==''\
           and board.s8f=='':
            moves = '7g9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w8g !='':
        if re.match(r'[sgk+]',    Wboard.w8g)and Wboard.w8h=='':
            moves = '8g8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgk+]',    Wboard.w8g)and Wboard.w7h=='':
            moves = '8g7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgk+]',    Wboard.w8g)and Wboard.w9h=='':
            moves = '8g9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w8g)and Wboard.w7g=='':
            moves = '8g7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w8g)and Wboard.w9g=='':
            moves = '8g9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w8g)and Wboard.w8f=='':
            moves = '8g8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w8g)and Wboard.w7f=='':
            moves = '8g7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w8g)and Wboard.w9f=='':
            moves = '8g9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[plsr]',   Wboard.w8g)and Wboard.w8h=='':
            moves = '8g8h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',     Wboard.w8g)and Wboard.w7h=='':
            moves = '8g7h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'[bs]',     Wboard.w8g)and Wboard.w9h=='':
            moves = '8g9h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('r',         Wboard.w8g)and Wboard.w7g=='':
            moves = '8g7g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',         Wboard.w8g)and Wboard.w9g=='':
            moves = '8g9g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',         Wboard.w8g)and Wboard.w8f=='':
            moves = '8g8f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',     Wboard.w8g)and Wboard.w7f=='':
            moves = '8g7f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',     Wboard.w8g)and Wboard.w9f=='':
            moves = '8g9f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w8g)and Wboard.w7i=='':
            moves = '8g7i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w8g)and Wboard.w9i=='':
            moves = '8g9i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w8g)and Wboard.w8i==''\
           and board.s8h=='':
            moves = '8g8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w8g)and Wboard.w8i==''\
           and board.s8h=='':
            moves = '8g8i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w8g)and Wboard.w8e==''\
           and board.s8f=='':
            moves = '8g8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w8g)and Wboard.w8e==''\
           and board.s8f=='':
            moves = '8g8e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w8g)and Wboard.w8d==''\
           and board.s8f+board.s8e=='':
            moves = '8g8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w8g)and Wboard.w8d==''\
           and board.s8f+board.s8e=='':
            moves = '8g8d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w8g)and Wboard.w8c==''\
           and board.s8f+board.s8e+board.s8d=='':
            moves = '8g8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w8g)and Wboard.w8c==''\
           and board.s8f+board.s8e+board.s8d=='':
            moves = '8g8c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w8g)and Wboard.w8b==''\
           and board.s8f+board.s8e+board.s8d+board.s8c=='':
            moves = '8g8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w8g)and Wboard.w8b==''\
           and board.s8f+board.s8e+board.s8d+board.s8c=='':
            moves = '8g8b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w8g)and Wboard.w8a==''\
           and board.s8f+board.s8e+board.s8d+board.s8c+board.s8b=='':
            moves = '8g8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w8g)and Wboard.w8a==''\
           and board.s8f+board.s8e+board.s8d+board.s8c+board.s8b=='':
            moves = '8g8a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w8g)and Wboard.w6g==''\
           and board.s7g=='':
            moves = '8g6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w8g)and Wboard.w6g==''\
           and board.s7g=='':
            moves = '8g6g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w8g)and Wboard.w5g==''\
           and board.s7g+board.s6g=='':
            moves = '8g5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w8g)and Wboard.w5g==''\
           and board.s7g+board.s6g=='':
            moves = '8g5g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w8g)and Wboard.w4g==''\
           and board.s7g+board.s6g+board.s5g=='':
            moves = '8g4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w8g)and Wboard.w4g==''\
           and board.s7g+board.s6g+board.s5g=='':
            moves = '8g4g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w8g)and Wboard.w3g==''\
           and board.s7g+board.s6g+board.s5g+board.s4g=='':
            moves = '8g3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w8g)and Wboard.w3g==''\
           and board.s7g+board.s6g+board.s5g+board.s4g=='':
            moves = '8g3g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w8g)and Wboard.w2g==''\
           and board.s7g+board.s6g+board.s5g+board.s4g+board.s3g=='':
            moves = '8g2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w8g)and Wboard.w2g==''\
           and board.s7g+board.s6g+board.s5g+board.s4g+board.s3g=='':
            moves = '8g2g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w8g)and Wboard.w1g==''\
           and board.s7g+board.s6g+board.s5g+board.s4g+board.s3g+board.s2g=='':
            moves = '8g1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w8g)and Wboard.w1g==''\
           and board.s7g+board.s6g+board.s5g+board.s4g+board.s3g+board.s2g=='':
            moves = '8g1g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w8g)and Wboard.w6e==''\
           and board.s7f=='':
            moves = '8g6e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w8g)and Wboard.w5d==''\
           and board.s7f+board.s6e=='':
            moves = '8g5d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w8g)and Wboard.w4c==''\
           and board.s7f+board.s6e+board.s5d=='':
            moves = '8g4c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w8g)and Wboard.w3b==''\
           and board.s7f+board.s6e+board.s5d+board.s4c=='':
            moves = '8g3b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w8g)and Wboard.w2a==''\
           and board.s7f+board.s6e+board.s5d+board.s4c+board.s3b=='':
            moves = '8g2a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w8g)and Wboard.w6e==''\
           and board.s7f=='':
            moves = '8g6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w8g)and Wboard.w5d==''\
           and board.s7f+board.s6e=='':
            moves = '8g5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w8g)and Wboard.w4c==''\
           and board.s7f+board.s6e+board.s5d=='':
            moves = '8g4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w8g)and Wboard.w3b==''\
           and board.s7f+board.s6e+board.s5d+board.s4c=='':
            moves = '8g3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w8g)and Wboard.w2a==''\
           and board.s7f+board.s6e+board.s5d+board.s4c+board.s3b=='':
            moves = '8g2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w8g)and Wboard.w6i==''\
           and board.s7h=='':
            moves = '8g6i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w8g)and Wboard.w6i==''\
           and board.s7h=='':
            moves = '8g6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w9g !='':
        if re.match(r'[sgk+]',    Wboard.w9g)and Wboard.w9h=='':
            moves = '9g9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgk+]',    Wboard.w9g)and Wboard.w8h=='':
            moves = '9g8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w9g)and Wboard.w8g=='':
            moves = '9g8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w9g)and Wboard.w9f=='':
            moves = '9g9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w9g)and Wboard.w8f=='':
            moves = '9g8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[plsr]',   Wboard.w9g)and Wboard.w9h=='':
            moves = '9g9h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',     Wboard.w9g)and Wboard.w8h=='':
            moves = '9g8h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('r',         Wboard.w9g)and Wboard.w8g=='':
            moves = '9g8g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',         Wboard.w9g)and Wboard.w9f=='':
            moves = '9g9f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',     Wboard.w9g)and Wboard.w8f=='':
            moves = '9g8f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w9g)and Wboard.w8i=='':
            moves = '9g8i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w9g)and Wboard.w9i==''\
           and board.s9h=='':
            moves = '9g9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w9g)and Wboard.w9i==''\
           and board.s9h=='':
            moves = '9g9i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w9g)and Wboard.w9e==''\
           and board.s9f=='':
            moves = '9g9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w9g)and Wboard.w9e==''\
           and board.s9f=='':
            moves = '9g9e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w9g)and Wboard.w9d==''\
           and board.s9f+board.s9e=='':
            moves = '9g9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w9g)and Wboard.w9d==''\
           and board.s9f+board.s9e=='':
            moves = '9g9d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w9g)and Wboard.w9c==''\
           and board.s9f+board.s9e+board.s9d=='':
            moves = '9g9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w9g)and Wboard.w9c==''\
           and board.s9f+board.s9e+board.s9d=='':
            moves = '9g9c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w9g)and Wboard.w9b==''\
           and board.s9f+board.s9e+board.s9d+board.s9c=='':
            moves = '9g9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w9g)and Wboard.w9b==''\
           and board.s9f+board.s9e+board.s9d+board.s9c=='':
            moves = '9g9b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w9g)and Wboard.w9a==''\
           and board.s9f+board.s9e+board.s9d+board.s9c+board.s9b=='':
            moves = '9g9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w9g)and Wboard.w9a==''\
           and board.s9f+board.s9e+board.s9d+board.s9c+board.s9b=='':
            moves = '9g9a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w9g)and Wboard.w7g==''\
           and board.s8g=='':
            moves = '9g7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w9g)and Wboard.w7g==''\
           and board.s8g=='':
            moves = '9g7g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w9g)and Wboard.w6g==''\
           and board.s8g+board.s7g=='':
            moves = '9g6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w9g)and Wboard.w6g==''\
           and board.s8g+board.s7g=='':
            moves = '9g6g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w9g)and Wboard.w5g==''\
           and board.s8g+board.s7g+board.s6g=='':
            moves = '9g5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w9g)and Wboard.w5g==''\
           and board.s8g+board.s7g+board.s6g=='':
            moves = '9g5g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',   Wboard.w9g)and Wboard.w4g==''\
           and board.s8g+board.s7g+board.s6g+board.s5g=='':
            moves = '9g4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',   Wboard.w9g)and Wboard.w4g==''\
           and board.s8g+board.s7g+board.s6g+board.s5g=='':
            moves = '9g4g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w9g)and Wboard.w3g==''\
           and board.s8g+board.s7g+board.s6g+board.s5g+board.s4g=='':
            moves = '9g3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w9g)and Wboard.w3g==''\
           and board.s8g+board.s7g+board.s6g+board.s5g+board.s4g=='':
            moves = '9g3g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w9g)and Wboard.w2g==''\
           and board.s8g+board.s7g+board.s6g+board.s5g+board.s4g+board.s3g=='':
            moves = '9g2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w9g)and Wboard.w2g==''\
           and board.s8g+board.s7g+board.s6g+board.s5g+board.s4g+board.s3g=='':
            moves = '9g2g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',      Wboard.w9g)and Wboard.w1g==''\
           and board.s8g+board.s7g+board.s6g+board.s5g+board.s4g+board.s3g+board.s2g=='':
            moves = '9g1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('r',      Wboard.w9g)and Wboard.w1g==''\
           and board.s8g+board.s7g+board.s6g+board.s5g+board.s4g+board.s3g+board.s2g=='':
            moves = '9g1g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w9g)and Wboard.w7i==''\
           and board.s8h=='':
            moves = '9g7i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w9g)and Wboard.w7e==''\
           and board.s8f=='':
            moves = '9g7e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w9g)and Wboard.w6d==''\
           and board.s8f+board.s7e=='':
            moves = '9g6d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w9g)and Wboard.w5c==''\
           and board.s8f+board.s7e+board.s6d=='':
            moves = '9g5c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w9g)and Wboard.w4b==''\
           and board.s8f+board.s7e+board.s6d+board.s5c=='':
            moves = '9g4b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w9g)and Wboard.w3a==''\
           and board.s8f+board.s7e+board.s6d+board.s5c+board.s4b=='':
            moves = '9g3a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w9g)and Wboard.w7i==''\
           and board.s8h=='':
            moves = '9g7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w9g)and Wboard.w7e==''\
           and board.s8f=='':
            moves = '9g7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w9g)and Wboard.w6d==''\
           and board.s8f+board.s7e=='':
            moves = '9g6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w9g)and Wboard.w5c==''\
           and board.s8f+board.s7e+board.s6d=='':
            moves = '9g5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w9g)and Wboard.w4b==''\
           and board.s8f+board.s7e+board.s6d+board.s5c=='':
            moves = '9g4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w9g)and Wboard.w3a==''\
           and board.s8f+board.s7e+board.s6d+board.s5c+board.s4b=='':
            moves = '9g3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w1f !='':
        if re.match(r'[lsgk+]',   Wboard.w1f)and Wboard.w1g=='':
            moves = '1f1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgk+]',    Wboard.w1f)and Wboard.w2g=='':
            moves = '1f2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w1f)and Wboard.w2f=='':
            moves = '1f2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w1f)and Wboard.w1e=='':
            moves = '1f1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w1f)and Wboard.w2e=='':
            moves = '1f2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[plsr]',   Wboard.w1f)and Wboard.w1g=='':
            moves = '1f1g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',     Wboard.w1f)and Wboard.w2g=='':
            moves = '1f2g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('n',         Wboard.w1f)and Wboard.w2h=='':
            moves = '1f2h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w1f)and Wboard.w1i==''\
           and board.s1h+board.s1g=='':
            moves = '1f1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w1f)and Wboard.w1i==''\
           and board.s1h+board.s1g=='':
            moves = '1f1i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w1f)and Wboard.w1h==''\
           and board.s1g=='':
            moves = '1f1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w1f)and Wboard.w1h==''\
           and board.s1g=='':
            moves = '1f1h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w1f)and Wboard.w1d==''\
           and board.s1e=='':
            moves = '1f1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w1f)and Wboard.w1c==''\
           and board.s1e+board.s1d=='':
            moves = '1f1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w1f)and Wboard.w1b==''\
           and board.s1e+board.s1d+board.s1c=='':
            moves = '1f1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w1f)and Wboard.w1a==''\
           and board.s1e+board.s1d+board.s1c+board.s1b=='':
            moves = '1f1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w1f)and Wboard.w3f==''\
           and board.s2f=='':
            moves = '1f3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w1f)and Wboard.w4f==''\
           and board.s2f+board.s3f=='':
            moves = '1f4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w1f)and Wboard.w5f==''\
           and board.s2f+board.s3f+board.s4f=='':
            moves = '1f5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w1f)and Wboard.w6f==''\
           and board.s2f+board.s3f+board.s4f+board.s5f=='':
            moves = '1f6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w1f)and Wboard.w7f==''\
           and board.s2f+board.s3f+board.s4f+board.s5f+board.s6f=='':
            moves = '1f7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w1f)and Wboard.w8f==''\
           and board.s2f+board.s3f+board.s4f+board.s5f+board.s6f+board.s7f=='':
            moves = '1f8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w1f)and Wboard.w9f==''\
           and board.s2f+board.s3f+board.s4f+board.s5f+board.s6f+board.s7f+board.s8f=='':
            moves = '1f9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w1f)and Wboard.w3d==''\
           and board.s2e=='':
            moves = '1f3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w1f)and Wboard.w4c==''\
           and board.s2e+board.s3d=='':
            moves = '1f4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w1f)and Wboard.w5b==''\
           and board.s2e+board.s3d+board.s4c=='':
            moves = '1f5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w1f)and Wboard.w6a==''\
           and board.s2e+board.s3d+board.s4c+board.s5b=='':
            moves = '1f6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w1f)and Wboard.w4i==''\
           and board.s3h+board.s2g=='':
            moves = '1f4i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w1f)and Wboard.w3h==''\
           and board.s2g=='':
            moves = '1f3h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w1f)and Wboard.w4i==''\
           and board.s3h+board.s2g=='':
            moves = '1f4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w1f)and Wboard.w3h==''\
           and board.s2g=='':
            moves = '1f3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w2f !='':
        if re.match(r'[lsgk+]',   Wboard.w2f)and Wboard.w2g=='':
            moves = '2f2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgk+]',    Wboard.w2f)and Wboard.w1g=='':
            moves = '2f1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgk+]',    Wboard.w2f)and Wboard.w3g=='':
            moves = '2f3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w2f)and Wboard.w1f=='':
            moves = '2f1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w2f)and Wboard.w3f=='':
            moves = '2f3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w2f)and Wboard.w2e=='':
            moves = '2f2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w2f)and Wboard.w1e=='':
            moves = '2f1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w2f)and Wboard.w3e=='':
            moves = '2f3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[plsr]',   Wboard.w2f)and Wboard.w2g=='':
            moves = '2f2g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',     Wboard.w2f)and Wboard.w1g=='':
            moves = '2f1g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'[bs]',     Wboard.w2f)and Wboard.w3g=='':
            moves = '2f3g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('n',         Wboard.w2f)and Wboard.w1h=='':
            moves = '2f1h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w2f)and Wboard.w3h=='':
            moves = '2f3h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w2f)and Wboard.w2i==''\
           and board.s2h+board.s2g=='':
            moves = '2f2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w2f)and Wboard.w2i==''\
           and board.s2h+board.s2g=='':
            moves = '2f2i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w2f)and Wboard.w2h==''\
           and board.s2g=='':
            moves = '2f2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w2f)and Wboard.w2h==''\
           and board.s2g=='':
            moves = '2f2h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w2f)and Wboard.w2d==''\
           and board.s2e=='':
            moves = '2f2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w2f)and Wboard.w2c==''\
           and board.s2e+board.s2d=='':
            moves = '2f2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w2f)and Wboard.w2b==''\
           and board.s2e+board.s2d+board.s2c=='':
            moves = '2f2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w2f)and Wboard.w2a==''\
           and board.s2e+board.s2d+board.s2c+board.s2b=='':
            moves = '2f2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w2f)and Wboard.w4f==''\
           and board.s3f=='':
            moves = '2f4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w2f)and Wboard.w5f==''\
           and board.s3f+board.s4f=='':
            moves = '2f5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w2f)and Wboard.w6f==''\
           and board.s3f+board.s4f+board.s5f=='':
            moves = '2f6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w2f)and Wboard.w7f==''\
           and board.s3f+board.s4f+board.s5f+board.s6f=='':
            moves = '2f7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w2f)and Wboard.w8f==''\
           and board.s3f+board.s4f+board.s5f+board.s6f+board.s7f=='':
            moves = '2f8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w2f)and Wboard.w9f==''\
           and board.s3f+board.s4f+board.s5f+board.s6f+board.s7f+board.s8f=='':
            moves = '2f9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w2f)and Wboard.w4d==''\
           and board.s3e=='':
            moves = '2f4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w2f)and Wboard.w5c==''\
           and board.s3e+board.s4d=='':
            moves = '2f5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w2f)and Wboard.w6b==''\
           and board.s3e+board.s4d+board.s5c=='':
            moves = '2f6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w2f)and Wboard.w7a==''\
           and board.s3e+board.s4d+board.s5c+board.s6b=='':
            moves = '2f7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w2f)and Wboard.w5i==''\
           and board.s4h+board.s3g=='':
            moves = '2f5i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w2f)and Wboard.w4h==''\
           and board.s3g=='':
            moves = '2f4h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w2f)and Wboard.w5i==''\
           and board.s4h+board.s3g=='':
            moves = '2f5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w2f)and Wboard.w4h==''\
           and board.s3g=='':
            moves = '2f4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w3f !='':
        if re.match(r'[lsgk+]',   Wboard.w3f)and Wboard.w3g=='':
            moves = '3f3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgk+]',    Wboard.w3f)and Wboard.w2g=='':
            moves = '3f2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgk+]',    Wboard.w3f)and Wboard.w4g=='':
            moves = '3f4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w3f)and Wboard.w2f=='':
            moves = '3f2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w3f)and Wboard.w4f=='':
            moves = '3f4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w3f)and Wboard.w3e=='':
            moves = '3f3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w3f)and Wboard.w2e=='':
            moves = '3f2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w3f)and Wboard.w4e=='':
            moves = '3f4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[plsr]',   Wboard.w3f)and Wboard.w3g=='':
            moves = '3f3g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',     Wboard.w3f)and Wboard.w2g=='':
            moves = '3f2g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'[bs]',     Wboard.w3f)and Wboard.w4g=='':
            moves = '3f4g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('n',         Wboard.w3f)and Wboard.w2h=='':
            moves = '3f2h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w3f)and Wboard.w4h=='':
            moves = '3f4h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w3f)and Wboard.w3i==''\
           and board.s3h+board.s3g=='':
            moves = '3f3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w3f)and Wboard.w3i==''\
           and board.s3h+board.s3g=='':
            moves = '3f3i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w3f)and Wboard.w3h==''\
           and board.s3g=='':
            moves = '3f3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w3f)and Wboard.w3h==''\
           and board.s3g=='':
            moves = '3f3h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w3f)and Wboard.w3d==''\
           and board.s3e=='':
            moves = '3f3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w3f)and Wboard.w3c==''\
           and board.s3e+board.s3d=='':
            moves = '3f3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w3f)and Wboard.w3b==''\
           and board.s3e+board.s3d+board.s3c=='':
            moves = '3f3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w3f)and Wboard.w3a==''\
           and board.s3e+board.s3d+board.s3c+board.s3b=='':
            moves = '3f3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w3f)and Wboard.w1f==''\
           and board.s2f=='':
            moves = '3f1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w3f)and Wboard.w5f==''\
           and board.s4f=='':
            moves = '3f5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w3f)and Wboard.w6f==''\
           and board.s4f+board.s5f=='':
            moves = '3f6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w3f)and Wboard.w7f==''\
           and board.s4f+board.s5f+board.s6f=='':
            moves = '3f7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w3f)and Wboard.w8f==''\
           and board.s4f+board.s5f+board.s6f+board.s7f=='':
            moves = '3f8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w3f)and Wboard.w9f==''\
           and board.s4f+board.s5f+board.s6f+board.s7f+board.s8f=='':
            moves = '3f9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w3f)and Wboard.w1h==''\
           and board.s2g=='':
            moves = '3f1h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w3f)and Wboard.w1h==''\
           and board.s2g=='':
            moves = '3f1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w3f)and Wboard.w5d==''\
           and board.s4e=='':
            moves = '3f5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w3f)and Wboard.w6c==''\
           and board.s4e+board.s5d=='':
            moves = '3f6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w3f)and Wboard.w7b==''\
           and board.s4e+board.s5d+board.s6c=='':
            moves = '3f7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w3f)and Wboard.w8a==''\
           and board.s4e+board.s5d+board.s6c+board.s7b=='':
            moves = '3f8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w3f)and Wboard.w6i==''\
           and board.s5h+board.s4g=='':
            moves = '3f6i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w3f)and Wboard.w5h==''\
           and board.s4g=='':
            moves = '3f5h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w3f)and Wboard.w6i==''\
           and board.s5h+board.s4g=='':
            moves = '3f6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w3f)and Wboard.w5h==''\
           and board.s4g=='':
            moves = '3f5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w3f)and Wboard.w1d==''\
           and board.s2e=='':
            moves = '3f1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w4f !='':
        if re.match(r'[lsgk+]',   Wboard.w4f)and Wboard.w4g=='':
            moves = '4f4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgk+]',    Wboard.w4f)and Wboard.w3g=='':
            moves = '4f3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgk+]',    Wboard.w4f)and Wboard.w5g=='':
            moves = '4f5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w4f)and Wboard.w3f=='':
            moves = '4f3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w4f)and Wboard.w5f=='':
            moves = '4f5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w4f)and Wboard.w4e=='':
            moves = '4f4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w4f)and Wboard.w3e=='':
            moves = '4f3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w4f)and Wboard.w5e=='':
            moves = '4f5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[plsr]',   Wboard.w4f)and Wboard.w4g=='':
            moves = '4f4g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',     Wboard.w4f)and Wboard.w3g=='':
            moves = '4f3g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'[bs]',     Wboard.w4f)and Wboard.w5g=='':
            moves = '4f5g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('n',         Wboard.w4f)and Wboard.w3h=='':
            moves = '4f3h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w4f)and Wboard.w5h=='':
            moves = '4f5h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w4f)and Wboard.w4i==''\
           and board.s4h+board.s4g=='':
            moves = '4f4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w4f)and Wboard.w4i==''\
           and board.s4h+board.s4g=='':
            moves = '4f4i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w4f)and Wboard.w4h==''\
           and board.s4g=='':
            moves = '4f4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w4f)and Wboard.w4h==''\
           and board.s4g=='':
            moves = '4f4h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w4f)and Wboard.w4d==''\
           and board.s4e=='':
            moves = '4f4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w4f)and Wboard.w4c==''\
           and board.s4e+board.s4d=='':
            moves = '4f4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w4f)and Wboard.w4b==''\
           and board.s4e+board.s4d+board.s4c=='':
            moves = '4f4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w4f)and Wboard.w4a==''\
           and board.s4e+board.s4d+board.s4c+board.s4b=='':
            moves = '4f4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w4f)and Wboard.w1f==''\
           and board.s2f+board.s3f=='':
            moves = '4f1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w4f)and Wboard.w2f==''\
           and board.s3f=='':
            moves = '4f2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w4f)and Wboard.w6f==''\
           and board.s5f=='':
            moves = '4f6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w4f)and Wboard.w7f==''\
           and board.s5f+board.s6f=='':
            moves = '4f7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w4f)and Wboard.w8f==''\
           and board.s5f+board.s6f+board.s7f=='':
            moves = '4f8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w4f)and Wboard.w9f==''\
           and board.s5f+board.s6f+board.s7f+board.s8f=='':
            moves = '4f9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w4f)and Wboard.w1i==''\
           and board.s2h+board.s3g=='':
            moves = '4f1i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w4f)and Wboard.w2h==''\
           and board.s3g=='':
            moves = '4f2h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w4f)and Wboard.w1i==''\
           and board.s2h+board.s3g=='':
            moves = '4f1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w4f)and Wboard.w2h==''\
           and board.s3g=='':
            moves = '4f2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w4f)and Wboard.w6d==''\
           and board.s5e=='':
            moves = '4f6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w4f)and Wboard.w7c==''\
           and board.s5e+board.s6d=='':
            moves = '4f7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w4f)and Wboard.w8b==''\
           and board.s5e+board.s6d+board.s7c=='':
            moves = '4f8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w4f)and Wboard.w9a==''\
           and board.s5e+board.s6d+board.s7c+board.s8b=='':
            moves = '4f9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w4f)and Wboard.w7i==''\
           and board.s6h+board.s5g=='':
            moves = '4f7i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w4f)and Wboard.w6h==''\
           and board.s5g=='':
            moves = '4f6h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w4f)and Wboard.w7i==''\
           and board.s6h+board.s5g=='':
            moves = '4f7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w4f)and Wboard.w6h==''\
           and board.s5g=='':
            moves = '4f6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w4f)and Wboard.w2d==''\
           and board.s3e=='':
            moves = '4f2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w4f)and Wboard.w1c==''\
           and board.s3e+board.s2d=='':
            moves = '4f1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w5f !='':
        if re.match(r'[lsgk+]',   Wboard.w5f)and Wboard.w5g=='':
            moves = '5f5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgk+]',    Wboard.w5f)and Wboard.w4g=='':
            moves = '5f4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgk+]',    Wboard.w5f)and Wboard.w6g=='':
            moves = '5f6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w5f)and Wboard.w4f=='':
            moves = '5f4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w5f)and Wboard.w6f=='':
            moves = '5f6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w5f)and Wboard.w5e=='':
            moves = '5f5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w5f)and Wboard.w4e=='':
            moves = '5f4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w5f)and Wboard.w6e=='':
            moves = '5f6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[plsr]',   Wboard.w5f)and Wboard.w5g=='':
            moves = '5f5g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',     Wboard.w5f)and Wboard.w4g=='':
            moves = '5f4g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'[bs]',     Wboard.w5f)and Wboard.w6g=='':
            moves = '5f6g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('n',         Wboard.w5f)and Wboard.w4h=='':
            moves = '5f4h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w5f)and Wboard.w6h=='':
            moves = '5f6h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w5f)and Wboard.w5i==''\
           and board.s5h+board.s5g=='':
            moves = '5f5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w5f)and Wboard.w5i==''\
           and board.s5h+board.s5g=='':
            moves = '5f5i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w5f)and Wboard.w5h==''\
           and board.s5g=='':
            moves = '5f5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w5f)and Wboard.w5h==''\
           and board.s5g=='':
            moves = '5f5h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w5f)and Wboard.w5d==''\
           and board.s5e=='':
            moves = '5f5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w5f)and Wboard.w5c==''\
           and board.s5e+board.s5d=='':
            moves = '5f5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w5f)and Wboard.w5b==''\
           and board.s5e+board.s5d+board.s5c=='':
            moves = '5f5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w5f)and Wboard.w5a==''\
           and board.s5e+board.s5d+board.s5c+board.s5b=='':
            moves = '5f5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w5f)and Wboard.w1f==''\
           and board.s2f+board.s3f+board.s4f=='':
            moves = '5f1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w5f)and Wboard.w2f==''\
           and board.s3f+board.s4f=='':
            moves = '5f2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w5f)and Wboard.w3f==''\
           and board.s4f=='':
            moves = '5f3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w5f)and Wboard.w7f==''\
           and board.s6f=='':
            moves = '5f7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w5f)and Wboard.w8f==''\
           and board.s6f+board.s7f=='':
            moves = '5f8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w5f)and Wboard.w9f==''\
           and board.s6f+board.s7f+board.s8f=='':
            moves = '5f9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w5f)and Wboard.w2i==''\
          and board.s3h+board.s4g=='':
           moves ='5f2i+'
           kaihimore(moves)
           if oute.oute == 0:
              depth1.append(moves)
        if re.match('b',Wboard.w5f)and Wboard.w3h==''\
          and board.s4g=='':
           moves ='5f3h+'
           kaihimore(moves)
           if oute.oute == 0:
              depth1.append(moves)
        if re.match('\+b',  Wboard.w5f)and Wboard.w2i==''\
          and board.s3h+board.s4g=='':
           moves ='5f2i'
           kaihimore(moves)
           if oute.oute == 0:
              depth1.append(moves)
        if re.match('\+b',Wboard.w5f)and Wboard.w3h==''\
          and board.s4g=='':
           moves ='5f3h'
           kaihimore(moves)
           if oute.oute == 0:
              depth1.append(moves)
        if re.match(r'\+b|b',  Wboard.w5f)and Wboard.w7d==''\
          and board.s6e=='':
           moves ='5f7d'
           kaihimore(moves)
           if oute.oute == 0:
              depth1.append(moves)
        if re.match(r'\+b|b',  Wboard.w5f)and Wboard.w8c==''\
          and board.s6e+board.s7d=='':
           moves ='5f8c'
           kaihimore(moves)
           if oute.oute == 0:
              depth1.append(moves)
        if re.match(r'\+b|b',  Wboard.w5f)and Wboard.w9b==''\
          and board.s6e+board.s7d+board.s8c=='':
           moves ='5f9b'
           kaihimore(moves)
           if oute.oute == 0:
              depth1.append(moves)
        if re.match('b',Wboard.w5f)and Wboard.w8i==''\
          and board.s7h+board.s6g=='':
           moves ='5f8i+'
           kaihimore(moves)
           if oute.oute == 0:
              depth1.append(moves)
        if re.match('b',Wboard.w5f)and Wboard.w7h==''\
          and board.s6g=='':
           moves ='5f7h+'
           kaihimore(moves)
           if oute.oute == 0:
              depth1.append(moves)
        if re.match('\+b',  Wboard.w5f)and Wboard.w8i==''\
          and board.s7h+board.s6g=='':
           moves ='5f8i'
           kaihimore(moves)
           if oute.oute == 0:
              depth1.append(moves)
        if re.match('\+b',Wboard.w5f)and Wboard.w7h==''\
          and board.s6g=='':
           moves ='5f7h'
           kaihimore(moves)
           if oute.oute == 0:
              depth1.append(moves)
        if re.match(r'\+b|b',  Wboard.w5f)and Wboard.w3d==''\
          and board.s4e=='':
           moves ='5f3d'
           kaihimore(moves)
           if oute.oute == 0:
              depth1.append(moves)
        if re.match(r'\+b|b',  Wboard.w5f)and Wboard.w2c==''\
          and board.s4e+board.s3d=='':
           moves ='5f2c'
           kaihimore(moves)
           if oute.oute == 0:
              depth1.append(moves)

    if Wboard.w6f !='':
        if re.match(r'[lsgk+]',   Wboard.w6f)and Wboard.w6g=='':
            moves = '6f6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgk+]',    Wboard.w6f)and Wboard.w5g=='':
            moves = '6f5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgk+]',    Wboard.w6f)and Wboard.w7g=='':
            moves = '6f7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w6f)and Wboard.w5f=='':
            moves = '6f5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w6f)and Wboard.w7f=='':
            moves = '6f7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w6f)and Wboard.w6e=='':
            moves = '6f6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w6f)and Wboard.w5e=='':
            moves = '6f5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w6f)and Wboard.w7e=='':
            moves = '6f7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[plsr]',   Wboard.w6f)and Wboard.w6g=='':
            moves = '6f6g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',     Wboard.w6f)and Wboard.w5g=='':
            moves = '6f5g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'[bs]',     Wboard.w6f)and Wboard.w7g=='':
            moves = '6f7g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('n',         Wboard.w6f)and Wboard.w5h=='':
            moves = '6f5h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w6f)and Wboard.w7h=='':
            moves = '6f7h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w6f)and Wboard.w6i==''\
           and board.s6h+board.s6g=='':
            moves = '6f6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w6f)and Wboard.w6i==''\
           and board.s6h+board.s6g=='':
            moves = '6f6i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w6f)and Wboard.w6h==''\
           and board.s6g=='':
            moves = '6f6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w6f)and Wboard.w6h==''\
           and board.s6g=='':
            moves = '6f6h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w6f)and Wboard.w6d==''\
           and board.s6e=='':
            moves = '6f6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w6f)and Wboard.w6c==''\
           and board.s6e+board.s6d=='':
            moves = '6f6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w6f)and Wboard.w6b==''\
           and board.s6e+board.s6d+board.s6c=='':
            moves = '6f6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w6f)and Wboard.w6a==''\
           and board.s6e+board.s6d+board.s6c+board.s6b=='':
            moves = '6f6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w6f)and Wboard.w9f==''\
           and board.s8f+board.s7f=='':
            moves = '6f9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w6f)and Wboard.w8f==''\
           and board.s7f=='':
            moves = '6f8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w6f)and Wboard.w4f==''\
           and board.s5f=='':
            moves = '6f4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w6f)and Wboard.w3f==''\
           and board.s5f+board.s4f=='':
            moves = '6f3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w6f)and Wboard.w2f==''\
           and board.s5f+board.s4f+board.s3f=='':
            moves = '6f2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w6f)and Wboard.w1f==''\
           and board.s5f+board.s4f+board.s3f+board.s2f=='':
            moves = '6f1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w6f)and Wboard.w9i==''\
           and board.s8h+board.s7g=='':
            moves = '6f9i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w6f)and Wboard.w8h==''\
           and board.s7g=='':
            moves = '6f8h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w6f)and Wboard.w9i==''\
           and board.s8h+board.s7g=='':
            moves = '6f9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w6f)and Wboard.w8h==''\
           and board.s7g=='':
            moves = '6f8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w6f)and Wboard.w4d==''\
           and board.s5e=='':
            moves = '6f4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w6f)and Wboard.w3c==''\
           and board.s5e+board.s4d=='':
            moves = '6f3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w6f)and Wboard.w2b==''\
           and board.s5e+board.s4d+board.s3c=='':
            moves = '6f2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w6f)and Wboard.w1a==''\
           and board.s5e+board.s4d+board.s3c+board.s2b=='':
            moves = '6f1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w6f)and Wboard.w3i==''\
           and board.s4h+board.s5g=='':
            moves = '6f3i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w6f)and Wboard.w4h==''\
           and board.s5g=='':
            moves = '6f4h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w6f)and Wboard.w3i==''\
           and board.s4h+board.s5g=='':
            moves = '6f3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w6f)and Wboard.w4h==''\
           and board.s5g=='':
            moves = '6f4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w6f)and Wboard.w8d==''\
           and board.s7e=='':
            moves = '6f8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w6f)and Wboard.w9c==''\
           and board.s7e+board.s8d=='':
            moves = '6f9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w7f !='':
        if re.match(r'[lsgk+]',   Wboard.w7f)and Wboard.w7g=='':
            moves = '7f7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgk+]',    Wboard.w7f)and Wboard.w6g=='':
            moves = '7f6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgk+]',    Wboard.w7f)and Wboard.w8g=='':
            moves = '7f8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w7f)and Wboard.w6f=='':
            moves = '7f6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w7f)and Wboard.w8f=='':
            moves = '7f8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w7f)and Wboard.w7e=='':
            moves = '7f7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w7f)and Wboard.w6e=='':
            moves = '7f6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w7f)and Wboard.w8e=='':
            moves = '7f8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[plsr]',   Wboard.w7f)and Wboard.w7g=='':
            moves = '7f7g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',     Wboard.w7f)and Wboard.w6g=='':
            moves = '7f6g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'[bs]',     Wboard.w7f)and Wboard.w8g=='':
            moves = '7f8g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('n',         Wboard.w7f)and Wboard.w6h=='':
            moves = '7f6h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w7f)and Wboard.w8h=='':
            moves = '7f8h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w7f)and Wboard.w7i==''\
           and board.s7h+board.s7g=='':
            moves = '7f7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w7f)and Wboard.w7i==''\
           and board.s7h+board.s7g=='':
            moves = '7f7i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w7f)and Wboard.w7h==''\
           and board.s7g=='':
            moves = '7f7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w7f)and Wboard.w7h==''\
           and board.s7g=='':
            moves = '7f7h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w7f)and Wboard.w7d==''\
           and board.s7e=='':
            moves = '7f7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w7f)and Wboard.w7c==''\
           and board.s7e+board.s7d=='':
            moves = '7f7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w7f)and Wboard.w7b==''\
           and board.s7e+board.s7d+board.s7c=='':
            moves = '7f7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w7f)and Wboard.w7a==''\
           and board.s7e+board.s7d+board.s7c+board.s7b=='':
            moves = '7f7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w7f)and Wboard.w9f==''\
           and board.s8f=='':
            moves = '7f9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w7f)and Wboard.w5f==''\
           and board.s6f=='':
            moves = '7f5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w7f)and Wboard.w4f==''\
           and board.s6f+board.s5f=='':
            moves = '7f4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w7f)and Wboard.w3f==''\
           and board.s6f+board.s5f+board.s4f=='':
            moves = '7f3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w7f)and Wboard.w2f==''\
           and board.s6f+board.s5f+board.s4f+board.s3f=='':
            moves = '7f2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w7f)and Wboard.w1f==''\
           and board.s6f+board.s5f+board.s4f+board.s3f+board.s2f=='':
            moves = '7f1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w7f)and Wboard.w9h==''\
           and board.s8g=='':
            moves = '7f9h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w7f)and Wboard.w9h==''\
           and board.s8g=='':
            moves = '7f9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w7f)and Wboard.w5d==''\
           and board.s6e=='':
            moves = '7f5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w7f)and Wboard.w4c==''\
           and board.s6e+board.s5d=='':
            moves = '7f4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w7f)and Wboard.w3b==''\
           and board.s6e+board.s5d+board.s4c=='':
            moves = '7f3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w7f)and Wboard.w2a==''\
           and board.s6e+board.s5d+board.s4c+board.s3b=='':
            moves = '7f2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w7f)and Wboard.w4i==''\
           and board.s5h+board.s6g=='':
            moves = '7f4i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w7f)and Wboard.w5h==''\
           and board.s6g=='':
            moves = '7f5h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w7f)and Wboard.w4i==''\
           and board.s5h+board.s6g=='':
            moves = '7f4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w7f)and Wboard.w5h==''\
           and board.s6g=='':
            moves = '7f5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w7f)and Wboard.w9d==''\
           and board.s8e=='':
            moves = '7f9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w8f !='':
        if re.match(r'[lsgk+]',   Wboard.w8f)and Wboard.w8g=='':
            moves = '8f8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgk+]',    Wboard.w8f)and Wboard.w7g=='':
            moves = '8f7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgk+]',    Wboard.w8f)and Wboard.w9g=='':
            moves = '8f9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w8f)and Wboard.w7f=='':
            moves = '8f7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w8f)and Wboard.w9f=='':
            moves = '8f9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w8f)and Wboard.w8e=='':
            moves = '8f8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w8f)and Wboard.w7e=='':
            moves = '8f7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w8f)and Wboard.w9e=='':
            moves = '8f9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[plsr]',   Wboard.w8f)and Wboard.w8g=='':
            moves = '8f8g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',     Wboard.w8f)and Wboard.w7g=='':
            moves = '8f7g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'[bs]',     Wboard.w8f)and Wboard.w9g=='':
            moves = '8f9g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('n',         Wboard.w8f)and Wboard.w7h=='':
            moves = '8f7h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w8f)and Wboard.w9h=='':
            moves = '8f9h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w8f)and Wboard.w8i==''\
           and board.s8h+board.s8g=='':
            moves = '8f8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w8f)and Wboard.w8i==''\
           and board.s8h+board.s8g=='':
            moves = '8f8i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w8f)and Wboard.w8h==''\
           and board.s8g=='':
            moves = '8f8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w8f)and Wboard.w8h==''\
           and board.s8g=='':
            moves = '8f8h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w8f)and Wboard.w8d==''\
           and board.s8e=='':
            moves = '8f8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w8f)and Wboard.w8c==''\
           and board.s8e+board.s8d=='':
            moves = '8f8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w8f)and Wboard.w8b==''\
           and board.s8e+board.s8d+board.s8c=='':
            moves = '8f8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w8f)and Wboard.w8a==''\
           and board.s8e+board.s8d+board.s8c+board.s8b=='':
            moves = '8f8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w8f)and Wboard.w6f==''\
           and board.s7f=='':
            moves = '8f6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w8f)and Wboard.w5f==''\
           and board.s7f+board.s6f=='':
            moves = '8f5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w8f)and Wboard.w4f==''\
           and board.s7f+board.s6f+board.s5f=='':
            moves = '8f4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w8f)and Wboard.w3f==''\
           and board.s7f+board.s6f+board.s5f+board.s4f=='':
            moves = '8f3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w8f)and Wboard.w2f==''\
           and board.s7f+board.s6f+board.s5f+board.s4f+board.s3f=='':
            moves = '8f2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w8f)and Wboard.w1f==''\
           and board.s7f+board.s6f+board.s5f+board.s4f+board.s3f+board.s2f=='':
            moves = '8f1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w8f)and Wboard.w6d==''\
           and board.s7e=='':
            moves = '8f6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w8f)and Wboard.w5c==''\
           and board.s7e+board.s6d=='':
            moves = '8f5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w8f)and Wboard.w4b==''\
           and board.s7e+board.s6d+board.s5c=='':
            moves = '8f4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w8f)and Wboard.w3a==''\
           and board.s7e+board.s6d+board.s5c+board.s4b=='':
            moves = '8f3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w8f)and Wboard.w5i==''\
           and board.s6h+board.s7g=='':
            moves = '8f5i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w8f)and Wboard.w6h==''\
           and board.s7g=='':
            moves = '8f6h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w8f)and Wboard.w5i==''\
           and board.s6h+board.s7g=='':
            moves = '8f5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w8f)and Wboard.w6h==''\
           and board.s7g=='':
            moves = '8f6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w9f !='':
        if re.match(r'[lsgk+]',   Wboard.w9f)and Wboard.w9g=='':
            moves = '9f9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgk+]',    Wboard.w9f)and Wboard.w8g=='':
            moves = '9f8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w9f)and Wboard.w8f=='':
            moves = '9f8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[gk+]',     Wboard.w9f)and Wboard.w9e=='':
            moves = '9f9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|s|k',Wboard.w9f)and Wboard.w8e=='':
            moves = '9f8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[plsr]',   Wboard.w9f)and Wboard.w9g=='':
            moves = '9f9g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[bs]',     Wboard.w9f)and Wboard.w8g=='':
            moves = '9f8g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('n',         Wboard.w9f)and Wboard.w8h=='':
            moves = '9f8h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w9f)and Wboard.w9i==''\
           and board.s9h+board.s9g=='':
            moves = '9f9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w9f)and Wboard.w9i==''\
           and board.s9h+board.s9g=='':
            moves = '9f9i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w9f)and Wboard.w9h==''\
           and board.s9g=='':
            moves = '9f9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w9f)and Wboard.w9h==''\
           and board.s9g=='':
            moves = '9f9h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w9f)and Wboard.w9d==''\
           and board.s9e=='':
            moves = '9f9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w9f)and Wboard.w9c==''\
           and board.s9e+board.s9d=='':
            moves = '9f9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w9f)and Wboard.w9b==''\
           and board.s9e+board.s9d+board.s9c=='':
            moves = '9f9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w9f)and Wboard.w9a==''\
           and board.s9e+board.s9d+board.s9c+board.s9b=='':
            moves = '9f9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w9f)and Wboard.w7f==''\
           and board.s8f=='':
            moves = '9f7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w9f)and Wboard.w6f==''\
           and board.s8f+board.s7f=='':
            moves = '9f6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w9f)and Wboard.w5f==''\
           and board.s8f+board.s7f+board.s6f=='':
            moves = '9f5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w9f)and Wboard.w4f==''\
           and board.s8f+board.s7f+board.s6f+board.s5f=='':
            moves = '9f4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w9f)and Wboard.w3f==''\
           and board.s8f+board.s7f+board.s6f+board.s5f+board.s4f=='':
            moves = '9f3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w9f)and Wboard.w2f==''\
           and board.s8f+board.s7f+board.s6f+board.s5f+board.s4f+board.s3f=='':
            moves = '9f2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w9f)and Wboard.w1f==''\
           and board.s8f+board.s7f+board.s6f+board.s5f+board.s4f+board.s3f+board.s2f=='':
            moves = '9f1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w9f)and Wboard.w7d==''\
           and board.s8e=='':
            moves = '9f7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w9f)and Wboard.w6c==''\
           and board.s8e+board.s7d=='':
            moves = '9f6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w9f)and Wboard.w5b==''\
           and board.s8e+board.s7d+board.s6c=='':
            moves = '9f5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w9f)and Wboard.w4a==''\
           and board.s8e+board.s7d+board.s6c+board.s5b=='':
            moves = '9f4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w9f)and Wboard.w6i==''\
           and board.s7h+board.s8g=='':
            moves = '9f6i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w9f)and Wboard.w7h==''\
           and board.s8g=='':
            moves = '9f7h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w9f)and Wboard.w6i==''\
           and board.s7h+board.s8g=='':
            moves = '9f6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w9f)and Wboard.w7h==''\
           and board.s8g=='':
            moves = '9f7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w1e !='':
        if re.match(r'[plsgrk+]',   Wboard.w1e)and Wboard.w1f=='':
            moves = '1e1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w1e)and Wboard.w2f=='':
            moves = '1e2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w1e)and Wboard.w2e=='':
            moves = '1e2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w1e)and Wboard.w1d=='':
            moves = '1e1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w1e)and Wboard.w2d=='':
            moves = '1e2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w1e)and Wboard.w2g=='':
            moves = '1e2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w1e)and Wboard.w2g=='':
            moves = '1e2g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w1e)and Wboard.w1i==''\
           and board.s1h+board.s1g+board.s1f=='':
            moves = '1e1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w1e)and Wboard.w1i==''\
           and board.s1h+board.s1g+board.s1f=='':
            moves = '1e1i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w1e)and Wboard.w1h==''\
           and board.s1g+board.s1f=='':
            moves = '1e1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w1e)and Wboard.w1h==''\
           and board.s1g+board.s1f=='':
            moves = '1e1h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|l',    Wboard.w1e)and Wboard.w1g==''\
           and board.s1f=='':
            moves = '1e1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w1e)and Wboard.w1g==''\
           and board.s1f=='':
            moves = '1e1g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w1e)and Wboard.w1c==''\
           and board.s1d=='':
            moves = '1e1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w1e)and Wboard.w1b==''\
           and board.s1d+board.s1c=='':
            moves = '1e1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w1e)and Wboard.w1a==''\
           and board.s1d+board.s1c+board.s1b=='':
            moves = '1e1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w1e)and Wboard.w3e==''\
           and board.s2e=='':
            moves = '1e3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w1e)and Wboard.w4e==''\
           and board.s2e+board.s3e=='':
            moves = '1e4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w1e)and Wboard.w5e==''\
           and board.s2e+board.s3e+board.s4e=='':
            moves = '1e5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w1e)and Wboard.w6e==''\
           and board.s2e+board.s3e+board.s4e+board.s5e=='':
            moves = '1e6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w1e)and Wboard.w7e==''\
           and board.s2e+board.s3e+board.s4e+board.s5e+board.s6e=='':
            moves = '1e7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w1e)and Wboard.w8e==''\
           and board.s2e+board.s3e+board.s4e+board.s5e+board.s6e+board.s7e=='':
            moves = '1e8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w1e)and Wboard.w9e==''\
           and board.s2e+board.s3e+board.s4e+board.s5e+board.s6e+board.s7e+board.s8e=='':
            moves = '1e9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w1e)and Wboard.w3c==''\
           and board.s2d=='':
            moves = '1e3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w1e)and Wboard.w4b==''\
           and board.s2d+board.s3c=='':
            moves = '1e4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w1e)and Wboard.w5a==''\
           and board.s2d+board.s3c+board.s4b=='':
            moves = '1e5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w1e)and Wboard.w5i==''\
           and board.s4h+board.s3g+board.s2f=='':
            moves = '1e5i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w1e)and Wboard.w4h==''\
           and board.s3g+board.s2f=='':
            moves = '1e4h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w1e)and Wboard.w3g==''\
           and board.s2f=='':
            moves = '1e3g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w1e)and Wboard.w5i==''\
           and board.s4h+board.s3g+board.s2f=='':
            moves = '1e5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w1e)and Wboard.w4h==''\
           and board.s3g+board.s2f=='':
            moves = '1e4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',Wboard.w1e)and Wboard.w3g==''\
           and board.s2f=='':
            moves = '1e3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w2e !='':
        if re.match(r'[plsgrk+]',   Wboard.w2e)and Wboard.w2f=='':
            moves = '2e2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w2e)and Wboard.w1f=='':
            moves = '2e1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w2e)and Wboard.w3f=='':
            moves = '2e3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w2e)and Wboard.w1e=='':
            moves = '2e1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w2e)and Wboard.w3e=='':
            moves = '2e3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w2e)and Wboard.w2d=='':
            moves = '2e2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w2e)and Wboard.w1d=='':
            moves = '2e1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w2e)and Wboard.w3d=='':
            moves = '2e3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w2e)and Wboard.w1g=='':
            moves = '2e1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w2e)and Wboard.w3g=='':
            moves = '2e3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w2e)and Wboard.w1g=='':
            moves = '2e1g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w2e)and Wboard.w3g=='':
            moves = '2e3g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w2e)and Wboard.w2i==''\
           and board.s2h+board.s2g+board.s2f=='':
            moves = '2e2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w2e)and Wboard.w2i==''\
           and board.s2h+board.s2g+board.s2f=='':
            moves = '2e2i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w2e)and Wboard.w2h==''\
           and board.s2g+board.s2f=='':
            moves = '2e2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w2e)and Wboard.w2h==''\
           and board.s2g+board.s2f=='':
            moves = '2e2h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|l',    Wboard.w2e)and Wboard.w2g==''\
           and board.s2f=='':
            moves = '2e2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w2e)and Wboard.w2g==''\
           and board.s2f=='':
            moves = '2e2g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w2e)and Wboard.w2c==''\
           and board.s2d=='':
            moves = '2e2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w2e)and Wboard.w2b==''\
           and board.s2d+board.s2c=='':
            moves = '2e2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w2e)and Wboard.w2a==''\
           and board.s2d+board.s2c+board.s2b=='':
            moves = '2e2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w2e)and Wboard.w4e==''\
           and board.s3e=='':
            moves = '2e4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w2e)and Wboard.w5e==''\
           and board.s3e+board.s4e=='':
            moves = '2e5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w2e)and Wboard.w6e==''\
           and board.s3e+board.s4e+board.s5e=='':
            moves = '2e6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w2e)and Wboard.w7e==''\
           and board.s3e+board.s4e+board.s5e+board.s6e=='':
            moves = '2e7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w2e)and Wboard.w8e==''\
           and board.s3e+board.s4e+board.s5e+board.s6e+board.s7e=='':
            moves = '2e8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w2e)and Wboard.w9e==''\
           and board.s3e+board.s4e+board.s5e+board.s6e+board.s7e+board.s8e=='':
            moves = '2e9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w2e)and Wboard.w4c==''\
           and board.s3d=='':
            moves = '2e4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w2e)and Wboard.w5b==''\
           and board.s3d+board.s4c=='':
            moves = '2e5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w2e)and Wboard.w6a==''\
           and board.s3d+board.s4c+board.s5b=='':
            moves = '2e6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w2e)and Wboard.w6i==''\
           and board.s5h+board.s4g+board.s3f=='':
            moves = '2e6i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w2e)and Wboard.w5h==''\
           and board.s4g+board.s3f=='':
            moves = '2e5h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w2e)and Wboard.w4g==''\
           and board.s3f=='':
            moves = '2e4g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w2e)and Wboard.w6i==''\
           and board.s5h+board.s4g+board.s3f=='':
            moves = '2e6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w2e)and Wboard.w5h==''\
           and board.s4g+board.s3f=='':
            moves = '2e5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',Wboard.w2e)and Wboard.w4g==''\
           and board.s3f=='':
            moves = '2e4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w3e !='':
        if re.match(r'[plsgrk+]',   Wboard.w3e)and Wboard.w3f=='':
            moves = '3e3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w3e)and Wboard.w2f=='':
            moves = '3e2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w3e)and Wboard.w4f=='':
            moves = '3e4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w3e)and Wboard.w2e=='':
            moves = '3e2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w3e)and Wboard.w4e=='':
            moves = '3e4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w3e)and Wboard.w3d=='':
            moves = '3e3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w3e)and Wboard.w2d=='':
            moves = '3e2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w3e)and Wboard.w4d=='':
            moves = '3e4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w3e)and Wboard.w2g=='':
            moves = '3e2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w3e)and Wboard.w4g=='':
            moves = '3e4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w3e)and Wboard.w2g=='':
            moves = '3e2g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w3e)and Wboard.w4g=='':
            moves = '3e4g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w3e)and Wboard.w3i==''\
           and board.s3h+board.s3g+board.s3f=='':
            moves = '3e3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w3e)and Wboard.w3i==''\
           and board.s3h+board.s3g+board.s3f=='':
            moves = '3e3i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w3e)and Wboard.w3h==''\
           and board.s3g+board.s3f=='':
            moves = '3e3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w3e)and Wboard.w3h==''\
           and board.s3g+board.s3f=='':
            moves = '3e3h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|l',    Wboard.w3e)and Wboard.w3g==''\
           and board.s3f=='':
            moves = '3e3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w3e)and Wboard.w3g==''\
           and board.s3f=='':
            moves = '3e3g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w3e)and Wboard.w3c==''\
           and board.s3d=='':
            moves = '3e3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w3e)and Wboard.w3b==''\
           and board.s3d+board.s3c=='':
            moves = '3e3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w3e)and Wboard.w3a==''\
           and board.s3d+board.s3c+board.s3b=='':
            moves = '3e3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w3e)and Wboard.w1e==''\
           and board.s2e=='':
            moves = '3e1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w3e)and Wboard.w5e==''\
           and board.s4e=='':
            moves = '3e5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w3e)and Wboard.w6e==''\
           and board.s4e+board.s5e=='':
            moves = '3e6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w3e)and Wboard.w7e==''\
           and board.s4e+board.s5e+board.s6e=='':
            moves = '3e7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w3e)and Wboard.w8e==''\
           and board.s4e+board.s5e+board.s6e+board.s7e=='':
            moves = '3e8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w3e)and Wboard.w9e==''\
           and board.s4e+board.s5e+board.s6e+board.s7e+board.s8e=='':
            moves = '3e9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w3e)and Wboard.w1g==''\
           and board.s2f=='':
            moves = '3e1g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',Wboard.w3e)and Wboard.w1g==''\
           and board.s2f=='':
            moves = '3e1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w3e)and Wboard.w5c==''\
           and board.s2d=='':
            moves = '3e5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w3e)and Wboard.w6b==''\
           and board.s2d+board.s5c=='':
            moves = '3e6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w3e)and Wboard.w7a==''\
           and board.s2d+board.s5c+board.s6b=='':
            moves = '3e7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w3e)and Wboard.w7i==''\
           and board.s6h+board.s5g+board.s4f=='':
            moves = '3e7i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w3e)and Wboard.w6h==''\
           and board.s5g+board.s4f=='':
            moves = '3e6h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w3e)and Wboard.w5g==''\
           and board.s4f=='':
            moves = '3e5g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w3e)and Wboard.w7i==''\
           and board.s6h+board.s5g+board.s4f=='':
            moves = '3e7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w3e)and Wboard.w6h==''\
           and board.s5g+board.s4f=='':
            moves = '3e6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',Wboard.w3e)and Wboard.w5g==''\
           and board.s4f=='':
            moves = '3e5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w3e)and Wboard.w1c==''\
           and board.s2d=='':
            moves = '3e1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w4e !='':
        if re.match(r'[plsgrk+]',   Wboard.w4e)and Wboard.w4f=='':
            moves = '4e4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w4e)and Wboard.w3f=='':
            moves = '4e3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w4e)and Wboard.w5f=='':
            moves = '4e5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w4e)and Wboard.w3e=='':
            moves = '4e3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w4e)and Wboard.w5e=='':
            moves = '4e5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w4e)and Wboard.w4d=='':
            moves = '4e4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w4e)and Wboard.w3d=='':
            moves = '4e3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w4e)and Wboard.w5d=='':
            moves = '4e5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w4e)and Wboard.w3g=='':
            moves = '4e3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w4e)and Wboard.w5g=='':
            moves = '4e5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w4e)and Wboard.w3g=='':
            moves = '4e3g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w4e)and Wboard.w5g=='':
            moves = '4e5g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w4e)and Wboard.w4i==''\
           and board.s4h+board.s4g+board.s4f=='':
            moves = '4e4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w4e)and Wboard.w4i==''\
           and board.s4h+board.s4g+board.s4f=='':
            moves = '4e4i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w4e)and Wboard.w4h==''\
           and board.s4g+board.s4f=='':
            moves = '4e4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w4e)and Wboard.w4h==''\
           and board.s4g+board.s4f=='':
            moves = '4e4h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|l',    Wboard.w4e)and Wboard.w4g==''\
           and board.s4f=='':
            moves = '4e4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w4e)and Wboard.w4g==''\
           and board.s4f=='':
            moves = '4e4g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w4e)and Wboard.w4c==''\
           and board.s4d=='':
            moves = '4e4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w4e)and Wboard.w4b==''\
           and board.s4d+board.s4c=='':
            moves = '4e4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w4e)and Wboard.w4a==''\
           and board.s4d+board.s4c+board.s4b=='':
            moves = '4e4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w4e)and Wboard.w1e==''\
           and board.s2e+board.s3e=='':
            moves = '4e1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w4e)and Wboard.w2e==''\
           and board.s3e=='':
            moves = '4e2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w4e)and Wboard.w6e==''\
           and board.s5e=='':
            moves = '4e6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w4e)and Wboard.w7e==''\
           and board.s5e+board.s6e=='':
            moves = '4e7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w4e)and Wboard.w8e==''\
           and board.s5e+board.s6e+board.s7e=='':
            moves = '4e8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w4e)and Wboard.w9e==''\
           and board.s5e+board.s6e+board.s7e+board.s8e=='':
            moves = '4e9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w4e)and Wboard.w1h==''\
           and board.s2g+board.s3f=='':
            moves = '4e1h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w4e)and Wboard.w2g==''\
           and board.s3f=='':
            moves = '4e2g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w4e)and Wboard.w1h==''\
           and board.s2g+board.s3f=='':
            moves = '4e1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',Wboard.w4e)and Wboard.w2g==''\
           and board.s3f=='':
            moves = '4e2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w4e)and Wboard.w6c==''\
           and board.s5d=='':
            moves = '4e6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w4e)and Wboard.w7b==''\
           and board.s5d+board.s6c=='':
            moves = '4e7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w4e)and Wboard.w8a==''\
           and board.s5d+board.s6c+board.s7b=='':
            moves = '4e8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w4e)and Wboard.w8i==''\
           and board.s7h+board.s6g+board.s5f=='':
            moves = '4e8i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w4e)and Wboard.w7h==''\
           and board.s6g+board.s5f=='':
            moves = '4e7h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w4e)and Wboard.w6g==''\
           and board.s5f=='':
            moves = '4e6g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w4e)and Wboard.w8i==''\
           and board.s7h+board.s6g+board.s5f=='':
            moves = '4e8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w4e)and Wboard.w7h==''\
           and board.s6g+board.s5f=='':
            moves = '4e7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',Wboard.w4e)and Wboard.w6g==''\
           and board.s5f=='':
            moves = '4e6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w4e)and Wboard.w2c==''\
           and board.s3d=='':
            moves = '4e2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w4e)and Wboard.w1b==''\
           and board.s3d+board.s2c=='':
            moves = '4e1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w5e !='':
        if re.match(r'[plsgrk+]',   Wboard.w5e)and Wboard.w5f=='':
            moves = '5e5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w5e)and Wboard.w4f=='':
            moves = '5e4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w5e)and Wboard.w6f=='':
            moves = '5e6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w5e)and Wboard.w4e=='':
            moves = '5e4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w5e)and Wboard.w6e=='':
            moves = '5e6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w5e)and Wboard.w5d=='':
            moves = '5e5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w5e)and Wboard.w4d=='':
            moves = '5e4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w5e)and Wboard.w6d=='':
            moves = '5e6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w5e)and Wboard.w4g=='':
            moves = '5e4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w5e)and Wboard.w6g=='':
            moves = '5e6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w5e)and Wboard.w4g=='':
            moves = '5e4g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w5e)and Wboard.w6g=='':
            moves = '5e6g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w5e)and Wboard.w5i==''\
           and board.s5h+board.s5g+board.s5f=='':
            moves = '5e5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w5e)and Wboard.w5i==''\
           and board.s5h+board.s5g+board.s5f=='':
            moves = '5e5i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w5e)and Wboard.w5h==''\
           and board.s5g+board.s5f=='':
            moves = '5e5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w5e)and Wboard.w5h==''\
           and board.s5g+board.s5f=='':
            moves = '5e5h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|l',    Wboard.w5e)and Wboard.w5g==''\
           and board.s5f=='':
            moves = '5e5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w5e)and Wboard.w5g==''\
           and board.s5f=='':
            moves = '5e5g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w5e)and Wboard.w5c==''\
           and board.s5d=='':
            moves = '5e5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w5e)and Wboard.w5b==''\
           and board.s5d+board.s5c=='':
            moves = '5e5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w5e)and Wboard.w5a==''\
           and board.s5d+board.s5c+board.s5b=='':
            moves = '5e5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w5e)and Wboard.w1e==''\
           and board.s2e+board.s3e+board.s4e=='':
            moves = '5e1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w5e)and Wboard.w2e==''\
           and board.s3e+board.s4e=='':
            moves = '5e2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w5e)and Wboard.w3e==''\
           and board.s4e=='':
            moves = '5e3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w5e)and Wboard.w7e==''\
           and board.s6e=='':
            moves = '5e7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w5e)and Wboard.w8e==''\
           and board.s6e+board.s7e=='':
            moves = '5e8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w5e)and Wboard.w9e==''\
           and board.s6e+board.s7e+board.s8e=='':
            moves = '5e9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w5e)and Wboard.w1i==''\
           and board.s2h+board.s3g+board.s4f=='':
            moves = '5e1i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w5e)and Wboard.w2h==''\
           and board.s3g+board.s4f=='':
            moves = '5e2h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w5e)and Wboard.w3g==''\
           and board.s4f=='':
            moves = '5e3g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w5e)and Wboard.w1i==''\
           and board.s2h+board.s3g+board.s4f=='':
            moves = '5e1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w5e)and Wboard.w2h==''\
           and board.s3g+board.s4f=='':
            moves = '5e2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',Wboard.w5e)and Wboard.w3g==''\
           and board.s4f=='':
            moves = '5e3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w5e)and Wboard.w7c==''\
           and board.s6d=='':
            moves = '5e7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w5e)and Wboard.w8b==''\
           and board.s6d+board.s7c=='':
            moves = '5e8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w5e)and Wboard.w9a==''\
           and board.s6d+board.s7c+board.s8b=='':
            moves = '5e9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w5e)and Wboard.w9i==''\
           and board.s8h+board.s7g+board.s6f=='':
            moves = '5e9i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w5e)and Wboard.w8h==''\
           and board.s7g+board.s6f=='':
            moves = '5e8h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w5e)and Wboard.w7g==''\
           and board.s6f=='':
            moves = '5e7g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w5e)and Wboard.w9i==''\
           and board.s8h+board.s7g+board.s6f=='':
            moves = '5e9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w5e)and Wboard.w8h==''\
           and board.s7g+board.s6f=='':
            moves = '5e8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',Wboard.w5e)and Wboard.w7g==''\
           and board.s6f=='':
            moves = '5e7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w5e)and Wboard.w3c==''\
           and board.s4d=='':
            moves = '5e3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w5e)and Wboard.w2b==''\
           and board.s4d+board.s3c=='':
            moves = '5e2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w5e)and Wboard.w1a==''\
           and board.s4d+board.s3c+board.s2b=='':
            moves = '5e1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w6e !='':
        if re.match(r'[plsgrk+]',   Wboard.w6e)and Wboard.w6f=='':
            moves = '6e6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w6e)and Wboard.w5f=='':
            moves = '6e5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w6e)and Wboard.w7f=='':
            moves = '6e7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w6e)and Wboard.w5e=='':
            moves = '6e5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w6e)and Wboard.w7e=='':
            moves = '6e7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w6e)and Wboard.w6d=='':
            moves = '6e6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w6e)and Wboard.w5d=='':
            moves = '6e5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w6e)and Wboard.w7d=='':
            moves = '6e7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w6e)and Wboard.w5g=='':
            moves = '6e5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w6e)and Wboard.w7g=='':
            moves = '6e7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w6e)and Wboard.w5g=='':
            moves = '6e5g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w6e)and Wboard.w7g=='':
            moves = '6e7g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w6e)and Wboard.w6i==''\
           and board.s6h+board.s6g+board.s6f=='':
            moves = '6e6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w6e)and Wboard.w6i==''\
           and board.s6h+board.s6g+board.s6f=='':
            moves = '6e6i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w6e)and Wboard.w6h==''\
           and board.s6g+board.s6f=='':
            moves = '6e6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w6e)and Wboard.w6h==''\
           and board.s6g+board.s6f=='':
            moves = '6e6h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|l',    Wboard.w6e)and Wboard.w6g==''\
           and board.s6f=='':
            moves = '6e6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w6e)and Wboard.w6g==''\
           and board.s6f=='':
            moves = '6e6g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w6e)and Wboard.w6c==''\
           and board.s6d=='':
            moves = '6e6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w6e)and Wboard.w6b==''\
           and board.s6d+board.s6c=='':
            moves = '6e6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w6e)and Wboard.w6a==''\
           and board.s6d+board.s6c+board.s6b=='':
            moves = '6e6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w6e)and Wboard.w9e==''\
           and board.s8e+board.s7e=='':
            moves = '6e9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w6e)and Wboard.w8e==''\
           and board.s7e=='':
            moves = '6e8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w6e)and Wboard.w4e==''\
           and board.s5e=='':
            moves = '6e4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w6e)and Wboard.w3e==''\
           and board.s5e+board.s4e=='':
            moves = '6e3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w6e)and Wboard.w2e==''\
           and board.s5e+board.s4e+board.s3e=='':
            moves = '6e2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w6e)and Wboard.w1e==''\
           and board.s5e+board.s4e+board.s3e+board.s2e=='':
            moves = '6e1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w6e)and Wboard.w9h==''\
           and board.s8g+board.s7f=='':
            moves = '6e9h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w6e)and Wboard.w8g==''\
           and board.s7f=='':
            moves = '6e8g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w6e)and Wboard.w9h==''\
           and board.s8g+board.s7f=='':
            moves = '6e9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',Wboard.w6e)and Wboard.w8g==''\
           and board.s7f=='':
            moves = '6e8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w6e)and Wboard.w4c==''\
           and board.s5d=='':
            moves = '6e4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w6e)and Wboard.w3b==''\
           and board.s5d+board.s4c=='':
            moves = '6e3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w6e)and Wboard.w2a==''\
           and board.s5d+board.s4c+board.s3b=='':
            moves = '6e2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w6e)and Wboard.w2i==''\
           and board.s3h+board.s4g+board.s5f=='':
            moves = '6e2i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w6e)and Wboard.w3h==''\
           and board.s4g+board.s5f=='':
            moves = '6e3h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w6e)and Wboard.w4g==''\
           and board.s5f=='':
            moves = '6e4g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w6e)and Wboard.w2i==''\
           and board.s3h+board.s4g+board.s5f=='':
            moves = '6e2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w6e)and Wboard.w3h==''\
           and board.s4g+board.s5f=='':
            moves = '6e3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',Wboard.w6e)and Wboard.w4g==''\
           and board.s5f=='':
            moves = '6e4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w6e)and Wboard.w8c==''\
           and board.s7d=='':
            moves = '6e8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w6e)and Wboard.w9b==''\
           and board.s7d+board.s8c=='':
            moves = '6e9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w7e !='':
        if re.match(r'[plsgrk+]',   Wboard.w7e)and Wboard.w7f=='':
            moves = '7e7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w7e)and Wboard.w6f=='':
            moves = '7e6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w7e)and Wboard.w8f=='':
            moves = '7e8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w7e)and Wboard.w6e=='':
            moves = '7e6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w7e)and Wboard.w8e=='':
            moves = '7e8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w7e)and Wboard.w7d=='':
            moves = '7e7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w7e)and Wboard.w6d=='':
            moves = '7e6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w7e)and Wboard.w8d=='':
            moves = '7e8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w7e)and Wboard.w6g=='':
            moves = '7e6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w7e)and Wboard.w8g=='':
            moves = '7e8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w7e)and Wboard.w6g=='':
            moves = '7e6g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w7e)and Wboard.w8g=='':
            moves = '7e8g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w7e)and Wboard.w7i==''\
           and board.s7h+board.s7g+board.s7f=='':
            moves = '7e7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w7e)and Wboard.w7i==''\
           and board.s7h+board.s7g+board.s7f=='':
            moves = '7e7i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w7e)and Wboard.w7h==''\
           and board.s7g+board.s7f=='':
            moves = '7e7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w7e)and Wboard.w7h==''\
           and board.s7g+board.s7f=='':
            moves = '7e7h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|l',    Wboard.w7e)and Wboard.w7g==''\
           and board.s7f=='':
            moves = '7e7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w7e)and Wboard.w7g==''\
           and board.s7f=='':
            moves = '7e7g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w7e)and Wboard.w7c==''\
           and board.s7d=='':
            moves = '7e7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w7e)and Wboard.w7b==''\
           and board.s7d+board.s7c=='':
            moves = '7e7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w7e)and Wboard.w7a==''\
           and board.s7d+board.s7c+board.s7b=='':
            moves = '7e7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w7e)and Wboard.w9e==''\
           and board.s8e=='':
            moves = '7e9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w7e)and Wboard.w5e==''\
           and board.s6e=='':
            moves = '7e5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w7e)and Wboard.w4e==''\
           and board.s6e+board.s5e=='':
            moves = '7e4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w7e)and Wboard.w3e==''\
           and board.s6e+board.s5e+board.s4e=='':
            moves = '7e3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w7e)and Wboard.w2e==''\
           and board.s6e+board.s5e+board.s4e+board.s3e=='':
            moves = '7e2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w7e)and Wboard.w1e==''\
           and board.s6e+board.s5e+board.s4e+board.s3e+board.s2e=='':
            moves = '7e1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w7e)and Wboard.w9g==''\
           and board.s8f=='':
            moves = '7e9g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',Wboard.w7e)and Wboard.w9g==''\
           and board.s8f=='':
            moves = '7e9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w7e)and Wboard.w5c==''\
           and board.s8d=='':
            moves = '7e5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w7e)and Wboard.w4b==''\
           and board.s8d+board.s5c=='':
            moves = '7e4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w7e)and Wboard.w3a==''\
           and board.s8d+board.s5c+board.s4b=='':
            moves = '7e3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w7e)and Wboard.w3i==''\
           and board.s4h+board.s5g+board.s6f=='':
            moves = '7e3i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w7e)and Wboard.w4h==''\
           and board.s5g+board.s6f=='':
            moves = '7e4h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w7e)and Wboard.w5g==''\
           and board.s6f=='':
            moves = '7e5g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w7e)and Wboard.w3i==''\
           and board.s4h+board.s5g+board.s6f=='':
            moves = '7e3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w7e)and Wboard.w4h==''\
           and board.s5g+board.s6f=='':
            moves = '7e4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',Wboard.w7e)and Wboard.w5g==''\
           and board.s6f=='':
            moves = '7e5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w7e)and Wboard.w9c==''\
           and board.s8d=='':
            moves = '7e9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w8e !='':
        if re.match(r'[plsgrk+]',   Wboard.w8e)and Wboard.w8f=='':
            moves = '8e8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w8e)and Wboard.w7f=='':
            moves = '8e7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w8e)and Wboard.w9f=='':
            moves = '8e9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w8e)and Wboard.w7e=='':
            moves = '8e7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w8e)and Wboard.w9e=='':
            moves = '8e9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w8e)and Wboard.w8d=='':
            moves = '8e8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w8e)and Wboard.w7d=='':
            moves = '8e7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w8e)and Wboard.w9d=='':
            moves = '8e9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w8e)and Wboard.w7g=='':
            moves = '8e7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w8e)and Wboard.w9g=='':
            moves = '8e9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w8e)and Wboard.w7g=='':
            moves = '8e7g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w8e)and Wboard.w9g=='':
            moves = '8e9g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w8e)and Wboard.w8i==''\
           and board.s8h+board.s8g+board.s8f=='':
            moves = '8e8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w8e)and Wboard.w8i==''\
           and board.s8h+board.s8g+board.s8f=='':
            moves = '8e8i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w8e)and Wboard.w8h==''\
           and board.s8g+board.s8f=='':
            moves = '8e8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w8e)and Wboard.w8h==''\
           and board.s8g+board.s8f=='':
            moves = '8e8h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|l',    Wboard.w8e)and Wboard.w8g==''\
           and board.s8f=='':
            moves = '8e8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w8e)and Wboard.w8g==''\
           and board.s8f=='':
            moves = '8e8g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w8e)and Wboard.w8c==''\
           and board.s8d=='':
            moves = '8e8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w8e)and Wboard.w8b==''\
           and board.s8d+board.s8c=='':
            moves = '8e8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w8e)and Wboard.w8a==''\
           and board.s8d+board.s8c+board.s8b=='':
            moves = '8e8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w8e)and Wboard.w6e==''\
           and board.s7e=='':
            moves = '8e6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w8e)and Wboard.w5e==''\
           and board.s7e+board.s6e=='':
            moves = '8e5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w8e)and Wboard.w4e==''\
           and board.s7e+board.s6e+board.s5e=='':
            moves = '8e4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w8e)and Wboard.w3e==''\
           and board.s7e+board.s6e+board.s5e+board.s4e=='':
            moves = '8e3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w8e)and Wboard.w2e==''\
           and board.s7e+board.s6e+board.s5e+board.s4e+board.s3e=='':
            moves = '8e2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w8e)and Wboard.w1e==''\
           and board.s7e+board.s6e+board.s5e+board.s4e+board.s3e+board.s2e=='':
            moves = '8e1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w8e)and Wboard.w6c==''\
           and board.s7d=='':
            moves = '8e6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w8e)and Wboard.w5b==''\
           and board.s7d+board.s6c=='':
            moves = '8e5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w8e)and Wboard.w4a==''\
           and board.s7d+board.s6c+board.s5b=='':
            moves = '8e4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w8e)and Wboard.w4i==''\
           and board.s5h+board.s6g+board.s7f=='':
            moves = '8e4i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w8e)and Wboard.w5h==''\
           and board.s6g+board.s7f=='':
            moves = '8e5h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w8e)and Wboard.w6g==''\
           and board.s7f=='':
            moves = '8e6g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w8e)and Wboard.w4i==''\
           and board.s5h+board.s6g+board.s7f=='':
            moves = '8e4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w8e)and Wboard.w5h==''\
           and board.s6g+board.s7f=='':
            moves = '8e5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',Wboard.w8e)and Wboard.w6g==''\
           and board.s7f=='':
            moves = '8e6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w9e !='':
        if re.match(r'[plsgrk+]',   Wboard.w9e)and Wboard.w9f=='':
            moves = '9e9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w9e)and Wboard.w8f=='':
            moves = '9e8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w9e)and Wboard.w8e=='':
            moves = '9e8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w9e)and Wboard.w9d=='':
            moves = '9e9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w9e)and Wboard.w8d=='':
            moves = '9e8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w9e)and Wboard.w8g=='':
            moves = '9e8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w9e)and Wboard.w8g=='':
            moves = '9e8g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w9e)and Wboard.w9i==''\
           and board.s9h+board.s9g+board.s9f=='':
            moves = '9e9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w9e)and Wboard.w9i==''\
           and board.s9h+board.s9g+board.s9f=='':
            moves = '9e9i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w9e)and Wboard.w9h==''\
           and board.s9g+board.s9f=='':
            moves = '9e9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w9e)and Wboard.w9h==''\
           and board.s9g+board.s9f=='':
            moves = '9e9h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|l',    Wboard.w9e)and Wboard.w9g==''\
           and board.s9f=='':
            moves = '9e9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w9e)and Wboard.w9g==''\
           and board.s9f=='':
            moves = '9e9g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w9e)and Wboard.w9c==''\
           and board.s9d=='':
            moves = '9e9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w9e)and Wboard.w9b==''\
           and board.s9d+board.s9c=='':
            moves = '9e9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w9e)and Wboard.w9a==''\
           and board.s9d+board.s9c+board.s9b=='':
            moves = '9e9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w9e)and Wboard.w9a==''\
           and board.s9d+board.s9c+board.s9b=='':
            moves = '9e9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w9e)and Wboard.w7e==''\
           and board.s8e=='':
            moves = '9e7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w9e)and Wboard.w6e==''\
           and board.s8e+board.s7e=='':
            moves = '9e6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w9e)and Wboard.w5e==''\
           and board.s8e+board.s7e+board.s6e=='':
            moves = '9e5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w9e)and Wboard.w4e==''\
           and board.s8e+board.s7e+board.s6e+board.s5e=='':
            moves = '9e4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w9e)and Wboard.w3e==''\
           and board.s8e+board.s7e+board.s6e+board.s5e+board.s4e=='':
            moves = '9e3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w9e)and Wboard.w2e==''\
           and board.s8e+board.s7e+board.s6e+board.s5e+board.s4e+board.s3e=='':
            moves = '9e2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w9e)and Wboard.w1e==''\
           and board.s8e+board.s7e+board.s6e+board.s5e+board.s4e+board.s3e+board.s2e=='':
            moves = '9e1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w9e)and Wboard.w7c==''\
           and board.s8d=='':
            moves = '9e7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w9e)and Wboard.w6b==''\
           and board.s8d+board.s7c=='':
            moves = '9e6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w9e)and Wboard.w5a==''\
           and board.s8d+board.s7c+board.s6b=='':
            moves = '9e5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w9e)and Wboard.w5i==''\
           and board.s6h+board.s7g+board.s8f=='':
            moves = '9e5i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w9e)and Wboard.w6h==''\
           and board.s7g+board.s8f=='':
            moves = '9e6h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w9e)and Wboard.w7g==''\
           and board.s8f=='':
            moves = '9e7g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w9e)and Wboard.w5i==''\
           and board.s6h+board.s7g+board.s8f=='':
            moves = '9e5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w9e)and Wboard.w6h==''\
           and board.s7g+board.s8f=='':
            moves = '9e6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',Wboard.w9e)and Wboard.w7g==''\
           and board.s8f=='':
            moves = '9e7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w1d !='':
        if re.match(r'[plsgrk+]',   Wboard.w1d)and Wboard.w1e=='':
            moves = '1d1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w1d)and Wboard.w2e=='':
            moves = '1d2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w1d)and Wboard.w2d=='':
            moves = '1d2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w1d)and Wboard.w1c=='':
            moves = '1d1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w1d)and Wboard.w2c=='':
            moves = '1d2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w1d)and Wboard.w2f=='':
            moves = '1d2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w1d)and Wboard.w1i==''\
           and board.s1h+board.s1g+board.s1f+board.s1e=='':
            moves = '1d1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w1d)and Wboard.w1i==''\
           and board.s1h+board.s1g+board.s1f+board.s1e=='':
            moves = '1d1i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w1d)and Wboard.w1h==''\
           and board.s1g+board.s1f+board.s1e=='':
            moves = '1d1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w1d)and Wboard.w1h==''\
           and board.s1g+board.s1f+board.s1e=='':
            moves = '1d1h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|l',    Wboard.w1d)and Wboard.w1g==''\
           and board.s1f+board.s1e=='':
            moves = '1d1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w1d)and Wboard.w1g==''\
           and board.s1f+board.s1e=='':
            moves = '1d1g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w1d)and Wboard.w1f==''\
           and board.s1e=='':
            moves = '1d1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w1d)and Wboard.w1b==''\
           and board.s1c=='':
            moves = '1d1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w1d)and Wboard.w1a==''\
           and board.s1c+board.s1b=='':
            moves = '1d1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w1d)and Wboard.w3d==''\
           and board.s2d=='':
            moves = '1d3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w1d)and Wboard.w4d==''\
           and board.s2d+board.s3d=='':
            moves = '1d4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w1d)and Wboard.w5d==''\
           and board.s2d+board.s3d+board.s4d=='':
            moves = '1d5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w1d)and Wboard.w6d==''\
           and board.s2d+board.s3d+board.s4d+board.s5d=='':
            moves = '1d6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w1d)and Wboard.w7d==''\
           and board.s2d+board.s3d+board.s4d+board.s5d+board.s6d=='':
            moves = '1d7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w1d)and Wboard.w8d==''\
           and board.s2d+board.s3d+board.s4d+board.s5d+board.s6d+board.s7d=='':
            moves = '1d8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w1d)and Wboard.w9d==''\
           and board.s2d+board.s3d+board.s4d+board.s5d+board.s6d+board.s7d+board.s8d=='':
            moves = '1d9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w1d)and Wboard.w3f==''\
           and board.s2e=='':
            moves = '1d3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w1d)and Wboard.w4g==''\
           and board.s2e+board.s3f=='':
            moves = '1d4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w1d)and Wboard.w5h==''\
           and board.s2e+board.s3f+board.s4g=='':
            moves = '1d5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w1d)and Wboard.w6i==''\
           and board.s2e+board.s3f+board.s4g+board.s5h=='':
            moves = '1d6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w1d)and Wboard.w4a==''\
           and board.s3b+board.s2c=='':
            moves = '1d4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w1d)and Wboard.w3b==''\
           and board.s2c=='':
            moves = '1d3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w1d)and Wboard.w4g==''\
           and board.s2e+board.s3f=='':
            moves = '1d4g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w1d)and Wboard.w5h==''\
           and board.s2e+board.s3f+board.s4g=='':
            moves = '1d5h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w1d)and Wboard.w6i==''\
           and board.s2e+board.s3f+board.s4g+board.s5h=='':
            moves = '1d6i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w2d !='':
        if re.match(r'[plsgrk+]',   Wboard.w2d)and Wboard.w2e=='':
            moves = '2d2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w2d)and Wboard.w1e=='':
            moves = '2d1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w2d)and Wboard.w3e=='':
            moves = '2d3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w2d)and Wboard.w1d=='':
            moves = '2d1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w2d)and Wboard.w3d=='':
            moves = '2d3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w2d)and Wboard.w2c=='':
            moves = '2d2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w2d)and Wboard.w1c=='':
            moves = '2d1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w2d)and Wboard.w3c=='':
            moves = '2d3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w2d)and Wboard.w1f=='':
            moves = '2d1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w2d)and Wboard.w3f=='':
            moves = '2d3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w2d)and Wboard.w2i==''\
           and board.s2h+board.s2g+board.s2f+board.s2e=='':
            moves = '2d2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w2d)and Wboard.w2i==''\
           and board.s2h+board.s2g+board.s2f+board.s2e=='':
            moves = '2d2i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w2d)and Wboard.w2h==''\
           and board.s2g+board.s2f+board.s2e=='':
            moves = '2d2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w2d)and Wboard.w2h==''\
           and board.s2g+board.s2f+board.s2e=='':
            moves = '2d2h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|l',    Wboard.w2d)and Wboard.w2g==''\
           and board.s2f+board.s2e=='':
            moves = '2d2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w2d)and Wboard.w2g==''\
           and board.s2f+board.s2e=='':
            moves = '2d2g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w2d)and Wboard.w2f==''\
           and board.s2e=='':
            moves = '2d2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w2d)and Wboard.w2b==''\
           and board.s2c=='':
            moves = '2d2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w2d)and Wboard.w2a==''\
           and board.s2c+board.s2b=='':
            moves = '2d2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w2d)and Wboard.w4d==''\
           and board.s3d=='':
            moves = '2d4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w2d)and Wboard.w5d==''\
           and board.s3d+board.s4d=='':
            moves = '2d5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w2d)and Wboard.w6d==''\
           and board.s3d+board.s4d+board.s5d=='':
            moves = '2d6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w2d)and Wboard.w7d==''\
           and board.s3d+board.s4d+board.s5d+board.s6d=='':
            moves = '2d7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w2d)and Wboard.w8d==''\
           and board.s3d+board.s4d+board.s5d+board.s6d+board.s7d=='':
            moves = '2d8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w2d)and Wboard.w9d==''\
           and board.s3d+board.s4d+board.s5d+board.s6d+board.s7d+board.s8d=='':
            moves = '2d9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w2d)and Wboard.w4f==''\
           and board.s3e=='':
            moves = '2d4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w2d)and Wboard.w5g==''\
           and board.s3e+board.s4f=='':
            moves = '2d5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w2d)and Wboard.w6h==''\
           and board.s3e+board.s4f+board.s5g=='':
            moves = '2d6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w2d)and Wboard.w7i==''\
           and board.s3e+board.s4f+board.s5g+board.s6h=='':
            moves = '2d7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w2d)and Wboard.w5a==''\
           and board.s4b+board.s3c=='':
            moves = '2d5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w2d)and Wboard.w4b==''\
           and board.s3c=='':
            moves = '2d4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w2d)and Wboard.w5g==''\
           and board.s3e+board.s4f=='':
            moves = '2d5g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w2d)and Wboard.w6h==''\
           and board.s3e+board.s4f+board.s5g=='':
            moves = '2d6h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w2d)and Wboard.w7i==''\
           and board.s3e+board.s4f+board.s5g+board.s6h=='':
            moves = '2d7i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w3d !='':
        if re.match(r'[plsgrk+]',   Wboard.w3d)and Wboard.w3e=='':
            moves = '3d3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w3d)and Wboard.w2e=='':
            moves = '3d2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w3d)and Wboard.w4e=='':
            moves = '3d4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w3d)and Wboard.w2d=='':
            moves = '3d2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w3d)and Wboard.w4d=='':
            moves = '3d4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w3d)and Wboard.w3c=='':
            moves = '3d3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w3d)and Wboard.w2c=='':
            moves = '3d2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w3d)and Wboard.w4c=='':
            moves = '3d4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w3d)and Wboard.w2f=='':
            moves = '3d2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w3d)and Wboard.w4f=='':
            moves = '3d4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w3d)and Wboard.w3i==''\
           and board.s3h+board.s3g+board.s3f+board.s3e=='':
            moves = '3d3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w3d)and Wboard.w3i==''\
           and board.s3h+board.s3g+board.s3f+board.s3e=='':
            moves = '3d3i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w3d)and Wboard.w3h==''\
           and board.s3g+board.s3f+board.s3e=='':
            moves = '3d3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w3d)and Wboard.w3h==''\
           and board.s3g+board.s3f+board.s3e=='':
            moves = '3d3h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|l',    Wboard.w3d)and Wboard.w3g==''\
           and board.s3f+board.s3e=='':
            moves = '3d3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w3d)and Wboard.w3g==''\
           and board.s3f+board.s3e=='':
            moves = '3d3g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w3d)and Wboard.w3f==''\
           and board.s3e=='':
            moves = '3d3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w3d)and Wboard.w3b==''\
           and board.s3c=='':
            moves = '3d3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w3d)and Wboard.w3a==''\
           and board.s3c+board.s3b=='':
            moves = '3d3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w3d)and Wboard.w1d==''\
           and board.s2d=='':
            moves = '3d1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w3d)and Wboard.w5d==''\
           and board.s4d=='':
            moves = '3d5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w3d)and Wboard.w6d==''\
           and board.s4d+board.s5d=='':
            moves = '3d6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w3d)and Wboard.w7d==''\
           and board.s4d+board.s5d+board.s6d=='':
            moves = '3d7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w3d)and Wboard.w8d==''\
           and board.s4d+board.s5d+board.s6d+board.s7d=='':
            moves = '3d8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w3d)and Wboard.w9d==''\
           and board.s4d+board.s5d+board.s6d+board.s7d+board.s8d=='':
            moves = '3d9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w3d)and Wboard.w1b==''\
           and board.s2c=='':
            moves = '3d1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w3d)and Wboard.w5f==''\
           and board.s4e=='':
            moves = '3d5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w3d)and Wboard.w6g==''\
           and board.s4e+board.s5f=='':
            moves = '3d6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w3d)and Wboard.w7h==''\
           and board.s4e+board.s5f+board.s6g=='':
            moves = '3d7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w3d)and Wboard.w8i==''\
           and board.s4e+board.s5f+board.s6g+board.s7h=='':
            moves = '3d8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w3d)and Wboard.w6a==''\
           and board.s5b+board.s4c=='':
            moves = '3d6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w3d)and Wboard.w5b==''\
           and board.s4c=='':
            moves = '3d5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w3d)and Wboard.w1f==''\
           and board.s2e=='':
            moves = '3d1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w3d)and Wboard.w6g==''\
           and board.s4e+board.s5f=='':
            moves = '3d6g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w3d)and Wboard.w7h==''\
           and board.s4e+board.s5f+board.s6g=='':
            moves = '3d7h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w3d)and Wboard.w8i==''\
           and board.s4e+board.s5f+board.s6g+board.s7h=='':
            moves = '3d8i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w4d !='':
        if re.match(r'[plsgrk+]',   Wboard.w4d)and Wboard.w4e=='':
            moves = '4d4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w4d)and Wboard.w3e=='':
            moves = '4d3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w4d)and Wboard.w5e=='':
            moves = '4d5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w4d)and Wboard.w3d=='':
            moves = '4d3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w4d)and Wboard.w5d=='':
            moves = '4d5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w4d)and Wboard.w4c=='':
            moves = '4d4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w4d)and Wboard.w3c=='':
            moves = '4d3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w4d)and Wboard.w5c=='':
            moves = '4d5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w4d)and Wboard.w3f=='':
            moves = '4d3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w4d)and Wboard.w5f=='':
            moves = '4d5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w4d)and Wboard.w4i==''\
           and board.s4h+board.s4g+board.s4f+board.s4e=='':
            moves = '4d4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w4d)and Wboard.w4i==''\
           and board.s4h+board.s4g+board.s4f+board.s4e=='':
            moves = '4d4i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w4d)and Wboard.w4h==''\
           and board.s4g+board.s4f+board.s4e=='':
            moves = '4d4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w4d)and Wboard.w4h==''\
           and board.s4g+board.s4f+board.s4e=='':
            moves = '4d4h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|l',    Wboard.w4d)and Wboard.w4g==''\
           and board.s4f+board.s4e=='':
            moves = '4d4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w4d)and Wboard.w4g==''\
           and board.s4f+board.s4e=='':
            moves = '4d4g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w4d)and Wboard.w4f==''\
           and board.s4e=='':
            moves = '4d4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w4d)and Wboard.w4b==''\
           and board.s4c=='':
            moves = '4d4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w4d)and Wboard.w4a==''\
           and board.s4c+board.s4b=='':
            moves = '4d4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w4d)and Wboard.w1d==''\
           and board.s2d+board.s3d=='':
            moves = '4d1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w4d)and Wboard.w2d==''\
           and board.s3d=='':
            moves = '4d2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w4d)and Wboard.w6d==''\
           and board.s5d=='':
            moves = '4d6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w4d)and Wboard.w7d==''\
           and board.s5d+board.s6d=='':
            moves = '4d7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w4d)and Wboard.w8d==''\
           and board.s5d+board.s6d+board.s7d=='':
            moves = '4d8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w4d)and Wboard.w9d==''\
           and board.s5d+board.s6d+board.s7d+board.s8d=='':
            moves = '4d9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w4d)and Wboard.w1a==''\
           and board.s2b+board.s3c=='':
            moves = '4d1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w4d)and Wboard.w2b==''\
           and board.s3c=='':
            moves = '4d2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w4d)and Wboard.w6f==''\
           and board.s5e=='':
            moves = '4d6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w4d)and Wboard.w7g==''\
           and board.s5e+board.s6f=='':
            moves = '4d7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w4d)and Wboard.w8h==''\
           and board.s5e+board.s6f+board.s7g=='':
            moves = '4d8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w4d)and Wboard.w9i==''\
           and board.s5e+board.s6f+board.s7g+board.s8h=='':
            moves = '4d9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w4d)and Wboard.w7a==''\
           and board.s6b+board.s5c=='':
            moves = '4d7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w4d)and Wboard.w6b==''\
           and board.s5c=='':
            moves = '4d6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w4d)and Wboard.w2f==''\
           and board.s3e=='':
            moves = '4d2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w4d)and Wboard.w1g==''\
           and board.s3e+board.s2f=='':
            moves = '4d1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w4d)and Wboard.w7g==''\
           and board.s5e+board.s6f=='':
            moves = '4d7g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w4d)and Wboard.w8h==''\
           and board.s5e+board.s6f+board.s7g=='':
            moves = '4d8h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w4d)and Wboard.w1g==''\
           and board.s3e+board.s2f=='':
            moves = '4d1g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w4d)and Wboard.w9i==''\
           and board.s5e+board.s6f+board.s7g+board.s8h=='':
            moves = '4d9i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w5d !='':
        if re.match(r'[plsgrk+]',   Wboard.w5d)and Wboard.w5e=='':
            moves = '5d5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w5d)and Wboard.w4e=='':
            moves = '5d4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w5d)and Wboard.w6e=='':
            moves = '5d6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w5d)and Wboard.w4d=='':
            moves = '5d4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w5d)and Wboard.w6d=='':
            moves = '5d6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w5d)and Wboard.w5c=='':
            moves = '5d5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w5d)and Wboard.w4c=='':
            moves = '5d4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w5d)and Wboard.w6c=='':
            moves = '5d6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w5d)and Wboard.w4f=='':
            moves = '5d4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w5d)and Wboard.w6f=='':
            moves = '5d6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w5d)and Wboard.w5i==''\
           and board.s5h+board.s5g+board.s5f+board.s5e=='':
            moves = '5d5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w5d)and Wboard.w5i==''\
           and board.s5h+board.s5g+board.s5f+board.s5e=='':
            moves = '5d5i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w5d)and Wboard.w5h==''\
           and board.s5g+board.s5f+board.s5e=='':
            moves = '5d5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w5d)and Wboard.w5h==''\
           and board.s5g+board.s5f+board.s5e=='':
            moves = '5d5h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|l',    Wboard.w5d)and Wboard.w5g==''\
           and board.s5f+board.s5e=='':
            moves = '5d5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w5d)and Wboard.w5g==''\
           and board.s5f+board.s5e=='':
            moves = '5d5g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w5d)and Wboard.w5f==''\
           and board.s5e=='':
            moves = '5d5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w5d)and Wboard.w5b==''\
           and board.s5c=='':
            moves = '5d5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w5d)and Wboard.w5a==''\
           and board.s5c+board.s5b=='':
            moves = '5d5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w5d)and Wboard.w1d==''\
           and board.s2d+board.s3d+board.s4d=='':
            moves = '5d1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w5d)and Wboard.w2d==''\
           and board.s3d+board.s4d=='':
            moves = '5d2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w5d)and Wboard.w3d==''\
           and board.s4d=='':
            moves = '5d3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w5d)and Wboard.w7d==''\
           and board.s6d=='':
            moves = '5d7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w5d)and Wboard.w8d==''\
           and board.s6d+board.s7d=='':
            moves = '5d8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w5d)and Wboard.w9d==''\
           and board.s6d+board.s7d+board.s8d=='':
            moves = '5d9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',  Wboard.w5d)and Wboard.w2a==''\
          and board.s3b+board.s4c=='':
           moves ='5d2a'
           kaihimore(moves)
           if oute.oute == 0:
              depth1.append(moves)
        if re.match(r'\+b|b',Wboard.w5d)and Wboard.w3b==''\
          and board.s4c=='':
           moves ='5d3b'
           kaihimore(moves)
           if oute.oute == 0:
              depth1.append(moves)
        if re.match(r'\+b|b',  Wboard.w5d)and Wboard.w7f==''\
          and board.s6e=='':
           moves ='5d7f'
           kaihimore(moves)
           if oute.oute == 0:
              depth1.append(moves)
        if re.match('\+b',  Wboard.w5d)and Wboard.w8g==''\
          and board.s6e+board.s7f=='':
           moves ='5d8g'
           kaihimore(moves)
           if oute.oute == 0:
              depth1.append(moves)
        if re.match('\+b',  Wboard.w5d)and Wboard.w9h==''\
          and board.s6e+board.s7f+board.s8g=='':
           moves ='5d9h'
           kaihimore(moves)
           if oute.oute == 0:
              depth1.append(moves)
        if re.match(r'\+b|b',  Wboard.w5d)and Wboard.w8a==''\
          and board.s7b+board.s6c=='':
           moves ='5d8a'
           kaihimore(moves)
           if oute.oute == 0:
              depth1.append(moves)
        if re.match(r'\+b|b',Wboard.w5d)and Wboard.w7b==''\
          and board.s6c=='':
           moves ='5d7b'
           kaihimore(moves)
           if oute.oute == 0:
              depth1.append(moves)
        if re.match(r'\+b|b',  Wboard.w5d)and Wboard.w3f==''\
          and board.s4e=='':
           moves ='5d3f'
           kaihimore(moves)
           if oute.oute == 0:
              depth1.append(moves)
        if re.match('\+b',  Wboard.w5d)and Wboard.w2g==''\
          and board.s4e+board.s3f=='':
           moves ='5d2g'
           kaihimore(moves)
           if oute.oute == 0:
              depth1.append(moves)
        if re.match('b',  Wboard.w5d)and Wboard.w8g==''\
          and board.s6e+board.s7f=='':
           moves ='5d8g+'
           kaihimore(moves)
           if oute.oute == 0:
              depth1.append(moves)
        if re.match('b',  Wboard.w5d)and Wboard.w2g==''\
          and board.s4e+board.s3f=='':
           moves ='5d2g+'
           kaihimore(moves)
           if oute.oute == 0:
              depth1.append(moves)

    if Wboard.w6d !='':
        if re.match(r'[plsgrk+]',   Wboard.w6d)and Wboard.w6e=='':
            moves = '6d6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w6d)and Wboard.w5e=='':
            moves = '6d5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w6d)and Wboard.w7e=='':
            moves = '6d7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w6d)and Wboard.w5d=='':
            moves = '6d5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w6d)and Wboard.w7d=='':
            moves = '6d7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w6d)and Wboard.w6c=='':
            moves = '6d6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w6d)and Wboard.w5c=='':
            moves = '6d5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w6d)and Wboard.w7c=='':
            moves = '6d7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w6d)and Wboard.w5f=='':
            moves = '6d5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w6d)and Wboard.w7f=='':
            moves = '6d7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w6d)and Wboard.w6i==''\
           and board.s6h+board.s6g+board.s6f+board.s6e=='':
            moves = '6d6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w6d)and Wboard.w6i==''\
           and board.s6h+board.s6g+board.s6f+board.s6e=='':
            moves = '6d6i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w6d)and Wboard.w6h==''\
           and board.s6g+board.s6f+board.s6e=='':
            moves = '6d6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w6d)and Wboard.w6h==''\
           and board.s6g+board.s6f+board.s6e=='':
            moves = '6d6h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|l',    Wboard.w6d)and Wboard.w6g==''\
           and board.s6f+board.s6e=='':
            moves = '6d6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w6d)and Wboard.w6g==''\
           and board.s6f+board.s6e=='':
            moves = '6d6g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w6d)and Wboard.w6f==''\
           and board.s6e=='':
            moves = '6d6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w6d)and Wboard.w6b==''\
           and board.s6c=='':
            moves = '6d6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w6d)and Wboard.w6a==''\
           and board.s6c+board.s6b=='':
            moves = '6d6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w6d)and Wboard.w9d==''\
           and board.s8d+board.s7d=='':
            moves = '6d9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w6d)and Wboard.w8d==''\
           and board.s7d=='':
            moves = '6d8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w6d)and Wboard.w4d==''\
           and board.s5d=='':
            moves = '6d4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w6d)and Wboard.w3d==''\
           and board.s5d+board.s4d=='':
            moves = '6d3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w6d)and Wboard.w2d==''\
           and board.s5d+board.s4d+board.s3d=='':
            moves = '6d2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w6d)and Wboard.w1d==''\
           and board.s5d+board.s4d+board.s3d+board.s2d=='':
            moves = '6d1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w6d)and Wboard.w9a==''\
           and board.s8b+board.s7c=='':
            moves = '6d9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w6d)and Wboard.w8b==''\
           and board.s7c=='':
            moves = '6d8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w6d)and Wboard.w4f==''\
           and board.s5e=='':
            moves = '6d4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w6d)and Wboard.w3g==''\
           and board.s5e+board.s4f=='':
            moves = '6d3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w6d)and Wboard.w2h==''\
           and board.s5e+board.s4f+board.s3g=='':
            moves = '6d2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w6d)and Wboard.w1i==''\
           and board.s5e+board.s4f+board.s3g+board.s2h=='':
            moves = '6d1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w6d)and Wboard.w3a==''\
           and board.s4b+board.s5c=='':
            moves = '6d3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w6d)and Wboard.w4b==''\
           and board.s5c=='':
            moves = '6d4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w6d)and Wboard.w8f==''\
           and board.s7e=='':
            moves = '6d8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w6d)and Wboard.w9g==''\
           and board.s7e+board.s8f=='':
            moves = '6d9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w6d)and Wboard.w3g==''\
           and board.s5e+board.s4f=='':
            moves = '6d3g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w6d)and Wboard.w2h==''\
           and board.s5e+board.s4f+board.s3g=='':
            moves = '6d2h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w6d)and Wboard.w9g==''\
           and board.s7e+board.s8f=='':
            moves = '6d9g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w6d)and Wboard.w1i==''\
           and board.s5e+board.s4f+board.s3g+board.s2h=='':
            moves = '6d1i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w7d !='':
        if re.match(r'[plsgrk+]',   Wboard.w7d)and Wboard.w7e=='':
            moves = '7d7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w7d)and Wboard.w6e=='':
            moves = '7d6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w7d)and Wboard.w8e=='':
            moves = '7d8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w7d)and Wboard.w6d=='':
            moves = '7d6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w7d)and Wboard.w8d=='':
            moves = '7d8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w7d)and Wboard.w7c=='':
            moves = '7d7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w7d)and Wboard.w6c=='':
            moves = '7d6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w7d)and Wboard.w8c=='':
            moves = '7d8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w7d)and Wboard.w6f=='':
            moves = '7d6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w7d)and Wboard.w8f=='':
            moves = '7d8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w7d)and Wboard.w7i==''\
           and board.s7h+board.s7g+board.s7f+board.s7e=='':
            moves = '7d7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w7d)and Wboard.w7i==''\
           and board.s7h+board.s7g+board.s7f+board.s7e=='':
            moves = '7d7i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w7d)and Wboard.w7h==''\
           and board.s7g+board.s7f+board.s7e=='':
            moves = '7d7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w7d)and Wboard.w7h==''\
           and board.s7g+board.s7f+board.s7e=='':
            moves = '7d7h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|l',    Wboard.w7d)and Wboard.w7g==''\
           and board.s7f+board.s7e=='':
            moves = '7d7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w7d)and Wboard.w7g==''\
           and board.s7f+board.s7e=='':
            moves = '7d7g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w7d)and Wboard.w7f==''\
           and board.s7e=='':
            moves = '7d7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w7d)and Wboard.w7b==''\
           and board.s7c=='':
            moves = '7d7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w7d)and Wboard.w7a==''\
           and board.s7c+board.s7b=='':
            moves = '7d7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w7d)and Wboard.w9d==''\
           and board.s8d=='':
            moves = '7d9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w7d)and Wboard.w5d==''\
           and board.s6d=='':
            moves = '7d5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w7d)and Wboard.w4d==''\
           and board.s6d+board.s5d=='':
            moves = '7d4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w7d)and Wboard.w3d==''\
           and board.s6d+board.s5d+board.s4d=='':
            moves = '7d3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w7d)and Wboard.w2d==''\
           and board.s6d+board.s5d+board.s4d+board.s3d=='':
            moves = '7d2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w7d)and Wboard.w1d==''\
           and board.s6d+board.s5d+board.s4d+board.s3d+board.s2d=='':
            moves = '7d1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w7d)and Wboard.w9b==''\
           and board.s8c=='':
            moves = '7d9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w7d)and Wboard.w5f==''\
           and board.s6e=='':
            moves = '7d5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w7d)and Wboard.w4g==''\
           and board.s6e+board.s5f=='':
            moves = '7d4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w7d)and Wboard.w3h==''\
           and board.s6e+board.s5f+board.s4g=='':
            moves = '7d3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w7d)and Wboard.w2i==''\
           and board.s6e+board.s5f+board.s4g+board.s3h=='':
            moves = '7d2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w7d)and Wboard.w4a==''\
           and board.s5b+board.s6c=='':
            moves = '7d4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w7d)and Wboard.w5b==''\
           and board.s6c=='':
            moves = '7d5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w7d)and Wboard.w9f==''\
           and board.s8e=='':
            moves = '7d9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w7d)and Wboard.w4g==''\
           and board.s6e+board.s5f=='':
            moves = '7d4g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w7d)and Wboard.w3h==''\
           and board.s6e+board.s5f+board.s4g=='':
            moves = '7d3h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w7d)and Wboard.w2i==''\
           and board.s6e+board.s5f+board.s4g+board.s3h=='':
            moves = '7d2i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w8d !='':
        if re.match(r'[plsgrk+]',   Wboard.w8d)and Wboard.w8e=='':
            moves = '8d8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w8d)and Wboard.w7e=='':
            moves = '8d7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w8d)and Wboard.w9e=='':
            moves = '8d9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w8d)and Wboard.w7d=='':
            moves = '8d7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w8d)and Wboard.w9d=='':
            moves = '8d9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w8d)and Wboard.w8c=='':
            moves = '8d8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w8d)and Wboard.w7c=='':
            moves = '8d7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w8d)and Wboard.w9c=='':
            moves = '8d9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w8d)and Wboard.w7f=='':
            moves = '8d7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w8d)and Wboard.w9f=='':
            moves = '8d9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w8d)and Wboard.w8i==''\
           and board.s8h+board.s8g+board.s8f+board.s8e=='':
            moves = '8d8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w8d)and Wboard.w8i==''\
           and board.s8h+board.s8g+board.s8f+board.s8e=='':
            moves = '8d8i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w8d)and Wboard.w8h==''\
           and board.s8g+board.s8f+board.s8e=='':
            moves = '8d8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w8d)and Wboard.w8h==''\
           and board.s8g+board.s8f+board.s8e=='':
            moves = '8d8h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|l',    Wboard.w8d)and Wboard.w8g==''\
           and board.s8f+board.s8e=='':
            moves = '8d8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w8d)and Wboard.w8g==''\
           and board.s8f+board.s8e=='':
            moves = '8d8g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w8d)and Wboard.w8f==''\
           and board.s8e=='':
            moves = '8d8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w8d)and Wboard.w8b==''\
           and board.s8c=='':
            moves = '8d8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w8d)and Wboard.w8a==''\
           and board.s8c+board.s8b=='':
            moves = '8d8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w8d)and Wboard.w6d==''\
           and board.s7d=='':
            moves = '8d6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w8d)and Wboard.w5d==''\
           and board.s7d+board.s6d=='':
            moves = '8d5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w8d)and Wboard.w4d==''\
           and board.s7d+board.s6d+board.s5d=='':
            moves = '8d4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w8d)and Wboard.w3d==''\
           and board.s7d+board.s6d+board.s5d+board.s4d=='':
            moves = '8d3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w8d)and Wboard.w2d==''\
           and board.s7d+board.s6d+board.s5d+board.s4d+board.s3d=='':
            moves = '8d2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w8d)and Wboard.w1d==''\
           and board.s7d+board.s6d+board.s5d+board.s4d+board.s3d+board.s2d=='':
            moves = '8d1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w8d)and Wboard.w6f==''\
           and board.s7e=='':
            moves = '8d6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w8d)and Wboard.w5g==''\
           and board.s7e+board.s6f=='':
            moves = '8d5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w8d)and Wboard.w4h==''\
           and board.s7e+board.s6f+board.s5g=='':
            moves = '8d4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w8d)and Wboard.w3i==''\
           and board.s7e+board.s6f+board.s5g+board.s4h=='':
            moves = '8d3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w8d)and Wboard.w5a==''\
           and board.s6b+board.s7c=='':
            moves = '8d5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w8d)and Wboard.w6b==''\
           and board.s7c=='':
            moves = '8d6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w8d)and Wboard.w5g==''\
           and board.s7e+board.s6f=='':
            moves = '8d5g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w8d)and Wboard.w4h==''\
           and board.s7e+board.s6f+board.s5g=='':
            moves = '8d4h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w8d)and Wboard.w3i==''\
           and board.s7e+board.s6f+board.s5g+board.s4h=='':
            moves = '8d3i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w9d !='':
        if re.match(r'[plsgrk+]',   Wboard.w9d)and Wboard.w9e=='':
            moves = '9d9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w9d)and Wboard.w8e=='':
            moves = '9d8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w9d)and Wboard.w8d=='':
            moves = '9d8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w9d)and Wboard.w9c=='':
            moves = '9d9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w9d)and Wboard.w8c=='':
            moves = '9d8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w9d)and Wboard.w8f=='':
            moves = '9d8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w9d)and Wboard.w9i==''\
           and board.s9h+board.s9g+board.s9f+board.s9e=='':
            moves = '9d9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w9d)and Wboard.w9i==''\
           and board.s9h+board.s9g+board.s9f+board.s9e=='':
            moves = '9d9i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w9d)and Wboard.w9h==''\
           and board.s9g+board.s9f+board.s9e=='':
            moves = '9d9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w9d)and Wboard.w9h==''\
           and board.s9g+board.s9f+board.s9e=='':
            moves = '9d9h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|l',    Wboard.w9d)and Wboard.w9g==''\
           and board.s9f+board.s9e=='':
            moves = '9d9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w9d)and Wboard.w9g==''\
           and board.s9f+board.s9e=='':
            moves = '9d9g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w9d)and Wboard.w9f==''\
           and board.s9e=='':
            moves = '9d9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w9d)and Wboard.w9b==''\
           and board.s9c=='':
            moves = '9d9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w9d)and Wboard.w9a==''\
           and board.s9c+board.s9b=='':
            moves = '9d9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w9d)and Wboard.w7d==''\
           and board.s8d=='':
            moves = '9d7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w9d)and Wboard.w6d==''\
           and board.s8d+board.s7d=='':
            moves = '9d6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w9d)and Wboard.w5d==''\
           and board.s8d+board.s7d+board.s6d=='':
            moves = '9d5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w9d)and Wboard.w4d==''\
           and board.s8d+board.s7d+board.s6d+board.s5d=='':
            moves = '9d4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w9d)and Wboard.w3d==''\
           and board.s8d+board.s7d+board.s6d+board.s5d+board.s4d=='':
            moves = '9d3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w9d)and Wboard.w2d==''\
           and board.s8d+board.s7d+board.s6d+board.s5d+board.s4d+board.s3d=='':
            moves = '9d2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w9d)and Wboard.w1d==''\
           and board.s8d+board.s7d+board.s6d+board.s5d+board.s4d+board.s3d+board.s2d=='':
            moves = '9d1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w9d)and Wboard.w7f==''\
           and board.s8e=='':
            moves = '9d7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w9d)and Wboard.w6g==''\
           and board.s8e+board.s7f=='':
            moves = '9d6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w9d)and Wboard.w5h==''\
           and board.s8e+board.s7f+board.s6g=='':
            moves = '9d5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w9d)and Wboard.w4i==''\
           and board.s8e+board.s7f+board.s6g+board.s5h=='':
            moves = '9d4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w9d)and Wboard.w6a==''\
           and board.s7b+board.s8c=='':
            moves = '9d6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w9d)and Wboard.w7b==''\
           and board.s8c=='':
            moves = '9d7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w9d)and Wboard.w6g==''\
           and board.s8e+board.s7f=='':
            moves = '9d6g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w9d)and Wboard.w5h==''\
           and board.s8e+board.s7f+board.s6g=='':
            moves = '9d5h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w9d)and Wboard.w4i==''\
           and board.s8e+board.s7f+board.s6g+board.s5h=='':
            moves = '9d4i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w1c !='':
        if re.match(r'[plsgrk+]',   Wboard.w1c)and Wboard.w1d=='':
            moves = '1c1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w1c)and Wboard.w2d=='':
            moves = '1c2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w1c)and Wboard.w2c=='':
            moves = '1c2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w1c)and Wboard.w1b=='':
            moves = '1c1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w1c)and Wboard.w2b=='':
            moves = '1c2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w1c)and Wboard.w2e=='':
            moves = '1c2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w1c)and Wboard.w1i==''\
           and board.s1h+board.s1g+board.s1f+board.s1e+board.s1d=='':
            moves = '1c1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w1c)and Wboard.w1i==''\
           and board.s1h+board.s1g+board.s1f+board.s1e+board.s1d=='':
            moves = '1c1i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w1c)and Wboard.w1h==''\
           and board.s1g+board.s1f+board.s1e+board.s1d=='':
            moves = '1c1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w1c)and Wboard.w1h==''\
           and board.s1g+board.s1f+board.s1e+board.s1d=='':
            moves = '1c1h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|l',    Wboard.w1c)and Wboard.w1g==''\
           and board.s1f+board.s1e+board.s1d=='':
            moves = '1c1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w1c)and Wboard.w1g==''\
           and board.s1f+board.s1e+board.s1d=='':
            moves = '1c1g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w1c)and Wboard.w1f==''\
           and board.s1e+board.s1d=='':
            moves = '1c1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w1c)and Wboard.w1e==''\
           and board.s1d=='':
            moves = '1c1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w1c)and Wboard.w1a==''\
           and board.s1b=='':
            moves = '1c1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w1c)and Wboard.w3c==''\
           and board.s2c=='':
            moves = '1c3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w1c)and Wboard.w4c==''\
           and board.s2c+board.s3c=='':
            moves = '1c4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w1c)and Wboard.w5c==''\
           and board.s2c+board.s3c+board.s4c=='':
            moves = '1c5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w1c)and Wboard.w6c==''\
           and board.s2c+board.s3c+board.s4c+board.s5c=='':
            moves = '1c6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w1c)and Wboard.w7c==''\
           and board.s2c+board.s3c+board.s4c+board.s5c+board.s6c=='':
            moves = '1c7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w1c)and Wboard.w8c==''\
           and board.s2c+board.s3c+board.s4c+board.s5c+board.s6c+board.s7c=='':
            moves = '1c8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w1c)and Wboard.w9c==''\
           and board.s2c+board.s3c+board.s4c+board.s5c+board.s6c+board.s7c+board.s8c=='':
            moves = '1c9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w1c)and Wboard.w5g==''\
           and board.s2d+board.s3e+board.s4f=='':
            moves = '1c5g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w1c)and Wboard.w6h==''\
           and board.s2d+board.s3e+board.s4f+board.s5g=='':
            moves = '1c6h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w1c)and Wboard.w7i==''\
           and board.s2d+board.s3e+board.s4f+board.s5g+board.s6h=='':
            moves = '1c7i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w1c)and Wboard.w3a==''\
           and board.s2b=='':
            moves = '1c3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w1c)and Wboard.w3e==''\
           and board.s2d=='':
            moves = '1c3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w1c)and Wboard.w4f==''\
           and board.s2d+board.s3e=='':
            moves = '1c4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w1c)and Wboard.w5g==''\
           and board.s2d+board.s3e+board.s4f=='':
            moves = '1c5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w1c)and Wboard.w6h==''\
           and board.s2d+board.s3e+board.s4f+board.s5g=='':
            moves = '1c6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w1c)and Wboard.w7i==''\
           and board.s2d+board.s3e+board.s4f+board.s5g+board.s6h=='':
            moves = '1c7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w2c !='':
        if re.match(r'[plsgrk+]',   Wboard.w2c)and Wboard.w2d=='':
            moves = '2c2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w2c)and Wboard.w1d=='':
            moves = '2c1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w2c)and Wboard.w3d=='':
            moves = '2c3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w2c)and Wboard.w1c=='':
            moves = '2c1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w2c)and Wboard.w3c=='':
            moves = '2c3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w2c)and Wboard.w2b=='':
            moves = '2c2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w2c)and Wboard.w1b=='':
            moves = '2c1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w2c)and Wboard.w3b=='':
            moves = '2c3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w2c)and Wboard.w1e=='':
            moves = '2c1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w2c)and Wboard.w3e=='':
            moves = '2c3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w2c)and Wboard.w2i==''\
           and board.s2h+board.s2g+board.s2f+board.s2e+board.s2d=='':
            moves = '2c2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w2c)and Wboard.w2i==''\
           and board.s2h+board.s2g+board.s2f+board.s2e+board.s2d=='':
            moves = '2c2i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w2c)and Wboard.w2h==''\
           and board.s2g+board.s2f+board.s2e+board.s2d=='':
            moves = '2c2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w2c)and Wboard.w2h==''\
           and board.s2g+board.s2f+board.s2e+board.s2d=='':
            moves = '2c2h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|l',    Wboard.w2c)and Wboard.w2g==''\
           and board.s2f+board.s2e+board.s2d=='':
            moves = '2c2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w2c)and Wboard.w2g==''\
           and board.s2f+board.s2e+board.s2d=='':
            moves = '2c2g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w2c)and Wboard.w2f==''\
           and board.s2e+board.s2d=='':
            moves = '2c2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w2c)and Wboard.w2e==''\
           and board.s2d=='':
            moves = '2c2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w2c)and Wboard.w2a==''\
           and board.s2b=='':
            moves = '2c2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w2c)and Wboard.w4c==''\
           and board.s3c=='':
            moves = '2c4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w2c)and Wboard.w5c==''\
           and board.s3c+board.s4c=='':
            moves = '2c5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w2c)and Wboard.w6c==''\
           and board.s3c+board.s4c+board.s5c=='':
            moves = '2c6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w2c)and Wboard.w7c==''\
           and board.s3c+board.s4c+board.s5c+board.s6c=='':
            moves = '2c7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w2c)and Wboard.w8c==''\
           and board.s3c+board.s4c+board.s5c+board.s6c+board.s7c=='':
            moves = '2c8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w2c)and Wboard.w9c==''\
           and board.s3c+board.s4c+board.s5c+board.s6c+board.s7c+board.s8c=='':
            moves = '2c9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w2c)and Wboard.w6g==''\
           and board.s3d+board.s4e+board.s5f=='':
            moves = '2c6g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w2c)and Wboard.w7h==''\
           and board.s3d+board.s4e+board.s5f+board.s6g=='':
            moves = '2c7h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w2c)and Wboard.w8i==''\
           and board.s3d+board.s4e+board.s5f+board.s6g+board.s7h=='':
            moves = '2c8i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w2c)and Wboard.w4e==''\
           and board.s3d=='':
            moves = '2c4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w2c)and Wboard.w5f==''\
           and board.s3d+board.s4e=='':
            moves = '2c5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w2c)and Wboard.w6g==''\
           and board.s3d+board.s4e+board.s5f=='':
            moves = '2c6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w2c)and Wboard.w7h==''\
           and board.s3d+board.s4e+board.s5f+board.s6g=='':
            moves = '2c7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w2c)and Wboard.w8i==''\
           and board.s3d+board.s4e+board.s5f+board.s6g+board.s7h=='':
            moves = '2c8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w2c)and Wboard.w4a==''\
           and board.s3b=='':
            moves = '2c4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w3c !='':
        if re.match(r'[plsgrk+]',   Wboard.w3c)and Wboard.w3d=='':
            moves = '3c3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w3c)and Wboard.w2d=='':
            moves = '3c2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w3c)and Wboard.w4d=='':
            moves = '3c4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w3c)and Wboard.w2c=='':
            moves = '3c2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w3c)and Wboard.w4c=='':
            moves = '3c4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w3c)and Wboard.w3b=='':
            moves = '3c3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w3c)and Wboard.w2b=='':
            moves = '3c2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w3c)and Wboard.w4b=='':
            moves = '3c4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w3c)and Wboard.w2e=='':
            moves = '3c2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w3c)and Wboard.w4e=='':
            moves = '3c4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w3c)and Wboard.w3i==''\
           and board.s3h+board.s3g+board.s3f+board.s3e+board.s3d=='':
            moves = '3c3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w3c)and Wboard.w3i==''\
           and board.s3h+board.s3g+board.s3f+board.s3e+board.s3d=='':
            moves = '3c3i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w3c)and Wboard.w3h==''\
           and board.s3g+board.s3f+board.s3e+board.s3d=='':
            moves = '3c3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w3c)and Wboard.w3h==''\
           and board.s3g+board.s3f+board.s3e+board.s3d=='':
            moves = '3c3h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|l',    Wboard.w3c)and Wboard.w3g==''\
           and board.s3f+board.s3e+board.s3d=='':
            moves = '3c3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w3c)and Wboard.w3g==''\
           and board.s3f+board.s3e+board.s3d=='':
            moves = '3c3g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w3c)and Wboard.w3f==''\
           and board.s3e+board.s3d=='':
            moves = '3c3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w3c)and Wboard.w3e==''\
           and board.s3d=='':
            moves = '3c3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w3c)and Wboard.w3a==''\
           and board.s3b=='':
            moves = '3c3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w3c)and Wboard.w1c==''\
           and board.s2c=='':
            moves = '3c1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w3c)and Wboard.w5c==''\
           and board.s4c=='':
            moves = '3c5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w3c)and Wboard.w6c==''\
           and board.s4c+board.s5c=='':
            moves = '3c6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w3c)and Wboard.w7c==''\
           and board.s4c+board.s5c+board.s6c=='':
            moves = '3c7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w3c)and Wboard.w8c==''\
           and board.s4c+board.s5c+board.s6c+board.s7c=='':
            moves = '3c8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w3c)and Wboard.w9c==''\
           and board.s4c+board.s5c+board.s6c+board.s7c+board.s8c=='':
            moves = '3c9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w3c)and Wboard.w7g==''\
           and board.s4d+board.s5e+board.s6f=='':
            moves = '3c7g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w3c)and Wboard.w8h==''\
           and board.s4d+board.s5e+board.s6f+board.s7g=='':
            moves = '3c8h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w3c)and Wboard.w9i==''\
           and board.s4d+board.s5e+board.s6f+board.s7g+board.s8h=='':
            moves = '3c9i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w3c)and Wboard.w1a==''\
           and board.s2b=='':
            moves = '3c1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w3c)and Wboard.w5e==''\
           and board.s4d=='':
            moves = '3c5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w3c)and Wboard.w6f==''\
           and board.s4d+board.s5e=='':
            moves = '3c6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w3c)and Wboard.w7g==''\
           and board.s4d+board.s5e+board.s6f=='':
            moves = '3c7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w3c)and Wboard.w8h==''\
           and board.s4d+board.s5e+board.s6f+board.s7g=='':
            moves = '3c8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w3c)and Wboard.w9i==''\
           and board.s4d+board.s5e+board.s6f+board.s7g+board.s8h=='':
            moves = '3c9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w3c)and Wboard.w5a==''\
           and board.s4b=='':
            moves = '3c5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w3c)and Wboard.w1e==''\
           and board.s2d=='':
            moves = '3c1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w4c !='':
        if re.match(r'[plsgrk+]',   Wboard.w4c)and Wboard.w4d=='':
            moves = '4c4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w4c)and Wboard.w3d=='':
            moves = '4c3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w4c)and Wboard.w5d=='':
            moves = '4c5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w4c)and Wboard.w3c=='':
            moves = '4c3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w4c)and Wboard.w5c=='':
            moves = '4c5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w4c)and Wboard.w4b=='':
            moves = '4c4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w4c)and Wboard.w3b=='':
            moves = '4c3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w4c)and Wboard.w5b=='':
            moves = '4c5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w4c)and Wboard.w3e=='':
            moves = '4c3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w4c)and Wboard.w5e=='':
            moves = '4c5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w4c)and Wboard.w4i==''\
           and board.s4h+board.s4g+board.s4f+board.s4e+board.s4d=='':
            moves = '4c4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w4c)and Wboard.w4i==''\
           and board.s4h+board.s4g+board.s4f+board.s4e+board.s4d=='':
            moves = '4c4i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w4c)and Wboard.w4h==''\
           and board.s4g+board.s4f+board.s4e+board.s4d=='':
            moves = '4c4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w4c)and Wboard.w4h==''\
           and board.s4g+board.s4f+board.s4e+board.s4d=='':
            moves = '4c4h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|l',    Wboard.w4c)and Wboard.w4g==''\
           and board.s4f+board.s4e+board.s4d=='':
            moves = '4c4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w4c)and Wboard.w4g==''\
           and board.s4f+board.s4e+board.s4d=='':
            moves = '4c4g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w4c)and Wboard.w4f==''\
           and board.s4e+board.s4d=='':
            moves = '4c4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w4c)and Wboard.w4e==''\
           and board.s4d=='':
            moves = '4c4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w4c)and Wboard.w4a==''\
           and board.s4b=='':
            moves = '4c4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w4c)and Wboard.w1c==''\
           and board.s2c+board.s3c=='':
            moves = '4c1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w4c)and Wboard.w2c==''\
           and board.s3c=='':
            moves = '4c2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w4c)and Wboard.w6c==''\
           and board.s5c=='':
            moves = '4c6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w4c)and Wboard.w7c==''\
           and board.s5c+board.s6c=='':
            moves = '4c7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w4c)and Wboard.w8c==''\
           and board.s5c+board.s6c+board.s7c=='':
            moves = '4c8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w4c)and Wboard.w9c==''\
           and board.s5c+board.s6c+board.s7c+board.s8c=='':
            moves = '4c9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w4c)and Wboard.w6e==''\
           and board.s5d=='':
            moves = '4c6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w4c)and Wboard.w7f==''\
           and board.s5d+board.s6e=='':
            moves = '4c7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w4c)and Wboard.w8g==''\
           and board.s5d+board.s6e+board.s7f=='':
            moves = '4c8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w4c)and Wboard.w9h==''\
           and board.s5d+board.s6e+board.s7f+board.s8g=='':
            moves = '4c9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w4c)and Wboard.w8g==''\
           and board.s5d+board.s6e+board.s7f=='':
            moves = '4c8g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w4c)and Wboard.w9h==''\
           and board.s5d+board.s6e+board.s7f+board.s8g=='':
            moves = '4c9h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w4c)and Wboard.w1f==''\
           and board.s2e+board.s3d=='':
            moves = '4c1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w4c)and Wboard.w2e==''\
           and board.s3d=='':
            moves = '4c2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w4c)and Wboard.w2a==''\
           and board.s3b=='':
            moves = '4c2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w4c)and Wboard.w6a==''\
           and board.s5b=='':
            moves = '4c6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w5c !='':
        if re.match(r'[plsgrk+]',   Wboard.w5c)and Wboard.w5d=='':
            moves = '5c5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w5c)and Wboard.w4d=='':
            moves = '5c4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w5c)and Wboard.w6d=='':
            moves = '5c6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w5c)and Wboard.w4c=='':
            moves = '5c4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w5c)and Wboard.w6c=='':
            moves = '5c6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w5c)and Wboard.w5b=='':
            moves = '5c5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w5c)and Wboard.w4b=='':
            moves = '5c4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w5c)and Wboard.w6b=='':
            moves = '5c6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w5c)and Wboard.w4e=='':
            moves = '5c4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w5c)and Wboard.w6e=='':
            moves = '5c6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w5c)and Wboard.w5i==''\
           and board.s5h+board.s5g+board.s5f+board.s5e+board.s5d=='':
            moves = '5c5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w5c)and Wboard.w5i==''\
           and board.s5h+board.s5g+board.s5f+board.s5e+board.s5d=='':
            moves = '5c5i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w5c)and Wboard.w5h==''\
           and board.s5g+board.s5f+board.s5e+board.s5d=='':
            moves = '5c5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w5c)and Wboard.w5h==''\
           and board.s5g+board.s5f+board.s5e+board.s5d=='':
            moves = '5c5h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|l',    Wboard.w5c)and Wboard.w5g==''\
           and board.s5f+board.s5e+board.s5d=='':
            moves = '5c5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w5c)and Wboard.w5g==''\
           and board.s5f+board.s5e+board.s5d=='':
            moves = '5c5g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w5c)and Wboard.w5f==''\
           and board.s5e+board.s5d=='':
            moves = '5c5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w5c)and Wboard.w5e==''\
           and board.s5d=='':
            moves = '5c5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w5c)and Wboard.w5a==''\
           and board.s5b=='':
            moves = '5c5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w5c)and Wboard.w1c==''\
           and board.s2c+board.s3c+board.s4c=='':
            moves = '5c1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w5c)and Wboard.w2c==''\
           and board.s3c+board.s4c=='':
            moves = '5c2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w5c)and Wboard.w3c==''\
           and board.s4c=='':
            moves = '5c3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w5c)and Wboard.w7c==''\
           and board.s6c=='':
            moves = '5c7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w5c)and Wboard.w8c==''\
           and board.s6c+board.s7c=='':
            moves = '5c8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w5c)and Wboard.w9c==''\
           and board.s6c+board.s7c+board.s8c=='':
            moves = '5c9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w5c)and Wboard.w7e==''\
           and board.s6d=='':
            moves = '5c7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w5c)and Wboard.w8f==''\
           and board.s6d+board.s7e=='':
            moves = '5c8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w5c)and Wboard.w9g==''\
           and board.s6d+board.s7e+board.s8f=='':
            moves = '5c9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w5c)and Wboard.w9g==''\
           and board.s6d+board.s7e+board.s8f=='':
            moves = '5c9g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w5c)and Wboard.w2f==''\
           and board.s3e+board.s4d=='':
            moves = '5c2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w5c)and Wboard.w3e==''\
           and board.s4d=='':
            moves = '5c3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w5c)and Wboard.w1g==''\
           and board.s4d+board.s3e+board.s2f=='':
            moves = '5c1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w5c)and Wboard.w1g==''\
           and board.s4d+board.s3e+board.s2f=='':
            moves = '5c1g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w5c)and Wboard.w3a==''\
           and board.s4b=='':
            moves = '5c3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w5c)and Wboard.w7a==''\
           and board.s6b=='':
            moves = '5c7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w6c !='':
        if re.match(r'[plsgrk+]',   Wboard.w6c)and Wboard.w6d=='':
            moves = '6c6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w6c)and Wboard.w5d=='':
            moves = '6c5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w6c)and Wboard.w7d=='':
            moves = '6c7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w6c)and Wboard.w5c=='':
            moves = '6c5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w6c)and Wboard.w7c=='':
            moves = '6c7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w6c)and Wboard.w6b=='':
            moves = '6c6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w6c)and Wboard.w5b=='':
            moves = '6c5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w6c)and Wboard.w7b=='':
            moves = '6c7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w6c)and Wboard.w5e=='':
            moves = '6c5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w6c)and Wboard.w7e=='':
            moves = '6c7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w6c)and Wboard.w6i==''\
           and board.s6h+board.s6g+board.s6f+board.s6e+board.s6d=='':
            moves = '6c6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w6c)and Wboard.w6i==''\
           and board.s6h+board.s6g+board.s6f+board.s6e+board.s6d=='':
            moves = '6c6i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w6c)and Wboard.w6h==''\
           and board.s6g+board.s6f+board.s6e+board.s6d=='':
            moves = '6c6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w6c)and Wboard.w6h==''\
           and board.s6g+board.s6f+board.s6e+board.s6d=='':
            moves = '6c6h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|l',    Wboard.w6c)and Wboard.w6g==''\
           and board.s6f+board.s6e+board.s6d=='':
            moves = '6c6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w6c)and Wboard.w6g==''\
           and board.s6f+board.s6e+board.s6d=='':
            moves = '6c6g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w6c)and Wboard.w6f==''\
           and board.s6e+board.s6d=='':
            moves = '6c6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w6c)and Wboard.w6e==''\
           and board.s6d=='':
            moves = '6c6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w6c)and Wboard.w6a==''\
           and board.s6b=='':
            moves = '6c6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w6c)and Wboard.w9c==''\
           and board.s8c+board.s7c=='':
            moves = '6c9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w6c)and Wboard.w8c==''\
           and board.s7c=='':
            moves = '6c8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w6c)and Wboard.w4c==''\
           and board.s5c=='':
            moves = '6c4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w6c)and Wboard.w3c==''\
           and board.s5c+board.s4c=='':
            moves = '6c3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w6c)and Wboard.w2c==''\
           and board.s5c+board.s4c+board.s3c=='':
            moves = '6c2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w6c)and Wboard.w1c==''\
           and board.s5c+board.s4c+board.s3c+board.s2c=='':
            moves = '6c1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w6c)and Wboard.w4e==''\
           and board.s5d=='':
            moves = '6c4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w6c)and Wboard.w3f==''\
           and board.s5d+board.s4e=='':
            moves = '6c3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w6c)and Wboard.w2g==''\
           and board.s5d+board.s4e+board.s3f=='':
            moves = '6c2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w6c)and Wboard.w1h==''\
           and board.s5d+board.s4e+board.s3f+board.s2g=='':
            moves = '6c1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w6c)and Wboard.w2g==''\
           and board.s5d+board.s4e+board.s3f=='':
            moves = '6c2g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w6c)and Wboard.w1h==''\
           and board.s5d+board.s4e+board.s3f+board.s2g=='':
            moves = '6c1h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w6c)and Wboard.w9f==''\
           and board.s8e+board.s7d=='':
            moves = '6c9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w6c)and Wboard.w8e==''\
           and board.s7d=='':
            moves = '6c8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w6c)and Wboard.w8a==''\
           and board.s7b=='':
            moves = '6c8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w6c)and Wboard.w4a==''\
           and board.s5b=='':
            moves = '6c4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w7c !='':
        if re.match(r'[plsgrk+]',   Wboard.w7c)and Wboard.w7d=='':
            moves = '7c7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w7c)and Wboard.w6d=='':
            moves = '7c6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w7c)and Wboard.w8d=='':
            moves = '7c8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w7c)and Wboard.w6c=='':
            moves = '7c6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w7c)and Wboard.w8c=='':
            moves = '7c8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w7c)and Wboard.w7b=='':
            moves = '7c7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w7c)and Wboard.w6b=='':
            moves = '7c6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w7c)and Wboard.w8b=='':
            moves = '7c8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w7c)and Wboard.w6e=='':
            moves = '7c6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w7c)and Wboard.w8e=='':
            moves = '7c8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w7c)and Wboard.w7i==''\
           and board.s7h+board.s7g+board.s7f+board.s7e+board.s7d=='':
            moves = '7c7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w7c)and Wboard.w7i==''\
           and board.s7h+board.s7g+board.s7f+board.s7e+board.s7d=='':
            moves = '7c7i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w7c)and Wboard.w7h==''\
           and board.s7g+board.s7f+board.s7e+board.s7d=='':
            moves = '7c7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w7c)and Wboard.w7h==''\
           and board.s7g+board.s7f+board.s7e+board.s7d=='':
            moves = '7c7h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|l',    Wboard.w7c)and Wboard.w7g==''\
           and board.s7f+board.s7e+board.s7d=='':
            moves = '7c7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w7c)and Wboard.w7g==''\
           and board.s7f+board.s7e+board.s7d=='':
            moves = '7c7g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w7c)and Wboard.w7f==''\
           and board.s7e+board.s7d=='':
            moves = '7c7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w7c)and Wboard.w7e==''\
           and board.s7d=='':
            moves = '7c7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w7c)and Wboard.w7a==''\
           and board.s7b=='':
            moves = '7c7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w7c)and Wboard.w9c==''\
           and board.s8c=='':
            moves = '7c9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w7c)and Wboard.w5c==''\
           and board.s6c=='':
            moves = '7c5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w7c)and Wboard.w4c==''\
           and board.s6c+board.s5c=='':
            moves = '7c4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w7c)and Wboard.w3c==''\
           and board.s6c+board.s5c+board.s4c=='':
            moves = '7c3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w7c)and Wboard.w2c==''\
           and board.s6c+board.s5c+board.s4c+board.s3c=='':
            moves = '7c2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w7c)and Wboard.w1c==''\
           and board.s6c+board.s5c+board.s4c+board.s3c+board.s2c=='':
            moves = '7c1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w7c)and Wboard.w3g==''\
           and board.s6d+board.s5e+board.s4f=='':
            moves = '7c3g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w7c)and Wboard.w2h==''\
           and board.s6d+board.s5e+board.s4f+board.s3g=='':
            moves = '7c2h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w7c)and Wboard.w1i==''\
           and board.s6d+board.s5e+board.s4f+board.s3g+board.s2h=='':
            moves = '7c1i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w7c)and Wboard.w9a==''\
           and board.s8b=='':
            moves = '7c9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w7c)and Wboard.w5e==''\
           and board.s6d=='':
            moves = '7c5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w7c)and Wboard.w4f==''\
           and board.s6d+board.s5e=='':
            moves = '7c4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w7c)and Wboard.w3g==''\
           and board.s6d+board.s5e+board.s4f=='':
            moves = '7c3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w7c)and Wboard.w2h==''\
           and board.s6d+board.s5e+board.s4f+board.s3g=='':
            moves = '7c2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w7c)and Wboard.w1i==''\
           and board.s6d+board.s5e+board.s4f+board.s3g+board.s2h=='':
            moves = '7c1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w7c)and Wboard.w5a==''\
           and board.s6b=='':
            moves = '7c5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w7c)and Wboard.w9e==''\
           and board.s8d=='':
            moves = '7c9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w8c !='':
        if re.match(r'[plsgrk+]',   Wboard.w8c)and Wboard.w8d=='':
            moves = '8c8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w8c)and Wboard.w7d=='':
            moves = '8c7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w8c)and Wboard.w9d=='':
            moves = '8c9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w8c)and Wboard.w7c=='':
            moves = '8c7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w8c)and Wboard.w9c=='':
            moves = '8c9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w8c)and Wboard.w8b=='':
            moves = '8c8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w8c)and Wboard.w7b=='':
            moves = '8c7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w8c)and Wboard.w9b=='':
            moves = '8c9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w8c)and Wboard.w7e=='':
            moves = '8c7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w8c)and Wboard.w9e=='':
            moves = '8c9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w8c)and Wboard.w8i==''\
           and board.s8h+board.s8g+board.s8f+board.s8e+board.s8d=='':
            moves = '8c8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w8c)and Wboard.w8i==''\
           and board.s8h+board.s8g+board.s8f+board.s8e+board.s8d=='':
            moves = '8c8i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w8c)and Wboard.w8h==''\
           and board.s8g+board.s8f+board.s8e+board.s8d=='':
            moves = '8c8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w8c)and Wboard.w8h==''\
           and board.s8g+board.s8f+board.s8e+board.s8d=='':
            moves = '8c8h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|l',    Wboard.w8c)and Wboard.w8g==''\
           and board.s8f+board.s8e+board.s8d=='':
            moves = '8c8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w8c)and Wboard.w8g==''\
           and board.s8f+board.s8e+board.s8d=='':
            moves = '8c8g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w8c)and Wboard.w8f==''\
           and board.s8e+board.s8d=='':
            moves = '8c8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w8c)and Wboard.w8e==''\
           and board.s8d=='':
            moves = '8c8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w8c)and Wboard.w8a==''\
           and board.s8b=='':
            moves = '8c8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w8c)and Wboard.w6c==''\
           and board.s7c=='':
            moves = '8c6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w8c)and Wboard.w5c==''\
           and board.s7c+board.s6c=='':
            moves = '8c5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w8c)and Wboard.w4c==''\
           and board.s7c+board.s6c+board.s5c=='':
            moves = '8c4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w8c)and Wboard.w3c==''\
           and board.s7c+board.s6c+board.s5c+board.s4c=='':
            moves = '8c3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w8c)and Wboard.w2c==''\
           and board.s7c+board.s6c+board.s5c+board.s4c+board.s3c=='':
            moves = '8c2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w8c)and Wboard.w1c==''\
           and board.s7c+board.s6c+board.s5c+board.s4c+board.s3c+board.s2c=='':
            moves = '8c1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w8c)and Wboard.w4g==''\
           and board.s7d+board.s6e+board.s5f=='':
            moves = '8c4g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w8c)and Wboard.w3h==''\
           and board.s7d+board.s6e+board.s5f+board.s4g=='':
            moves = '8c3h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w8c)and Wboard.w2i==''\
           and board.s7d+board.s6e+board.s5f+board.s4g+board.s3h=='':
            moves = '8c2i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w8c)and Wboard.w6e==''\
           and board.s7d=='':
            moves = '8c6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w8c)and Wboard.w5f==''\
           and board.s7d+board.s6e=='':
            moves = '8c5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w8c)and Wboard.w4g==''\
           and board.s7d+board.s6e+board.s5f=='':
            moves = '8c4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w8c)and Wboard.w3h==''\
           and board.s7d+board.s6e+board.s5f+board.s4g=='':
            moves = '8c3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w8c)and Wboard.w2i==''\
           and board.s7d+board.s6e+board.s5f+board.s4g+board.s3h=='':
            moves = '8c2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w8c)and Wboard.w6a==''\
           and board.s7b=='':
            moves = '8c6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w9c !='':
        if re.match(r'[plsgrk+]',   Wboard.w9c)and Wboard.w9d=='':
            moves = '9c9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w9c)and Wboard.w8d=='':
            moves = '9c8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w9c)and Wboard.w8c=='':
            moves = '9c8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w9c)and Wboard.w9b=='':
            moves = '9c9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w9c)and Wboard.w8b=='':
            moves = '9c8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w9c)and Wboard.w8e=='':
            moves = '9c8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w9c)and Wboard.w9i==''\
           and board.s9h+board.s9g+board.s9f+board.s9e+board.s9d=='':
            moves = '9c9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w9c)and Wboard.w9i==''\
           and board.s9h+board.s9g+board.s9f+board.s9e+board.s9d=='':
            moves = '9c9i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w9c)and Wboard.w9h==''\
           and board.s9g+board.s9f+board.s9e+board.s9d=='':
            moves = '9c9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w9c)and Wboard.w9h==''\
           and board.s9g+board.s9f+board.s9e+board.s9d=='':
            moves = '9c9h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|l',    Wboard.w9c)and Wboard.w9g==''\
           and board.s9f+board.s9e+board.s9d=='':
            moves = '9c9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w9c)and Wboard.w9g==''\
           and board.s9f+board.s9e+board.s9d=='':
            moves = '9c9g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w9c)and Wboard.w9f==''\
           and board.s9e+board.s9d=='':
            moves = '9c9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w9c)and Wboard.w9e==''\
           and board.s9d=='':
            moves = '9c9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w9c)and Wboard.w9a==''\
           and board.s9b=='':
            moves = '9c9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w9c)and Wboard.w7c==''\
           and board.s8c=='':
            moves = '9c7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w9c)and Wboard.w6c==''\
           and board.s8c+board.s7c=='':
            moves = '9c6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w9c)and Wboard.w5c==''\
           and board.s8c+board.s7c+board.s6c=='':
            moves = '9c5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w9c)and Wboard.w4c==''\
           and board.s8c+board.s7c+board.s6c+board.s5c=='':
            moves = '9c4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w9c)and Wboard.w3c==''\
           and board.s8c+board.s7c+board.s6c+board.s5c+board.s4c=='':
            moves = '9c3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w9c)and Wboard.w2c==''\
           and board.s8c+board.s7c+board.s6c+board.s5c+board.s4c+board.s3c=='':
            moves = '9c2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w9c)and Wboard.w1c==''\
           and board.s8c+board.s7c+board.s6c+board.s5c+board.s4c+board.s3c+board.s2c=='':
            moves = '9c1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w9c)and Wboard.w5g==''\
           and board.s8d+board.s7e+board.s6f=='':
            moves = '9c5g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w9c)and Wboard.w4h==''\
           and board.s8d+board.s7e+board.s6f+board.s5g=='':
            moves = '9c4h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w9c)and Wboard.w3i==''\
           and board.s8d+board.s7e+board.s6f+board.s5g+board.s4h=='':
            moves = '9c3i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w9c)and Wboard.w7a==''\
           and board.s8b=='':
            moves = '9c7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w9c)and Wboard.w7e==''\
           and board.s8d=='':
            moves = '9c7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w9c)and Wboard.w6f==''\
           and board.s8d+board.s7e=='':
            moves = '9c6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w9c)and Wboard.w5g==''\
           and board.s8d+board.s7e+board.s6f=='':
            moves = '9c5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w9c)and Wboard.w4h==''\
           and board.s8d+board.s7e+board.s6f+board.s5g=='':
            moves = '9c4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w9c)and Wboard.w3i==''\
           and board.s8d+board.s7e+board.s6f+board.s5g+board.s4h=='':
            moves = '9c3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w1b !='':
        if re.match(r'[plsgrk+]',   Wboard.w1b)and Wboard.w1c=='':
            moves = '1b1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w1b)and Wboard.w2c=='':
            moves = '1b2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w1b)and Wboard.w2b=='':
            moves = '1b2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w1b)and Wboard.w1a=='':
            moves = '1b1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w1b)and Wboard.w2a=='':
            moves = '1b2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w1b)and Wboard.w2d=='':
            moves = '1b2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w1b)and Wboard.w1i==''\
           and board.s1h+board.s1g+board.s1f+board.s1e+board.s1d+board.s1c=='':
            moves = '1b1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w1b)and Wboard.w1i==''\
           and board.s1h+board.s1g+board.s1f+board.s1e+board.s1d+board.s1c=='':
            moves = '1b1i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w1b)and Wboard.w1h==''\
           and board.s1g+board.s1f+board.s1e+board.s1d+board.s1c=='':
            moves = '1b1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w1b)and Wboard.w1h==''\
           and board.s1g+board.s1f+board.s1e+board.s1d+board.s1c=='':
            moves = '1b1h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|l',    Wboard.w1b)and Wboard.w1g==''\
           and board.s1f+board.s1e+board.s1d+board.s1c=='':
            moves = '1b1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w1b)and Wboard.w1g==''\
           and board.s1f+board.s1e+board.s1d+board.s1c=='':
            moves = '1b1g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w1b)and Wboard.w1f==''\
           and board.s1e+board.s1d+board.s1c=='':
            moves = '1b1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w1b)and Wboard.w1e==''\
           and board.s1d+board.s1c=='':
            moves = '1b1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w1b)and Wboard.w1d==''\
           and board.s1c=='':
            moves = '1b1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w1b)and Wboard.w3b==''\
           and board.s2b=='':
            moves = '1b3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w1b)and Wboard.w4b==''\
           and board.s2b+board.s3b=='':
            moves = '1b4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w1b)and Wboard.w5b==''\
           and board.s2b+board.s3b+board.s4b=='':
            moves = '1b5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w1b)and Wboard.w6b==''\
           and board.s2b+board.s3b+board.s4b+board.s5b=='':
            moves = '1b6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w1b)and Wboard.w7b==''\
           and board.s2b+board.s3b+board.s4b+board.s5b+board.s6b=='':
            moves = '1b7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w1b)and Wboard.w8b==''\
           and board.s2b+board.s3b+board.s4b+board.s5b+board.s6b+board.s7b=='':
            moves = '1b8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w1b)and Wboard.w9b==''\
           and board.s2b+board.s3b+board.s4b+board.s5b+board.s6b+board.s7b+board.s8b=='':
            moves = '1b9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w1b)and Wboard.w6g==''\
           and board.s2c+board.s3d+board.s4e+board.s5f=='':
            moves = '1b6g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w1b)and Wboard.w7h==''\
           and board.s2c+board.s3d+board.s4e+board.s5f+board.s6g=='':
            moves = '1b7h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w1b)and Wboard.w8i==''\
           and board.s2c+board.s3d+board.s4e+board.s5f+board.s6g+board.s7h=='':
            moves = '1b8i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w1b)and Wboard.w3d==''\
           and board.s2c=='':
            moves = '1b3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w1b)and Wboard.w4e==''\
           and board.s2c+board.s3d=='':
            moves = '1b4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w1b)and Wboard.w5f==''\
           and board.s2c+board.s3d+board.s4e=='':
            moves = '1b5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w1b)and Wboard.w6g==''\
           and board.s2c+board.s3d+board.s4e+board.s5f=='':
            moves = '1b6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w1b)and Wboard.w7h==''\
           and board.s2c+board.s3d+board.s4e+board.s5f+board.s6g=='':
            moves = '1b7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w1b)and Wboard.w8i==''\
           and board.s2c+board.s3d+board.s4e+board.s5f+board.s6g+board.s7h=='':
            moves = '1b8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w2b !='':
        if re.match(r'[plsgrk+]',   Wboard.w2b)and Wboard.w2c=='':
            moves = '2b2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w2b)and Wboard.w1c=='':
            moves = '2b1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w2b)and Wboard.w3c=='':
            moves = '2b3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w2b)and Wboard.w1b=='':
            moves = '2b1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w2b)and Wboard.w3b=='':
            moves = '2b3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w2b)and Wboard.w2a=='':
            moves = '2b2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w2b)and Wboard.w1a=='':
            moves = '2b1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w2b)and Wboard.w3a=='':
            moves = '2b3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w2b)and Wboard.w1d=='':
            moves = '2b1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w2b)and Wboard.w3d=='':
            moves = '2b3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w2b)and Wboard.w2i==''\
           and board.s2h+board.s2g+board.s2f+board.s2e+board.s2d+board.s2c=='':
            moves = '2b2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w2b)and Wboard.w2i==''\
           and board.s2h+board.s2g+board.s2f+board.s2e+board.s2d+board.s2c=='':
            moves = '2b2i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w2b)and Wboard.w2h==''\
           and board.s2g+board.s2f+board.s2e+board.s2d+board.s2c=='':
            moves = '2b2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w2b)and Wboard.w2h==''\
           and board.s2g+board.s2f+board.s2e+board.s2d+board.s2c=='':
            moves = '2b2h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|l',    Wboard.w2b)and Wboard.w2g==''\
           and board.s2f+board.s2e+board.s2d+board.s2c=='':
            moves = '2b2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w2b)and Wboard.w2g==''\
           and board.s2f+board.s2e+board.s2d+board.s2c=='':
            moves = '2b2g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w2b)and Wboard.w2f==''\
           and board.s2e+board.s2d+board.s2c=='':
            moves = '2b2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w2b)and Wboard.w2e==''\
           and board.s2d+board.s2c=='':
            moves = '2b2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w2b)and Wboard.w2d==''\
           and board.s2c=='':
            moves = '2b2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w2b)and Wboard.w4b==''\
           and board.s3b=='':
            moves = '2b4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w2b)and Wboard.w5b==''\
           and board.s3b+board.s4b=='':
            moves = '2b5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w2b)and Wboard.w6b==''\
           and board.s3b+board.s4b+board.s5b=='':
            moves = '2b6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w2b)and Wboard.w7b==''\
           and board.s3b+board.s4b+board.s5b+board.s6b=='':
            moves = '2b7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w2b)and Wboard.w8b==''\
           and board.s3b+board.s4b+board.s5b+board.s6b+board.s7b=='':
            moves = '2b8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w2b)and Wboard.w9b==''\
           and board.s3b+board.s4b+board.s5b+board.s6b+board.s7b+board.s8b=='':
            moves = '2b9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w2b)and Wboard.w7g==''\
           and board.s3c+board.s4d+board.s5e+board.s6f=='':
            moves = '2b7g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w2b)and Wboard.w8h==''\
           and board.s3c+board.s4d+board.s5e+board.s6f+board.s7g=='':
            moves = '2b8h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w2b)and Wboard.w9i==''\
           and board.s3c+board.s4d+board.s5e+board.s6f+board.s7g+board.s8h=='':
            moves = '2b9i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w2b)and Wboard.w4d==''\
           and board.s3c=='':
            moves = '2b4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w2b)and Wboard.w5e==''\
           and board.s3c+board.s4d=='':
            moves = '2b5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w2b)and Wboard.w6f==''\
           and board.s3c+board.s4d+board.s5e=='':
            moves = '2b6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w2b)and Wboard.w7g==''\
           and board.s3c+board.s4d+board.s5e+board.s6f=='':
            moves = '2b7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w2b)and Wboard.w8h==''\
           and board.s3c+board.s4d+board.s5e+board.s6f+board.s7g=='':
            moves = '2b8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w2b)and Wboard.w9i==''\
           and board.s3c+board.s4d+board.s5e+board.s6f+board.s7g+board.s8h=='':
            moves = '2b9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w3b !='':
        if re.match(r'[plsgrk+]',   Wboard.w3b)and Wboard.w3c=='':
            moves = '3b3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w3b)and Wboard.w2c=='':
            moves = '3b2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w3b)and Wboard.w4c=='':
            moves = '3b4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w3b)and Wboard.w2b=='':
            moves = '3b2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w3b)and Wboard.w4b=='':
            moves = '3b4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w3b)and Wboard.w3a=='':
            moves = '3b3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w3b)and Wboard.w2a=='':
            moves = '3b2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w3b)and Wboard.w4a=='':
            moves = '3b4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w3b)and Wboard.w2d=='':
            moves = '3b2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w3b)and Wboard.w4d=='':
            moves = '3b4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w3b)and Wboard.w3i==''\
           and board.s3h+board.s3g+board.s3f+board.s3e+board.s3d+board.s3c=='':
            moves = '3b3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w3b)and Wboard.w3i==''\
           and board.s3h+board.s3g+board.s3f+board.s3e+board.s3d+board.s3c=='':
            moves = '3b3i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w3b)and Wboard.w3h==''\
           and board.s3g+board.s3f+board.s3e+board.s3d+board.s3c=='':
            moves = '3b3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w3b)and Wboard.w3h==''\
           and board.s3g+board.s3f+board.s3e+board.s3d+board.s3c=='':
            moves = '3b3h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|l',    Wboard.w3b)and Wboard.w3g==''\
           and board.s3f+board.s3e+board.s3d+board.s3c=='':
            moves = '3b3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w3b)and Wboard.w3g==''\
           and board.s3f+board.s3e+board.s3d+board.s3c=='':
            moves = '3b3g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w3b)and Wboard.w3f==''\
           and board.s3e+board.s3d+board.s3c=='':
            moves = '3b3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w3b)and Wboard.w3e==''\
           and board.s3d+board.s3c=='':
            moves = '3b3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w3b)and Wboard.w3d==''\
           and board.s3c=='':
            moves = '3b3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w3b)and Wboard.w1b==''\
           and board.s2b=='':
            moves = '3b1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w3b)and Wboard.w5b==''\
           and board.s4b=='':
            moves = '3b5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w3b)and Wboard.w6b==''\
           and board.s4b+board.s5b=='':
            moves = '3b6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w3b)and Wboard.w7b==''\
           and board.s4b+board.s5b+board.s6b=='':
            moves = '3b7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w3b)and Wboard.w8b==''\
           and board.s4b+board.s5b+board.s6b+board.s7b=='':
            moves = '3b8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w3b)and Wboard.w9b==''\
           and board.s4b+board.s5b+board.s6b+board.s7b+board.s8b=='':
            moves = '3b9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w3b)and Wboard.w8g==''\
           and board.s4c+board.s5d+board.s6e+board.s7f=='':
            moves = '3b8g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w3b)and Wboard.w9h==''\
           and board.s4c+board.s5d+board.s6e+board.s7f+board.s8g=='':
            moves = '3b9h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w3b)and Wboard.w5d==''\
           and board.s4c=='':
            moves = '3b5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w3b)and Wboard.w6e==''\
           and board.s4c+board.s5d=='':
            moves = '3b6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w3b)and Wboard.w7f==''\
           and board.s4c+board.s5d+board.s6e=='':
            moves = '3b7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w3b)and Wboard.w8g==''\
           and board.s4c+board.s5d+board.s6e+board.s7f=='':
            moves = '3b8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w3b)and Wboard.w9h==''\
           and board.s4c+board.s5d+board.s6e+board.s7f+board.s8g=='':
            moves = '3b9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w3b)and Wboard.w1d==''\
           and board.s2c=='':
            moves = '3b1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w4b !='':
        if re.match(r'[plsgrk+]',   Wboard.w4b)and Wboard.w4c=='':
            moves = '4b4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w4b)and Wboard.w3c=='':
            moves = '4b3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w4b)and Wboard.w5c=='':
            moves = '4b5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w4b)and Wboard.w3b=='':
            moves = '4b3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w4b)and Wboard.w5b=='':
            moves = '4b5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w4b)and Wboard.w4a=='':
            moves = '4b4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w4b)and Wboard.w3a=='':
            moves = '4b3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w4b)and Wboard.w5a=='':
            moves = '4b5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w4b)and Wboard.w3d=='':
            moves = '4b3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w4b)and Wboard.w5d=='':
            moves = '4b5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w4b)and Wboard.w4i==''\
           and board.s4h+board.s4g+board.s4f+board.s4e+board.s4d+board.s4c=='':
            moves = '4b4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w4b)and Wboard.w4i==''\
           and board.s4h+board.s4g+board.s4f+board.s4e+board.s4d+board.s4c=='':
            moves = '4b4i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w4b)and Wboard.w4h==''\
           and board.s4g+board.s4f+board.s4e+board.s4d+board.s4c=='':
            moves = '4b4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w4b)and Wboard.w4h==''\
           and board.s4g+board.s4f+board.s4e+board.s4d+board.s4c=='':
            moves = '4b4h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|l',    Wboard.w4b)and Wboard.w4g==''\
           and board.s4f+board.s4e+board.s4d+board.s4c=='':
            moves = '4b4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w4b)and Wboard.w4g==''\
           and board.s4f+board.s4e+board.s4d+board.s4c=='':
            moves = '4b4g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w4b)and Wboard.w4f==''\
           and board.s4e+board.s4d+board.s4c=='':
            moves = '4b4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w4b)and Wboard.w4e==''\
           and board.s4d+board.s4c=='':
            moves = '4b4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w4b)and Wboard.w4d==''\
           and board.s4c=='':
            moves = '4b4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w4b)and Wboard.w1b==''\
           and board.s2b+board.s3b=='':
            moves = '4b1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w4b)and Wboard.w2b==''\
           and board.s3b=='':
            moves = '4b2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w4b)and Wboard.w6b==''\
           and board.s5b=='':
            moves = '4b6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w4b)and Wboard.w7b==''\
           and board.s5b+board.s6b=='':
            moves = '4b7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w4b)and Wboard.w8b==''\
           and board.s5b+board.s6b+board.s7b=='':
            moves = '4b8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w4b)and Wboard.w9b==''\
           and board.s5b+board.s6b+board.s7b+board.s8b=='':
            moves = '4b9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w4b)and Wboard.w6d==''\
           and board.s5c=='':
            moves = '4b6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w4b)and Wboard.w7e==''\
           and board.s5c+board.s6d=='':
            moves = '4b7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w4b)and Wboard.w8f==''\
           and board.s5c+board.s6d+board.s7e=='':
            moves = '4b8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w4b)and Wboard.w9g==''\
           and board.s5c+board.s6d+board.s7e+board.s8f=='':
            moves = '4b9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w4b)and Wboard.w9g==''\
           and board.s5c+board.s6d+board.s7e+board.s8f=='':
            moves = '4b9g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w4b)and Wboard.w1e==''\
           and board.s2d+board.s3c=='':
            moves = '4b1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w4b)and Wboard.w2d==''\
           and board.s3c=='':
            moves = '4b2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w5b !='':
        if re.match(r'[plsgrk+]',   Wboard.w5b)and Wboard.w5c=='':
            moves = '5b5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w5b)and Wboard.w4c=='':
            moves = '5b4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w5b)and Wboard.w6c=='':
            moves = '5b6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w5b)and Wboard.w4b=='':
            moves = '5b4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w5b)and Wboard.w6b=='':
            moves = '5b6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w5b)and Wboard.w5a=='':
            moves = '5b5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w5b)and Wboard.w4a=='':
            moves = '5b4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w5b)and Wboard.w6a=='':
            moves = '5b6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w5b)and Wboard.w4d=='':
            moves = '5b4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w5b)and Wboard.w6d=='':
            moves = '5b6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w5b)and Wboard.w5i==''\
           and board.s5h+board.s5g+board.s5f+board.s5e+board.s5d+board.s5c=='':
            moves = '5b5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w5b)and Wboard.w5i==''\
           and board.s5h+board.s5g+board.s5f+board.s5e+board.s5d+board.s5c=='':
            moves = '5b5i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w5b)and Wboard.w5h==''\
           and board.s5g+board.s5f+board.s5e+board.s5d+board.s5c=='':
            moves = '5b5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w5b)and Wboard.w5h==''\
           and board.s5g+board.s5f+board.s5e+board.s5d+board.s5c=='':
            moves = '5b5h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|l',    Wboard.w5b)and Wboard.w5g==''\
           and board.s5f+board.s5e+board.s5d+board.s5c=='':
            moves = '5b5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w5b)and Wboard.w5g==''\
           and board.s5f+board.s5e+board.s5d+board.s5c=='':
            moves = '5b5g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w5b)and Wboard.w5f==''\
           and board.s5e+board.s5d+board.s5c=='':
            moves = '5b5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w5b)and Wboard.w5e==''\
           and board.s5d+board.s5c=='':
            moves = '5b5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w5b)and Wboard.w5d==''\
           and board.s5c=='':
            moves = '5b5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w5b)and Wboard.w1b==''\
           and board.s2b+board.s3b+board.s4b=='':
            moves = '5b1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w5b)and Wboard.w2b==''\
           and board.s3b+board.s4b=='':
            moves = '5b2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w5b)and Wboard.w3b==''\
           and board.s4b=='':
            moves = '5b3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w5b)and Wboard.w7b==''\
           and board.s6b=='':
            moves = '5b7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w5b)and Wboard.w8b==''\
           and board.s6b+board.s7b=='':
            moves = '5b8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w5b)and Wboard.w9b==''\
           and board.s6b+board.s7b+board.s8b=='':
            moves = '5b9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w5b)and Wboard.w7d==''\
           and board.s6c=='':
            moves = '5b7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w5b)and Wboard.w8e==''\
           and board.s6c+board.s7d=='':
            moves = '5b8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w5b)and Wboard.w9f==''\
           and board.s6c+board.s7d+board.s8e=='':
            moves = '5b9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w5b)and Wboard.w2e==''\
           and board.s3d+board.s4c=='':
            moves = '5b2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w5b)and Wboard.w3d==''\
           and board.s4c=='':
            moves = '5b3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w5b)and Wboard.w1f==''\
           and board.s4c+board.s3d+board.s2e=='':
            moves = '5b1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w6b !='':
        if re.match(r'[plsgrk+]',   Wboard.w6b)and Wboard.w6c=='':
            moves = '6b6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w6b)and Wboard.w5c=='':
            moves = '6b5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w6b)and Wboard.w7c=='':
            moves = '6b7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w6b)and Wboard.w5b=='':
            moves = '6b5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w6b)and Wboard.w7b=='':
            moves = '6b7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w6b)and Wboard.w6a=='':
            moves = '6b6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w6b)and Wboard.w5a=='':
            moves = '6b5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w6b)and Wboard.w7a=='':
            moves = '6b7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w6b)and Wboard.w5d=='':
            moves = '6b5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w6b)and Wboard.w7d=='':
            moves = '6b7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w6b)and Wboard.w6i==''\
           and board.s6h+board.s6g+board.s6f+board.s6e+board.s6d+board.s6c=='':
            moves = '6b6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w6b)and Wboard.w6i==''\
           and board.s6h+board.s6g+board.s6f+board.s6e+board.s6d+board.s6c=='':
            moves = '6b6i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w6b)and Wboard.w6h==''\
           and board.s6g+board.s6f+board.s6e+board.s6d+board.s6c=='':
            moves = '6b6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w6b)and Wboard.w6h==''\
           and board.s6g+board.s6f+board.s6e+board.s6d+board.s6c=='':
            moves = '6b6h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|l',    Wboard.w6b)and Wboard.w6g==''\
           and board.s6f+board.s6e+board.s6d+board.s6c=='':
            moves = '6b6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w6b)and Wboard.w6g==''\
           and board.s6f+board.s6e+board.s6d+board.s6c=='':
            moves = '6b6g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w6b)and Wboard.w6f==''\
           and board.s6e+board.s6d+board.s6c=='':
            moves = '6b6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w6b)and Wboard.w6e==''\
           and board.s6d+board.s6c=='':
            moves = '6b6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w6b)and Wboard.w6d==''\
           and board.s6c=='':
            moves = '6b6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w6b)and Wboard.w9b==''\
           and board.s8b+board.s7b=='':
            moves = '6b9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w6b)and Wboard.w8b==''\
           and board.s7b=='':
            moves = '6b8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w6b)and Wboard.w4b==''\
           and board.s5b=='':
            moves = '6b4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w6b)and Wboard.w3b==''\
           and board.s5b+board.s4b=='':
            moves = '6b3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w6b)and Wboard.w2b==''\
           and board.s5b+board.s4b+board.s3b=='':
            moves = '6b2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w6b)and Wboard.w1b==''\
           and board.s5b+board.s4b+board.s3b+board.s2b=='':
            moves = '6b1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w6b)and Wboard.w4d==''\
           and board.s5c=='':
            moves = '6b4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w6b)and Wboard.w3e==''\
           and board.s5c+board.s4d=='':
            moves = '6b3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w6b)and Wboard.w2f==''\
           and board.s5c+board.s4d+board.s3e=='':
            moves = '6b2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w6b)and Wboard.w1g==''\
           and board.s5c+board.s4d+board.s3e+board.s2f=='':
            moves = '6b1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',   Wboard.w6b)and Wboard.w1g==''\
           and board.s5c+board.s4d+board.s3e+board.s2f=='':
            moves = '6b1g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w6b)and Wboard.w9e==''\
           and board.s8d+board.s7c=='':
            moves = '6b9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w6b)and Wboard.w8d==''\
           and board.s7c=='':
            moves = '6b8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w7b !='':
        if re.match(r'[plsgrk+]',   Wboard.w7b)and Wboard.w7c=='':
            moves = '7b7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w7b)and Wboard.w6c=='':
            moves = '7b6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w7b)and Wboard.w8c=='':
            moves = '7b8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w7b)and Wboard.w6b=='':
            moves = '7b6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w7b)and Wboard.w8b=='':
            moves = '7b8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w7b)and Wboard.w7a=='':
            moves = '7b7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w7b)and Wboard.w6a=='':
            moves = '7b6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w7b)and Wboard.w8a=='':
            moves = '7b8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w7b)and Wboard.w6d=='':
            moves = '7b6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w7b)and Wboard.w8d=='':
            moves = '7b8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w7b)and Wboard.w7i==''\
           and board.s7h+board.s7g+board.s7f+board.s7e+board.s7d+board.s7c=='':
            moves = '7b7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w7b)and Wboard.w7i==''\
           and board.s7h+board.s7g+board.s7f+board.s7e+board.s7d+board.s7c=='':
            moves = '7b7i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w7b)and Wboard.w7h==''\
           and board.s7g+board.s7f+board.s7e+board.s7d+board.s7c=='':
            moves = '7b7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w7b)and Wboard.w7h==''\
           and board.s7g+board.s7f+board.s7e+board.s7d+board.s7c=='':
            moves = '7b7h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|l',    Wboard.w7b)and Wboard.w7g==''\
           and board.s7f+board.s7e+board.s7d+board.s7c=='':
            moves = '7b7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w7b)and Wboard.w7g==''\
           and board.s7f+board.s7e+board.s7d+board.s7c=='':
            moves = '7b7g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w7b)and Wboard.w7f==''\
           and board.s7e+board.s7d+board.s7c=='':
            moves = '7b7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w7b)and Wboard.w7e==''\
           and board.s7d+board.s7c=='':
            moves = '7b7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w7b)and Wboard.w7d==''\
           and board.s7c=='':
            moves = '7b7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w7b)and Wboard.w9b==''\
           and board.s8b=='':
            moves = '7b9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w7b)and Wboard.w5b==''\
           and board.s6b=='':
            moves = '7b5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w7b)and Wboard.w4b==''\
           and board.s6b+board.s5b=='':
            moves = '7b4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w7b)and Wboard.w3b==''\
           and board.s6b+board.s5b+board.s4b=='':
            moves = '7b3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w7b)and Wboard.w2b==''\
           and board.s6b+board.s5b+board.s4b+board.s3b=='':
            moves = '7b2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w7b)and Wboard.w1b==''\
           and board.s6b+board.s5b+board.s4b+board.s3b+board.s2b=='':
            moves = '7b1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w7b)and Wboard.w2g==''\
           and board.s6c+board.s5d+board.s4e+board.s3f=='':
            moves = '7b2g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w7b)and Wboard.w1h==''\
           and board.s6c+board.s5d+board.s4e+board.s3f+board.s2g=='':
            moves = '7b1h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w7b)and Wboard.w5d==''\
           and board.s6c=='':
            moves = '7b5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w7b)and Wboard.w4e==''\
           and board.s6c+board.s5d=='':
            moves = '7b4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w7b)and Wboard.w3f==''\
           and board.s6c+board.s5d+board.s4e=='':
            moves = '7b3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w7b)and Wboard.w2g==''\
           and board.s6c+board.s5d+board.s4e+board.s3f=='':
            moves = '7b2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w7b)and Wboard.w1h==''\
           and board.s6c+board.s5d+board.s4e+board.s3f+board.s2g=='':
            moves = '7b1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w7b)and Wboard.w9d==''\
           and board.s8c=='':
            moves = '7b9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w8b !='':
        if re.match(r'[plsgrk+]',   Wboard.w8b)and Wboard.w8c=='':
            moves = '8b8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w8b)and Wboard.w7c=='':
            moves = '8b7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w8b)and Wboard.w9c=='':
            moves = '8b9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w8b)and Wboard.w7b=='':
            moves = '8b7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w8b)and Wboard.w9b=='':
            moves = '8b9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w8b)and Wboard.w8a=='':
            moves = '8b8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w8b)and Wboard.w7a=='':
            moves = '8b7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w8b)and Wboard.w9a=='':
            moves = '8b9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w8b)and Wboard.w7d=='':
            moves = '8b7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w8b)and Wboard.w9d=='':
            moves = '8b9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w8b)and Wboard.w8i==''\
           and board.s8h+board.s8g+board.s8f+board.s8e+board.s8d+board.s8c=='':
            moves = '8b8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w8b)and Wboard.w8i==''\
           and board.s8h+board.s8g+board.s8f+board.s8e+board.s8d+board.s8c=='':
            moves = '8b8i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w8b)and Wboard.w8h==''\
           and board.s8g+board.s8f+board.s8e+board.s8d+board.s8c=='':
            moves = '8b8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w8b)and Wboard.w8h==''\
           and board.s8g+board.s8f+board.s8e+board.s8d+board.s8c=='':
            moves = '8b8h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|l',    Wboard.w8b)and Wboard.w8g==''\
           and board.s8f+board.s8e+board.s8d+board.s8c=='':
            moves = '8b8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w8b)and Wboard.w8g==''\
           and board.s8f+board.s8e+board.s8d+board.s8c=='':
            moves = '8b8g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w8b)and Wboard.w8f==''\
           and board.s8e+board.s8d+board.s8c=='':
            moves = '8b8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w8b)and Wboard.w8e==''\
           and board.s8d+board.s8c=='':
            moves = '8b8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w8b)and Wboard.w8d==''\
           and board.s8c=='':
            moves = '8b8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w8b)and Wboard.w6b==''\
           and board.s7b=='':
            moves = '8b6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w8b)and Wboard.w5b==''\
           and board.s7b+board.s6b=='':
            moves = '8b5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w8b)and Wboard.w4b==''\
           and board.s7b+board.s6b+board.s5b=='':
            moves = '8b4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w8b)and Wboard.w3b==''\
           and board.s7b+board.s6b+board.s5b+board.s4b=='':
            moves = '8b3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w8b)and Wboard.w2b==''\
           and board.s7b+board.s6b+board.s5b+board.s4b+board.s3b=='':
            moves = '8b2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w8b)and Wboard.w1b==''\
           and board.s7b+board.s6b+board.s5b+board.s4b+board.s3b+board.s2b=='':
            moves = '8b1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w8b)and Wboard.w3g==''\
           and board.s7c+board.s6d+board.s5e+board.s4f=='':
            moves = '8b3g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w8b)and Wboard.w2h==''\
           and board.s7c+board.s6d+board.s5e+board.s4f+board.s3g=='':
            moves = '8b2h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w8b)and Wboard.w1i==''\
           and board.s7c+board.s6d+board.s5e+board.s4f+board.s3g+board.s2h=='':
            moves = '8b1i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w8b)and Wboard.w6d==''\
           and board.s7c=='':
            moves = '8b6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w8b)and Wboard.w5e==''\
           and board.s7c+board.s6d=='':
            moves = '8b5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w8b)and Wboard.w4f==''\
           and board.s7c+board.s6d+board.s5e=='':
            moves = '8b4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w8b)and Wboard.w3g==''\
           and board.s7c+board.s6d+board.s5e+board.s4f=='':
            moves = '8b3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w8b)and Wboard.w2h==''\
           and board.s7c+board.s6d+board.s5e+board.s4f+board.s3g=='':
            moves = '8b2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w8b)and Wboard.w1i==''\
           and board.s7c+board.s6d+board.s5e+board.s4f+board.s3g+board.s2h=='':
            moves = '8b1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w9b !='':
        if re.match(r'[plsgrk+]',   Wboard.w9b)and Wboard.w9c=='':
            moves = '9b9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w9b)and Wboard.w8c=='':
            moves = '9b8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w9b)and Wboard.w8b=='':
            moves = '9b8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w9b)and Wboard.w9a=='':
            moves = '9b9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|\+b|b|s|k',Wboard.w9b)and Wboard.w8a=='':
            moves = '9b8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w9b)and Wboard.w8d=='':
            moves = '9b8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w9b)and Wboard.w9i==''\
           and board.s9h+board.s9g+board.s9f+board.s9e+board.s9d+board.s9c=='':
            moves = '9b9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w9b)and Wboard.w9i==''\
           and board.s9h+board.s9g+board.s9f+board.s9e+board.s9d+board.s9c=='':
            moves = '9b9i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w9b)and Wboard.w9h==''\
           and board.s9g+board.s9f+board.s9e+board.s9d+board.s9c=='':
            moves = '9b9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w9b)and Wboard.w9h==''\
           and board.s9g+board.s9f+board.s9e+board.s9d+board.s9c=='':
            moves = '9b9h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|l',    Wboard.w9b)and Wboard.w9g==''\
           and board.s9f+board.s9e+board.s9d+board.s9c=='':
            moves = '9b9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w9b)and Wboard.w9g==''\
           and board.s9f+board.s9e+board.s9d+board.s9c=='':
            moves = '9b9g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w9b)and Wboard.w9f==''\
           and board.s9e+board.s9d+board.s9c=='':
            moves = '9b9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w9b)and Wboard.w9e==''\
           and board.s9d+board.s9c=='':
            moves = '9b9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w9b)and Wboard.w9d==''\
           and board.s9c=='':
            moves = '9b9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w9b)and Wboard.w7b==''\
           and board.s8b=='':
            moves = '9b7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w9b)and Wboard.w6b==''\
           and board.s8b+board.s7b=='':
            moves = '9b6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w9b)and Wboard.w5b==''\
           and board.s8b+board.s7b+board.s6b=='':
            moves = '9b5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w9b)and Wboard.w4b==''\
           and board.s8b+board.s7b+board.s6b+board.s5b=='':
            moves = '9b4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w9b)and Wboard.w3b==''\
           and board.s8b+board.s7b+board.s6b+board.s5b+board.s4b=='':
            moves = '9b3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w9b)and Wboard.w2b==''\
           and board.s8b+board.s7b+board.s6b+board.s5b+board.s4b+board.s3b=='':
            moves = '9b2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w9b)and Wboard.w1b==''\
           and board.s8b+board.s7b+board.s6b+board.s5b+board.s4b+board.s3b+board.s2b=='':
            moves = '9b1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w9b)and Wboard.w4g==''\
           and board.s8c+board.s7d+board.s6e+board.s5f=='':
            moves = '9b4g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w9b)and Wboard.w3h==''\
           and board.s8c+board.s7d+board.s6e+board.s5f+board.s4g=='':
            moves = '9b3h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w9b)and Wboard.w2i==''\
           and board.s8c+board.s7d+board.s6e+board.s5f+board.s4g+board.s3h=='':
            moves = '9b2i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w9b)and Wboard.w7d==''\
           and board.s8c=='':
            moves = '9b7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w9b)and Wboard.w6e==''\
           and board.s8c+board.s7d=='':
            moves = '9b6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w9b)and Wboard.w5f==''\
           and board.s8c+board.s7d+board.s6e=='':
            moves = '9b5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w9b)and Wboard.w4g==''\
           and board.s8c+board.s7d+board.s6e+board.s5f=='':
            moves = '9b4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w9b)and Wboard.w3h==''\
           and board.s8c+board.s7d+board.s6e+board.s5f+board.s4g=='':
            moves = '9b3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w9b)and Wboard.w2i==''\
           and board.s8c+board.s7d+board.s6e+board.s5f+board.s4g+board.s3h=='':
            moves = '9b2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w1a !='':
        if re.match(r'[plsgrk+]',   Wboard.w1a)and Wboard.w1b=='':
            moves = '1a1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w1a)and Wboard.w2b=='':
            moves = '1a2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w1a)and Wboard.w2a=='':
            moves = '1a2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w1a)and Wboard.w2c=='':
            moves = '1a2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w1a)and Wboard.w1i==''\
           and board.s1h+board.s1g+board.s1f+board.s1e+board.s1d+board.s1c+board.s1b=='':
            moves = '1a1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w1a)and Wboard.w1i==''\
           and board.s1h+board.s1g+board.s1f+board.s1e+board.s1d+board.s1c+board.s1b=='':
            moves = '1a1i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w1a)and Wboard.w1h==''\
           and board.s1g+board.s1f+board.s1e+board.s1d+board.s1c+board.s1b=='':
            moves = '1a1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w1a)and Wboard.w1h==''\
           and board.s1g+board.s1f+board.s1e+board.s1d+board.s1c+board.s1b=='':
            moves = '1a1h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|l',    Wboard.w1a)and Wboard.w1g==''\
           and board.s1f+board.s1e+board.s1d+board.s1c+board.s1b=='':
            moves = '1a1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w1a)and Wboard.w1g==''\
           and board.s1f+board.s1e+board.s1d+board.s1c+board.s1b=='':
            moves = '1a1g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w1a)and Wboard.w1f==''\
           and board.s1e+board.s1d+board.s1c+board.s1b=='':
            moves = '1a1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w1a)and Wboard.w1e==''\
           and board.s1d+board.s1c+board.s1b=='':
            moves = '1a1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w1a)and Wboard.w1d==''\
           and board.s1c+board.s1b=='':
            moves = '1a1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w1a)and Wboard.w1c==''\
           and board.s1b=='':
            moves = '1a1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w1a)and Wboard.w3a==''\
           and board.s2a=='':
            moves = '1a3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w1a)and Wboard.w4a==''\
           and board.s2a+board.s3a=='':
            moves = '1a4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w1a)and Wboard.w5a==''\
           and board.s2a+board.s3a+board.s4a=='':
            moves = '1a5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w1a)and Wboard.w6a==''\
           and board.s2a+board.s3a+board.s4a+board.s5a=='':
            moves = '1a6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w1a)and Wboard.w7a==''\
           and board.s2a+board.s3a+board.s4a+board.s5a+board.s6a=='':
            moves = '1a7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w1a)and Wboard.w8a==''\
           and board.s2a+board.s3a+board.s4a+board.s5a+board.s6a+board.s7a=='':
            moves = '1a8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w1a)and Wboard.w9a==''\
           and board.s2a+board.s3a+board.s4a+board.s5a+board.s6a+board.s7a+board.s8a=='':
            moves = '1a9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w1a)and Wboard.w7g==''\
           and board.s2b+board.s3c+board.s4d+board.s5e+board.s6f=='':
            moves = '1a7g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w1a)and Wboard.w8h==''\
           and board.s2b+board.s3c+board.s4d+board.s5e+board.s6f+board.s7g=='':
            moves = '1a8h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w1a)and Wboard.w9i==''\
           and board.s2b+board.s3c+board.s4d+board.s5e+board.s6f+board.s7g+board.s8h=='':
            moves = '1a9i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w1a)and Wboard.w3c==''\
           and board.s2b=='':
            moves = '1a3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w1a)and Wboard.w4d==''\
           and board.s2b+board.s3c=='':
            moves = '1a4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w1a)and Wboard.w5e==''\
           and board.s2b+board.s3c+board.s4d=='':
            moves = '1a5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w1a)and Wboard.w6f==''\
           and board.s2b+board.s3c+board.s4d+board.s5e=='':
            moves = '1a6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w1a)and Wboard.w7g==''\
           and board.s2b+board.s3c+board.s4d+board.s5e+board.s6f=='':
            moves = '1a7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w1a)and Wboard.w8h==''\
           and board.s2b+board.s3c+board.s4d+board.s5e+board.s6f+board.s7g=='':
            moves = '1a8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w1a)and Wboard.w9i==''\
           and board.s2b+board.s3c+board.s4d+board.s5e+board.s6f+board.s7g+board.s8h=='':
            moves = '1a9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w2a !='':
        if re.match(r'[plsgrk+]',   Wboard.w2a)and Wboard.w2b=='':
            moves = '2a2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w2a)and Wboard.w1b=='':
            moves = '2a1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w2a)and Wboard.w3b=='':
            moves = '2a3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w2a)and Wboard.w1a=='':
            moves = '2a1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w2a)and Wboard.w3a=='':
            moves = '2a3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w2a)and Wboard.w1c=='':
            moves = '2a1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w2a)and Wboard.w3c=='':
            moves = '2a3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w2a)and Wboard.w2i==''\
           and board.s2h+board.s2g+board.s2f+board.s2e+board.s2d+board.s2c+board.s2b=='':
            moves = '2a2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w2a)and Wboard.w2i==''\
           and board.s2h+board.s2g+board.s2f+board.s2e+board.s2d+board.s2c+board.s2b=='':
            moves = '2a2i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w2a)and Wboard.w2h==''\
           and board.s2g+board.s2f+board.s2e+board.s2d+board.s2c+board.s2b=='':
            moves = '2a2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w2a)and Wboard.w2h==''\
           and board.s2g+board.s2f+board.s2e+board.s2d+board.s2c+board.s2b=='':
            moves = '2a2h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|l',    Wboard.w2a)and Wboard.w2g==''\
           and board.s2f+board.s2e+board.s2d+board.s2c+board.s2b=='':
            moves = '2a2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w2a)and Wboard.w2g==''\
           and board.s2f+board.s2e+board.s2d+board.s2c+board.s2b=='':
            moves = '2a2g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w2a)and Wboard.w2f==''\
           and board.s2e+board.s2d+board.s2c+board.s2b=='':
            moves = '2a2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w2a)and Wboard.w2e==''\
           and board.s2d+board.s2c+board.s2b=='':
            moves = '2a2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w2a)and Wboard.w2d==''\
           and board.s2c+board.s2b=='':
            moves = '2a2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w2a)and Wboard.w2c==''\
           and board.s2b=='':
            moves = '2a2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w2a)and Wboard.w4a==''\
           and board.s3a=='':
            moves = '2a4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w2a)and Wboard.w5a==''\
           and board.s3a+board.s4a=='':
            moves = '2a5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w2a)and Wboard.w6a==''\
           and board.s3a+board.s4a+board.s5a=='':
            moves = '2a6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w2a)and Wboard.w7a==''\
           and board.s3a+board.s4a+board.s5a+board.s6a=='':
            moves = '2a7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w2a)and Wboard.w8a==''\
           and board.s3a+board.s4a+board.s5a+board.s6a+board.s7a=='':
            moves = '2a8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w2a)and Wboard.w9a==''\
           and board.s3a+board.s4a+board.s5a+board.s6a+board.s7a+board.s8a=='':
            moves = '2a9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w2a)and Wboard.w8g==''\
           and board.s3b+board.s4c+board.s5d+board.s6e+board.s7f=='':
            moves = '2a8g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w2a)and Wboard.w9h==''\
           and board.s3b+board.s4c+board.s5d+board.s6e+board.s7f+board.s8g=='':
            moves = '2a9h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w2a)and Wboard.w4c==''\
           and board.s3b=='':
            moves = '2a4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w2a)and Wboard.w5d==''\
           and board.s3b+board.s4c=='':
            moves = '2a5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w2a)and Wboard.w6e==''\
           and board.s3b+board.s4c+board.s5d=='':
            moves = '2a6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w2a)and Wboard.w7f==''\
           and board.s3b+board.s4c+board.s5d+board.s6e=='':
            moves = '2a7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w2a)and Wboard.w8g==''\
           and board.s3b+board.s4c+board.s5d+board.s6e+board.s7f=='':
            moves = '2a8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w2a)and Wboard.w9h==''\
           and board.s3b+board.s4c+board.s5d+board.s6e+board.s7f+board.s8g=='':
            moves = '2a9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w3a !='':
        if re.match(r'[plsgrk+]',   Wboard.w3a)and Wboard.w3b=='':
            moves = '3a3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w3a)and Wboard.w2b=='':
            moves = '3a2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w3a)and Wboard.w4b=='':
            moves = '3a4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w3a)and Wboard.w2a=='':
            moves = '3a2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w3a)and Wboard.w4a=='':
            moves = '3a4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w3a)and Wboard.w2c=='':
            moves = '3a2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w3a)and Wboard.w4c=='':
            moves = '3a4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w3a)and Wboard.w3i==''\
           and board.s3h+board.s3g+board.s3f+board.s3e+board.s3d+board.s3c+board.s3b=='':
            moves = '3a3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w3a)and Wboard.w3i==''\
           and board.s3h+board.s3g+board.s3f+board.s3e+board.s3d+board.s3c+board.s3b=='':
            moves = '3a3i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w3a)and Wboard.w3h==''\
           and board.s3g+board.s3f+board.s3e+board.s3d+board.s3c+board.s3b=='':
            moves = '3a3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w3a)and Wboard.w3h==''\
           and board.s3g+board.s3f+board.s3e+board.s3d+board.s3c+board.s3b=='':
            moves = '3a3h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|l',    Wboard.w3a)and Wboard.w3g==''\
           and board.s3f+board.s3e+board.s3d+board.s3c+board.s3b=='':
            moves = '3a3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w3a)and Wboard.w3g==''\
           and board.s3f+board.s3e+board.s3d+board.s3c+board.s3b=='':
            moves = '3a3g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w3a)and Wboard.w3f==''\
           and board.s3e+board.s3d+board.s3c+board.s3b=='':
            moves = '3a3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w3a)and Wboard.w3e==''\
           and board.s3d+board.s3c+board.s3b=='':
            moves = '3a3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w3a)and Wboard.w3d==''\
           and board.s3c+board.s3b=='':
            moves = '3a3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w3a)and Wboard.w3c==''\
           and board.s3b=='':
            moves = '3a3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w3a)and Wboard.w1a==''\
           and board.s2a=='':
            moves = '3a1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w3a)and Wboard.w5a==''\
           and board.s4a=='':
            moves = '3a5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w3a)and Wboard.w6a==''\
           and board.s4a+board.s5a=='':
            moves = '3a6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w3a)and Wboard.w7a==''\
           and board.s4a+board.s5a+board.s6a=='':
            moves = '3a7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w3a)and Wboard.w8a==''\
           and board.s4a+board.s5a+board.s6a+board.s7a=='':
            moves = '3a8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w3a)and Wboard.w9a==''\
           and board.s4a+board.s5a+board.s6a+board.s7a+board.s8a=='':
            moves = '3a9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w3a)and Wboard.w9g==''\
           and board.s4b+board.s5c+board.s6d+board.s7e+board.s8f=='':
            moves = '3a9g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w3a)and Wboard.w1c==''\
           and board.s2b=='':
            moves = '3a1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w3a)and Wboard.w5c==''\
           and board.s4b=='':
            moves = '3a5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w3a)and Wboard.w6d==''\
           and board.s4b+board.s5c=='':
            moves = '3a6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w3a)and Wboard.w6e==''\
           and board.s4b+board.s5c+board.s6d=='':
            moves = '3a7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w3a)and Wboard.w7f==''\
           and board.s4b+board.s5c+board.s6d+board.s7e=='':
            moves = '3a8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w3a)and Wboard.w9g==''\
           and board.s4b+board.s5c+board.s6d+board.s7e+board.s8f=='':
            moves = '3a9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w4a !='':
        if re.match(r'[plsgrk+]',   Wboard.w4a)and Wboard.w4b=='':
            moves = '4a4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w4a)and Wboard.w3b=='':
            moves = '4a3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w4a)and Wboard.w5b=='':
            moves = '4a5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w4a)and Wboard.w3a=='':
            moves = '4a3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w4a)and Wboard.w5a=='':
            moves = '4a5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w4a)and Wboard.w3c=='':
            moves = '4a3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w4a)and Wboard.w5c=='':
            moves = '4a5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w4a)and Wboard.w4i==''\
           and board.s4h+board.s4g+board.s4f+board.s4e+board.s4d+board.s4c+board.s4b=='':
            moves = '4a4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w4a)and Wboard.w4i==''\
           and board.s4h+board.s4g+board.s4f+board.s4e+board.s4d+board.s4c+board.s4b=='':
            moves = '4a4i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w4a)and Wboard.w4h==''\
           and board.s4g+board.s4f+board.s4e+board.s4d+board.s4c+board.s4b=='':
            moves = '4a4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w4a)and Wboard.w4h==''\
           and board.s4g+board.s4f+board.s4e+board.s4d+board.s4c+board.s4b=='':
            moves = '4a4h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|l',    Wboard.w4a)and Wboard.w4g==''\
           and board.s4f+board.s4e+board.s4d+board.s4c+board.s4b=='':
            moves = '4a4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w4a)and Wboard.w4g==''\
           and board.s4f+board.s4e+board.s4d+board.s4c+board.s4b=='':
            moves = '4a4g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w4a)and Wboard.w4f==''\
           and board.s4e+board.s4d+board.s4c+board.s4b=='':
            moves = '4a4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w4a)and Wboard.w4e==''\
           and board.s4d+board.s4c+board.s4b=='':
            moves = '4a4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w4a)and Wboard.w4d==''\
           and board.s4c+board.s4b=='':
            moves = '4a4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w4a)and Wboard.w4c==''\
           and board.s4b=='':
            moves = '4a4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w4a)and Wboard.w1a==''\
           and board.s2a+board.s3a=='':
            moves = '4a1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w4a)and Wboard.w2a==''\
           and board.s3a=='':
            moves = '4a2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w4a)and Wboard.w6a==''\
           and board.s5a=='':
            moves = '4a6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w4a)and Wboard.w7a==''\
           and board.s5a+board.s6a=='':
            moves = '4a7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w4a)and Wboard.w8a==''\
           and board.s5a+board.s6a+board.s7a=='':
            moves = '4a8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w4a)and Wboard.w9a==''\
           and board.s5a+board.s6a+board.s7a+board.s8a=='':
            moves = '4a9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w4a)and Wboard.w6c==''\
           and board.s5b=='':
            moves = '4a6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w4a)and Wboard.w7d==''\
           and board.s5b+board.s6c=='':
            moves = '4a7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w4a)and Wboard.w8e==''\
           and board.s5b+board.s6c+board.s7d=='':
            moves = '4a8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w4a)and Wboard.w9f==''\
           and board.s5b+board.s6c+board.s7d+board.s8e=='':
            moves = '4a9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w4a)and Wboard.w1d==''\
           and board.s2c+board.s3b=='':
            moves = '4a1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w4a)and Wboard.w2c==''\
           and board.s3b=='':
            moves = '4a2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w5a !='':
        if re.match(r'[plsgrk+]',   Wboard.w5a)and Wboard.w5b=='':
            moves = '5a5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w5a)and Wboard.w4b=='':
            moves = '5a4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w5a)and Wboard.w6b=='':
            moves = '5a6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w5a)and Wboard.w4a=='':
            moves = '5a4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w5a)and Wboard.w6a=='':
            moves = '5a6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w5a)and Wboard.w4c=='':
            moves = '5a4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w5a)and Wboard.w6c=='':
            moves = '5a6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w5a)and Wboard.w5i==''\
           and board.s5h+board.s5g+board.s5f+board.s5e+board.s5d+board.s5c+board.s5b=='':
            moves = '5a5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w5a)and Wboard.w5i==''\
           and board.s5h+board.s5g+board.s5f+board.s5e+board.s5d+board.s5c+board.s5b=='':
            moves = '5a5i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w5a)and Wboard.w5h==''\
           and board.s5g+board.s5f+board.s5e+board.s5d+board.s5c+board.s5b=='':
            moves = '5a5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w5a)and Wboard.w5h==''\
           and board.s5g+board.s5f+board.s5e+board.s5d+board.s5c+board.s5b=='':
            moves = '5a5h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|l',    Wboard.w5a)and Wboard.w5g==''\
           and board.s5f+board.s5e+board.s5d+board.s5c+board.s5b=='':
            moves = '5a5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w5a)and Wboard.w5g==''\
           and board.s5f+board.s5e+board.s5d+board.s5c+board.s5b=='':
            moves = '5a5g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w5a)and Wboard.w5f==''\
           and board.s5e+board.s5d+board.s5c+board.s5b=='':
            moves = '5a5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w5a)and Wboard.w5e==''\
           and board.s5d+board.s5c+board.s5b=='':
            moves = '5a5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w5a)and Wboard.w5d==''\
           and board.s5c+board.s5b=='':
            moves = '5a5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w5a)and Wboard.w5c==''\
           and board.s5b=='':
            moves = '5a5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w5a)and Wboard.w1a==''\
           and board.s2a+board.s3a+board.s4a=='':
            moves = '5a1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w5a)and Wboard.w2a==''\
           and board.s3a+board.s4a=='':
            moves = '5a2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w5a)and Wboard.w3a==''\
           and board.s4a=='':
            moves = '5a3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w5a)and Wboard.w7a==''\
           and board.s6a=='':
            moves = '5a7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w5a)and Wboard.w8a==''\
           and board.s6a+board.s7a=='':
            moves = '5a8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w5a)and Wboard.w9a==''\
           and board.s6a+board.s7a+board.s8a=='':
            moves = '5a9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w5a)and Wboard.w7c==''\
           and board.s6b=='':
            moves = '5a7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w5a)and Wboard.w8d==''\
           and board.s6b+board.s7c=='':
            moves = '5a8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w5a)and Wboard.w9e==''\
           and board.s6b+board.s7c+board.s8d=='':
            moves = '5a9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w5a)and Wboard.w2d==''\
           and board.s3c+board.s4b=='':
            moves = '5a2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w5a)and Wboard.w3c==''\
           and board.s4b=='':
            moves = '5a3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w5a)and Wboard.w1e==''\
           and board.s4b+board.s3c+board.s2d=='':
            moves = '5a1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w6a !='':
        if re.match(r'[plsgrk+]',   Wboard.w6a)and Wboard.w6b=='':
            moves = '6a6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w6a)and Wboard.w5b=='':
            moves = '6a5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w6a)and Wboard.w7b=='':
            moves = '6a7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w6a)and Wboard.w5a=='':
            moves = '6a5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w6a)and Wboard.w7a=='':
            moves = '6a7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w6a)and Wboard.w5c=='':
            moves = '6a5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w6a)and Wboard.w7c=='':
            moves = '6a7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w6a)and Wboard.w6i==''\
           and board.s6h+board.s6g+board.s6f+board.s6e+board.s6d+board.s6c+board.s6b=='':
            moves = '6a6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w6a)and Wboard.w6i==''\
           and board.s6h+board.s6g+board.s6f+board.s6e+board.s6d+board.s6c+board.s6b=='':
            moves = '6a6i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w6a)and Wboard.w6h==''\
           and board.s6g+board.s6f+board.s6e+board.s6d+board.s6c+board.s6b=='':
            moves = '6a6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w6a)and Wboard.w6h==''\
           and board.s6g+board.s6f+board.s6e+board.s6d+board.s6c+board.s6b=='':
            moves = '6a6h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|l',    Wboard.w6a)and Wboard.w6g==''\
           and board.s6f+board.s6e+board.s6d+board.s6c+board.s6b=='':
            moves = '6a6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w6a)and Wboard.w6g==''\
           and board.s6f+board.s6e+board.s6d+board.s6c+board.s6b=='':
            moves = '6a6g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w6a)and Wboard.w6f==''\
           and board.s6e+board.s6d+board.s6c+board.s6b=='':
            moves = '6a6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w6a)and Wboard.w6e==''\
           and board.s6d+board.s6c+board.s6b=='':
            moves = '6a6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w6a)and Wboard.w6d==''\
           and board.s6c+board.s6b=='':
            moves = '6a6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w6a)and Wboard.w6c==''\
           and board.s6b=='':
            moves = '6a6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w6a)and Wboard.w9a==''\
           and board.s8a+board.s7a=='':
            moves = '6a9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w6a)and Wboard.w8a==''\
           and board.s7a=='':
            moves = '6a8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w6a)and Wboard.w4a==''\
           and board.s5a=='':
            moves = '6a4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w6a)and Wboard.w3a==''\
           and board.s5a+board.s4a=='':
            moves = '6a3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w6a)and Wboard.w2a==''\
           and board.s5a+board.s4a+board.s3a=='':
            moves = '6a2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w6a)and Wboard.w1a==''\
           and board.s5a+board.s4a+board.s3a+board.s2a=='':
            moves = '6a1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w6a)and Wboard.w4c==''\
           and board.s5b=='':
            moves = '6a4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w6a)and Wboard.w3d==''\
           and board.s5b+board.s4c=='':
            moves = '6a3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w6a)and Wboard.w2e==''\
           and board.s5b+board.s4c+board.s3d=='':
            moves = '6a2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w6a)and Wboard.w1f==''\
           and board.s5b+board.s4c+board.s3d+board.s2e=='':
            moves = '6a1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w6a)and Wboard.w9d==''\
           and board.s8c+board.s7b=='':
            moves = '6a9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w6a)and Wboard.w8c==''\
           and board.s7b=='':
            moves = '6a8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w7a !='':
        if re.match(r'[plsgrk+]',   Wboard.w7a)and Wboard.w7b=='':
            moves = '7a7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w7a)and Wboard.w6b=='':
            moves = '7a6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w7a)and Wboard.w8b=='':
            moves = '7a8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w7a)and Wboard.w6a=='':
            moves = '7a6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w7a)and Wboard.w8a=='':
            moves = '7a8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w7a)and Wboard.w6c=='':
            moves = '7a6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w7a)and Wboard.w8c=='':
            moves = '7a8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w7a)and Wboard.w7i==''\
           and board.s7h+board.s7g+board.s7f+board.s7e+board.s7d+board.s7c+board.s7b=='':
            moves = '7a7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w7a)and Wboard.w7i==''\
           and board.s7h+board.s7g+board.s7f+board.s7e+board.s7d+board.s7c+board.s7b=='':
            moves = '7a7i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w7a)and Wboard.w7h==''\
           and board.s7g+board.s7f+board.s7e+board.s7d+board.s7c+board.s7b=='':
            moves = '7a7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w7a)and Wboard.w7h==''\
           and board.s7g+board.s7f+board.s7e+board.s7d+board.s7c+board.s7b=='':
            moves = '7a7h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|l',    Wboard.w7a)and Wboard.w7g==''\
           and board.s7f+board.s7e+board.s7d+board.s7c+board.s7b=='':
            moves = '7a7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w7a)and Wboard.w7g==''\
           and board.s7f+board.s7e+board.s7d+board.s7c+board.s7b=='':
            moves = '7a7g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w7a)and Wboard.w7f==''\
           and board.s7e+board.s7d+board.s7c+board.s7b=='':
            moves = '7a7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w7a)and Wboard.w7e==''\
           and board.s7d+board.s7c+board.s7b=='':
            moves = '7a7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w7a)and Wboard.w7d==''\
           and board.s7c+board.s7b=='':
            moves = '7a7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w7a)and Wboard.w7c==''\
           and board.s7b=='':
            moves = '7a7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w7a)and Wboard.w9a==''\
           and board.s8a=='':
            moves = '7a9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w7a)and Wboard.w5a==''\
           and board.s6a=='':
            moves = '7a5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w7a)and Wboard.w4a==''\
           and board.s6a+board.s5a=='':
            moves = '7a4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w7a)and Wboard.w3a==''\
           and board.s6a+board.s5a+board.s4a=='':
            moves = '7a3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w7a)and Wboard.w2a==''\
           and board.s6a+board.s5a+board.s4a+board.s3a=='':
            moves = '7a2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w7a)and Wboard.w1a==''\
           and board.s6a+board.s5a+board.s4a+board.s3a+board.s2a=='':
            moves = '7a1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w7a)and Wboard.w1g==''\
           and board.s6b+board.s5c+board.s4d+board.s3e+board.s2f=='':
            moves = '7a1g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w7a)and Wboard.w9c==''\
           and board.s8b=='':
            moves = '7a9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w7a)and Wboard.w5c==''\
           and board.s6b=='':
            moves = '7a5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w7a)and Wboard.w4d==''\
           and board.s6b+board.s5c=='':
            moves = '7a4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w7a)and Wboard.w4e==''\
           and board.s6b+board.s5c+board.s4d=='':
            moves = '7a3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w7a)and Wboard.w3f==''\
           and board.s6b+board.s5c+board.s4d+board.s3e=='':
            moves = '7a2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w7a)and Wboard.w1g==''\
           and board.s6b+board.s5c+board.s4d+board.s3e+board.s2f=='':
            moves = '7a1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w8a !='':
        if re.match(r'[plsgrk+]',   Wboard.w8a)and Wboard.w8b=='':
            moves = '8a8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w8a)and Wboard.w7b=='':
            moves = '8a7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w8a)and Wboard.w9b=='':
            moves = '8a9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w8a)and Wboard.w7a=='':
            moves = '8a7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w8a)and Wboard.w9a=='':
            moves = '8a9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w8a)and Wboard.w7c=='':
            moves = '8a7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w8a)and Wboard.w9c=='':
            moves = '8a9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w8a)and Wboard.w8i==''\
           and board.s8h+board.s8g+board.s8f+board.s8e+board.s8d+board.s8c+board.s8b=='':
            moves = '8a8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w8a)and Wboard.w8i==''\
           and board.s8h+board.s8g+board.s8f+board.s8e+board.s8d+board.s8c+board.s8b=='':
            moves = '8a8i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w8a)and Wboard.w8h==''\
           and board.s8g+board.s8f+board.s8e+board.s8d+board.s8c+board.s8b=='':
            moves = '8a8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w8a)and Wboard.w8h==''\
           and board.s8g+board.s8f+board.s8e+board.s8d+board.s8c+board.s8b=='':
            moves = '8a8h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|l',    Wboard.w8a)and Wboard.w8g==''\
           and board.s8f+board.s8e+board.s8d+board.s8c+board.s8b=='':
            moves = '8a8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w8a)and Wboard.w8g==''\
           and board.s8f+board.s8e+board.s8d+board.s8c+board.s8b=='':
            moves = '8a8g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w8a)and Wboard.w8f==''\
           and board.s8e+board.s8d+board.s8c+board.s8b=='':
            moves = '8a8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w8a)and Wboard.w8e==''\
           and board.s8d+board.s8c+board.s8b=='':
            moves = '8a8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w8a)and Wboard.w8d==''\
           and board.s8c+board.s8b=='':
            moves = '8a8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w8a)and Wboard.w8c==''\
           and board.s8b=='':
            moves = '8a8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w8a)and Wboard.w6a==''\
           and board.s7a=='':
            moves = '8a6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w8a)and Wboard.w5a==''\
           and board.s7a+board.s6a=='':
            moves = '8a5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w8a)and Wboard.w4a==''\
           and board.s7a+board.s6a+board.s5a=='':
            moves = '8a4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w8a)and Wboard.w3a==''\
           and board.s7a+board.s6a+board.s5a+board.s4a=='':
            moves = '8a3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w8a)and Wboard.w2a==''\
           and board.s7a+board.s6a+board.s5a+board.s4a+board.s3a=='':
            moves = '8a2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w8a)and Wboard.w1a==''\
           and board.s7a+board.s6a+board.s5a+board.s4a+board.s3a+board.s2a=='':
            moves = '8a1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w8a)and Wboard.w2g==''\
           and board.s7b+board.s6c+board.s5d+board.s4e+board.s3f=='':
            moves = '8a2g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w8a)and Wboard.w1h==''\
           and board.s7b+board.s6c+board.s5d+board.s4e+board.s3f+board.s2g=='':
            moves = '8a1h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w8a)and Wboard.w6c==''\
           and board.s7b=='':
            moves = '8a6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w8a)and Wboard.w5d==''\
           and board.s7b+board.s6c=='':
            moves = '8a5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w8a)and Wboard.w4e==''\
           and board.s7b+board.s6c+board.s5d=='':
            moves = '8a4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w8a)and Wboard.w3f==''\
           and board.s7b+board.s6c+board.s5d+board.s4e=='':
            moves = '8a3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w8a)and Wboard.w2g==''\
           and board.s7b+board.s6c+board.s5d+board.s4e+board.s3f=='':
            moves = '8a2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w8a)and Wboard.w1h==''\
           and board.s7b+board.s6c+board.s5d+board.s4e+board.s3f+board.s2g=='':
            moves = '8a1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Wboard.w9a !='':
        if re.match(r'[plsgrk+]',   Wboard.w9a)and Wboard.w9b=='':
            moves = '9a9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[sgbk+]',    Wboard.w9a)and Wboard.w8b=='':
            moves = '9a8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[grk+]',     Wboard.w9a)and Wboard.w8a=='':
            moves = '9a8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('n',         Wboard.w9a)and Wboard.w8c=='':
            moves = '9a8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w9a)and Wboard.w9i==''\
           and board.s9h+board.s9g+board.s9f+board.s9e+board.s9d+board.s9c+board.s9b=='':
            moves = '9a9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w9a)and Wboard.w9i==''\
           and board.s9h+board.s9g+board.s9f+board.s9e+board.s9d+board.s9c+board.s9b=='':
            moves = '9a9i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+r',        Wboard.w9a)and Wboard.w9h==''\
           and board.s9g+board.s9f+board.s9e+board.s9d+board.s9c+board.s9b=='':
            moves = '9a9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w9a)and Wboard.w9h==''\
           and board.s9g+board.s9f+board.s9e+board.s9d+board.s9c+board.s9b=='':
            moves = '9a9h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|l',    Wboard.w9a)and Wboard.w9g==''\
           and board.s9f+board.s9e+board.s9d+board.s9c+board.s9b=='':
            moves = '9a9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'r|l',      Wboard.w9a)and Wboard.w9g==''\
           and board.s9f+board.s9e+board.s9d+board.s9c+board.s9b=='':
            moves = '9a9g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w9a)and Wboard.w9f==''\
           and board.s9e+board.s9d+board.s9c+board.s9b=='':
            moves = '9a9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w9a)and Wboard.w9e==''\
           and board.s9d+board.s9c+board.s9b=='':
            moves = '9a9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w9a)and Wboard.w9d==''\
           and board.s9c+board.s9b=='':
            moves = '9a9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r|l',   Wboard.w9a)and Wboard.w9c==''\
           and board.s9b=='':
            moves = '9a9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w9a)and Wboard.w7a==''\
           and board.s8a=='':
            moves = '9a7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w9a)and Wboard.w6a==''\
           and board.s8a+board.s7a=='':
            moves = '9a6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w9a)and Wboard.w5a==''\
           and board.s8a+board.s7a+board.s6a=='':
            moves = '9a5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',   Wboard.w9a)and Wboard.w4a==''\
           and board.s8a+board.s7a+board.s6a+board.s5a=='':
            moves = '9a4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w9a)and Wboard.w3a==''\
           and board.s8a+board.s7a+board.s6a+board.s5a+board.s4a=='':
            moves = '9a3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w9a)and Wboard.w2a==''\
           and board.s8a+board.s7a+board.s6a+board.s5a+board.s4a+board.s3a=='':
            moves = '9a2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+r|r',      Wboard.w9a)and Wboard.w1a==''\
           and board.s8a+board.s7a+board.s6a+board.s5a+board.s4a+board.s3a+board.s2a=='':
            moves = '9a1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w9a)and Wboard.w3g==''\
           and board.s8b+board.s7c+board.s6d+board.s5e+board.s4f=='':
            moves = '9a3g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w9a)and Wboard.w2h==''\
           and board.s8b+board.s7c+board.s6d+board.s5e+board.s4f+board.s3g=='':
            moves = '9a2h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('b',Wboard.w9a)and Wboard.w1i==''\
           and board.s8b+board.s7c+board.s6d+board.s5e+board.s4f+board.s3g+board.s2h=='':
            moves = '9a1i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w9a)and Wboard.w7c==''\
           and board.s8b=='':
            moves = '9a7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w9a)and Wboard.w6d==''\
           and board.s8b+board.s7c=='':
            moves = '9a6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w9a)and Wboard.w5e==''\
           and board.s8b+board.s7c+board.s6d=='':
            moves = '9a5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+b|b',   Wboard.w9a)and Wboard.w4f==''\
           and board.s8b+board.s7c+board.s6d+board.s5e=='':
            moves = '9a4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w9a)and Wboard.w3g==''\
           and board.s8b+board.s7c+board.s6d+board.s5e+board.s4f=='':
            moves = '9a3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w9a)and Wboard.w2h==''\
           and board.s8b+board.s7c+board.s6d+board.s5e+board.s4f+board.s3g=='':
            moves = '9a2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+b',   Wboard.w9a)and Wboard.w1i==''\
           and board.s8b+board.s7c+board.s6d+board.s5e+board.s4f+board.s3g+board.s2h=='':
            moves = '9a1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s1i =='':
        if Wboard.s>0:
            moves = 'S*1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s1h =='':
        if Wboard.p>0 and (Wboard.w1h !='p' and Wboard.w1g !='p' and Wboard.w1f !='p' and Wboard.w1e !='p' and Wboard.w1d !='p' and Wboard.w1c !='p' and Wboard.w1b !='p' and Wboard.w1a !='p'):
            moves = 'P*1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s1g =='':
        if Wboard.p>0 and (Wboard.w1h !='p' and Wboard.w1g !='p' and Wboard.w1f !='p' and Wboard.w1e !='p' and Wboard.w1d !='p' and Wboard.w1c !='p' and Wboard.w1b !='p' and Wboard.w1a !='p'):
            moves = 'P*1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s1f =='':
        if Wboard.p>0 and (Wboard.w1h !='p' and Wboard.w1g !='p' and Wboard.w1f !='p' and Wboard.w1e !='p' and Wboard.w1d !='p' and Wboard.w1c !='p' and Wboard.w1b !='p' and Wboard.w1a !='p'):
            moves = 'P*1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s1e =='':
        if Wboard.p>0 and (Wboard.w1h !='p' and Wboard.w1g !='p' and Wboard.w1f !='p' and Wboard.w1e !='p' and Wboard.w1d !='p' and Wboard.w1c !='p' and Wboard.w1b !='p' and Wboard.w1a !='p'):
            moves = 'P*1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s1d =='':
        if Wboard.p>0 and (Wboard.w1h !='p' and Wboard.w1g !='p' and Wboard.w1f !='p' and Wboard.w1e !='p' and Wboard.w1d !='p' and Wboard.w1c !='p' and Wboard.w1b !='p' and Wboard.w1a !='p'):
            moves = 'P*1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s1c =='':
        if Wboard.p>0 and (Wboard.w1h !='p' and Wboard.w1g !='p' and Wboard.w1f !='p' and Wboard.w1e !='p' and Wboard.w1d !='p' and Wboard.w1c !='p' and Wboard.w1b !='p' and Wboard.w1a !='p'):
            moves = 'P*1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s1b =='':
        if Wboard.p>0 and (Wboard.w1h !='p' and Wboard.w1g !='p' and Wboard.w1f !='p' and Wboard.w1e !='p' and Wboard.w1d !='p' and Wboard.w1c !='p' and Wboard.w1b !='p' and Wboard.w1a !='p'):
            moves = 'P*1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s1a =='':
        if Wboard.p>0 and (Wboard.w1h !='p' and Wboard.w1g !='p' and Wboard.w1f !='p' and Wboard.w1e !='p' and Wboard.w1d !='p' and Wboard.w1c !='p' and Wboard.w1b !='p' and Wboard.w1a !='p'):
            moves = 'P*1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s2i =='':
        if Wboard.s>0:
            moves = 'S*2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s2h =='':
        if Wboard.p>0 and (Wboard.w2h !='p' and Wboard.w2g !='p' and Wboard.w2f !='p' and Wboard.w2e !='p' and Wboard.w2d !='p' and Wboard.w2c !='p' and Wboard.w2b !='p' and Wboard.w2a !='p'):
            moves = 'P*2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s2g =='':
        if Wboard.p>0 and (Wboard.w2h !='p' and Wboard.w2g !='p' and Wboard.w2f !='p' and Wboard.w2e !='p' and Wboard.w2d !='p' and Wboard.w2c !='p' and Wboard.w2b !='p' and Wboard.w2a !='p'):
            moves = 'P*2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s2f =='':
        if Wboard.p>0 and (Wboard.w2h !='p' and Wboard.w2g !='p' and Wboard.w2f !='p' and Wboard.w2e !='p' and Wboard.w2d !='p' and Wboard.w2c !='p' and Wboard.w2b !='p' and Wboard.w2a !='p'):
            moves = 'P*2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s2e =='':
        if Wboard.p>0 and (Wboard.w2h !='p' and Wboard.w2g !='p' and Wboard.w2f !='p' and Wboard.w2e !='p' and Wboard.w2d !='p' and Wboard.w2c !='p' and Wboard.w2b !='p' and Wboard.w2a !='p'):
            moves = 'P*2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s2d =='':
        if Wboard.p>0 and (Wboard.w2h !='p' and Wboard.w2g !='p' and Wboard.w2f !='p' and Wboard.w2e !='p' and Wboard.w2d !='p' and Wboard.w2c !='p' and Wboard.w2b !='p' and Wboard.w2a !='p'):
            moves = 'P*2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s2c =='':
        if Wboard.p>0 and (Wboard.w2h !='p' and Wboard.w2g !='p' and Wboard.w2f !='p' and Wboard.w2e !='p' and Wboard.w2d !='p' and Wboard.w2c !='p' and Wboard.w2b !='p' and Wboard.w2a !='p'):
            moves = 'P*2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s2b =='':
        if Wboard.p>0 and (Wboard.w2h !='p' and Wboard.w2g !='p' and Wboard.w2f !='p' and Wboard.w2e !='p' and Wboard.w2d !='p' and Wboard.w2c !='p' and Wboard.w2b !='p' and Wboard.w2a !='p'):
            moves = 'P*2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s2a =='':
        if Wboard.p>0 and (Wboard.w2h !='p' and Wboard.w2g !='p' and Wboard.w2f !='p' and Wboard.w2e !='p' and Wboard.w2d !='p' and Wboard.w2c !='p' and Wboard.w2b !='p' and Wboard.w2a !='p'):
            moves = 'P*2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s3i =='':
        if Wboard.s>0:
            moves = 'S*3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s3h =='':
        if Wboard.p>0 and (Wboard.w3h !='p' and Wboard.w3g !='p' and Wboard.w3f !='p' and Wboard.w3e !='p' and Wboard.w3d !='p' and Wboard.w3c !='p' and Wboard.w3b !='p' and Wboard.w3a !='p'):
            moves = 'P*3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s3g =='':
        if Wboard.p>0 and (Wboard.w3h !='p' and Wboard.w3g !='p' and Wboard.w3f !='p' and Wboard.w3e !='p' and Wboard.w3d !='p' and Wboard.w3c !='p' and Wboard.w3b !='p' and Wboard.w3a !='p'):
            moves = 'P*3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s3f =='':
        if Wboard.p>0 and (Wboard.w3h !='p' and Wboard.w3g !='p' and Wboard.w3f !='p' and Wboard.w3e !='p' and Wboard.w3d !='p' and Wboard.w3c !='p' and Wboard.w3b !='p' and Wboard.w3a !='p'):
            moves = 'P*3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s3e =='':
        if Wboard.p>0 and (Wboard.w3h !='p' and Wboard.w3g !='p' and Wboard.w3f !='p' and Wboard.w3e !='p' and Wboard.w3d !='p' and Wboard.w3c !='p' and Wboard.w3b !='p' and Wboard.w3a !='p'):
            moves = 'P*3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s3d =='':
        if Wboard.p>0 and (Wboard.w3h !='p' and Wboard.w3g !='p' and Wboard.w3f !='p' and Wboard.w3e !='p' and Wboard.w3d !='p' and Wboard.w3c !='p' and Wboard.w3b !='p' and Wboard.w3a !='p'):
            moves = 'P*3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s3c =='':
        if Wboard.p>0 and (Wboard.w3h !='p' and Wboard.w3g !='p' and Wboard.w3f !='p' and Wboard.w3e !='p' and Wboard.w3d !='p' and Wboard.w3c !='p' and Wboard.w3b !='p' and Wboard.w3a !='p'):
            moves = 'P*3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s3b =='':
        if Wboard.p>0 and (Wboard.w3h !='p' and Wboard.w3g !='p' and Wboard.w3f !='p' and Wboard.w3e !='p' and Wboard.w3d !='p' and Wboard.w3c !='p' and Wboard.w3b !='p' and Wboard.w3a !='p'):
            moves = 'P*3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s3a =='':
        if Wboard.p>0 and (Wboard.w3h !='p' and Wboard.w3g !='p' and Wboard.w3f !='p' and Wboard.w3e !='p' and Wboard.w3d !='p' and Wboard.w3c !='p' and Wboard.w3b !='p' and Wboard.w3a !='p'):
            moves = 'P*3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s4i =='':
        if Wboard.s>0:
            moves = 'S*4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s4h =='':
        if Wboard.p>0 and (Wboard.w4h !='p' and Wboard.w4g !='p' and Wboard.w4f !='p' and Wboard.w4e !='p' and Wboard.w4d !='p' and Wboard.w4c !='p' and Wboard.w4b !='p' and Wboard.w4a !='p'):
            moves = 'P*4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s4g =='':
        if Wboard.p>0 and (Wboard.w4h !='p' and Wboard.w4g !='p' and Wboard.w4f !='p' and Wboard.w4e !='p' and Wboard.w4d !='p' and Wboard.w4c !='p' and Wboard.w4b !='p' and Wboard.w4a !='p'):
            moves = 'P*4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s4f =='':
        if Wboard.p>0 and (Wboard.w4h !='p' and Wboard.w4g !='p' and Wboard.w4f !='p' and Wboard.w4e !='p' and Wboard.w4d !='p' and Wboard.w4c !='p' and Wboard.w4b !='p' and Wboard.w4a !='p'):
            moves = 'P*4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s4e =='':
        if Wboard.p>0 and (Wboard.w4h !='p' and Wboard.w4g !='p' and Wboard.w4f !='p' and Wboard.w4e !='p' and Wboard.w4d !='p' and Wboard.w4c !='p' and Wboard.w4b !='p' and Wboard.w4a !='p'):
            moves = 'P*4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s4d =='':
        if Wboard.p>0 and (Wboard.w4h !='p' and Wboard.w4g !='p' and Wboard.w4f !='p' and Wboard.w4e !='p' and Wboard.w4d !='p' and Wboard.w4c !='p' and Wboard.w4b !='p' and Wboard.w4a !='p'):
            moves = 'P*4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s4c =='':
        if Wboard.p>0 and (Wboard.w4h !='p' and Wboard.w4g !='p' and Wboard.w4f !='p' and Wboard.w4e !='p' and Wboard.w4d !='p' and Wboard.w4c !='p' and Wboard.w4b !='p' and Wboard.w4a !='p'):
            moves = 'P*4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s4b =='':
        if Wboard.p>0 and (Wboard.w4h !='p' and Wboard.w4g !='p' and Wboard.w4f !='p' and Wboard.w4e !='p' and Wboard.w4d !='p' and Wboard.w4c !='p' and Wboard.w4b !='p' and Wboard.w4a !='p'):
            moves = 'P*4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s4a =='':
        if Wboard.p>0 and (Wboard.w4h !='p' and Wboard.w4g !='p' and Wboard.w4f !='p' and Wboard.w4e !='p' and Wboard.w4d !='p' and Wboard.w4c !='p' and Wboard.w4b !='p' and Wboard.w4a !='p'):
            moves = 'P*4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s9i =='':
        if Wboard.s>0:
            moves = 'S*9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s9h =='':
        if Wboard.p>0 and (Wboard.w9h !='p' and Wboard.w9g !='p' and Wboard.w9f !='p' and Wboard.w9e !='p' and Wboard.w9d !='p' and Wboard.w9c !='p' and Wboard.w9b !='p' and Wboard.w9a !='p'):
            moves = 'P*9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s9g =='':
        if Wboard.p>0 and (Wboard.w9h !='p' and Wboard.w9g !='p' and Wboard.w9f !='p' and Wboard.w9e !='p' and Wboard.w9d !='p' and Wboard.w9c !='p' and Wboard.w9b !='p' and Wboard.w9a !='p'):
            moves = 'P*9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s9f =='':
        if Wboard.p>0 and (Wboard.w9h !='p' and Wboard.w9g !='p' and Wboard.w9f !='p' and Wboard.w9e !='p' and Wboard.w9d !='p' and Wboard.w9c !='p' and Wboard.w9b !='p' and Wboard.w9a !='p'):
            moves = 'P*9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s9e =='':
        if Wboard.p>0 and (Wboard.w9h !='p' and Wboard.w9g !='p' and Wboard.w9f !='p' and Wboard.w9e !='p' and Wboard.w9d !='p' and Wboard.w9c !='p' and Wboard.w9b !='p' and Wboard.w9a !='p'):
            moves = 'P*9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s9d =='':
        if Wboard.p>0 and (Wboard.w9h !='p' and Wboard.w9g !='p' and Wboard.w9f !='p' and Wboard.w9e !='p' and Wboard.w9d !='p' and Wboard.w9c !='p' and Wboard.w9b !='p' and Wboard.w9a !='p'):
            moves = 'P*9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s9c =='':
        if Wboard.p>0 and (Wboard.w9h !='p' and Wboard.w9g !='p' and Wboard.w9f !='p' and Wboard.w9e !='p' and Wboard.w9d !='p' and Wboard.w9c !='p' and Wboard.w9b !='p' and Wboard.w9a !='p'):
            moves = 'P*9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s9b =='':
        if Wboard.p>0 and (Wboard.w9h !='p' and Wboard.w9g !='p' and Wboard.w9f !='p' and Wboard.w9e !='p' and Wboard.w9d !='p' and Wboard.w9c !='p' and Wboard.w9b !='p' and Wboard.w9a !='p'):
            moves = 'P*9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s9a =='':
        if Wboard.p>0 and (Wboard.w9h !='p' and Wboard.w9g !='p' and Wboard.w9f !='p' and Wboard.w9e !='p' and Wboard.w9d !='p' and Wboard.w9c !='p' and Wboard.w9b !='p' and Wboard.w9a !='p'):
            moves = 'P*9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s8i =='':
        if Wboard.s>0:
            moves = 'S*8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s8h =='':
        if Wboard.p>0 and (Wboard.w8h !='p' and Wboard.w8g !='p' and Wboard.w8f !='p' and Wboard.w8e !='p' and Wboard.w8d !='p' and Wboard.w8c !='p' and Wboard.w8b !='p' and Wboard.w8a !='p'):
            moves = 'P*8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s8g =='':
        if Wboard.p>0 and (Wboard.w8h !='p' and Wboard.w8g !='p' and Wboard.w8f !='p' and Wboard.w8e !='p' and Wboard.w8d !='p' and Wboard.w8c !='p' and Wboard.w8b !='p' and Wboard.w8a !='p'):
            moves = 'P*8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s8f =='':
        if Wboard.p>0 and (Wboard.w8h !='p' and Wboard.w8g !='p' and Wboard.w8f !='p' and Wboard.w8e !='p' and Wboard.w8d !='p' and Wboard.w8c !='p' and Wboard.w8b !='p' and Wboard.w8a !='p'):
            moves = 'P*8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s8e =='':
        if Wboard.p>0 and (Wboard.w8h !='p' and Wboard.w8g !='p' and Wboard.w8f !='p' and Wboard.w8e !='p' and Wboard.w8d !='p' and Wboard.w8c !='p' and Wboard.w8b !='p' and Wboard.w8a !='p'):
            moves = 'P*8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s8d =='':
        if Wboard.p>0 and (Wboard.w8h !='p' and Wboard.w8g !='p' and Wboard.w8f !='p' and Wboard.w8e !='p' and Wboard.w8d !='p' and Wboard.w8c !='p' and Wboard.w8b !='p' and Wboard.w8a !='p'):
            moves = 'P*8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s8c =='':
        if Wboard.p>0 and (Wboard.w8h !='p' and Wboard.w8g !='p' and Wboard.w8f !='p' and Wboard.w8e !='p' and Wboard.w8d !='p' and Wboard.w8c !='p' and Wboard.w8b !='p' and Wboard.w8a !='p'):
            moves = 'P*8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s8b =='':
        if Wboard.p>0 and (Wboard.w8h !='p' and Wboard.w8g !='p' and Wboard.w8f !='p' and Wboard.w8e !='p' and Wboard.w8d !='p' and Wboard.w8c !='p' and Wboard.w8b !='p' and Wboard.w8a !='p'):
            moves = 'P*8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s8a =='':
        if Wboard.p>0 and (Wboard.w8h !='p' and Wboard.w8g !='p' and Wboard.w8f !='p' and Wboard.w8e !='p' and Wboard.w8d !='p' and Wboard.w8c !='p' and Wboard.w8b !='p' and Wboard.w8a !='p'):
            moves = 'P*8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s7i =='':
        if Wboard.s>0:
            moves = 'S*7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s7h =='':
        if Wboard.p>0 and (Wboard.w7h !='p' and Wboard.w7g !='p' and Wboard.w7f !='p' and Wboard.w7e !='p' and Wboard.w7d !='p' and Wboard.w7c !='p' and Wboard.w7b !='p' and Wboard.w7a !='p'):
            moves = 'P*7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s7g =='':
        if Wboard.p>0 and (Wboard.w7h !='p' and Wboard.w7g !='p' and Wboard.w7f !='p' and Wboard.w7e !='p' and Wboard.w7d !='p' and Wboard.w7c !='p' and Wboard.w7b !='p' and Wboard.w7a !='p'):
            moves = 'P*7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s7f =='':
        if Wboard.p>0 and (Wboard.w7h !='p' and Wboard.w7g !='p' and Wboard.w7f !='p' and Wboard.w7e !='p' and Wboard.w7d !='p' and Wboard.w7c !='p' and Wboard.w7b !='p' and Wboard.w7a !='p'):
            moves = 'P*7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s7e =='':
        if Wboard.p>0 and (Wboard.w7h !='p' and Wboard.w7g !='p' and Wboard.w7f !='p' and Wboard.w7e !='p' and Wboard.w7d !='p' and Wboard.w7c !='p' and Wboard.w7b !='p' and Wboard.w7a !='p'):
            moves = 'P*7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s7d =='':
        if Wboard.p>0 and (Wboard.w7h !='p' and Wboard.w7g !='p' and Wboard.w7f !='p' and Wboard.w7e !='p' and Wboard.w7d !='p' and Wboard.w7c !='p' and Wboard.w7b !='p' and Wboard.w7a !='p'):
            moves = 'P*7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s7c =='':
        if Wboard.p>0 and (Wboard.w7h !='p' and Wboard.w7g !='p' and Wboard.w7f !='p' and Wboard.w7e !='p' and Wboard.w7d !='p' and Wboard.w7c !='p' and Wboard.w7b !='p' and Wboard.w7a !='p'):
            moves = 'P*7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s7b =='':
        if Wboard.p>0 and (Wboard.w7h !='p' and Wboard.w7g !='p' and Wboard.w7f !='p' and Wboard.w7e !='p' and Wboard.w7d !='p' and Wboard.w7c !='p' and Wboard.w7b !='p' and Wboard.w7a !='p'):
            moves = 'P*7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s7a =='':
        if Wboard.p>0 and (Wboard.w7h !='p' and Wboard.w7g !='p' and Wboard.w7f !='p' and Wboard.w7e !='p' and Wboard.w7d !='p' and Wboard.w7c !='p' and Wboard.w7b !='p' and Wboard.w7a !='p'):
            moves = 'P*7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s6i =='':
        if Wboard.s>0:
            moves = 'S*6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s6h =='':
        if Wboard.p>0 and (Wboard.w6h !='p' and Wboard.w6g !='p' and Wboard.w6f !='p' and Wboard.w6e !='p' and Wboard.w6d !='p' and Wboard.w6c !='p' and Wboard.w6b !='p' and Wboard.w6a !='p'):
            moves = 'P*6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s6g =='':
        if Wboard.p>0 and (Wboard.w6h !='p' and Wboard.w6g !='p' and Wboard.w6f !='p' and Wboard.w6e !='p' and Wboard.w6d !='p' and Wboard.w6c !='p' and Wboard.w6b !='p' and Wboard.w6a !='p'):
            moves = 'P*6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s6f =='':
        if Wboard.p>0 and (Wboard.w6h !='p' and Wboard.w6g !='p' and Wboard.w6f !='p' and Wboard.w6e !='p' and Wboard.w6d !='p' and Wboard.w6c !='p' and Wboard.w6b !='p' and Wboard.w6a !='p'):
            moves = 'P*6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s6e =='':
        if Wboard.p>0 and (Wboard.w6h !='p' and Wboard.w6g !='p' and Wboard.w6f !='p' and Wboard.w6e !='p' and Wboard.w6d !='p' and Wboard.w6c !='p' and Wboard.w6b !='p' and Wboard.w6a !='p'):
            moves = 'P*6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s6d =='':
        if Wboard.p>0 and (Wboard.w6h !='p' and Wboard.w6g !='p' and Wboard.w6f !='p' and Wboard.w6e !='p' and Wboard.w6d !='p' and Wboard.w6c !='p' and Wboard.w6b !='p' and Wboard.w6a !='p'):
            moves = 'P*6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s6c =='':
        if Wboard.p>0 and (Wboard.w6h !='p' and Wboard.w6g !='p' and Wboard.w6f !='p' and Wboard.w6e !='p' and Wboard.w6d !='p' and Wboard.w6c !='p' and Wboard.w6b !='p' and Wboard.w6a !='p'):
            moves = 'P*6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s6b =='':
        if Wboard.p>0 and (Wboard.w6h !='p' and Wboard.w6g !='p' and Wboard.w6f !='p' and Wboard.w6e !='p' and Wboard.w6d !='p' and Wboard.w6c !='p' and Wboard.w6b !='p' and Wboard.w6a !='p'):
            moves = 'P*6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s6a =='':
        if Wboard.p>0 and (Wboard.w6h !='p' and Wboard.w6g !='p' and Wboard.w6f !='p' and Wboard.w6e !='p' and Wboard.w6d !='p' and Wboard.w6c !='p' and Wboard.w6b !='p' and Wboard.w6a !='p'):
            moves = 'P*6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s5i =='':
        if Wboard.s>0:
            moves = 'S*5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s5h =='':
        if Wboard.p>0 and (Wboard.w5h !='p' and Wboard.w5g !='p' and Wboard.w5f !='p' and Wboard.w5e !='p' and Wboard.w5d !='p' and Wboard.w5c !='p' and Wboard.w5b !='p' and Wboard.w5a !='p'):
            moves = 'P*5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s5g =='':
        if Wboard.p>0 and (Wboard.w5h !='p' and Wboard.w5g !='p' and Wboard.w5f !='p' and Wboard.w5e !='p' and Wboard.w5d !='p' and Wboard.w5c !='p' and Wboard.w5b !='p' and Wboard.w5a !='p'):
            moves = 'P*5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s5f =='':
        if Wboard.p>0 and (Wboard.w5h !='p' and Wboard.w5g !='p' and Wboard.w5f !='p' and Wboard.w5e !='p' and Wboard.w5d !='p' and Wboard.w5c !='p' and Wboard.w5b !='p' and Wboard.w5a !='p'):
            moves = 'P*5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s5e =='':
        if Wboard.p>0 and (Wboard.w5h !='p' and Wboard.w5g !='p' and Wboard.w5f !='p' and Wboard.w5e !='p' and Wboard.w5d !='p' and Wboard.w5c !='p' and Wboard.w5b !='p' and Wboard.w5a !='p'):
            moves = 'P*5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s5d =='':
        if Wboard.p>0 and (Wboard.w5h !='p' and Wboard.w5g !='p' and Wboard.w5f !='p' and Wboard.w5e !='p' and Wboard.w5d !='p' and Wboard.w5c !='p' and Wboard.w5b !='p' and Wboard.w5a !='p'):
            moves = 'P*5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s5c =='':
        if Wboard.p>0 and (Wboard.w5h !='p' and Wboard.w5g !='p' and Wboard.w5f !='p' and Wboard.w5e !='p' and Wboard.w5d !='p' and Wboard.w5c !='p' and Wboard.w5b !='p' and Wboard.w5a !='p'):
            moves = 'P*5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s5b =='':
        if Wboard.p>0 and (Wboard.w5h !='p' and Wboard.w5g !='p' and Wboard.w5f !='p' and Wboard.w5e !='p' and Wboard.w5d !='p' and Wboard.w5c !='p' and Wboard.w5b !='p' and Wboard.w5a !='p'):
            moves = 'P*5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s5a =='':
        if Wboard.p>0 and (Wboard.w5h !='p' and Wboard.w5g !='p' and Wboard.w5f !='p' and Wboard.w5e !='p' and Wboard.w5d !='p' and Wboard.w5c !='p' and Wboard.w5b !='p' and Wboard.w5a !='p'):
            moves = 'P*5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.l>0:
            moves = 'L*5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.n>0:
            moves = 'N*5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.s>0:
            moves = 'S*5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.g>0:
            moves = 'G*5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.b>0:
            moves = 'B*5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Wboard.r>0:
            moves = 'R*5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
