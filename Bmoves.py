#先手番合法手生成
import re
import Bboard
import Bboardbak
import Wboard
import Wboardbak
import board
import oute


#動かした後に先手玉に王手がかかっていないか判定
def kaihimore(sfen):
    mae = sfen[0:2]
    ushiro = sfen[2:4]
    nari = sfen[4:5]
    if mae[1:2]=='*':
        exec('Bboard.b{}="{}"'.format(ushiro,mae[0:1]))
    else:
        exec('Bboard.b{}=Bboard.b{}'.format(ushiro,mae))
        if nari == '+':
            exec("Bboard.b{}= '+'+Bboard.b{}".format(ushiro,ushiro))
        exec("Bboard.b{}=''".format(mae))
        exec("Wboard.w{}=''".format(ushiro))
    oute.boute()
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
    if Bboard.b1a !='':
        if re.match(r'[GK+]',Bboard.b1a)and Bboard.b2a=='':
            moves = '1a2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',Bboard.b1a)and Bboard.b1b=='':
            moves = '1a1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b1a)and Bboard.b2b=='':
            moves = '1a2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',Bboard.b1a)and Bboard.b2a=='':
            moves = '1a2a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',Bboard.b1a)and Bboard.b1b=='':
            moves = '1a1b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',Bboard.b1a)and Bboard.b1b=='':
            moves = '1a2b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b1a)and Bboard.b1c==''\
           and board.s1b=='':
            moves = '1a1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b1a)and Bboard.b1c==''\
           and board.s1b=='':
            moves = '1a1c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b1a)and Bboard.b1d==''\
           and board.s1b+board.s1c=='':
            moves = '1a1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b1a)and Bboard.b1d==''\
           and board.s1b+board.s1c=='':
            moves = '1a1d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b1a)and Bboard.b1e==''\
           and board.s1b+board.s1c+board.s1d=='':
            moves = '1a1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b1a)and Bboard.b1e==''\
           and board.s1b+board.s1c+board.s1d=='':
            moves = '1a1e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b1a)and Bboard.b1f==''\
           and board.s1b+board.s1c+board.s1d+board.s1e=='':
            moves = '1a1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b1a)and Bboard.b1f==''\
           and board.s1b+board.s1c+board.s1d+board.s1e=='':
            moves = '1a1f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b1a)and Bboard.b1g==''\
           and board.s1b+board.s1c+board.s1d+board.s1e+board.s1f=='':
            moves = '1a1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b1a)and Bboard.b1g==''\
           and board.s1b+board.s1c+board.s1d+board.s1e+board.s1f=='':
            moves = '1a1g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b1a)and Bboard.b1h==''\
           and board.s1b+board.s1c+board.s1d+board.s1e+board.s1f+board.s1g=='':
            moves = '1a1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b1a)and Bboard.b1h==''\
           and board.s1b+board.s1c+board.s1d+board.s1e+board.s1f+board.s1g=='':
            moves = '1a1h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b1a)and Bboard.b1i==''\
           and board.s1b+board.s1c+board.s1d+board.s1e+board.s1f+board.s1g+board.s1h=='':
            moves = '1a1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b1a)and Bboard.b1i==''\
           and board.s1b+board.s1c+board.s1d+board.s1e+board.s1f+board.s1g+board.s1h=='':
            moves = '1a1i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b1a)and Bboard.b3a==''\
           and board.s2a=='':
            moves = '1a3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b1a)and Bboard.b3a==''\
           and board.s2a=='':
            moves = '1a3a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b1a)and Bboard.b4a==''\
           and board.s2a+board.s3a=='':
            moves = '1a4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b1a)and Bboard.b4a==''\
           and board.s2a+board.s3a=='':
            moves = '1a4a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b1a)and Bboard.b5a==''\
           and board.s2a+board.s3a+board.s4a=='':
            moves = '1a5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b1a)and Bboard.b5a==''\
           and board.s2a+board.s3a+board.s4a=='':
            moves = '1a5a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b1a)and Bboard.b6a==''\
           and board.s2a+board.s3a+board.s4a+board.s5a=='':
            moves = '1a6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b1a)and Bboard.b6a==''\
           and board.s2a+board.s3a+board.s4a+board.s5a=='':
            moves = '1a6a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b1a)and Bboard.b7a==''\
           and board.s2a+board.s3a+board.s4a+board.s5a+board.s6a=='':
            moves = '1a7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b1a)and Bboard.b7a==''\
           and board.s2a+board.s3a+board.s4a+board.s5a+board.s6a=='':
            moves = '1a7a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b1a)and Bboard.b8a==''\
           and board.s2a+board.s3a+board.s4a+board.s5a+board.s6a+board.s7a=='':
            moves = '1a8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b1a)and Bboard.b8a==''\
           and board.s2a+board.s3a+board.s4a+board.s5a+board.s6a+board.s7a=='':
            moves = '1a8a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b1a)and Bboard.b9a==''\
           and board.s2a+board.s3a+board.s4a+board.s5a+board.s6a+board.s7a+board.s8a=='':
            moves = '1a9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b1a)and Bboard.b9a==''\
           and board.s2a+board.s3a+board.s4a+board.s5a+board.s6a+board.s7a+board.s8a=='':
            moves = '1a9a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b1a)and Bboard.b3c==''\
           and board.s2b=='':
            moves = '1a3c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b1a)and Bboard.b4d==''\
           and board.s2b+board.s3c=='':
            moves = '1a4d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b1a)and Bboard.b5e==''\
           and board.s2b+board.s3c+board.s4d=='':
            moves = '1a5e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b1a)and Bboard.b6f==''\
           and board.s2b+board.s3c+board.s4d+board.s5e=='':
            moves = '1a6f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b1a)and Bboard.b7g==''\
           and board.s2b+board.s3c+board.s4d+board.s5e+board.s6f=='':
            moves = '1a7g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b1a)and Bboard.b8h==''\
           and board.s2b+board.s3c+board.s4d+board.s5e+board.s6f+board.s7g=='':
            moves = '1a8h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b1a)and Bboard.b9i==''\
           and board.s2b+board.s3c+board.s4d+board.s5e+board.s6f+board.s7g+board.s8h=='':
            moves = '1a9i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b1a)and Bboard.b3c==''\
           and board.s2b=='':
            moves = '1a3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b1a)and Bboard.b4d==''\
           and board.s2b+board.s3c=='':
            moves = '1a4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b1a)and Bboard.b5e==''\
           and board.s2b+board.s3c+board.s4d=='':
            moves = '1a5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b1a)and Bboard.b6f==''\
           and board.s2b+board.s3c+board.s4d+board.s5e=='':
            moves = '1a6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b1a)and Bboard.b7g==''\
           and board.s2b+board.s3c+board.s4d+board.s5e+board.s6f=='':
            moves = '1a7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b1a)and Bboard.b8h==''\
           and board.s2b+board.s3c+board.s4d+board.s5e+board.s6f+board.s7g=='':
            moves = '1a8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b1a)and Bboard.b9i==''\
           and board.s2b+board.s3c+board.s4d+board.s5e+board.s6f+board.s7g+board.s8h=='':
            moves = '1a9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b2a !='':
        if re.match(r'[GK+]',Bboard.b2a)and Bboard.b1a=='':
            moves = '2a1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',Bboard.b2a)and Bboard.b3a=='':
            moves = '2a3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',Bboard.b2a)and Bboard.b2b=='':
            moves = '2a2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b2a)and Bboard.b1b=='':
            moves = '2a1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'\+R|\+B|S|K',Bboard.b2a)and Bboard.b3b=='':
            moves = '2a3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',Bboard.b2a)and Bboard.b1a=='':
            moves = '2a1a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',Bboard.b2a)and Bboard.b3a=='':
            moves = '2a3a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',Bboard.b2a)and Bboard.b2b=='':
            moves = '2a2b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',Bboard.b2a)and Bboard.b1b=='':
            moves = '2a1b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',Bboard.b2a)and Bboard.b3b=='':
            moves = '2a3b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b2a)and Bboard.b2c==''\
           and board.s2b=='':
            moves = '2a2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b2a)and Bboard.b2c==''\
           and board.s2b=='':
            moves = '2a2c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b2a)and Bboard.b2d==''\
           and board.s2b+board.s2c=='':
            moves = '2a2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b2a)and Bboard.b2d==''\
           and board.s2b+board.s2c=='':
            moves = '2a2d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b2a)and Bboard.b2e==''\
           and board.s2b+board.s2c+board.s2d=='':
            moves = '2a2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b2a)and Bboard.b2e==''\
           and board.s2b+board.s2c+board.s2d=='':
            moves = '2a2e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b2a)and Bboard.b2f==''\
           and board.s2b+board.s2c+board.s2d+board.s2e=='':
            moves = '2a2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b2a)and Bboard.b2f==''\
           and board.s2b+board.s2c+board.s2d+board.s2e=='':
            moves = '2a2f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b2a)and Bboard.b2g==''\
           and board.s2b+board.s2c+board.s2d+board.s2e+board.s2f=='':
            moves = '2a2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b2a)and Bboard.b2g==''\
           and board.s2b+board.s2c+board.s2d+board.s2e+board.s2f=='':
            moves = '2a2g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b2a)and Bboard.b2h==''\
           and board.s2b+board.s2c+board.s2d+board.s2e+board.s2f+board.s2g=='':
            moves = '2a2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b2a)and Bboard.b2h==''\
           and board.s2b+board.s2c+board.s2d+board.s2e+board.s2f+board.s2g=='':
            moves = '2a2h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b2a)and Bboard.b2i==''\
           and board.s2b+board.s2c+board.s2d+board.s2e+board.s2f+board.s2g+board.s2h=='':
            moves = '2a2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b2a)and Bboard.b2i==''\
           and board.s2b+board.s2c+board.s2d+board.s2e+board.s2f+board.s2g+board.s2h=='':
            moves = '2a2i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b2a)and Bboard.b4a==''\
           and board.s3a=='':
            moves = '2a4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b2a)and Bboard.b4a==''\
           and board.s3a=='':
            moves = '2a4a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b2a)and Bboard.b5a==''\
           and board.s3a+board.s4a=='':
            moves = '2a5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b2a)and Bboard.b5a==''\
           and board.s3a+board.s4a=='':
            moves = '2a5a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b2a)and Bboard.b6a==''\
           and board.s3a+board.s4a+board.s5a=='':
            moves = '2a6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b2a)and Bboard.b6a==''\
           and board.s3a+board.s4a+board.s5a=='':
            moves = '2a6a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b2a)and Bboard.b7a==''\
           and board.s3a+board.s4a+board.s5a+board.s6a=='':
            moves = '2a7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b2a)and Bboard.b7a==''\
           and board.s3a+board.s4a+board.s5a+board.s6a=='':
            moves = '2a7a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b2a)and Bboard.b8a==''\
           and board.s3a+board.s4a+board.s5a+board.s6a+board.s7a=='':
            moves = '2a8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b2a)and Bboard.b8a==''\
           and board.s3a+board.s4a+board.s5a+board.s6a+board.s7a=='':
            moves = '2a8a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b2a)and Bboard.b9a==''\
           and board.s3a+board.s4a+board.s5a+board.s6a+board.s7a+board.s8a=='':
            moves = '2a9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b2a)and Bboard.b9a==''\
           and board.s3a+board.s4a+board.s5a+board.s6a+board.s7a+board.s8a=='':
            moves = '2a9a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b2a)and Bboard.b4c==''\
           and board.s3b=='':
            moves = '2a4c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b2a)and Bboard.b5d==''\
           and board.s3b+board.s4c=='':
            moves = '2a5d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b2a)and Bboard.b6e==''\
           and board.s3b+board.s4c+board.s5d=='':
            moves = '2a6e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b2a)and Bboard.b7f==''\
           and board.s3b+board.s4c+board.s5d+board.s6e=='':
            moves = '2a7f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b2a)and Bboard.b8g==''\
           and board.s3b+board.s4c+board.s5d+board.s6e+board.s7f=='':
            moves = '2a8g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b2a)and Bboard.b9h==''\
           and board.s3b+board.s4c+board.s5d+board.s6e+board.s7f+board.s8g=='':
            moves = '2a9h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b2a)and Bboard.b4c==''\
           and board.s3b=='':
            moves = '2a4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b2a)and Bboard.b5d==''\
           and board.s3b+board.s4c=='':
            moves = '2a5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b2a)and Bboard.b6e==''\
           and board.s3b+board.s4c+board.s5d=='':
            moves = '2a6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b2a)and Bboard.b7f==''\
           and board.s3b+board.s4c+board.s5d+board.s6e=='':
            moves = '2a7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b2a)and Bboard.b8g==''\
           and board.s3b+board.s4c+board.s5d+board.s6e+board.s7f=='':
            moves = '2a8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b2a)and Bboard.b9h==''\
           and board.s3b+board.s4c+board.s5d+board.s6e+board.s7f+board.s8g=='':
            moves = '2a9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b3a !='':
        if re.match(r'[GK+]',Bboard.b3a)and Bboard.b2a=='':
            moves = '3a2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',Bboard.b3a)and Bboard.b4a=='':
            moves = '3a4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',Bboard.b3a)and Bboard.b3b=='':
            moves = '3a3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b3a)and Bboard.b2b=='':
            moves = '3a2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'\+R|\+B|S|K',Bboard.b3a)and Bboard.b4b=='':
            moves = '3a4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',Bboard.b3a)and Bboard.b2a=='':
            moves = '3a2a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',Bboard.b3a)and Bboard.b4a=='':
            moves = '3a4a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',Bboard.b3a)and Bboard.b3b=='':
            moves = '3a3b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',Bboard.b3a)and Bboard.b2b=='':
            moves = '3a2b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',Bboard.b3a)and Bboard.b4b=='':
            moves = '3a4b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b3a)and Bboard.b3c==''\
           and board.s3b=='':
            moves = '3a3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b3a)and Bboard.b3c==''\
           and board.s3b=='':
            moves = '3a3c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b3a)and Bboard.b3d==''\
           and board.s3b+board.s3c=='':
            moves = '3a3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b3a)and Bboard.b3d==''\
           and board.s3b+board.s3c=='':
            moves = '3a3d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b3a)and Bboard.b3e==''\
           and board.s3b+board.s3c+board.s3d=='':
            moves = '3a3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b3a)and Bboard.b3e==''\
           and board.s3b+board.s3c+board.s3d=='':
            moves = '3a3e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b3a)and Bboard.b3f==''\
           and board.s3b+board.s3c+board.s3d+board.s3e=='':
            moves = '3a3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b3a)and Bboard.b3f==''\
           and board.s3b+board.s3c+board.s3d+board.s3e=='':
            moves = '3a3f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b3a)and Bboard.b3g==''\
           and board.s3b+board.s3c+board.s3d+board.s3e+board.s3f=='':
            moves = '3a3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b3a)and Bboard.b3g==''\
           and board.s3b+board.s3c+board.s3d+board.s3e+board.s3f=='':
            moves = '3a3g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b3a)and Bboard.b3h==''\
           and board.s3b+board.s3c+board.s3d+board.s3e+board.s3f+board.s3g=='':
            moves = '3a3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b3a)and Bboard.b3h==''\
           and board.s3b+board.s3c+board.s3d+board.s3e+board.s3f+board.s3g=='':
            moves = '3a3h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b3a)and Bboard.b3i==''\
           and board.s3b+board.s3c+board.s3d+board.s3e+board.s3f+board.s3g+board.s3h=='':
            moves = '3a3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b3a)and Bboard.b3i==''\
           and board.s3b+board.s3c+board.s3d+board.s3e+board.s3f+board.s3g+board.s3h=='':
            moves = '3a3i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b3a)and Bboard.b1a==''\
           and board.s2a=='':
            moves = '3a1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b3a)and Bboard.b1a==''\
           and board.s2a=='':
            moves = '3a1a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b3a)and Bboard.b5a==''\
           and board.s4a=='':
            moves = '3a5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b3a)and Bboard.b5a==''\
           and board.s4a=='':
            moves = '3a5a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b3a)and Bboard.b6a==''\
           and board.s4a+board.s5a=='':
            moves = '3a6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b3a)and Bboard.b6a==''\
           and board.s4a+board.s5a=='':
            moves = '3a6a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b3a)and Bboard.b7a==''\
           and board.s4a+board.s5a+board.s6a=='':
            moves = '3a7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b3a)and Bboard.b7a==''\
           and board.s4a+board.s5a+board.s6a=='':
            moves = '3a7a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b3a)and Bboard.b8a==''\
           and board.s4a+board.s5a+board.s6a+board.s7a=='':
            moves = '3a8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b3a)and Bboard.b8a==''\
           and board.s4a+board.s5a+board.s6a+board.s7a=='':
            moves = '3a8a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b3a)and Bboard.b9a==''\
           and board.s4a+board.s5a+board.s6a+board.s7a+board.s8a=='':
            moves = '3a9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b3a)and Bboard.b9a==''\
           and board.s4a+board.s5a+board.s6a+board.s7a+board.s8a=='':
            moves = '3a9a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b3a)and Bboard.b1c==''\
           and board.s2b=='':
            moves = '3a1c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b3a)and Bboard.b5c==''\
           and board.s4b=='':
            moves = '3a5c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b3a)and Bboard.b6d==''\
           and board.s4b+board.s5c=='':
            moves = '3a6d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b3a)and Bboard.b6e==''\
           and board.s4b+board.s5c+board.s6d=='':
            moves = '3a7e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b3a)and Bboard.b7f==''\
           and board.s4b+board.s5c+board.s6d+board.s7e=='':
            moves = '3a8f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b3a)and Bboard.b9g==''\
           and board.s4b+board.s5c+board.s6d+board.s7e+board.s8f=='':
            moves = '3a9g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b3a)and Bboard.b1c==''\
           and board.s2b=='':
            moves = '3a1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b3a)and Bboard.b5c==''\
           and board.s4b=='':
            moves = '3a5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b3a)and Bboard.b6d==''\
           and board.s4b+board.s5c=='':
            moves = '3a6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b3a)and Bboard.b6e==''\
           and board.s4b+board.s5c+board.s6d=='':
            moves = '3a7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b3a)and Bboard.b7f==''\
           and board.s4b+board.s5c+board.s6d+board.s7e=='':
            moves = '3a8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b3a)and Bboard.b9g==''\
           and board.s4b+board.s5c+board.s6d+board.s7e+board.s8f=='':
            moves = '3a9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b4a !='':
        if re.match(r'[GK+]',Bboard.b4a)and Bboard.b3a=='':
            moves = '4a3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',Bboard.b4a)and Bboard.b5a=='':
            moves = '4a5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',Bboard.b4a)and Bboard.b4b=='':
            moves = '4a4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b4a)and Bboard.b3b=='':
            moves = '4a3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'\+R|\+B|S|K',Bboard.b4a)and Bboard.b5b=='':
            moves = '4a5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',Bboard.b4a)and Bboard.b3a=='':
            moves = '4a3a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',Bboard.b4a)and Bboard.b5a=='':
            moves = '4a5a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',Bboard.b4a)and Bboard.b4b=='':
            moves = '4a4b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',Bboard.b4a)and Bboard.b3b=='':
            moves = '4a3b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',Bboard.b4a)and Bboard.b5b=='':
            moves = '4a5b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b4a)and Bboard.b4c==''\
           and board.s4b=='':
            moves = '4a4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b4a)and Bboard.b4c==''\
           and board.s4b=='':
            moves = '4a4c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b4a)and Bboard.b4d==''\
           and board.s4b+board.s4c=='':
            moves = '4a4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b4a)and Bboard.b4d==''\
           and board.s4b+board.s4c=='':
            moves = '4a4d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b4a)and Bboard.b4e==''\
           and board.s4b+board.s4c+board.s4d=='':
            moves = '4a4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b4a)and Bboard.b4e==''\
           and board.s4b+board.s4c+board.s4d=='':
            moves = '4a4e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b4a)and Bboard.b4f==''\
           and board.s4b+board.s4c+board.s4d+board.s4e=='':
            moves = '4a4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b4a)and Bboard.b4f==''\
           and board.s4b+board.s4c+board.s4d+board.s4e=='':
            moves = '4a4f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b4a)and Bboard.b4g==''\
           and board.s4b+board.s4c+board.s4d+board.s4e+board.s4f=='':
            moves = '4a4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b4a)and Bboard.b4g==''\
           and board.s4b+board.s4c+board.s4d+board.s4e+board.s4f=='':
            moves = '4a4g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b4a)and Bboard.b4h==''\
           and board.s4b+board.s4c+board.s4d+board.s4e+board.s4f+board.s4g=='':
            moves = '4a4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b4a)and Bboard.b4h==''\
           and board.s4b+board.s4c+board.s4d+board.s4e+board.s4f+board.s4g=='':
            moves = '4a4h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b4a)and Bboard.b4i==''\
           and board.s4b+board.s4c+board.s4d+board.s4e+board.s4f+board.s4g+board.s4h=='':
            moves = '4a4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b4a)and Bboard.b4i==''\
           and board.s4b+board.s4c+board.s4d+board.s4e+board.s4f+board.s4g+board.s4h=='':
            moves = '4a4i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b4a)and Bboard.b1a==''\
           and board.s2a+board.s3a=='':
            moves = '4a1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b4a)and Bboard.b1a==''\
           and board.s2a+board.s3a=='':
            moves = '4a1a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b4a)and Bboard.b2a==''\
           and board.s3a=='':
            moves = '4a2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b4a)and Bboard.b2a==''\
           and board.s3a=='':
            moves = '4a2a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b4a)and Bboard.b6a==''\
           and board.s5a=='':
            moves = '4a6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b4a)and Bboard.b6a==''\
           and board.s5a=='':
            moves = '4a6a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b4a)and Bboard.b7a==''\
           and board.s5a+board.s6a=='':
            moves = '4a7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b4a)and Bboard.b7a==''\
           and board.s5a+board.s6a=='':
            moves = '4a7a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b4a)and Bboard.b8a==''\
           and board.s5a+board.s6a+board.s7a=='':
            moves = '4a8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b4a)and Bboard.b8a==''\
           and board.s5a+board.s6a+board.s7a=='':
            moves = '4a8a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b4a)and Bboard.b9a==''\
           and board.s5a+board.s6a+board.s7a+board.s8a=='':
            moves = '4a9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b4a)and Bboard.b9a==''\
           and board.s5a+board.s6a+board.s7a+board.s8a=='':
            moves = '4a9a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b4a)and Bboard.b6c==''\
           and board.s5b=='':
            moves = '4a6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b4a)and Bboard.b7d==''\
           and board.s5b+board.s6c=='':
            moves = '4a7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b4a)and Bboard.b8e==''\
           and board.s5b+board.s6c+board.s7d=='':
            moves = '4a8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b4a)and Bboard.b9f==''\
           and board.s5b+board.s6c+board.s7d+board.s8e=='':
            moves = '4a9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b4a)and Bboard.b6c==''\
           and board.s5b=='':
            moves = '4a6c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b4a)and Bboard.b7d==''\
           and board.s5b+board.s6c=='':
            moves = '4a7d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b4a)and Bboard.b8e==''\
           and board.s5b+board.s6c+board.s7d=='':
            moves = '4a8e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b4a)and Bboard.b9f==''\
           and board.s5b+board.s6c+board.s7d+board.s8e=='':
            moves = '4a9f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b4a)and Bboard.b1d==''\
           and board.s2c+board.s3b=='':
            moves = '4a1d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b4a)and Bboard.b2c==''\
           and board.s3b=='':
            moves = '4a2c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b4a)and Bboard.b1d==''\
           and board.s2c+board.s3b=='':
            moves = '4a1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b4a)and Bboard.b2c==''\
           and board.s3b=='':
            moves = '4a2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b5a !='':
        if re.match(r'[GK+]',Bboard.b5a)and Bboard.b4a=='':
            moves = '5a4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',Bboard.b5a)and Bboard.b6a=='':
            moves = '5a6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',Bboard.b5a)and Bboard.b5b=='':
            moves = '5a5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b5a)and Bboard.b4b=='':
            moves = '5a4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'\+R|\+B|S|K',Bboard.b5a)and Bboard.b6b=='':
            moves = '5a6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',Bboard.b5a)and Bboard.b4a=='':
            moves = '5a4a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',Bboard.b5a)and Bboard.b6a=='':
            moves = '5a6a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',Bboard.b5a)and Bboard.b5b=='':
            moves = '5a5b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',Bboard.b5a)and Bboard.b4b=='':
            moves = '5a4b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',Bboard.b5a)and Bboard.b6b=='':
            moves = '5a6b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b5a)and Bboard.b5c==''\
           and board.s5b=='':
            moves = '5a5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b5a)and Bboard.b5c==''\
           and board.s5b=='':
            moves = '5a5c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b5a)and Bboard.b5d==''\
           and board.s5b+board.s5c=='':
            moves = '5a5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b5a)and Bboard.b5d==''\
           and board.s5b+board.s5c=='':
            moves = '5a5d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b5a)and Bboard.b5e==''\
           and board.s5b+board.s5c+board.s5d=='':
            moves = '5a5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b5a)and Bboard.b5e==''\
           and board.s5b+board.s5c+board.s5d=='':
            moves = '5a5e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b5a)and Bboard.b5f==''\
           and board.s5b+board.s5c+board.s5d+board.s5e=='':
            moves = '5a5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b5a)and Bboard.b5f==''\
           and board.s5b+board.s5c+board.s5d+board.s5e=='':
            moves = '5a5f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b5a)and Bboard.b5g==''\
           and board.s5b+board.s5c+board.s5d+board.s5e+board.s5f=='':
            moves = '5a5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b5a)and Bboard.b5g==''\
           and board.s5b+board.s5c+board.s5d+board.s5e+board.s5f=='':
            moves = '5a5g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b5a)and Bboard.b5h==''\
           and board.s5b+board.s5c+board.s5d+board.s5e+board.s5f+board.s5g=='':
            moves = '5a5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b5a)and Bboard.b5h==''\
           and board.s5b+board.s5c+board.s5d+board.s5e+board.s5f+board.s5g=='':
            moves = '5a5h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b5a)and Bboard.b5i==''\
           and board.s5b+board.s5c+board.s5d+board.s5e+board.s5f+board.s5g+board.s5h=='':
            moves = '5a5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b5a)and Bboard.b5i==''\
           and board.s5b+board.s5c+board.s5d+board.s5e+board.s5f+board.s5g+board.s5h=='':
            moves = '5a5i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b5a)and Bboard.b1a==''\
           and board.s2a+board.s3a+board.s4a=='':
            moves = '5a1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b5a)and Bboard.b1a==''\
           and board.s2a+board.s3a+board.s4a=='':
            moves = '5a1a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b5a)and Bboard.b2a==''\
           and board.s3a+board.s4a=='':
            moves = '5a2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b5a)and Bboard.b2a==''\
           and board.s3a+board.s4a=='':
            moves = '5a2a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b5a)and Bboard.b3a==''\
           and board.s4a=='':
            moves = '5a3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b5a)and Bboard.b3a==''\
           and board.s4a=='':
            moves = '5a3a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b5a)and Bboard.b7a==''\
           and board.s6a=='':
            moves = '5a7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b5a)and Bboard.b7a==''\
           and board.s6a=='':
            moves = '5a7a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b5a)and Bboard.b8a==''\
           and board.s6a+board.s7a=='':
            moves = '5a8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b5a)and Bboard.b8a==''\
           and board.s6a+board.s7a=='':
            moves = '5a8a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b5a)and Bboard.b9a==''\
           and board.s6a+board.s7a+board.s8a=='':
            moves = '5a9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b5a)and Bboard.b9a==''\
           and board.s6a+board.s7a+board.s8a=='':
            moves = '5a9a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b5a)and Bboard.b7c==''\
           and board.s6b=='':
            moves = '5a7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b5a)and Bboard.b8d==''\
           and board.s6b+board.s7c=='':
            moves = '5a8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b5a)and Bboard.b9e==''\
           and board.s6b+board.s7c+board.s8d=='':
            moves = '5a9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b5a)and Bboard.b7c==''\
           and board.s6b=='':
            moves = '5a7c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b5a)and Bboard.b8d==''\
           and board.s6b+board.s7c=='':
            moves = '5a8d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b5a)and Bboard.b9e==''\
           and board.s6b+board.s7c+board.s8d=='':
            moves = '5a9e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b5a)and Bboard.b2d==''\
           and board.s3c+board.s4b=='':
            moves = '5a2d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b5a)and Bboard.b3c==''\
           and board.s4b=='':
            moves = '5a3c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b5a)and Bboard.b2d==''\
           and board.s3c+board.s4b=='':
            moves = '5a2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b5a)and Bboard.b3c==''\
           and board.s4b=='':
            moves = '5a3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b5a)and Bboard.b1e==''\
           and board.s4b+board.s3c+board.s2d=='':
            moves = '5a1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b5a)and Bboard.b1e==''\
           and board.s4b+board.s3c+board.s2d=='':
            moves = '5a1e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b6a !='':
        if re.match(r'[GK+]',Bboard.b6a)and Bboard.b5a=='':
            moves = '6a5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',Bboard.b6a)and Bboard.b7a=='':
            moves = '6a7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',Bboard.b6a)and Bboard.b6b=='':
            moves = '6a6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b6a)and Bboard.b5b=='':
            moves = '6a5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'\+R|\+B|S|K',Bboard.b6a)and Bboard.b7b=='':
            moves = '6a7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',Bboard.b6a)and Bboard.b5a=='':
            moves = '6a5a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',Bboard.b6a)and Bboard.b7a=='':
            moves = '6a7a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',Bboard.b6a)and Bboard.b6b=='':
            moves = '6a6b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',Bboard.b6a)and Bboard.b5b=='':
            moves = '6a5b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',Bboard.b6a)and Bboard.b7b=='':
            moves = '6a7b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b6a)and Bboard.b6c==''\
           and board.s6b=='':
            moves = '6a6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b6a)and Bboard.b6c==''\
           and board.s6b=='':
            moves = '6a6c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b6a)and Bboard.b6d==''\
           and board.s6b+board.s6c=='':
            moves = '6a6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b6a)and Bboard.b6d==''\
           and board.s6b+board.s6c=='':
            moves = '6a6d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b6a)and Bboard.b6e==''\
           and board.s6b+board.s6c+board.s6d=='':
            moves = '6a6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b6a)and Bboard.b6e==''\
           and board.s6b+board.s6c+board.s6d=='':
            moves = '6a6e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b6a)and Bboard.b6f==''\
           and board.s6b+board.s6c+board.s6d+board.s6e=='':
            moves = '6a6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b6a)and Bboard.b6f==''\
           and board.s6b+board.s6c+board.s6d+board.s6e=='':
            moves = '6a6f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b6a)and Bboard.b6g==''\
           and board.s6b+board.s6c+board.s6d+board.s6e+board.s6f=='':
            moves = '6a6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b6a)and Bboard.b6g==''\
           and board.s6b+board.s6c+board.s6d+board.s6e+board.s6f=='':
            moves = '6a6g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b6a)and Bboard.b6h==''\
           and board.s6b+board.s6c+board.s6d+board.s6e+board.s6f+board.s6g=='':
            moves = '6a6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b6a)and Bboard.b6h==''\
           and board.s6b+board.s6c+board.s6d+board.s6e+board.s6f+board.s6g=='':
            moves = '6a6h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b6a)and Bboard.b6i==''\
           and board.s6b+board.s6c+board.s6d+board.s6e+board.s6f+board.s6g+board.s6h=='':
            moves = '6a6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b6a)and Bboard.b6i==''\
           and board.s6b+board.s6c+board.s6d+board.s6e+board.s6f+board.s6g+board.s6h=='':
            moves = '6a6i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b6a)and Bboard.b9a==''\
           and board.s8a+board.s7a=='':
            moves = '6a9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b6a)and Bboard.b9a==''\
           and board.s8a+board.s7a=='':
            moves = '6a9a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b6a)and Bboard.b8a==''\
           and board.s7a=='':
            moves = '6a8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b6a)and Bboard.b8a==''\
           and board.s7a=='':
            moves = '6a8a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b6a)and Bboard.b4a==''\
           and board.s5a=='':
            moves = '6a4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b6a)and Bboard.b4a==''\
           and board.s5a=='':
            moves = '6a4a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b6a)and Bboard.b3a==''\
           and board.s5a+board.s4a=='':
            moves = '6a3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b6a)and Bboard.b3a==''\
           and board.s5a+board.s4a=='':
            moves = '6a3a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b6a)and Bboard.b2a==''\
           and board.s5a+board.s4a+board.s3a=='':
            moves = '6a2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b6a)and Bboard.b2a==''\
           and board.s5a+board.s4a+board.s3a=='':
            moves = '6a2a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b6a)and Bboard.b1a==''\
           and board.s5a+board.s4a+board.s3a+board.s2a=='':
            moves = '6a1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b6a)and Bboard.b1a==''\
           and board.s5a+board.s4a+board.s3a+board.s2a=='':
            moves = '6a1a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b6a)and Bboard.b4c==''\
           and board.s5b=='':
            moves = '6a4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b6a)and Bboard.b3d==''\
           and board.s5b+board.s4c=='':
            moves = '6a3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b6a)and Bboard.b2e==''\
           and board.s5b+board.s4c+board.s3d=='':
            moves = '6a2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b6a)and Bboard.b1f==''\
           and board.s5b+board.s4c+board.s3d+board.s2e=='':
            moves = '6a1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b6a)and Bboard.b4c==''\
           and board.s5b=='':
            moves = '6a4c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b6a)and Bboard.b3d==''\
           and board.s5b+board.s4c=='':
            moves = '6a3d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b6a)and Bboard.b2e==''\
           and board.s5b+board.s4c+board.s3d=='':
            moves = '6a2e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b6a)and Bboard.b1f==''\
           and board.s5b+board.s4c+board.s3d+board.s2e=='':
            moves = '6a1f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b6a)and Bboard.b9d==''\
           and board.s8c+board.s7b=='':
            moves = '6a9d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b6a)and Bboard.b8c==''\
           and board.s7b=='':
            moves = '6a8c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b6a)and Bboard.b9d==''\
           and board.s8c+board.s7b=='':
            moves = '6a9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b6a)and Bboard.b8c==''\
           and board.s7b=='':
            moves = '6a8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b7a !='':
        if re.match(r'[GK+]',Bboard.b7a)and Bboard.b6a=='':
            moves = '7a6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',Bboard.b7a)and Bboard.b8a=='':
            moves = '7a8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',Bboard.b7a)and Bboard.b7b=='':
            moves = '7a7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b7a)and Bboard.b6b=='':
            moves = '7a6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'\+R|\+B|S|K',Bboard.b7a)and Bboard.b8b=='':
            moves = '7a8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',Bboard.b7a)and Bboard.b6a=='':
            moves = '7a6a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',Bboard.b7a)and Bboard.b8a=='':
            moves = '7a8a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',Bboard.b7a)and Bboard.b7b=='':
            moves = '7a7b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',Bboard.b7a)and Bboard.b6b=='':
            moves = '7a6b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',Bboard.b7a)and Bboard.b8b=='':
            moves = '7a8b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b7a)and Bboard.b7c==''\
           and board.s7b=='':
            moves = '7a7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b7a)and Bboard.b7c==''\
           and board.s7b=='':
            moves = '7a7c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b7a)and Bboard.b7d==''\
           and board.s7b+board.s7c=='':
            moves = '7a7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b7a)and Bboard.b7d==''\
           and board.s7b+board.s7c=='':
            moves = '7a7d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b7a)and Bboard.b7e==''\
           and board.s7b+board.s7c+board.s7d=='':
            moves = '7a7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b7a)and Bboard.b7e==''\
           and board.s7b+board.s7c+board.s7d=='':
            moves = '7a7e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b7a)and Bboard.b7f==''\
           and board.s7b+board.s7c+board.s7d+board.s7e=='':
            moves = '7a7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b7a)and Bboard.b7f==''\
           and board.s7b+board.s7c+board.s7d+board.s7e=='':
            moves = '7a7f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b7a)and Bboard.b7g==''\
           and board.s7b+board.s7c+board.s7d+board.s7e+board.s7f=='':
            moves = '7a7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b7a)and Bboard.b7g==''\
           and board.s7b+board.s7c+board.s7d+board.s7e+board.s7f=='':
            moves = '7a7g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b7a)and Bboard.b7h==''\
           and board.s7b+board.s7c+board.s7d+board.s7e+board.s7f+board.s7g=='':
            moves = '7a7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b7a)and Bboard.b7h==''\
           and board.s7b+board.s7c+board.s7d+board.s7e+board.s7f+board.s7g=='':
            moves = '7a7h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b7a)and Bboard.b7i==''\
           and board.s7b+board.s7c+board.s7d+board.s7e+board.s7f+board.s7g+board.s7h=='':
            moves = '7a7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b7a)and Bboard.b7i==''\
           and board.s7b+board.s7c+board.s7d+board.s7e+board.s7f+board.s7g+board.s7h=='':
            moves = '7a7i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b7a)and Bboard.b9a==''\
           and board.s8a=='':
            moves = '7a9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b7a)and Bboard.b9a==''\
           and board.s8a=='':
            moves = '7a9a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b7a)and Bboard.b5a==''\
           and board.s6a=='':
            moves = '7a5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b7a)and Bboard.b5a==''\
           and board.s6a=='':
            moves = '7a5a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b7a)and Bboard.b4a==''\
           and board.s6a+board.s5a=='':
            moves = '7a4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b7a)and Bboard.b4a==''\
           and board.s6a+board.s5a=='':
            moves = '7a4a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b7a)and Bboard.b3a==''\
           and board.s6a+board.s5a+board.s4a=='':
            moves = '7a3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b7a)and Bboard.b3a==''\
           and board.s6a+board.s5a+board.s4a=='':
            moves = '7a3a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b7a)and Bboard.b2a==''\
           and board.s6a+board.s5a+board.s4a+board.s3a=='':
            moves = '7a2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b7a)and Bboard.b2a==''\
           and board.s6a+board.s5a+board.s4a+board.s3a=='':
            moves = '7a2a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b7a)and Bboard.b1a==''\
           and board.s6a+board.s5a+board.s4a+board.s3a+board.s2a=='':
            moves = '7a1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b7a)and Bboard.b1a==''\
           and board.s6a+board.s5a+board.s4a+board.s3a+board.s2a=='':
            moves = '7a1a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b7a)and Bboard.b9c==''\
           and board.s8b=='':
            moves = '7a9c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b7a)and Bboard.b5c==''\
           and board.s6b=='':
            moves = '7a5c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b7a)and Bboard.b4d==''\
           and board.s6b+board.s5c=='':
            moves = '7a4d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b7a)and Bboard.b4e==''\
           and board.s6b+board.s5c+board.s4d=='':
            moves = '7a3e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b7a)and Bboard.b3f==''\
           and board.s6b+board.s5c+board.s4d+board.s3e=='':
            moves = '7a2f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b7a)and Bboard.b1g==''\
           and board.s6b+board.s5c+board.s4d+board.s3e+board.s2f=='':
            moves = '7a1g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b7a)and Bboard.b9c==''\
           and board.s8b=='':
            moves = '7a9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b7a)and Bboard.b5c==''\
           and board.s6b=='':
            moves = '7a5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b7a)and Bboard.b4d==''\
           and board.s6b+board.s5c=='':
            moves = '7a4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b7a)and Bboard.b4e==''\
           and board.s6b+board.s5c+board.s4d=='':
            moves = '7a3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b7a)and Bboard.b3f==''\
           and board.s6b+board.s5c+board.s4d+board.s3e=='':
            moves = '7a2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b7a)and Bboard.b1g==''\
           and board.s6b+board.s5c+board.s4d+board.s3e+board.s2f=='':
            moves = '7a1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b8a !='':
        if re.match(r'[GK+]',Bboard.b8a)and Bboard.b7a=='':
            moves = '8a7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',Bboard.b8a)and Bboard.b9a=='':
            moves = '8a9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',Bboard.b8a)and Bboard.b8b=='':
            moves = '8a8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b8a)and Bboard.b7b=='':
            moves = '8a7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'\+R|\+B|S|K',Bboard.b8a)and Bboard.b9b=='':
            moves = '8a9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',Bboard.b8a)and Bboard.b7a=='':
            moves = '8a7a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',Bboard.b8a)and Bboard.b9a=='':
            moves = '8a9a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',Bboard.b8a)and Bboard.b8b=='':
            moves = '8a8b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',Bboard.b8a)and Bboard.b7b=='':
            moves = '8a7b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',Bboard.b8a)and Bboard.b9b=='':
            moves = '8a9b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b8a)and Bboard.b8c==''\
           and board.s8b=='':
            moves = '8a8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b8a)and Bboard.b8c==''\
           and board.s8b=='':
            moves = '8a8c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b8a)and Bboard.b8d==''\
           and board.s8b+board.s8c=='':
            moves = '8a8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b8a)and Bboard.b8d==''\
           and board.s8b+board.s8c=='':
            moves = '8a8d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b8a)and Bboard.b8e==''\
           and board.s8b+board.s8c+board.s8d=='':
            moves = '8a8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b8a)and Bboard.b8e==''\
           and board.s8b+board.s8c+board.s8d=='':
            moves = '8a8e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b8a)and Bboard.b8f==''\
           and board.s8b+board.s8c+board.s8d+board.s8e=='':
            moves = '8a8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b8a)and Bboard.b8f==''\
           and board.s8b+board.s8c+board.s8d+board.s8e=='':
            moves = '8a8f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b8a)and Bboard.b8g==''\
           and board.s8b+board.s8c+board.s8d+board.s8e+board.s8f=='':
            moves = '8a8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b8a)and Bboard.b8g==''\
           and board.s8b+board.s8c+board.s8d+board.s8e+board.s8f=='':
            moves = '8a8g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b8a)and Bboard.b8h==''\
           and board.s8b+board.s8c+board.s8d+board.s8e+board.s8f+board.s8g=='':
            moves = '8a8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b8a)and Bboard.b8h==''\
           and board.s8b+board.s8c+board.s8d+board.s8e+board.s8f+board.s8g=='':
            moves = '8a8h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b8a)and Bboard.b8i==''\
           and board.s8b+board.s8c+board.s8d+board.s8e+board.s8f+board.s8g+board.s8h=='':
            moves = '8a8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b8a)and Bboard.b8i==''\
           and board.s8b+board.s8c+board.s8d+board.s8e+board.s8f+board.s8g+board.s8h=='':
            moves = '8a8i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b8a)and Bboard.b6a==''\
           and board.s7a=='':
            moves = '8a6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b8a)and Bboard.b6a==''\
           and board.s7a=='':
            moves = '8a6a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b8a)and Bboard.b5a==''\
           and board.s7a+board.s6a=='':
            moves = '8a5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b8a)and Bboard.b5a==''\
           and board.s7a+board.s6a=='':
            moves = '8a5a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b8a)and Bboard.b4a==''\
           and board.s7a+board.s6a+board.s5a=='':
            moves = '8a4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b8a)and Bboard.b4a==''\
           and board.s7a+board.s6a+board.s5a=='':
            moves = '8a4a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b8a)and Bboard.b3a==''\
           and board.s7a+board.s6a+board.s5a+board.s4a=='':
            moves = '8a3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b8a)and Bboard.b3a==''\
           and board.s7a+board.s6a+board.s5a+board.s4a=='':
            moves = '8a3a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b8a)and Bboard.b2a==''\
           and board.s7a+board.s6a+board.s5a+board.s4a+board.s3a=='':
            moves = '8a2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b8a)and Bboard.b2a==''\
           and board.s7a+board.s6a+board.s5a+board.s4a+board.s3a=='':
            moves = '8a2a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b8a)and Bboard.b1a==''\
           and board.s7a+board.s6a+board.s5a+board.s4a+board.s3a+board.s2a=='':
            moves = '8a1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b8a)and Bboard.b1a==''\
           and board.s7a+board.s6a+board.s5a+board.s4a+board.s3a+board.s2a=='':
            moves = '8a1a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b8a)and Bboard.b6c==''\
           and board.s7b=='':
            moves = '8a6c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b8a)and Bboard.b5d==''\
           and board.s7b+board.s6c=='':
            moves = '8a5d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b8a)and Bboard.b4e==''\
           and board.s7b+board.s6c+board.s5d=='':
            moves = '8a4e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b8a)and Bboard.b3f==''\
           and board.s7b+board.s6c+board.s5d+board.s4e=='':
            moves = '8a3f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b8a)and Bboard.b2g==''\
           and board.s7b+board.s6c+board.s5d+board.s4e+board.s3f=='':
            moves = '8a2g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b8a)and Bboard.b1h==''\
           and board.s7b+board.s6c+board.s5d+board.s4e+board.s3f+board.s2g=='':
            moves = '8a1h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b8a)and Bboard.b6c==''\
           and board.s7b=='':
            moves = '8a6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b8a)and Bboard.b5d==''\
           and board.s7b+board.s6c=='':
            moves = '8a5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b8a)and Bboard.b4e==''\
           and board.s7b+board.s6c+board.s5d=='':
            moves = '8a4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b8a)and Bboard.b3f==''\
           and board.s7b+board.s6c+board.s5d+board.s4e=='':
            moves = '8a3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b8a)and Bboard.b2g==''\
           and board.s7b+board.s6c+board.s5d+board.s4e+board.s3f=='':
            moves = '8a2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b8a)and Bboard.b1h==''\
           and board.s7b+board.s6c+board.s5d+board.s4e+board.s3f+board.s2g=='':
            moves = '8a1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b9a !='':
        if re.match(r'[GK+]',Bboard.b9a)and Bboard.b8a=='':
            moves = '9a8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',Bboard.b9a)and Bboard.b9b=='':
            moves = '9a9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b9a)and Bboard.b8b=='':
            moves = '9a8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('R',Bboard.b9a)and Bboard.b8a=='':
            moves = '9a8a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',Bboard.b9a)and Bboard.b9b=='':
            moves = '9a9b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',Bboard.b9a)and Bboard.b8b=='':
            moves = '9a8b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b9a)and Bboard.b9c==''\
           and board.s9b=='':
            moves = '9a9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b9a)and Bboard.b9c==''\
           and board.s9b=='':
            moves = '9a9c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b9a)and Bboard.b9d==''\
           and board.s9b+board.s9c=='':
            moves = '9a9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b9a)and Bboard.b9d==''\
           and board.s9b+board.s9c=='':
            moves = '9a9d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b9a)and Bboard.b9e==''\
           and board.s9b+board.s9c+board.s9d=='':
            moves = '9a9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b9a)and Bboard.b9e==''\
           and board.s9b+board.s9c+board.s9d=='':
            moves = '9a9e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b9a)and Bboard.b9f==''\
           and board.s9b+board.s9c+board.s9d+board.s9e=='':
            moves = '9a9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b9a)and Bboard.b9f==''\
           and board.s9b+board.s9c+board.s9d+board.s9e=='':
            moves = '9a9f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b9a)and Bboard.b9g==''\
           and board.s9b+board.s9c+board.s9d+board.s9e+board.s9f=='':
            moves = '9a9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b9a)and Bboard.b9g==''\
           and board.s9b+board.s9c+board.s9d+board.s9e+board.s9f=='':
            moves = '9a9g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b9a)and Bboard.b9h==''\
           and board.s9b+board.s9c+board.s9d+board.s9e+board.s9f+board.s9g=='':
            moves = '9a9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b9a)and Bboard.b9h==''\
           and board.s9b+board.s9c+board.s9d+board.s9e+board.s9f+board.s9g=='':
            moves = '9a9h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b9a)and Bboard.b9i==''\
           and board.s9b+board.s9c+board.s9d+board.s9e+board.s9f+board.s9g+board.s9h=='':
            moves = '9a9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b9a)and Bboard.b9i==''\
           and board.s9b+board.s9c+board.s9d+board.s9e+board.s9f+board.s9g+board.s9h=='':
            moves = '9a9i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b9a)and Bboard.b7a==''\
           and board.s8a=='':
            moves = '9a7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b9a)and Bboard.b7a==''\
           and board.s8a=='':
            moves = '9a7a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b9a)and Bboard.b6a==''\
           and board.s8a+board.s7a=='':
            moves = '9a6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b9a)and Bboard.b6a==''\
           and board.s8a+board.s7a=='':
            moves = '9a6a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b9a)and Bboard.b5a==''\
           and board.s8a+board.s7a+board.s6a=='':
            moves = '9a5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b9a)and Bboard.b5a==''\
           and board.s8a+board.s7a+board.s6a=='':
            moves = '9a5a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b9a)and Bboard.b4a==''\
           and board.s8a+board.s7a+board.s6a+board.s5a=='':
            moves = '9a4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b9a)and Bboard.b4a==''\
           and board.s8a+board.s7a+board.s6a+board.s5a=='':
            moves = '9a4a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b9a)and Bboard.b3a==''\
           and board.s8a+board.s7a+board.s6a+board.s5a+board.s4a=='':
            moves = '9a3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b9a)and Bboard.b3a==''\
           and board.s8a+board.s7a+board.s6a+board.s5a+board.s4a=='':
            moves = '9a3a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b9a)and Bboard.b2a==''\
           and board.s8a+board.s7a+board.s6a+board.s5a+board.s4a+board.s3a=='':
            moves = '9a2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b9a)and Bboard.b2a==''\
           and board.s8a+board.s7a+board.s6a+board.s5a+board.s4a+board.s3a=='':
            moves = '9a2a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b9a)and Bboard.b1a==''\
           and board.s8a+board.s7a+board.s6a+board.s5a+board.s4a+board.s3a+board.s2a=='':
            moves = '9a1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b9a)and Bboard.b1a==''\
           and board.s8a+board.s7a+board.s6a+board.s5a+board.s4a+board.s3a+board.s2a=='':
            moves = '9a1a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b9a)and Bboard.b7c==''\
           and board.s8b=='':
            moves = '9a7c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b9a)and Bboard.b6d==''\
           and board.s8b+board.s7c=='':
            moves = '9a6d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b9a)and Bboard.b5e==''\
           and board.s8b+board.s7c+board.s6d=='':
            moves = '9a5e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b9a)and Bboard.b4f==''\
           and board.s8b+board.s7c+board.s6d+board.s5e=='':
            moves = '9a4f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b9a)and Bboard.b3g==''\
           and board.s8b+board.s7c+board.s6d+board.s5e+board.s4f=='':
            moves = '9a3g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b9a)and Bboard.b2h==''\
           and board.s8b+board.s7c+board.s6d+board.s5e+board.s4f+board.s3g=='':
            moves = '9a2h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b9a)and Bboard.b1i==''\
           and board.s8b+board.s7c+board.s6d+board.s5e+board.s4f+board.s3g+board.s2h=='':
            moves = '9a1i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b9a)and Bboard.b7c==''\
           and board.s8b=='':
            moves = '9a7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b9a)and Bboard.b6d==''\
           and board.s8b+board.s7c=='':
            moves = '9a6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b9a)and Bboard.b5e==''\
           and board.s8b+board.s7c+board.s6d=='':
            moves = '9a5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b9a)and Bboard.b4f==''\
           and board.s8b+board.s7c+board.s6d+board.s5e=='':
            moves = '9a4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b9a)and Bboard.b3g==''\
           and board.s8b+board.s7c+board.s6d+board.s5e+board.s4f=='':
            moves = '9a3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b9a)and Bboard.b2h==''\
           and board.s8b+board.s7c+board.s6d+board.s5e+board.s4f+board.s3g=='':
            moves = '9a2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b9a)and Bboard.b1i==''\
           and board.s8b+board.s7c+board.s6d+board.s5e+board.s4f+board.s3g+board.s2h=='':
            moves = '9a1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b1b !='':
        if re.match(r'[SGK+]',Bboard.b1b)and Bboard.b1a=='':
            moves = '1b1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGK+]',Bboard.b1b)and Bboard.b2a=='':
            moves = '1b2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',Bboard.b1b)and Bboard.b2b=='':
            moves = '1b2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',Bboard.b1b)and Bboard.b1c=='':
            moves = '1b1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b1b)and Bboard.b2c=='':
            moves = '1b2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[PLSR]',Bboard.b1b)and Bboard.b1a=='':
            moves = '1b1a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',Bboard.b1b)and Bboard.b2a=='':
            moves = '1b2a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('R',Bboard.b1b)and Bboard.b2b=='':
            moves = '1b2b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',Bboard.b1b)and Bboard.b1c=='':
            moves = '1b1c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',Bboard.b1b)and Bboard.b2c=='':
            moves = '1b2c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b1b)and Bboard.b1d==''\
           and board.s1e=='':
            moves = '1b1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b1b)and Bboard.b1d==''\
           and board.s1e=='':
            moves = '1b1d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b1b)and Bboard.b1e==''\
           and board.s1c+board.s1d=='':
            moves = '1b1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b1b)and Bboard.b1e==''\
           and board.s1c+board.s1d=='':
            moves = '1b1e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b1b)and Bboard.b1f==''\
           and board.s1c+board.s1d+board.s1e=='':
            moves = '1b1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b1b)and Bboard.b1f==''\
           and board.s1c+board.s1d+board.s1e=='':
            moves = '1b1f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b1b)and Bboard.b1g==''\
           and board.s1c+board.s1d+board.s1e+board.s1f=='':
            moves = '1b1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b1b)and Bboard.b1g==''\
           and board.s1c+board.s1d+board.s1e+board.s1f=='':
            moves = '1b1g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b1b)and Bboard.b1h==''\
           and board.s1c+board.s1d+board.s1e+board.s1f+board.s1g=='':
            moves = '1b1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b1b)and Bboard.b1h==''\
           and board.s1c+board.s1d+board.s1e+board.s1f+board.s1g=='':
            moves = '1b1h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b1b)and Bboard.b1i==''\
           and board.s1c+board.s1d+board.s1e+board.s1f+board.s1g+board.s1h=='':
            moves = '1b1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b1b)and Bboard.b1i==''\
           and board.s1c+board.s1d+board.s1e+board.s1f+board.s1g+board.s1h=='':
            moves = '1b1i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b1b)and Bboard.b3b==''\
           and board.s2b=='':
            moves = '1b3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b1b)and Bboard.b3b==''\
           and board.s2b=='':
            moves = '1b3b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b1b)and Bboard.b4b==''\
           and board.s2b+board.s3b=='':
            moves = '1b4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b1b)and Bboard.b4b==''\
           and board.s2b+board.s3b=='':
            moves = '1b4b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b1b)and Bboard.b5b==''\
           and board.s2b+board.s3b+board.s4b=='':
            moves = '1b5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b1b)and Bboard.b5b==''\
           and board.s2b+board.s3b+board.s4b=='':
            moves = '1b5b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b1b)and Bboard.b6b==''\
           and board.s2b+board.s3b+board.s4b+board.s5b=='':
            moves = '1b6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b1b)and Bboard.b6b==''\
           and board.s2b+board.s3b+board.s4b+board.s5b=='':
            moves = '1b6b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b1b)and Bboard.b7b==''\
           and board.s2b+board.s3b+board.s4b+board.s5b+board.s6b=='':
            moves = '1b7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b1b)and Bboard.b7b==''\
           and board.s2b+board.s3b+board.s4b+board.s5b+board.s6b=='':
            moves = '1b7b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b1b)and Bboard.b8b==''\
           and board.s2b+board.s3b+board.s4b+board.s5b+board.s6b+board.s7b=='':
            moves = '1b8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b1b)and Bboard.b8b==''\
           and board.s2b+board.s3b+board.s4b+board.s5b+board.s6b+board.s7b=='':
            moves = '1b8b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b1b)and Bboard.b9b==''\
           and board.s2b+board.s3b+board.s4b+board.s5b+board.s6b+board.s7b+board.s8b=='':
            moves = '1b9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b1b)and Bboard.b9b==''\
           and board.s2b+board.s3b+board.s4b+board.s5b+board.s6b+board.s7b+board.s8b=='':
            moves = '1b9b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b1b)and Bboard.b3d==''\
           and board.s2c=='':
            moves = '1b3d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b1b)and Bboard.b4e==''\
           and board.s2c+board.s3d=='':
            moves = '1b4e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b1b)and Bboard.b5f==''\
           and board.s2c+board.s3d+board.s4e=='':
            moves = '1b5f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b1b)and Bboard.b6g==''\
           and board.s2c+board.s3d+board.s4e+board.s5f=='':
            moves = '1b6g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b1b)and Bboard.b7h==''\
           and board.s2c+board.s3d+board.s4e+board.s5f+board.s6g=='':
            moves = '1b7h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b1b)and Bboard.b8i==''\
           and board.s2c+board.s3d+board.s4e+board.s5f+board.s6g+board.s7h=='':
            moves = '1b8i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b1b)and Bboard.b3d==''\
           and board.s2c=='':
            moves = '1b3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b1b)and Bboard.b4e==''\
           and board.s2c+board.s3d=='':
            moves = '1b4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b1b)and Bboard.b5f==''\
           and board.s2c+board.s3d+board.s4e=='':
            moves = '1b5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b1b)and Bboard.b6g==''\
           and board.s2c+board.s3d+board.s4e+board.s5f=='':
            moves = '1b6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b1b)and Bboard.b7h==''\
           and board.s2c+board.s3d+board.s4e+board.s5f+board.s6g=='':
            moves = '1b7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b1b)and Bboard.b8i==''\
           and board.s2c+board.s3d+board.s4e+board.s5f+board.s6g+board.s7h=='':
            moves = '1b8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b2b !='':
        if re.match(r'[SGK+]',Bboard.b2b)and Bboard.b2a=='':
            moves = '2b2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGK+]',Bboard.b2b)and Bboard.b1a=='':
            moves = '2b1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGK+]',Bboard.b2b)and Bboard.b3a=='':
            moves = '2b3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',Bboard.b2b)and Bboard.b1b=='':
            moves = '2b1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',Bboard.b2b)and Bboard.b3b=='':
            moves = '2b3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',Bboard.b2b)and Bboard.b2c=='':
            moves = '2b2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b2b)and Bboard.b1c=='':
            moves = '2b1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b2b)and Bboard.b3c=='':
            moves = '2b3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[PLSR]',Bboard.b2b)and Bboard.b2a=='':
            moves = '2b2a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',Bboard.b2b)and Bboard.b1a=='':
            moves = '2b1a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'[BS]',Bboard.b2b)and Bboard.b3a=='':
            moves = '2b3a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('R',Bboard.b2b)and Bboard.b1b=='':
            moves = '2b1b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',Bboard.b2b)and Bboard.b3b=='':
            moves = '2b3b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',Bboard.b2b)and Bboard.b2c=='':
            moves = '2b2c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',Bboard.b2b)and Bboard.b1c=='':
            moves = '2b1c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',Bboard.b2b)and Bboard.b3c=='':
            moves = '2b3c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b2b)and Bboard.b2d==''\
           and board.s2e=='':
            moves = '2b2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b2b)and Bboard.b2d==''\
           and board.s2e=='':
            moves = '2b2d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b2b)and Bboard.b2e==''\
           and board.s2c+board.s2d=='':
            moves = '2b2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b2b)and Bboard.b2e==''\
           and board.s2c+board.s2d=='':
            moves = '2b2e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b2b)and Bboard.b2f==''\
           and board.s2c+board.s2d+board.s2e=='':
            moves = '2b2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b2b)and Bboard.b2f==''\
           and board.s2c+board.s2d+board.s2e=='':
            moves = '2b2f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b2b)and Bboard.b2g==''\
           and board.s2c+board.s2d+board.s2e+board.s2f=='':
            moves = '2b2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b2b)and Bboard.b2g==''\
           and board.s2c+board.s2d+board.s2e+board.s2f=='':
            moves = '2b2g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b2b)and Bboard.b2h==''\
           and board.s2c+board.s2d+board.s2e+board.s2f+board.s2g=='':
            moves = '2b2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b2b)and Bboard.b2h==''\
           and board.s2c+board.s2d+board.s2e+board.s2f+board.s2g=='':
            moves = '2b2h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b2b)and Bboard.b2i==''\
           and board.s2c+board.s2d+board.s2e+board.s2f+board.s2g+board.s2h=='':
            moves = '2b2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b2b)and Bboard.b2i==''\
           and board.s2c+board.s2d+board.s2e+board.s2f+board.s2g+board.s2h=='':
            moves = '2b2i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b2b)and Bboard.b4b==''\
           and board.s3b=='':
            moves = '2b4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b2b)and Bboard.b4b==''\
           and board.s3b=='':
            moves = '2b4b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b2b)and Bboard.b5b==''\
           and board.s3b+board.s4b=='':
            moves = '2b5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b2b)and Bboard.b5b==''\
           and board.s3b+board.s4b=='':
            moves = '2b5b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b2b)and Bboard.b6b==''\
           and board.s3b+board.s4b+board.s5b=='':
            moves = '2b6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b2b)and Bboard.b6b==''\
           and board.s3b+board.s4b+board.s5b=='':
            moves = '2b6b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b2b)and Bboard.b7b==''\
           and board.s3b+board.s4b+board.s5b+board.s6b=='':
            moves = '2b7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b2b)and Bboard.b7b==''\
           and board.s3b+board.s4b+board.s5b+board.s6b=='':
            moves = '2b7b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b2b)and Bboard.b8b==''\
           and board.s3b+board.s4b+board.s5b+board.s6b+board.s7b=='':
            moves = '2b8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b2b)and Bboard.b8b==''\
           and board.s3b+board.s4b+board.s5b+board.s6b+board.s7b=='':
            moves = '2b8b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b2b)and Bboard.b9b==''\
           and board.s3b+board.s4b+board.s5b+board.s6b+board.s7b+board.s8b=='':
            moves = '2b9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b2b)and Bboard.b9b==''\
           and board.s3b+board.s4b+board.s5b+board.s6b+board.s7b+board.s8b=='':
            moves = '2b9b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b2b)and Bboard.b4d==''\
           and board.s3c=='':
            moves = '2b4d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b2b)and Bboard.b5e==''\
           and board.s3c+board.s4d=='':
            moves = '2b5e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b2b)and Bboard.b6f==''\
           and board.s3c+board.s4d+board.s5e=='':
            moves = '2b6f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b2b)and Bboard.b7g==''\
           and board.s3c+board.s4d+board.s5e+board.s6f=='':
            moves = '2b7g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b2b)and Bboard.b8h==''\
           and board.s3c+board.s4d+board.s5e+board.s6f+board.s7g=='':
            moves = '2b8h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b2b)and Bboard.b9i==''\
           and board.s3c+board.s4d+board.s5e+board.s6f+board.s7g+board.s8h=='':
            moves = '2b9i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b2b)and Bboard.b4d==''\
           and board.s3c=='':
            moves = '2b4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b2b)and Bboard.b5e==''\
           and board.s3c+board.s4d=='':
            moves = '2b5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b2b)and Bboard.b6f==''\
           and board.s3c+board.s4d+board.s5e=='':
            moves = '2b6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b2b)and Bboard.b7g==''\
           and board.s3c+board.s4d+board.s5e+board.s6f=='':
            moves = '2b7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b2b)and Bboard.b8h==''\
           and board.s3c+board.s4d+board.s5e+board.s6f+board.s7g=='':
            moves = '2b8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b2b)and Bboard.b9i==''\
           and board.s3c+board.s4d+board.s5e+board.s6f+board.s7g+board.s8h=='':
            moves = '2b9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b3b !='':
        if re.match(r'[SGK+]',Bboard.b3b)and Bboard.b3a=='':
            moves = '3b3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGK+]',Bboard.b3b)and Bboard.b2a=='':
            moves = '3b2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGK+]',Bboard.b3b)and Bboard.b4a=='':
            moves = '3b4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',Bboard.b3b)and Bboard.b2b=='':
            moves = '3b2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',Bboard.b3b)and Bboard.b4b=='':
            moves = '3b4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',Bboard.b3b)and Bboard.b3c=='':
            moves = '3b3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b3b)and Bboard.b2c=='':
            moves = '3b2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b3b)and Bboard.b4c=='':
            moves = '3b4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[PLSR]',Bboard.b3b)and Bboard.b3a=='':
            moves = '3b3a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',Bboard.b3b)and Bboard.b2a=='':
            moves = '3b2a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'[BS]',Bboard.b3b)and Bboard.b4a=='':
            moves = '3b4a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('R',Bboard.b3b)and Bboard.b2b=='':
            moves = '3b2b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',Bboard.b3b)and Bboard.b4b=='':
            moves = '3b4b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',Bboard.b3b)and Bboard.b3c=='':
            moves = '3b3c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',Bboard.b3b)and Bboard.b2c=='':
            moves = '3b2c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',Bboard.b3b)and Bboard.b4c=='':
            moves = '3b4c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b3b)and Bboard.b3d==''\
           and board.s3e=='':
            moves = '3b3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b3b)and Bboard.b3d==''\
           and board.s3e=='':
            moves = '3b3d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b3b)and Bboard.b3e==''\
           and board.s3c+board.s3d=='':
            moves = '3b3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b3b)and Bboard.b3e==''\
           and board.s3c+board.s3d=='':
            moves = '3b3e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b3b)and Bboard.b3f==''\
           and board.s3c+board.s3d+board.s3e=='':
            moves = '3b3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b3b)and Bboard.b3f==''\
           and board.s3c+board.s3d+board.s3e=='':
            moves = '3b3f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b3b)and Bboard.b3g==''\
           and board.s3c+board.s3d+board.s3e+board.s3f=='':
            moves = '3b3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b3b)and Bboard.b3g==''\
           and board.s3c+board.s3d+board.s3e+board.s3f=='':
            moves = '3b3g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b3b)and Bboard.b3h==''\
           and board.s3c+board.s3d+board.s3e+board.s3f+board.s3g=='':
            moves = '3b3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b3b)and Bboard.b3h==''\
           and board.s3c+board.s3d+board.s3e+board.s3f+board.s3g=='':
            moves = '3b3h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b3b)and Bboard.b3i==''\
           and board.s3c+board.s3d+board.s3e+board.s3f+board.s3g+board.s3h=='':
            moves = '3b3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b3b)and Bboard.b3i==''\
           and board.s3c+board.s3d+board.s3e+board.s3f+board.s3g+board.s3h=='':
            moves = '3b3i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b3b)and Bboard.b1b==''\
           and board.s2b=='':
            moves = '3b1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b3b)and Bboard.b1b==''\
           and board.s2b=='':
            moves = '3b1b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b3b)and Bboard.b5b==''\
           and board.s4b=='':
            moves = '3b5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b3b)and Bboard.b5b==''\
           and board.s4b=='':
            moves = '3b5b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b3b)and Bboard.b6b==''\
           and board.s4b+board.s5b=='':
            moves = '3b6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b3b)and Bboard.b6b==''\
           and board.s4b+board.s5b=='':
            moves = '3b6b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b3b)and Bboard.b7b==''\
           and board.s4b+board.s5b+board.s6b=='':
            moves = '3b7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b3b)and Bboard.b7b==''\
           and board.s4b+board.s5b+board.s6b=='':
            moves = '3b7b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b3b)and Bboard.b8b==''\
           and board.s4b+board.s5b+board.s6b+board.s7b=='':
            moves = '3b8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b3b)and Bboard.b8b==''\
           and board.s4b+board.s5b+board.s6b+board.s7b=='':
            moves = '3b8b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b3b)and Bboard.b9b==''\
           and board.s4b+board.s5b+board.s6b+board.s7b+board.s8b=='':
            moves = '3b9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b3b)and Bboard.b9b==''\
           and board.s4b+board.s5b+board.s6b+board.s7b+board.s8b=='':
            moves = '3b9b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b3b)and Bboard.b5d==''\
           and board.s4c=='':
            moves = '3b5d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b3b)and Bboard.b6e==''\
           and board.s4c+board.s5d=='':
            moves = '3b6e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b3b)and Bboard.b7f==''\
           and board.s4c+board.s5d+board.s6e=='':
            moves = '3b7f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b3b)and Bboard.b8g==''\
           and board.s4c+board.s5d+board.s6e+board.s7f=='':
            moves = '3b8g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b3b)and Bboard.b9h==''\
           and board.s4c+board.s5d+board.s6e+board.s7f+board.s8g=='':
            moves = '3b9h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b3b)and Bboard.b5d==''\
           and board.s4c=='':
            moves = '3b5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b3b)and Bboard.b6e==''\
           and board.s4c+board.s5d=='':
            moves = '3b6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b3b)and Bboard.b7f==''\
           and board.s4c+board.s5d+board.s6e=='':
            moves = '3b7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b3b)and Bboard.b8g==''\
           and board.s4c+board.s5d+board.s6e+board.s7f=='':
            moves = '3b8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b3b)and Bboard.b9h==''\
           and board.s4c+board.s5d+board.s6e+board.s7f+board.s8g=='':
            moves = '3b9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b3b)and Bboard.b1d==''\
           and board.s2c=='':
            moves = '3b1d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b3b)and Bboard.b1d==''\
           and board.s2c=='':
            moves = '3b1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b4b !='':
        if re.match(r'[SGK+]',    Bboard.b4b)and Bboard.b4a=='':
            moves = '4b4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGK+]',    Bboard.b4b)and Bboard.b3a=='':
            moves = '4b3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGK+]',    Bboard.b4b)and Bboard.b5a=='':
            moves = '4b5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b4b)and Bboard.b3b=='':
            moves = '4b3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b4b)and Bboard.b5b=='':
            moves = '4b5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b4b)and Bboard.b4c=='':
            moves = '4b4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b4b)and Bboard.b3c=='':
            moves = '4b3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b4b)and Bboard.b5c=='':
            moves = '4b5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[PLSR]',   Bboard.b4b)and Bboard.b4a=='':
            moves = '4b4a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',     Bboard.b4b)and Bboard.b3a=='':
            moves = '4b3a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'[BS]',     Bboard.b4b)and Bboard.b5a=='':
            moves = '4b5a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('R',         Bboard.b4b)and Bboard.b3b=='':
            moves = '4b3b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',         Bboard.b4b)and Bboard.b5b=='':
            moves = '4b5b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',         Bboard.b4b)and Bboard.b4c=='':
            moves = '4b4c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',     Bboard.b4b)and Bboard.b3c=='':
            moves = '4b3c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',     Bboard.b4b)and Bboard.b5c=='':
            moves = '4b5c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b4b)and Bboard.b4d==''\
           and board.s4e=='':
            moves = '4b4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b4b)and Bboard.b4d==''\
           and board.s4e=='':
            moves = '4b4d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b4b)and Bboard.b4e==''\
           and board.s4c+board.s4d=='':
            moves = '4b4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b4b)and Bboard.b4e==''\
           and board.s4c+board.s4d=='':
            moves = '4b4e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b4b)and Bboard.b4f==''\
           and board.s4c+board.s4d+board.s4e=='':
            moves = '4b4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b4b)and Bboard.b4f==''\
           and board.s4c+board.s4d+board.s4e=='':
            moves = '4b4f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b4b)and Bboard.b4g==''\
           and board.s4c+board.s4d+board.s4e+board.s4f=='':
            moves = '4b4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b4b)and Bboard.b4g==''\
           and board.s4c+board.s4d+board.s4e+board.s4f=='':
            moves = '4b4g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b4b)and Bboard.b4h==''\
           and board.s4c+board.s4d+board.s4e+board.s4f+board.s4g=='':
            moves = '4b4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b4b)and Bboard.b4h==''\
           and board.s4c+board.s4d+board.s4e+board.s4f+board.s4g=='':
            moves = '4b4h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b4b)and Bboard.b4i==''\
           and board.s4c+board.s4d+board.s4e+board.s4f+board.s4g+board.s4h=='':
            moves = '4b4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b4b)and Bboard.b4i==''\
           and board.s4c+board.s4d+board.s4e+board.s4f+board.s4g+board.s4h=='':
            moves = '4b4i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b4b)and Bboard.b1b==''\
           and board.s2b+board.s3b=='':
            moves = '4b1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b4b)and Bboard.b1b==''\
           and board.s2b+board.s3b=='':
            moves = '4b1b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b4b)and Bboard.b5b==''\
           and board.s3b=='':
            moves = '4b2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b4b)and Bboard.b5b==''\
           and board.s3b=='':
            moves = '4b2b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b4b)and Bboard.b6b==''\
           and board.s5b=='':
            moves = '4b6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b4b)and Bboard.b6b==''\
           and board.s5b=='':
            moves = '4b6b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b4b)and Bboard.b7b==''\
           and board.s5b+board.s6b=='':
            moves = '4b7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b4b)and Bboard.b7b==''\
           and board.s5b+board.s6b=='':
            moves = '4b7b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b4b)and Bboard.b8b==''\
           and board.s5b+board.s6b+board.s7b=='':
            moves = '4b8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b4b)and Bboard.b8b==''\
           and board.s5b+board.s6b+board.s7b=='':
            moves = '4b8b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b4b)and Bboard.b9b==''\
           and board.s5b+board.s6b+board.s7b+board.s8b=='':
            moves = '4b9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b4b)and Bboard.b9b==''\
           and board.s5b+board.s6b+board.s7b+board.s8b=='':
            moves = '4b9b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b4b)and Bboard.b6d==''\
           and board.s5c=='':
            moves = '4b6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b4b)and Bboard.b7e==''\
           and board.s5c+board.s6d=='':
            moves = '4b7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b4b)and Bboard.b8f==''\
           and board.s5c+board.s6d+board.s7e=='':
            moves = '4b8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b4b)and Bboard.b9g==''\
           and board.s5c+board.s6d+board.s7e+board.s8f=='':
            moves = '4b9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b4b)and Bboard.b6d==''\
           and board.s5c=='':
            moves = '4b6d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b4b)and Bboard.b7e==''\
           and board.s5c+board.s6d=='':
            moves = '4b7e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b4b)and Bboard.b8f==''\
           and board.s5c+board.s6d+board.s7e=='':
            moves = '4b8f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b4b)and Bboard.b9g==''\
           and board.s5c+board.s6d+board.s7e+board.s8f=='':
            moves = '4b9g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b4b)and Bboard.b1e==''\
           and board.s2d+board.s3c=='':
            moves = '4b1e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b4b)and Bboard.b2d==''\
           and board.s3c=='':
            moves = '4b2d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b4b)and Bboard.b1e==''\
           and board.s2d+board.s3c=='':
            moves = '4b1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b4b)and Bboard.b2d==''\
           and board.s3c=='':
            moves = '4b2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b5b !='':
        if re.match(r'[SGK+]',    Bboard.b5b)and Bboard.b5a=='':
            moves = '5b5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGK+]',    Bboard.b5b)and Bboard.b4a=='':
            moves = '5b4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGK+]',    Bboard.b5b)and Bboard.b6a=='':
            moves = '5b6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b5b)and Bboard.b4b=='':
            moves = '5b4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b5b)and Bboard.b6b=='':
            moves = '5b6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b5b)and Bboard.b5c=='':
            moves = '5b5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b5b)and Bboard.b4c=='':
            moves = '5b4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b5b)and Bboard.b6c=='':
            moves = '5b6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[PLSR]',   Bboard.b5b)and Bboard.b5a=='':
            moves = '5b5a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',     Bboard.b5b)and Bboard.b4a=='':
            moves = '5b4a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'[BS]',     Bboard.b5b)and Bboard.b6a=='':
            moves = '5b6a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('R',         Bboard.b5b)and Bboard.b4b=='':
            moves = '5b4b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',         Bboard.b5b)and Bboard.b6b=='':
            moves = '5b6b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',         Bboard.b5b)and Bboard.b5c=='':
            moves = '5b5c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',     Bboard.b5b)and Bboard.b4c=='':
            moves = '5b4c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',     Bboard.b5b)and Bboard.b6c=='':
            moves = '5b6c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b5b)and Bboard.b5d==''\
           and board.s5e=='':
            moves = '5b5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b5b)and Bboard.b5d==''\
           and board.s5e=='':
            moves = '5b5d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b5b)and Bboard.b5e==''\
           and board.s5c+board.s5d=='':
            moves = '5b5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b5b)and Bboard.b5e==''\
           and board.s5c+board.s5d=='':
            moves = '5b5e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b5b)and Bboard.b5f==''\
           and board.s5c+board.s5d+board.s5e=='':
            moves = '5b5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b5b)and Bboard.b5f==''\
           and board.s5c+board.s5d+board.s5e=='':
            moves = '5b5f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b5b)and Bboard.b5g==''\
           and board.s5c+board.s5d+board.s5e+board.s5f=='':
            moves = '5b5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b5b)and Bboard.b5g==''\
           and board.s5c+board.s5d+board.s5e+board.s5f=='':
            moves = '5b5g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b5b)and Bboard.b5h==''\
           and board.s5c+board.s5d+board.s5e+board.s5f+board.s5g=='':
            moves = '5b5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b5b)and Bboard.b5h==''\
           and board.s5c+board.s5d+board.s5e+board.s5f+board.s5g=='':
            moves = '5b5h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b5b)and Bboard.b5i==''\
           and board.s5c+board.s5d+board.s5e+board.s5f+board.s5g+board.s5h=='':
            moves = '5b5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b5b)and Bboard.b5i==''\
           and board.s5c+board.s5d+board.s5e+board.s5f+board.s5g+board.s5h=='':
            moves = '5b5i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b5b)and Bboard.b1b==''\
           and board.s2b+board.s3b+board.s4b=='':
            moves = '5b1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b5b)and Bboard.b1b==''\
           and board.s2b+board.s3b+board.s4b=='':
            moves = '5b1b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b5b)and Bboard.b2b==''\
           and board.s3b+board.s4b=='':
            moves = '5b2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b5b)and Bboard.b2b==''\
           and board.s3b+board.s4b=='':
            moves = '5b2b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b5b)and Bboard.b3b==''\
           and board.s4b=='':
            moves = '5b3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b5b)and Bboard.b3b==''\
           and board.s4b=='':
            moves = '5b3b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b5b)and Bboard.b7b==''\
           and board.s6b=='':
            moves = '5b7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b5b)and Bboard.b7b==''\
           and board.s6b=='':
            moves = '5b7b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b5b)and Bboard.b8b==''\
           and board.s6b+board.s7b=='':
            moves = '5b8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b5b)and Bboard.b8b==''\
           and board.s6b+board.s7b=='':
            moves = '5b8b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b5b)and Bboard.b9b==''\
           and board.s6b+board.s7b+board.s8b=='':
            moves = '5b9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b5b)and Bboard.b9b==''\
           and board.s6b+board.s7b+board.s8b=='':
            moves = '5b9b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b5b)and Bboard.b7d==''\
           and board.s6c=='':
            moves = '5b7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b5b)and Bboard.b8e==''\
           and board.s6c+board.s7d=='':
            moves = '5b8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b5b)and Bboard.b9f==''\
           and board.s6c+board.s7d+board.s8e=='':
            moves = '5b9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b5b)and Bboard.b7d==''\
           and board.s6c=='':
            moves = '5b7d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b5b)and Bboard.b8e==''\
           and board.s6c+board.s7d=='':
            moves = '5b8e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b5b)and Bboard.b9f==''\
           and board.s6c+board.s7d+board.s8e=='':
            moves = '5b9f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b5b)and Bboard.b2e==''\
           and board.s3d+board.s4c=='':
            moves = '5b2e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b5b)and Bboard.b3d==''\
           and board.s4c=='':
            moves = '5b3d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b5b)and Bboard.b2e==''\
           and board.s3d+board.s4c=='':
            moves = '5b2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b5b)and Bboard.b3d==''\
           and board.s4c=='':
            moves = '5b3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b5b)and Bboard.b1f==''\
           and board.s4c+board.s3d+board.s2e=='':
            moves = '5b1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b5b)and Bboard.b1f==''\
           and board.s4c+board.s3d+board.s2e=='':
            moves = '5b1f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b6b !='':
        if re.match(r'[SGK+]',    Bboard.b6b)and Bboard.b6a=='':
            moves = '6b6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGK+]',    Bboard.b6b)and Bboard.b5a=='':
            moves = '6b5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGK+]',    Bboard.b6b)and Bboard.b7a=='':
            moves = '6b7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b6b)and Bboard.b5b=='':
            moves = '6b5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b6b)and Bboard.b7b=='':
            moves = '6b7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b6b)and Bboard.b6c=='':
            moves = '6b6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b6b)and Bboard.b5c=='':
            moves = '6b5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b6b)and Bboard.b7c=='':
            moves = '6b7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[PLSR]',   Bboard.b6b)and Bboard.b6a=='':
            moves = '6b6a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',     Bboard.b6b)and Bboard.b5a=='':
            moves = '6b5a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'[BS]',     Bboard.b6b)and Bboard.b7a=='':
            moves = '6b7a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('R',         Bboard.b6b)and Bboard.b5b=='':
            moves = '6b5b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',         Bboard.b6b)and Bboard.b7b=='':
            moves = '6b7b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',         Bboard.b6b)and Bboard.b6c=='':
            moves = '6b6c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',     Bboard.b6b)and Bboard.b5c=='':
            moves = '6b5c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',     Bboard.b6b)and Bboard.b7c=='':
            moves = '6b7c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b6b)and Bboard.b6d==''\
           and board.s6e=='':
            moves = '6b6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b6b)and Bboard.b6d==''\
           and board.s6e=='':
            moves = '6b6d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b6b)and Bboard.b6e==''\
           and board.s6c+board.s6d=='':
            moves = '6b6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b6b)and Bboard.b6e==''\
           and board.s6c+board.s6d=='':
            moves = '6b6e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b6b)and Bboard.b6f==''\
           and board.s6c+board.s6d+board.s6e=='':
            moves = '6b6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b6b)and Bboard.b6f==''\
           and board.s6c+board.s6d+board.s6e=='':
            moves = '6b6f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b6b)and Bboard.b6g==''\
           and board.s6c+board.s6d+board.s6e+board.s6f=='':
            moves = '6b6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b6b)and Bboard.b6g==''\
           and board.s6c+board.s6d+board.s6e+board.s6f=='':
            moves = '6b6g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b6b)and Bboard.b6h==''\
           and board.s6c+board.s6d+board.s6e+board.s6f+board.s6g=='':
            moves = '6b6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b6b)and Bboard.b6h==''\
           and board.s6c+board.s6d+board.s6e+board.s6f+board.s6g=='':
            moves = '6b6h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b6b)and Bboard.b6i==''\
           and board.s6c+board.s6d+board.s6e+board.s6f+board.s6g+board.s6h=='':
            moves = '6b6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b6b)and Bboard.b6i==''\
           and board.s6c+board.s6d+board.s6e+board.s6f+board.s6g+board.s6h=='':
            moves = '6b6i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b6b)and Bboard.b9b==''\
           and board.s8b+board.s7b=='':
            moves = '6b9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b6b)and Bboard.b9b==''\
           and board.s8b+board.s7b=='':
            moves = '6b9b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b6b)and Bboard.b5b==''\
           and board.s7b=='':
            moves = '6b8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b6b)and Bboard.b5b==''\
           and board.s7b=='':
            moves = '6b8b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b6b)and Bboard.b4b==''\
           and board.s5b=='':
            moves = '6b4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b6b)and Bboard.b4b==''\
           and board.s5b=='':
            moves = '6b4b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b6b)and Bboard.b3b==''\
           and board.s5b+board.s4b=='':
            moves = '6b3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b6b)and Bboard.b3b==''\
           and board.s5b+board.s4b=='':
            moves = '6b3b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b6b)and Bboard.b2b==''\
           and board.s5b+board.s4b+board.s3b=='':
            moves = '6b2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b6b)and Bboard.b2b==''\
           and board.s5b+board.s4b+board.s3b=='':
            moves = '6b2b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b6b)and Bboard.b1b==''\
           and board.s5b+board.s4b+board.s3b+board.s2b=='':
            moves = '6b1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b6b)and Bboard.b1b==''\
           and board.s5b+board.s4b+board.s3b+board.s2b=='':
            moves = '6b1b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b6b)and Bboard.b4d==''\
           and board.s5c=='':
            moves = '6b4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b6b)and Bboard.b3e==''\
           and board.s5c+board.s4d=='':
            moves = '6b3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b6b)and Bboard.b2f==''\
           and board.s5c+board.s4d+board.s3e=='':
            moves = '6b2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b6b)and Bboard.b1g==''\
           and board.s5c+board.s4d+board.s3e+board.s2f=='':
            moves = '6b1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b6b)and Bboard.b4d==''\
           and board.s5c=='':
            moves = '6b4d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b6b)and Bboard.b3e==''\
           and board.s5c+board.s4d=='':
            moves = '6b3e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b6b)and Bboard.b2f==''\
           and board.s5c+board.s4d+board.s3e=='':
            moves = '6b2f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b6b)and Bboard.b1g==''\
           and board.s5c+board.s4d+board.s3e+board.s2f=='':
            moves = '6b1g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b6b)and Bboard.b9e==''\
           and board.s8d+board.s7c=='':
            moves = '6b9e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b6b)and Bboard.b8d==''\
           and board.s7c=='':
            moves = '6b8d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b6b)and Bboard.b9e==''\
           and board.s8d+board.s7c=='':
            moves = '6b9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b6b)and Bboard.b8d==''\
           and board.s7c=='':
            moves = '6b8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b7b !='':
        if re.match(r'[SGK+]',    Bboard.b7b)and Bboard.b7a=='':
            moves = '7b7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGK+]',    Bboard.b7b)and Bboard.b6a=='':
            moves = '7b6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGK+]',    Bboard.b7b)and Bboard.b8a=='':
            moves = '7b8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b7b)and Bboard.b6b=='':
            moves = '7b6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b7b)and Bboard.b8b=='':
            moves = '7b8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b7b)and Bboard.b7c=='':
            moves = '7b7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b7b)and Bboard.b6c=='':
            moves = '7b6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b7b)and Bboard.b8c=='':
            moves = '7b8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[PLSR]',   Bboard.b7b)and Bboard.b7a=='':
            moves = '7b7a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',     Bboard.b7b)and Bboard.b6a=='':
            moves = '7b6a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'[BS]',     Bboard.b7b)and Bboard.b8a=='':
            moves = '7b8a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('R',         Bboard.b7b)and Bboard.b6b=='':
            moves = '7b6b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',         Bboard.b7b)and Bboard.b8b=='':
            moves = '7b8b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',         Bboard.b7b)and Bboard.b7c=='':
            moves = '7b7c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',     Bboard.b7b)and Bboard.b6c=='':
            moves = '7b6c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',     Bboard.b7b)and Bboard.b8c=='':
            moves = '7b8c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b7b)and Bboard.b7d==''\
           and board.s7e=='':
            moves = '7b7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b7b)and Bboard.b7d==''\
           and board.s7e=='':
            moves = '7b7d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b7b)and Bboard.b7e==''\
           and board.s7c+board.s7d=='':
            moves = '7b7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b7b)and Bboard.b7e==''\
           and board.s7c+board.s7d=='':
            moves = '7b7e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b7b)and Bboard.b7f==''\
           and board.s7c+board.s7d+board.s7e=='':
            moves = '7b7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b7b)and Bboard.b7f==''\
           and board.s7c+board.s7d+board.s7e=='':
            moves = '7b7f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b7b)and Bboard.b7g==''\
           and board.s7c+board.s7d+board.s7e+board.s7f=='':
            moves = '7b7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b7b)and Bboard.b7g==''\
           and board.s7c+board.s7d+board.s7e+board.s7f=='':
            moves = '7b7g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b7b)and Bboard.b7h==''\
           and board.s7c+board.s7d+board.s7e+board.s7f+board.s7g=='':
            moves = '7b7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b7b)and Bboard.b7h==''\
           and board.s7c+board.s7d+board.s7e+board.s7f+board.s7g=='':
            moves = '7b7h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b7b)and Bboard.b7i==''\
           and board.s7c+board.s7d+board.s7e+board.s7f+board.s7g+board.s7h=='':
            moves = '7b7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b7b)and Bboard.b7i==''\
           and board.s7c+board.s7d+board.s7e+board.s7f+board.s7g+board.s7h=='':
            moves = '7b7i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b7b)and Bboard.b9b==''\
           and board.s8b=='':
            moves = '7b9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b7b)and Bboard.b9b==''\
           and board.s8b=='':
            moves = '7b9b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b7b)and Bboard.b5b==''\
           and board.s6b=='':
            moves = '7b5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b7b)and Bboard.b5b==''\
           and board.s6b=='':
            moves = '7b5b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b7b)and Bboard.b4b==''\
           and board.s6b+board.s5b=='':
            moves = '7b4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b7b)and Bboard.b4b==''\
           and board.s6b+board.s5b=='':
            moves = '7b4b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b7b)and Bboard.b3b==''\
           and board.s6b+board.s5b+board.s4b=='':
            moves = '7b3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b7b)and Bboard.b3b==''\
           and board.s6b+board.s5b+board.s4b=='':
            moves = '7b3b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b7b)and Bboard.b2b==''\
           and board.s6b+board.s5b+board.s4b+board.s3b=='':
            moves = '7b2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b7b)and Bboard.b2b==''\
           and board.s6b+board.s5b+board.s4b+board.s3b=='':
            moves = '7b2b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b7b)and Bboard.b1b==''\
           and board.s6b+board.s5b+board.s4b+board.s3b+board.s2b=='':
            moves = '7b1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b7b)and Bboard.b1b==''\
           and board.s6b+board.s5b+board.s4b+board.s3b+board.s2b=='':
            moves = '7b1b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b7b)and Bboard.b5d==''\
           and board.s6c=='':
            moves = '7b5d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b7b)and Bboard.b4e==''\
           and board.s6c+board.s5d=='':
            moves = '7b4e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b7b)and Bboard.b3f==''\
           and board.s6c+board.s5d+board.s4e=='':
            moves = '7b3f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b7b)and Bboard.b2g==''\
           and board.s6c+board.s5d+board.s4e+board.s3f=='':
            moves = '7b2g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b7b)and Bboard.b1h==''\
           and board.s6c+board.s5d+board.s4e+board.s3f+board.s2g=='':
            moves = '7b1h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b7b)and Bboard.b5d==''\
           and board.s6c=='':
            moves = '7b5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b7b)and Bboard.b4e==''\
           and board.s6c+board.s5d=='':
            moves = '7b4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b7b)and Bboard.b3f==''\
           and board.s6c+board.s5d+board.s4e=='':
            moves = '7b3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b7b)and Bboard.b2g==''\
           and board.s6c+board.s5d+board.s4e+board.s3f=='':
            moves = '7b2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b7b)and Bboard.b1h==''\
           and board.s6c+board.s5d+board.s4e+board.s3f+board.s2g=='':
            moves = '7b1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b7b)and Bboard.b9d==''\
           and board.s8c=='':
            moves = '7b9d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b7b)and Bboard.b9d==''\
           and board.s8c=='':
            moves = '7b9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b8b !='':
        if re.match(r'[SGK+]',    Bboard.b8b)and Bboard.b8a=='':
            moves = '8b8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGK+]',    Bboard.b8b)and Bboard.b7a=='':
            moves = '8b7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGK+]',    Bboard.b8b)and Bboard.b9a=='':
            moves = '8b9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b8b)and Bboard.b7b=='':
            moves = '8b7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b8b)and Bboard.b9b=='':
            moves = '8b9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b8b)and Bboard.b8c=='':
            moves = '8b8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b8b)and Bboard.b7c=='':
            moves = '8b7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b8b)and Bboard.b9c=='':
            moves = '8b9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[PLSR]',   Bboard.b8b)and Bboard.b8a=='':
            moves = '8b8a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',     Bboard.b8b)and Bboard.b7a=='':
            moves = '8b7a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'[BS]',     Bboard.b8b)and Bboard.b9a=='':
            moves = '8b9a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('R',         Bboard.b8b)and Bboard.b7b=='':
            moves = '8b7b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',         Bboard.b8b)and Bboard.b9b=='':
            moves = '8b9b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',         Bboard.b8b)and Bboard.b8c=='':
            moves = '8b8c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',     Bboard.b8b)and Bboard.b7c=='':
            moves = '8b7c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',     Bboard.b8b)and Bboard.b9c=='':
            moves = '8b9c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b8b)and Bboard.b8d==''\
           and board.s8e=='':
            moves = '8b8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b8b)and Bboard.b8d==''\
           and board.s8e=='':
            moves = '8b8d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b8b)and Bboard.b8e==''\
           and board.s8c+board.s8d=='':
            moves = '8b8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b8b)and Bboard.b8e==''\
           and board.s8c+board.s8d=='':
            moves = '8b8e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b8b)and Bboard.b8f==''\
           and board.s8c+board.s8d+board.s8e=='':
            moves = '8b8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b8b)and Bboard.b8f==''\
           and board.s8c+board.s8d+board.s8e=='':
            moves = '8b8f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b8b)and Bboard.b8g==''\
           and board.s8c+board.s8d+board.s8e+board.s8f=='':
            moves = '8b8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b8b)and Bboard.b8g==''\
           and board.s8c+board.s8d+board.s8e+board.s8f=='':
            moves = '8b8g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b8b)and Bboard.b8h==''\
           and board.s8c+board.s8d+board.s8e+board.s8f+board.s8g=='':
            moves = '8b8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b8b)and Bboard.b8h==''\
           and board.s8c+board.s8d+board.s8e+board.s8f+board.s8g=='':
            moves = '8b8h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b8b)and Bboard.b8i==''\
           and board.s8c+board.s8d+board.s8e+board.s8f+board.s8g+board.s8h=='':
            moves = '8b8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b8b)and Bboard.b8i==''\
           and board.s8c+board.s8d+board.s8e+board.s8f+board.s8g+board.s8h=='':
            moves = '8b8i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b8b)and Bboard.b6b==''\
           and board.s7b=='':
            moves = '8b6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b8b)and Bboard.b6b==''\
           and board.s7b=='':
            moves = '8b6b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b8b)and Bboard.b5b==''\
           and board.s7b+board.s6b=='':
            moves = '8b5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b8b)and Bboard.b5b==''\
           and board.s7b+board.s6b=='':
            moves = '8b5b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b8b)and Bboard.b4b==''\
           and board.s7b+board.s6b+board.s5b=='':
            moves = '8b4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b8b)and Bboard.b4b==''\
           and board.s7b+board.s6b+board.s5b=='':
            moves = '8b4b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b8b)and Bboard.b3b==''\
           and board.s7b+board.s6b+board.s5b+board.s4b=='':
            moves = '8b3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b8b)and Bboard.b3b==''\
           and board.s7b+board.s6b+board.s5b+board.s4b=='':
            moves = '8b3b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b8b)and Bboard.b2b==''\
           and board.s7b+board.s6b+board.s5b+board.s4b+board.s3b=='':
            moves = '8b2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b8b)and Bboard.b2b==''\
           and board.s7b+board.s6b+board.s5b+board.s4b+board.s3b=='':
            moves = '8b2b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b8b)and Bboard.b1b==''\
           and board.s7b+board.s6b+board.s5b+board.s4b+board.s3b+board.s2b=='':
            moves = '8b1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b8b)and Bboard.b1b==''\
           and board.s7b+board.s6b+board.s5b+board.s4b+board.s3b+board.s2b=='':
            moves = '8b1b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b8b)and Bboard.b6d==''\
           and board.s7c=='':
            moves = '8b6d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b8b)and Bboard.b5e==''\
           and board.s7c+board.s6d=='':
            moves = '8b5e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b8b)and Bboard.b4f==''\
           and board.s7c+board.s6d+board.s5e=='':
            moves = '8b4f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b8b)and Bboard.b3g==''\
           and board.s7c+board.s6d+board.s5e+board.s4f=='':
            moves = '8b3g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b8b)and Bboard.b2h==''\
           and board.s7c+board.s6d+board.s5e+board.s4f+board.s3g=='':
            moves = '8b2h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b8b)and Bboard.b1i==''\
           and board.s7c+board.s6d+board.s5e+board.s4f+board.s3g+board.s2h=='':
            moves = '8b1i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b8b)and Bboard.b6d==''\
           and board.s7c=='':
            moves = '8b6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b8b)and Bboard.b5e==''\
           and board.s7c+board.s6d=='':
            moves = '8b5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b8b)and Bboard.b4f==''\
           and board.s7c+board.s6d+board.s5e=='':
            moves = '8b4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b8b)and Bboard.b3g==''\
           and board.s7c+board.s6d+board.s5e+board.s4f=='':
            moves = '8b3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b8b)and Bboard.b2h==''\
           and board.s7c+board.s6d+board.s5e+board.s4f+board.s3g=='':
            moves = '8b2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b8b)and Bboard.b1i==''\
           and board.s7c+board.s6d+board.s5e+board.s4f+board.s3g+board.s2h=='':
            moves = '8b1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b9b !='':
        if re.match(r'[SGK+]',    Bboard.b9b)and Bboard.b9a=='':
            moves = '9b9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGK+]',    Bboard.b9b)and Bboard.b8a=='':
            moves = '9b8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b9b)and Bboard.b8b=='':
            moves = '9b8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b9b)and Bboard.b9c=='':
            moves = '9b9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b9b)and Bboard.b8c=='':
            moves = '9b8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[PLSR]',   Bboard.b9b)and Bboard.b9a=='':
            moves = '9b9a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',     Bboard.b9b)and Bboard.b8a=='':
            moves = '9b8a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('R',         Bboard.b9b)and Bboard.b8b=='':
            moves = '9b8b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',         Bboard.b9b)and Bboard.b9c=='':
            moves = '9b9c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',     Bboard.b9b)and Bboard.b8c=='':
            moves = '9b8c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b9b)and Bboard.b9d==''\
           and board.s9e=='':
            moves = '9b9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b9b)and Bboard.b9d==''\
           and board.s9e=='':
            moves = '9b9d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b9b)and Bboard.b9e==''\
           and board.s9c+board.s9d=='':
            moves = '9b9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b9b)and Bboard.b9e==''\
           and board.s9c+board.s9d=='':
            moves = '9b9e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b9b)and Bboard.b9f==''\
           and board.s9c+board.s9d+board.s9e=='':
            moves = '9b9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b9b)and Bboard.b9f==''\
           and board.s9c+board.s9d+board.s9e=='':
            moves = '9b9f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b9b)and Bboard.b9g==''\
           and board.s9c+board.s9d+board.s9e+board.s9f=='':
            moves = '9b9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b9b)and Bboard.b9g==''\
           and board.s9c+board.s9d+board.s9e+board.s9f=='':
            moves = '9b9g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b9b)and Bboard.b9h==''\
           and board.s9c+board.s9d+board.s9e+board.s9f+board.s9g=='':
            moves = '9b9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b9b)and Bboard.b9h==''\
           and board.s9c+board.s9d+board.s9e+board.s9f+board.s9g=='':
            moves = '9b9h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b9b)and Bboard.b9i==''\
           and board.s9c+board.s9d+board.s9e+board.s9f+board.s9g+board.s9h=='':
            moves = '9b9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b9b)and Bboard.b9i==''\
           and board.s9c+board.s9d+board.s9e+board.s9f+board.s9g+board.s9h=='':
            moves = '9b9i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b9b)and Bboard.b7b==''\
           and board.s8b=='':
            moves = '9b7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b9b)and Bboard.b7b==''\
           and board.s8b=='':
            moves = '9b7b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b9b)and Bboard.b6b==''\
           and board.s8b+board.s7b=='':
            moves = '9b6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b9b)and Bboard.b6b==''\
           and board.s8b+board.s7b=='':
            moves = '9b6b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b9b)and Bboard.b5b==''\
           and board.s8b+board.s7b+board.s6b=='':
            moves = '9b5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b9b)and Bboard.b5b==''\
           and board.s8b+board.s7b+board.s6b=='':
            moves = '9b5b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b9b)and Bboard.b4b==''\
           and board.s8b+board.s7b+board.s6b+board.s5b=='':
            moves = '9b4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b9b)and Bboard.b4b==''\
           and board.s8b+board.s7b+board.s6b+board.s5b=='':
            moves = '9b4b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b9b)and Bboard.b3b==''\
           and board.s8b+board.s7b+board.s6b+board.s5b+board.s4b=='':
            moves = '9b3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b9b)and Bboard.b3b==''\
           and board.s8b+board.s7b+board.s6b+board.s5b+board.s4b=='':
            moves = '9b3b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b9b)and Bboard.b2b==''\
           and board.s8b+board.s7b+board.s6b+board.s5b+board.s4b+board.s3b=='':
            moves = '9b2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b9b)and Bboard.b2b==''\
           and board.s8b+board.s7b+board.s6b+board.s5b+board.s4b+board.s3b=='':
            moves = '9b2b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b9b)and Bboard.b1b==''\
           and board.s8b+board.s7b+board.s6b+board.s5b+board.s4b+board.s3b+board.s2b=='':
            moves = '9b1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b9b)and Bboard.b1b==''\
           and board.s8b+board.s7b+board.s6b+board.s5b+board.s4b+board.s3b+board.s2b=='':
            moves = '9b1b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b9b)and Bboard.b7d==''\
           and board.s8c=='':
            moves = '9b7d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b9b)and Bboard.b6e==''\
           and board.s8c+board.s7d=='':
            moves = '9b6e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b9b)and Bboard.b5f==''\
           and board.s8c+board.s7d+board.s6e=='':
            moves = '9b5f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b9b)and Bboard.b4g==''\
           and board.s8c+board.s7d+board.s6e+board.s5f=='':
            moves = '9b4g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b9b)and Bboard.b3h==''\
           and board.s8c+board.s7d+board.s6e+board.s5f+board.s4g=='':
            moves = '9b3h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b9b)and Bboard.b2i==''\
           and board.s8c+board.s7d+board.s6e+board.s5f+board.s4g+board.s3h=='':
            moves = '9b2i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b9b)and Bboard.b7d==''\
           and board.s8c=='':
            moves = '9b7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b9b)and Bboard.b6e==''\
           and board.s8c+board.s7d=='':
            moves = '9b6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b9b)and Bboard.b5f==''\
           and board.s8c+board.s7d+board.s6e=='':
            moves = '9b5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b9b)and Bboard.b4g==''\
           and board.s8c+board.s7d+board.s6e+board.s5f=='':
            moves = '9b4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b9b)and Bboard.b3h==''\
           and board.s8c+board.s7d+board.s6e+board.s5f+board.s4g=='':
            moves = '9b3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b9b)and Bboard.b2i==''\
           and board.s8c+board.s7d+board.s6e+board.s5f+board.s4g+board.s3h=='':
            moves = '9b2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b1c !='':
        if re.match(r'[SGK+]',    Bboard.b1c)and Bboard.b1b=='':
            moves = '1c1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGK+]',    Bboard.b1c)and Bboard.b2b=='':
            moves = '1c2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b1c)and Bboard.b2c=='':
            moves = '1c2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b1c)and Bboard.b1d=='':
            moves = '1c1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b1c)and Bboard.b2d=='':
            moves = '1c2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[PLSR]',   Bboard.b1c)and Bboard.b1b=='':
            moves = '1c1b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',     Bboard.b1c)and Bboard.b2b=='':
            moves = '1c2b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('R',         Bboard.b1c)and Bboard.b2c=='':
            moves = '1c2c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',         Bboard.b1c)and Bboard.b1d=='':
            moves = '1c1d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',     Bboard.b1c)and Bboard.b2d=='':
            moves = '1c2d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b1c)and Bboard.b2a=='':
            moves = '1c2a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b1c)and Bboard.b1a==''\
           and board.s1b=='':
            moves = '1c1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b1c)and Bboard.b1a==''\
           and board.s1b=='':
            moves = '1c1a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b1c)and Bboard.b1e==''\
           and board.s1d=='':
            moves = '1c1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b1c)and Bboard.b1e==''\
           and board.s1d=='':
            moves = '1c1e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b1c)and Bboard.b1f==''\
           and board.s1d+board.s1e=='':
            moves = '1c1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b1c)and Bboard.b1f==''\
           and board.s1d+board.s1e=='':
            moves = '1c1f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b1c)and Bboard.b1g==''\
           and board.s1d+board.s1e+board.s1f=='':
            moves = '1c1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b1c)and Bboard.b1g==''\
           and board.s1d+board.s1e+board.s1f=='':
            moves = '1c1g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b1c)and Bboard.b1h==''\
           and board.s1d+board.s1e+board.s1f+board.s1g=='':
            moves = '1c1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b1c)and Bboard.b1h==''\
           and board.s1d+board.s1e+board.s1f+board.s1g=='':
            moves = '1c1h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b1c)and Bboard.b1i==''\
           and board.s1d+board.s1e+board.s1f+board.s1g+board.s1h=='':
            moves = '1c1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b1c)and Bboard.b1i==''\
           and board.s1d+board.s1e+board.s1f+board.s1g+board.s1h=='':
            moves = '1c1i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b1c)and Bboard.b3c==''\
           and board.s2c=='':
            moves = '1c3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b1c)and Bboard.b3c==''\
           and board.s2c=='':
            moves = '1c3c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b1c)and Bboard.b4c==''\
           and board.s2c+board.s3c=='':
            moves = '1c4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b1c)and Bboard.b4c==''\
           and board.s2c+board.s3c=='':
            moves = '1c4c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b1c)and Bboard.b5c==''\
           and board.s2c+board.s3c+board.s4c=='':
            moves = '1c5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b1c)and Bboard.b5c==''\
           and board.s2c+board.s3c+board.s4c=='':
            moves = '1c5c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b1c)and Bboard.b6c==''\
           and board.s2c+board.s3c+board.s4c+board.s5c=='':
            moves = '1c6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b1c)and Bboard.b6c==''\
           and board.s2c+board.s3c+board.s4c+board.s5c=='':
            moves = '1c6c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b1c)and Bboard.b7c==''\
           and board.s2c+board.s3c+board.s4c+board.s5c+board.s6c=='':
            moves = '1c7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b1c)and Bboard.b7c==''\
           and board.s2c+board.s3c+board.s4c+board.s5c+board.s6c=='':
            moves = '1c7c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b1c)and Bboard.b8c==''\
           and board.s2c+board.s3c+board.s4c+board.s5c+board.s6c+board.s7c=='':
            moves = '1c8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b1c)and Bboard.b8c==''\
           and board.s2c+board.s3c+board.s4c+board.s5c+board.s6c+board.s7c=='':
            moves = '1c8c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b1c)and Bboard.b9c==''\
           and board.s2c+board.s3c+board.s4c+board.s5c+board.s6c+board.s7c+board.s8c=='':
            moves = '1c9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b1c)and Bboard.b9c==''\
           and board.s2c+board.s3c+board.s4c+board.s5c+board.s6c+board.s7c+board.s8c=='':
            moves = '1c9c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b1c)and Bboard.b3a==''\
           and board.s2b=='':
            moves = '1c3a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b1c)and Bboard.b3e==''\
           and board.s2d=='':
            moves = '1c3e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b1c)and Bboard.b4f==''\
           and board.s2d+board.s3e=='':
            moves = '1c4f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b1c)and Bboard.b5g==''\
           and board.s2d+board.s3e+board.s4f=='':
            moves = '1c5g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b1c)and Bboard.b6h==''\
           and board.s2d+board.s3e+board.s4f+board.s5g=='':
            moves = '1c6h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b1c)and Bboard.b7i==''\
           and board.s2d+board.s3e+board.s4f+board.s5g+board.s6h=='':
            moves = '1c7i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b1c)and Bboard.b3a==''\
           and board.s2b=='':
            moves = '1c3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b1c)and Bboard.b3e==''\
           and board.s2d=='':
            moves = '1c3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b1c)and Bboard.b4f==''\
           and board.s2d+board.s3e=='':
            moves = '1c4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b1c)and Bboard.b5g==''\
           and board.s2d+board.s3e+board.s4f=='':
            moves = '1c5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b1c)and Bboard.b6h==''\
           and board.s2d+board.s3e+board.s4f+board.s5g=='':
            moves = '1c6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b1c)and Bboard.b7i==''\
           and board.s2d+board.s3e+board.s4f+board.s5g+board.s6h=='':
            moves = '1c7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b2c !='':
        if re.match(r'[SGK+]',    Bboard.b2c)and Bboard.b2b=='':
            moves = '2c2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGK+]',    Bboard.b2c)and Bboard.b1b=='':
            moves = '2c1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGK+]',    Bboard.b2c)and Bboard.b3b=='':
            moves = '2c3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b2c)and Bboard.b1c=='':
            moves = '2c1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b2c)and Bboard.b3c=='':
            moves = '2c3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b2c)and Bboard.b2d=='':
            moves = '2c2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b2c)and Bboard.b1d=='':
            moves = '2c1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b2c)and Bboard.b3d=='':
            moves = '2c3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[PLSR]',   Bboard.b2c)and Bboard.b2b=='':
            moves = '2c2b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',     Bboard.b2c)and Bboard.b1b=='':
            moves = '2c1b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'[BS]',     Bboard.b2c)and Bboard.b3b=='':
            moves = '2c3b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('R',         Bboard.b2c)and Bboard.b1c=='':
            moves = '2c1c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',         Bboard.b2c)and Bboard.b3c=='':
            moves = '2c3c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',         Bboard.b2c)and Bboard.b2d=='':
            moves = '2c2d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',     Bboard.b2c)and Bboard.b1d=='':
            moves = '2c1d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',     Bboard.b2c)and Bboard.b3d=='':
            moves = '2c3d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b2c)and Bboard.b1a=='':
            moves = '2c1a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b2c)and Bboard.b3a=='':
            moves = '2c3a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b2c)and Bboard.b2a==''\
           and board.s2b=='':
            moves = '2c2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b2c)and Bboard.b2a==''\
           and board.s2b=='':
            moves = '2c2a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b2c)and Bboard.b2e==''\
           and board.s2d=='':
            moves = '2c2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b2c)and Bboard.b2e==''\
           and board.s2d=='':
            moves = '2c2e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b2c)and Bboard.b2f==''\
           and board.s2d+board.s2e=='':
            moves = '2c2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b2c)and Bboard.b2f==''\
           and board.s2d+board.s2e=='':
            moves = '2c2f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b2c)and Bboard.b2g==''\
           and board.s2d+board.s2e+board.s2f=='':
            moves = '2c2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b2c)and Bboard.b2g==''\
           and board.s2d+board.s2e+board.s2f=='':
            moves = '2c2g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b2c)and Bboard.b2h==''\
           and board.s2d+board.s2e+board.s2f+board.s2g=='':
            moves = '2c2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b2c)and Bboard.b2h==''\
           and board.s2d+board.s2e+board.s2f+board.s2g=='':
            moves = '2c2h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b2c)and Bboard.b2i==''\
           and board.s2d+board.s2e+board.s2f+board.s2g+board.s2h=='':
            moves = '2c2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b2c)and Bboard.b2i==''\
           and board.s2d+board.s2e+board.s2f+board.s2g+board.s2h=='':
            moves = '2c2i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b2c)and Bboard.b4c==''\
           and board.s3c=='':
            moves = '2c4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b2c)and Bboard.b4c==''\
           and board.s3c=='':
            moves = '2c4c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b2c)and Bboard.b5c==''\
           and board.s3c+board.s4c=='':
            moves = '2c5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b2c)and Bboard.b5c==''\
           and board.s3c+board.s4c=='':
            moves = '2c5c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b2c)and Bboard.b6c==''\
           and board.s3c+board.s4c+board.s5c=='':
            moves = '2c6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b2c)and Bboard.b6c==''\
           and board.s3c+board.s4c+board.s5c=='':
            moves = '2c6c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b2c)and Bboard.b7c==''\
           and board.s3c+board.s4c+board.s5c+board.s6c=='':
            moves = '2c7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b2c)and Bboard.b7c==''\
           and board.s3c+board.s4c+board.s5c+board.s6c=='':
            moves = '2c7c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b2c)and Bboard.b8c==''\
           and board.s3c+board.s4c+board.s5c+board.s6c+board.s7c=='':
            moves = '2c8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b2c)and Bboard.b8c==''\
           and board.s3c+board.s4c+board.s5c+board.s6c+board.s7c=='':
            moves = '2c8c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b2c)and Bboard.b9c==''\
           and board.s3c+board.s4c+board.s5c+board.s6c+board.s7c+board.s8c=='':
            moves = '2c9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b2c)and Bboard.b9c==''\
           and board.s3c+board.s4c+board.s5c+board.s6c+board.s7c+board.s8c=='':
            moves = '2c9c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b2c)and Bboard.b4e==''\
           and board.s3d=='':
            moves = '2c4e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b2c)and Bboard.b5f==''\
           and board.s3d+board.s4e=='':
            moves = '2c5f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b2c)and Bboard.b6g==''\
           and board.s3d+board.s4e+board.s5f=='':
            moves = '2c6g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b2c)and Bboard.b7h==''\
           and board.s3d+board.s4e+board.s5f+board.s6g=='':
            moves = '2c7h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b2c)and Bboard.b8i==''\
           and board.s3d+board.s4e+board.s5f+board.s6g+board.s7h=='':
            moves = '2c8i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b2c)and Bboard.b4e==''\
           and board.s3d=='':
            moves = '2c4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b2c)and Bboard.b5f==''\
           and board.s3d+board.s4e=='':
            moves = '2c5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b2c)and Bboard.b6g==''\
           and board.s3d+board.s4e+board.s5f=='':
            moves = '2c6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b2c)and Bboard.b7h==''\
           and board.s3d+board.s4e+board.s5f+board.s6g=='':
            moves = '2c7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b2c)and Bboard.b8i==''\
           and board.s3d+board.s4e+board.s5f+board.s6g+board.s7h=='':
            moves = '2c8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b2c)and Bboard.b4a==''\
           and board.s3b=='':
            moves = '2c4a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b2c)and Bboard.b4a==''\
           and board.s3b=='':
            moves = '2c4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b3c !='':
        if re.match(r'[SGK+]',    Bboard.b3c)and Bboard.b3b=='':
            moves = '3c3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGK+]',    Bboard.b3c)and Bboard.b2b=='':
            moves = '3c2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGK+]',    Bboard.b3c)and Bboard.b4b=='':
            moves = '3c4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b3c)and Bboard.b2c=='':
            moves = '3c2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b3c)and Bboard.b4c=='':
            moves = '3c4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b3c)and Bboard.b3d=='':
            moves = '3c3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b3c)and Bboard.b2d=='':
            moves = '3c2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b3c)and Bboard.b4d=='':
            moves = '3c4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[PLSR]',   Bboard.b3c)and Bboard.b3b=='':
            moves = '3c3b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',     Bboard.b3c)and Bboard.b2b=='':
            moves = '3c2b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'[BS]',     Bboard.b3c)and Bboard.b4b=='':
            moves = '3c4b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('R',         Bboard.b3c)and Bboard.b2c=='':
            moves = '3c2c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',         Bboard.b3c)and Bboard.b4c=='':
            moves = '3c4c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',         Bboard.b3c)and Bboard.b3d=='':
            moves = '3c3d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',     Bboard.b3c)and Bboard.b2d=='':
            moves = '3c2d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',     Bboard.b3c)and Bboard.b4d=='':
            moves = '3c4d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b3c)and Bboard.b2a=='':
            moves = '3c2a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b3c)and Bboard.b4a=='':
            moves = '3c4a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b3c)and Bboard.b3a==''\
           and board.s3b=='':
            moves = '3c3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b3c)and Bboard.b3a==''\
           and board.s3b=='':
            moves = '3c3a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b3c)and Bboard.b3e==''\
           and board.s3d=='':
            moves = '3c3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b3c)and Bboard.b3e==''\
           and board.s3d=='':
            moves = '3c3e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b3c)and Bboard.b3f==''\
           and board.s3d+board.s3e=='':
            moves = '3c3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b3c)and Bboard.b3f==''\
           and board.s3d+board.s3e=='':
            moves = '3c3f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b3c)and Bboard.b3g==''\
           and board.s3d+board.s3e+board.s3f=='':
            moves = '3c3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b3c)and Bboard.b3g==''\
           and board.s3d+board.s3e+board.s3f=='':
            moves = '3c3g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b3c)and Bboard.b3h==''\
           and board.s3d+board.s3e+board.s3f+board.s3g=='':
            moves = '3c3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b3c)and Bboard.b3h==''\
           and board.s3d+board.s3e+board.s3f+board.s3g=='':
            moves = '3c3h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b3c)and Bboard.b3i==''\
           and board.s3d+board.s3e+board.s3f+board.s3g+board.s3h=='':
            moves = '3c3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b3c)and Bboard.b3i==''\
           and board.s3d+board.s3e+board.s3f+board.s3g+board.s3h=='':
            moves = '3c3i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b3c)and Bboard.b1c==''\
           and board.s2c=='':
            moves = '3c1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b3c)and Bboard.b1c==''\
           and board.s2c=='':
            moves = '3c1c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b3c)and Bboard.b5c==''\
           and board.s4c=='':
            moves = '3c5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b3c)and Bboard.b5c==''\
           and board.s4c=='':
            moves = '3c5c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b3c)and Bboard.b6c==''\
           and board.s4c+board.s5c=='':
            moves = '3c6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b3c)and Bboard.b6c==''\
           and board.s4c+board.s5c=='':
            moves = '3c6c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b3c)and Bboard.b7c==''\
           and board.s4c+board.s5c+board.s6c=='':
            moves = '3c7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b3c)and Bboard.b7c==''\
           and board.s4c+board.s5c+board.s6c=='':
            moves = '3c7c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b3c)and Bboard.b8c==''\
           and board.s4c+board.s5c+board.s6c+board.s7c=='':
            moves = '3c8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b3c)and Bboard.b8c==''\
           and board.s4c+board.s5c+board.s6c+board.s7c=='':
            moves = '3c8c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b3c)and Bboard.b9c==''\
           and board.s4c+board.s5c+board.s6c+board.s7c+board.s8c=='':
            moves = '3c9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b3c)and Bboard.b9c==''\
           and board.s4c+board.s5c+board.s6c+board.s7c+board.s8c=='':
            moves = '3c9c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b3c)and Bboard.b1a==''\
           and board.s2b=='':
            moves = '3c1a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b3c)and Bboard.b5e==''\
           and board.s4d=='':
            moves = '3c5e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b3c)and Bboard.b6f==''\
           and board.s4d+board.s5e=='':
            moves = '3c6f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b3c)and Bboard.b7g==''\
           and board.s4d+board.s5e+board.s6f=='':
            moves = '3c7g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b3c)and Bboard.b8h==''\
           and board.s4d+board.s5e+board.s6f+board.s7g=='':
            moves = '3c8h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b3c)and Bboard.b9i==''\
           and board.s4d+board.s5e+board.s6f+board.s7g+board.s8h=='':
            moves = '3c9i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b3c)and Bboard.b1a==''\
           and board.s2b=='':
            moves = '3c1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b3c)and Bboard.b5e==''\
           and board.s4d=='':
            moves = '3c5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b3c)and Bboard.b6f==''\
           and board.s4d+board.s5e=='':
            moves = '3c6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b3c)and Bboard.b7g==''\
           and board.s4d+board.s5e+board.s6f=='':
            moves = '3c7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b3c)and Bboard.b8h==''\
           and board.s4d+board.s5e+board.s6f+board.s7g=='':
            moves = '3c8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b3c)and Bboard.b9i==''\
           and board.s4d+board.s5e+board.s6f+board.s7g+board.s8h=='':
            moves = '3c9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b3c)and Bboard.b5a==''\
           and board.s4b=='':
            moves = '3c5a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b3c)and Bboard.b1e==''\
           and board.s2d=='':
            moves = '3c1e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b3c)and Bboard.b5a==''\
           and board.s4b=='':
            moves = '3c5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b3c)and Bboard.b1e==''\
           and board.s2d=='':
            moves = '3c1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b4c !='':
        if re.match(r'[SGK+]',    Bboard.b4c)and Bboard.b4b=='':
            moves = '4c4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGK+]',    Bboard.b4c)and Bboard.b3b=='':
            moves = '4c3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGK+]',    Bboard.b4c)and Bboard.b5b=='':
            moves = '4c5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b4c)and Bboard.b3c=='':
            moves = '4c3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b4c)and Bboard.b5c=='':
            moves = '4c5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b4c)and Bboard.b4d=='':
            moves = '4c4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b4c)and Bboard.b3d=='':
            moves = '4c3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b4c)and Bboard.b5d=='':
            moves = '4c5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[PLSR]',   Bboard.b4c)and Bboard.b4b=='':
            moves = '4c4b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',     Bboard.b4c)and Bboard.b3b=='':
            moves = '4c3b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'[BS]',     Bboard.b4c)and Bboard.b5b=='':
            moves = '4c5b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('R',         Bboard.b4c)and Bboard.b3c=='':
            moves = '4c3c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',         Bboard.b4c)and Bboard.b5c=='':
            moves = '4c5c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',         Bboard.b4c)and Bboard.b4d=='':
            moves = '4c4d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',     Bboard.b4c)and Bboard.b3d=='':
            moves = '4c3d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',     Bboard.b4c)and Bboard.b5d=='':
            moves = '4c5d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b4c)and Bboard.b3a=='':
            moves = '4c3a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b4c)and Bboard.b5a=='':
            moves = '4c5a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b4c)and Bboard.b4a==''\
           and board.s4b=='':
            moves = '4c4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b4c)and Bboard.b4a==''\
           and board.s4b=='':
            moves = '4c4a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b4c)and Bboard.b4e==''\
           and board.s4d=='':
            moves = '4c4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b4c)and Bboard.b4e==''\
           and board.s4d=='':
            moves = '4c4e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b4c)and Bboard.b4f==''\
           and board.s4d+board.s4e=='':
            moves = '4c4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b4c)and Bboard.b4f==''\
           and board.s4d+board.s4e=='':
            moves = '4c4f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b4c)and Bboard.b4g==''\
           and board.s4d+board.s4e+board.s4f=='':
            moves = '4c4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b4c)and Bboard.b4g==''\
           and board.s4d+board.s4e+board.s4f=='':
            moves = '4c4g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b4c)and Bboard.b4h==''\
           and board.s4d+board.s4e+board.s4f+board.s4g=='':
            moves = '4c4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b4c)and Bboard.b4h==''\
           and board.s4d+board.s4e+board.s4f+board.s4g=='':
            moves = '4c4h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b4c)and Bboard.b4i==''\
           and board.s4d+board.s4e+board.s4f+board.s4g+board.s4h=='':
            moves = '4c4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b4c)and Bboard.b4i==''\
           and board.s4d+board.s4e+board.s4f+board.s4g+board.s4h=='':
            moves = '4c4i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b4c)and Bboard.b1c==''\
           and board.s2c+board.s3c=='':
            moves = '4c1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b4c)and Bboard.b1c==''\
           and board.s2c+board.s3c=='':
            moves = '4c1c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b4c)and Bboard.b5c==''\
           and board.s3c=='':
            moves = '4c2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b4c)and Bboard.b5c==''\
           and board.s3c=='':
            moves = '4c2c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b4c)and Bboard.b6c==''\
           and board.s5c=='':
            moves = '4c6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b4c)and Bboard.b6c==''\
           and board.s5c=='':
            moves = '4c6c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b4c)and Bboard.b7c==''\
           and board.s5c+board.s6c=='':
            moves = '4c7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b4c)and Bboard.b7c==''\
           and board.s5c+board.s6c=='':
            moves = '4c7c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b4c)and Bboard.b8c==''\
           and board.s5c+board.s6c+board.s7c=='':
            moves = '4c8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b4c)and Bboard.b8c==''\
           and board.s5c+board.s6c+board.s7c=='':
            moves = '4c8c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b4c)and Bboard.b9c==''\
           and board.s5c+board.s6c+board.s7c+board.s8c=='':
            moves = '4c9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b4c)and Bboard.b9c==''\
           and board.s5c+board.s6c+board.s7c+board.s8c=='':
            moves = '4c9c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b4c)and Bboard.b6e==''\
           and board.s5d=='':
            moves = '4c6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b4c)and Bboard.b7f==''\
           and board.s5d+board.s6e=='':
            moves = '4c7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b4c)and Bboard.b8g==''\
           and board.s5d+board.s6e+board.s7f=='':
            moves = '4c8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b4c)and Bboard.b9h==''\
           and board.s5d+board.s6e+board.s7f+board.s8g=='':
            moves = '4c9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b4c)and Bboard.b6e==''\
           and board.s5d=='':
            moves = '4c6e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b4c)and Bboard.b7f==''\
           and board.s5d+board.s6e=='':
            moves = '4c7f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b4c)and Bboard.b8g==''\
           and board.s5d+board.s6e+board.s7f=='':
            moves = '4c8g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b4c)and Bboard.b9h==''\
           and board.s5d+board.s6e+board.s7f+board.s8g=='':
            moves = '4c9h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b4c)and Bboard.b1f==''\
           and board.s2e+board.s3d=='':
            moves = '4c1f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b4c)and Bboard.b2e==''\
           and board.s3d=='':
            moves = '4c2e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b4c)and Bboard.b1f==''\
           and board.s2e+board.s3d=='':
            moves = '4c1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b4c)and Bboard.b2e==''\
           and board.s3d=='':
            moves = '4c2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b4c)and Bboard.b2a==''\
           and board.s3b=='':
            moves = '4c2a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b4c)and Bboard.b2a==''\
           and board.s3b=='':
            moves = '4c2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b4c)and Bboard.b6a==''\
           and board.s5b=='':
            moves = '4c6a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b4c)and Bboard.b6a==''\
           and board.s5b=='':
            moves = '4c6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b5c !='':
        if re.match(r'[SGK+]',    Bboard.b5c)and Bboard.b5b=='':
            moves = '5c5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGK+]',    Bboard.b5c)and Bboard.b4b=='':
            moves = '5c4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGK+]',    Bboard.b5c)and Bboard.b6b=='':
            moves = '5c6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b5c)and Bboard.b4c=='':
            moves = '5c4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b5c)and Bboard.b6c=='':
            moves = '5c6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b5c)and Bboard.b5d=='':
            moves = '5c5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b5c)and Bboard.b4d=='':
            moves = '5c4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b5c)and Bboard.b6d=='':
            moves = '5c6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[PLSR]',   Bboard.b5c)and Bboard.b5b=='':
            moves = '5c5b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',     Bboard.b5c)and Bboard.b4b=='':
            moves = '5c4b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'[BS]',     Bboard.b5c)and Bboard.b6b=='':
            moves = '5c6b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('R',         Bboard.b5c)and Bboard.b4c=='':
            moves = '5c4c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',         Bboard.b5c)and Bboard.b6c=='':
            moves = '5c6c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',         Bboard.b5c)and Bboard.b5d=='':
            moves = '5c5d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',     Bboard.b5c)and Bboard.b4d=='':
            moves = '5c4d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',     Bboard.b5c)and Bboard.b6d=='':
            moves = '5c6d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b5c)and Bboard.b4a=='':
            moves = '5c4a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b5c)and Bboard.b6a=='':
            moves = '5c6a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b5c)and Bboard.b5a==''\
           and board.s5b=='':
            moves = '5c5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b5c)and Bboard.b5a==''\
           and board.s5b=='':
            moves = '5c5a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b5c)and Bboard.b5e==''\
           and board.s5d=='':
            moves = '5c5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b5c)and Bboard.b5e==''\
           and board.s5d=='':
            moves = '5c5e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b5c)and Bboard.b5f==''\
           and board.s5d+board.s5e=='':
            moves = '5c5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b5c)and Bboard.b5f==''\
           and board.s5d+board.s5e=='':
            moves = '5c5f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b5c)and Bboard.b5g==''\
           and board.s5d+board.s5e+board.s5f=='':
            moves = '5c5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b5c)and Bboard.b5g==''\
           and board.s5d+board.s5e+board.s5f=='':
            moves = '5c5g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b5c)and Bboard.b5h==''\
           and board.s5d+board.s5e+board.s5f+board.s5g=='':
            moves = '5c5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b5c)and Bboard.b5h==''\
           and board.s5d+board.s5e+board.s5f+board.s5g=='':
            moves = '5c5h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b5c)and Bboard.b5i==''\
           and board.s5d+board.s5e+board.s5f+board.s5g+board.s5h=='':
            moves = '5c5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b5c)and Bboard.b5i==''\
           and board.s5d+board.s5e+board.s5f+board.s5g+board.s5h=='':
            moves = '5c5i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b5c)and Bboard.b1c==''\
           and board.s2c+board.s3c+board.s4c=='':
            moves = '5c1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b5c)and Bboard.b1c==''\
           and board.s2c+board.s3c+board.s4c=='':
            moves = '5c1c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b5c)and Bboard.b2c==''\
           and board.s3c+board.s4c=='':
            moves = '5c2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b5c)and Bboard.b2c==''\
           and board.s3c+board.s4c=='':
            moves = '5c2c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b5c)and Bboard.b3c==''\
           and board.s4c=='':
            moves = '5c3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b5c)and Bboard.b3c==''\
           and board.s4c=='':
            moves = '5c3c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b5c)and Bboard.b7c==''\
           and board.s6c=='':
            moves = '5c7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b5c)and Bboard.b7c==''\
           and board.s6c=='':
            moves = '5c7c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b5c)and Bboard.b8c==''\
           and board.s6c+board.s7c=='':
            moves = '5c8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b5c)and Bboard.b8c==''\
           and board.s6c+board.s7c=='':
            moves = '5c8c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b5c)and Bboard.b9c==''\
           and board.s6c+board.s7c+board.s8c=='':
            moves = '5c9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b5c)and Bboard.b9c==''\
           and board.s6c+board.s7c+board.s8c=='':
            moves = '5c9c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b5c)and Bboard.b7e==''\
           and board.s6d=='':
            moves = '5c7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b5c)and Bboard.b8f==''\
           and board.s6d+board.s7e=='':
            moves = '5c8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b5c)and Bboard.b9g==''\
           and board.s6d+board.s7e+board.s8f=='':
            moves = '5c9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b5c)and Bboard.b7e==''\
           and board.s6d=='':
            moves = '5c7e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b5c)and Bboard.b8f==''\
           and board.s6d+board.s7e=='':
            moves = '5c8f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b5c)and Bboard.b9g==''\
           and board.s6d+board.s7e+board.s8f=='':
            moves = '5c9g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b5c)and Bboard.b2f==''\
           and board.s3e+board.s4d=='':
            moves = '5c2f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b5c)and Bboard.b3e==''\
           and board.s4d=='':
            moves = '5c3e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b5c)and Bboard.b2f==''\
           and board.s3e+board.s4d=='':
            moves = '5c2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b5c)and Bboard.b3e==''\
           and board.s4d=='':
            moves = '5c3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b5c)and Bboard.b1g==''\
           and board.s4d+board.s3e+board.s2f=='':
            moves = '5c1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b5c)and Bboard.b1g==''\
           and board.s4d+board.s3e+board.s2f=='':
            moves = '5c1g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b5c)and Bboard.b3a==''\
           and board.s4b=='':
            moves = '5c3a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b5c)and Bboard.b3a==''\
           and board.s4b=='':
            moves = '5c3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b5c)and Bboard.b7a==''\
           and board.s6b=='':
            moves = '5c7a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b5c)and Bboard.b7a==''\
           and board.s6b=='':
            moves = '5c7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b6c !='':
        if re.match(r'[SGK+]',    Bboard.b6c)and Bboard.b6b=='':
            moves = '6c6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGK+]',    Bboard.b6c)and Bboard.b5b=='':
            moves = '6c5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGK+]',    Bboard.b6c)and Bboard.b7b=='':
            moves = '6c7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b6c)and Bboard.b5c=='':
            moves = '6c5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b6c)and Bboard.b7c=='':
            moves = '6c7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b6c)and Bboard.b6d=='':
            moves = '6c6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b6c)and Bboard.b5d=='':
            moves = '6c5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b6c)and Bboard.b7d=='':
            moves = '6c7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[PLSR]',   Bboard.b6c)and Bboard.b6b=='':
            moves = '6c6b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',     Bboard.b6c)and Bboard.b5b=='':
            moves = '6c5b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'[BS]',     Bboard.b6c)and Bboard.b7b=='':
            moves = '6c7b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('R',         Bboard.b6c)and Bboard.b5c=='':
            moves = '6c5c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',         Bboard.b6c)and Bboard.b7c=='':
            moves = '6c7c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',         Bboard.b6c)and Bboard.b6d=='':
            moves = '6c6d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',     Bboard.b6c)and Bboard.b5d=='':
            moves = '6c5d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',     Bboard.b6c)and Bboard.b7d=='':
            moves = '6c7d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b6c)and Bboard.b5a=='':
            moves = '6c5a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b6c)and Bboard.b7a=='':
            moves = '6c7a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b6c)and Bboard.b6a==''\
           and board.s6b=='':
            moves = '6c6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b6c)and Bboard.b6a==''\
           and board.s6b=='':
            moves = '6c6a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b6c)and Bboard.b6e==''\
           and board.s6d=='':
            moves = '6c6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b6c)and Bboard.b6e==''\
           and board.s6d=='':
            moves = '6c6e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b6c)and Bboard.b6f==''\
           and board.s6d+board.s6e=='':
            moves = '6c6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b6c)and Bboard.b6f==''\
           and board.s6d+board.s6e=='':
            moves = '6c6f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b6c)and Bboard.b6g==''\
           and board.s6d+board.s6e+board.s6f=='':
            moves = '6c6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b6c)and Bboard.b6g==''\
           and board.s6d+board.s6e+board.s6f=='':
            moves = '6c6g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b6c)and Bboard.b6h==''\
           and board.s6d+board.s6e+board.s6f+board.s6g=='':
            moves = '6c6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b6c)and Bboard.b6h==''\
           and board.s6d+board.s6e+board.s6f+board.s6g=='':
            moves = '6c6h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b6c)and Bboard.b6i==''\
           and board.s6d+board.s6e+board.s6f+board.s6g+board.s6h=='':
            moves = '6c6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b6c)and Bboard.b6i==''\
           and board.s6d+board.s6e+board.s6f+board.s6g+board.s6h=='':
            moves = '6c6i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b6c)and Bboard.b9c==''\
           and board.s8c+board.s7c=='':
            moves = '6c9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b6c)and Bboard.b9c==''\
           and board.s8c+board.s7c=='':
            moves = '6c9c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b6c)and Bboard.b5c==''\
           and board.s7c=='':
            moves = '6c8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b6c)and Bboard.b5c==''\
           and board.s7c=='':
            moves = '6c8c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b6c)and Bboard.b4c==''\
           and board.s5c=='':
            moves = '6c4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b6c)and Bboard.b4c==''\
           and board.s5c=='':
            moves = '6c4c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b6c)and Bboard.b3c==''\
           and board.s5c+board.s4c=='':
            moves = '6c3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b6c)and Bboard.b3c==''\
           and board.s5c+board.s4c=='':
            moves = '6c3c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b6c)and Bboard.b2c==''\
           and board.s5c+board.s4c+board.s3c=='':
            moves = '6c2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b6c)and Bboard.b2c==''\
           and board.s5c+board.s4c+board.s3c=='':
            moves = '6c2c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b6c)and Bboard.b1c==''\
           and board.s5c+board.s4c+board.s3c+board.s2c=='':
            moves = '6c1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b6c)and Bboard.b1c==''\
           and board.s5c+board.s4c+board.s3c+board.s2c=='':
            moves = '6c1c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b6c)and Bboard.b4e==''\
           and board.s5d=='':
            moves = '6c4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b6c)and Bboard.b3f==''\
           and board.s5d+board.s4e=='':
            moves = '6c3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b6c)and Bboard.b2g==''\
           and board.s5d+board.s4e+board.s3f=='':
            moves = '6c2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b6c)and Bboard.b1h==''\
           and board.s5d+board.s4e+board.s3f+board.s2g=='':
            moves = '6c1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b6c)and Bboard.b4e==''\
           and board.s5d=='':
            moves = '6c4e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b6c)and Bboard.b3f==''\
           and board.s5d+board.s4e=='':
            moves = '6c3f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b6c)and Bboard.b2g==''\
           and board.s5d+board.s4e+board.s3f=='':
            moves = '6c2g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b6c)and Bboard.b1h==''\
           and board.s5d+board.s4e+board.s3f+board.s2g=='':
            moves = '6c1h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b6c)and Bboard.b9f==''\
           and board.s8e+board.s7d=='':
            moves = '6c9f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b6c)and Bboard.b8e==''\
           and board.s7d=='':
            moves = '6c8e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b6c)and Bboard.b9f==''\
           and board.s8e+board.s7d=='':
            moves = '6c9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b6c)and Bboard.b8e==''\
           and board.s7d=='':
            moves = '6c8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b6c)and Bboard.b8a==''\
           and board.s7b=='':
            moves = '6c8a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b6c)and Bboard.b8a==''\
           and board.s7b=='':
            moves = '6c8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b6c)and Bboard.b4a==''\
           and board.s5b=='':
            moves = '6c4a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b6c)and Bboard.b4a==''\
           and board.s5b=='':
            moves = '6c4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b7c !='':
        if re.match(r'[SGK+]',    Bboard.b7c)and Bboard.b7b=='':
            moves = '7c7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGK+]',    Bboard.b7c)and Bboard.b6b=='':
            moves = '7c6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGK+]',    Bboard.b7c)and Bboard.b8b=='':
            moves = '7c8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b7c)and Bboard.b6c=='':
            moves = '7c6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b7c)and Bboard.b8c=='':
            moves = '7c8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b7c)and Bboard.b7d=='':
            moves = '7c7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b7c)and Bboard.b6d=='':
            moves = '7c6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b7c)and Bboard.b8d=='':
            moves = '7c8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[PLSR]',   Bboard.b7c)and Bboard.b7b=='':
            moves = '7c7b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',     Bboard.b7c)and Bboard.b6b=='':
            moves = '7c6b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'[BS]',     Bboard.b7c)and Bboard.b8b=='':
            moves = '7c8b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('R',         Bboard.b7c)and Bboard.b6c=='':
            moves = '7c6c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',         Bboard.b7c)and Bboard.b8c=='':
            moves = '7c8c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',         Bboard.b7c)and Bboard.b7d=='':
            moves = '7c7d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',     Bboard.b7c)and Bboard.b6d=='':
            moves = '7c6d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',     Bboard.b7c)and Bboard.b8d=='':
            moves = '7c8d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b7c)and Bboard.b6a=='':
            moves = '7c6a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b7c)and Bboard.b8a=='':
            moves = '7c8a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b7c)and Bboard.b7a==''\
           and board.s7b=='':
            moves = '7c7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b7c)and Bboard.b7a==''\
           and board.s7b=='':
            moves = '7c7a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b7c)and Bboard.b7e==''\
           and board.s7d=='':
            moves = '7c7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b7c)and Bboard.b7e==''\
           and board.s7d=='':
            moves = '7c7e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b7c)and Bboard.b7f==''\
           and board.s7d+board.s7e=='':
            moves = '7c7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b7c)and Bboard.b7f==''\
           and board.s7d+board.s7e=='':
            moves = '7c7f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b7c)and Bboard.b7g==''\
           and board.s7d+board.s7e+board.s7f=='':
            moves = '7c7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b7c)and Bboard.b7g==''\
           and board.s7d+board.s7e+board.s7f=='':
            moves = '7c7g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b7c)and Bboard.b7h==''\
           and board.s7d+board.s7e+board.s7f+board.s7g=='':
            moves = '7c7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b7c)and Bboard.b7h==''\
           and board.s7d+board.s7e+board.s7f+board.s7g=='':
            moves = '7c7h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b7c)and Bboard.b7i==''\
           and board.s7d+board.s7e+board.s7f+board.s7g+board.s7h=='':
            moves = '7c7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b7c)and Bboard.b7i==''\
           and board.s7d+board.s7e+board.s7f+board.s7g+board.s7h=='':
            moves = '7c7i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b7c)and Bboard.b9c==''\
           and board.s8c=='':
            moves = '7c9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b7c)and Bboard.b9c==''\
           and board.s8c=='':
            moves = '7c9c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b7c)and Bboard.b5c==''\
           and board.s6c=='':
            moves = '7c5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b7c)and Bboard.b5c==''\
           and board.s6c=='':
            moves = '7c5c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b7c)and Bboard.b4c==''\
           and board.s6c+board.s5c=='':
            moves = '7c4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b7c)and Bboard.b4c==''\
           and board.s6c+board.s5c=='':
            moves = '7c4c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b7c)and Bboard.b3c==''\
           and board.s6c+board.s5c+board.s4c=='':
            moves = '7c3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b7c)and Bboard.b3c==''\
           and board.s6c+board.s5c+board.s4c=='':
            moves = '7c3c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b7c)and Bboard.b2c==''\
           and board.s6c+board.s5c+board.s4c+board.s3c=='':
            moves = '7c2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b7c)and Bboard.b2c==''\
           and board.s6c+board.s5c+board.s4c+board.s3c=='':
            moves = '7c2c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b7c)and Bboard.b1c==''\
           and board.s6c+board.s5c+board.s4c+board.s3c+board.s2c=='':
            moves = '7c1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b7c)and Bboard.b1c==''\
           and board.s6c+board.s5c+board.s4c+board.s3c+board.s2c=='':
            moves = '7c1c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b7c)and Bboard.b9a==''\
           and board.s8b=='':
            moves = '7c9a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b7c)and Bboard.b5e==''\
           and board.s6d=='':
            moves = '7c5e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b7c)and Bboard.b4f==''\
           and board.s6d+board.s5e=='':
            moves = '7c4f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b7c)and Bboard.b3g==''\
           and board.s6d+board.s5e+board.s4f=='':
            moves = '7c3g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b7c)and Bboard.b2h==''\
           and board.s6d+board.s5e+board.s4f+board.s3g=='':
            moves = '7c2h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b7c)and Bboard.b1i==''\
           and board.s6d+board.s5e+board.s4f+board.s3g+board.s2h=='':
            moves = '7c1i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b7c)and Bboard.b9a==''\
           and board.s8b=='':
            moves = '7c9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b7c)and Bboard.b5e==''\
           and board.s6d=='':
            moves = '7c5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b7c)and Bboard.b4f==''\
           and board.s6d+board.s5e=='':
            moves = '7c4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b7c)and Bboard.b3g==''\
           and board.s6d+board.s5e+board.s4f=='':
            moves = '7c3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b7c)and Bboard.b2h==''\
           and board.s6d+board.s5e+board.s4f+board.s3g=='':
            moves = '7c2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b7c)and Bboard.b1i==''\
           and board.s6d+board.s5e+board.s4f+board.s3g+board.s2h=='':
            moves = '7c1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b7c)and Bboard.b5a==''\
           and board.s6b=='':
            moves = '7c5a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b7c)and Bboard.b9e==''\
           and board.s8d=='':
            moves = '7c9e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b7c)and Bboard.b5a==''\
           and board.s6b=='':
            moves = '7c5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b7c)and Bboard.b9e==''\
           and board.s8d=='':
            moves = '7c9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b8c !='':
        if re.match(r'[SGK+]',    Bboard.b8c)and Bboard.b8b=='':
            moves = '8c8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGK+]',    Bboard.b8c)and Bboard.b7b=='':
            moves = '8c7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGK+]',    Bboard.b8c)and Bboard.b9b=='':
            moves = '8c9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b8c)and Bboard.b7c=='':
            moves = '8c7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b8c)and Bboard.b9c=='':
            moves = '8c9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b8c)and Bboard.b8d=='':
            moves = '8c8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b8c)and Bboard.b7d=='':
            moves = '8c7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b8c)and Bboard.b9d=='':
            moves = '8c9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[PLSR]',   Bboard.b8c)and Bboard.b8b=='':
            moves = '8c8b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',     Bboard.b8c)and Bboard.b7b=='':
            moves = '8c7b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'[BS]',     Bboard.b8c)and Bboard.b9b=='':
            moves = '8c9b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('R',         Bboard.b8c)and Bboard.b7c=='':
            moves = '8c7c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',         Bboard.b8c)and Bboard.b9c=='':
            moves = '8c9c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',         Bboard.b8c)and Bboard.b8d=='':
            moves = '8c8d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',     Bboard.b8c)and Bboard.b7d=='':
            moves = '8c7d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',     Bboard.b8c)and Bboard.b9d=='':
            moves = '8c9d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b8c)and Bboard.b7a=='':
            moves = '8c7a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b8c)and Bboard.b9a=='':
            moves = '8c9a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b8c)and Bboard.b8a==''\
           and board.s8b=='':
            moves = '8c8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b8c)and Bboard.b8a==''\
           and board.s8b=='':
            moves = '8c8a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b8c)and Bboard.b8e==''\
           and board.s8d=='':
            moves = '8c8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b8c)and Bboard.b8e==''\
           and board.s8d=='':
            moves = '8c8e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b8c)and Bboard.b8f==''\
           and board.s8d+board.s8e=='':
            moves = '8c8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b8c)and Bboard.b8f==''\
           and board.s8d+board.s8e=='':
            moves = '8c8f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b8c)and Bboard.b8g==''\
           and board.s8d+board.s8e+board.s8f=='':
            moves = '8c8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b8c)and Bboard.b8g==''\
           and board.s8d+board.s8e+board.s8f=='':
            moves = '8c8g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b8c)and Bboard.b8h==''\
           and board.s8d+board.s8e+board.s8f+board.s8g=='':
            moves = '8c8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b8c)and Bboard.b8h==''\
           and board.s8d+board.s8e+board.s8f+board.s8g=='':
            moves = '8c8h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b8c)and Bboard.b8i==''\
           and board.s8d+board.s8e+board.s8f+board.s8g+board.s8h=='':
            moves = '8c8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b8c)and Bboard.b8i==''\
           and board.s8d+board.s8e+board.s8f+board.s8g+board.s8h=='':
            moves = '8c8i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b8c)and Bboard.b6c==''\
           and board.s7c=='':
            moves = '8c6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b8c)and Bboard.b6c==''\
           and board.s7c=='':
            moves = '8c6c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b8c)and Bboard.b5c==''\
           and board.s7c+board.s6c=='':
            moves = '8c5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b8c)and Bboard.b5c==''\
           and board.s7c+board.s6c=='':
            moves = '8c5c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b8c)and Bboard.b4c==''\
           and board.s7c+board.s6c+board.s5c=='':
            moves = '8c4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b8c)and Bboard.b4c==''\
           and board.s7c+board.s6c+board.s5c=='':
            moves = '8c4c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b8c)and Bboard.b3c==''\
           and board.s7c+board.s6c+board.s5c+board.s4c=='':
            moves = '8c3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b8c)and Bboard.b3c==''\
           and board.s7c+board.s6c+board.s5c+board.s4c=='':
            moves = '8c3c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b8c)and Bboard.b2c==''\
           and board.s7c+board.s6c+board.s5c+board.s4c+board.s3c=='':
            moves = '8c2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b8c)and Bboard.b2c==''\
           and board.s7c+board.s6c+board.s5c+board.s4c+board.s3c=='':
            moves = '8c2c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b8c)and Bboard.b1c==''\
           and board.s7c+board.s6c+board.s5c+board.s4c+board.s3c+board.s2c=='':
            moves = '8c1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b8c)and Bboard.b1c==''\
           and board.s7c+board.s6c+board.s5c+board.s4c+board.s3c+board.s2c=='':
            moves = '8c1c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b8c)and Bboard.b6e==''\
           and board.s7d=='':
            moves = '8c6e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b8c)and Bboard.b5f==''\
           and board.s7d+board.s6e=='':
            moves = '8c5f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b8c)and Bboard.b4g==''\
           and board.s7d+board.s6e+board.s5f=='':
            moves = '8c4g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b8c)and Bboard.b3h==''\
           and board.s7d+board.s6e+board.s5f+board.s4g=='':
            moves = '8c3h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b8c)and Bboard.b2i==''\
           and board.s7d+board.s6e+board.s5f+board.s4g+board.s3h=='':
            moves = '8c2i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b8c)and Bboard.b6e==''\
           and board.s7d=='':
            moves = '8c6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b8c)and Bboard.b5f==''\
           and board.s7d+board.s6e=='':
            moves = '8c5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b8c)and Bboard.b4g==''\
           and board.s7d+board.s6e+board.s5f=='':
            moves = '8c4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b8c)and Bboard.b3h==''\
           and board.s7d+board.s6e+board.s5f+board.s4g=='':
            moves = '8c3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b8c)and Bboard.b2i==''\
           and board.s7d+board.s6e+board.s5f+board.s4g+board.s3h=='':
            moves = '8c2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b8c)and Bboard.b6a==''\
           and board.s7b=='':
            moves = '8c6a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b8c)and Bboard.b6a==''\
           and board.s7b=='':
            moves = '8c6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b9c !='':
        if re.match(r'[SGK+]',    Bboard.b9c)and Bboard.b9b=='':
            moves = '9c9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGK+]',    Bboard.b9c)and Bboard.b8b=='':
            moves = '9c8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b9c)and Bboard.b8c=='':
            moves = '9c8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b9c)and Bboard.b9d=='':
            moves = '9c9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b9c)and Bboard.b8d=='':
            moves = '9c8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[PLSR]',   Bboard.b9c)and Bboard.b9b=='':
            moves = '9c9b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',     Bboard.b9c)and Bboard.b8b=='':
            moves = '9c8b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('R',         Bboard.b9c)and Bboard.b8c=='':
            moves = '9c8c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',         Bboard.b9c)and Bboard.b9d=='':
            moves = '9c9d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',     Bboard.b9c)and Bboard.b8d=='':
            moves = '9c8d+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b9c)and Bboard.b8a=='':
            moves = '9c8a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b9c)and Bboard.b9a==''\
           and board.s9b=='':
            moves = '9c9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b9c)and Bboard.b9a==''\
           and board.s9b=='':
            moves = '9c9a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b9c)and Bboard.b9e==''\
           and board.s9d=='':
            moves = '9c9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b9c)and Bboard.b9e==''\
           and board.s9d=='':
            moves = '9c9e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b9c)and Bboard.b9f==''\
           and board.s9d+board.s9e=='':
            moves = '9c9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b9c)and Bboard.b9f==''\
           and board.s9d+board.s9e=='':
            moves = '9c9f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b9c)and Bboard.b9g==''\
           and board.s9d+board.s9e+board.s9f=='':
            moves = '9c9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b9c)and Bboard.b9g==''\
           and board.s9d+board.s9e+board.s9f=='':
            moves = '9c9g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b9c)and Bboard.b9h==''\
           and board.s9d+board.s9e+board.s9f+board.s9g=='':
            moves = '9c9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b9c)and Bboard.b9h==''\
           and board.s9d+board.s9e+board.s9f+board.s9g=='':
            moves = '9c9h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b9c)and Bboard.b9i==''\
           and board.s9d+board.s9e+board.s9f+board.s9g+board.s9h=='':
            moves = '9c9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b9c)and Bboard.b9i==''\
           and board.s9d+board.s9e+board.s9f+board.s9g+board.s9h=='':
            moves = '9c9i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b9c)and Bboard.b7c==''\
           and board.s8c=='':
            moves = '9c7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b9c)and Bboard.b7c==''\
           and board.s8c=='':
            moves = '9c7c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b9c)and Bboard.b6c==''\
           and board.s8c+board.s7c=='':
            moves = '9c6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b9c)and Bboard.b6c==''\
           and board.s8c+board.s7c=='':
            moves = '9c6c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b9c)and Bboard.b5c==''\
           and board.s8c+board.s7c+board.s6c=='':
            moves = '9c5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b9c)and Bboard.b5c==''\
           and board.s8c+board.s7c+board.s6c=='':
            moves = '9c5c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',   Bboard.b9c)and Bboard.b4c==''\
           and board.s8c+board.s7c+board.s6c+board.s5c=='':
            moves = '9c4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',   Bboard.b9c)and Bboard.b4c==''\
           and board.s8c+board.s7c+board.s6c+board.s5c=='':
            moves = '9c4c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b9c)and Bboard.b3c==''\
           and board.s8c+board.s7c+board.s6c+board.s5c+board.s4c=='':
            moves = '9c3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b9c)and Bboard.b3c==''\
           and board.s8c+board.s7c+board.s6c+board.s5c+board.s4c=='':
            moves = '9c3c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b9c)and Bboard.b2c==''\
           and board.s8c+board.s7c+board.s6c+board.s5c+board.s4c+board.s3c=='':
            moves = '9c2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b9c)and Bboard.b2c==''\
           and board.s8c+board.s7c+board.s6c+board.s5c+board.s4c+board.s3c=='':
            moves = '9c2c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',      Bboard.b9c)and Bboard.b1c==''\
           and board.s8c+board.s7c+board.s6c+board.s5c+board.s4c+board.s3c+board.s2c=='':
            moves = '9c1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('R',      Bboard.b9c)and Bboard.b1c==''\
           and board.s8c+board.s7c+board.s6c+board.s5c+board.s4c+board.s3c+board.s2c=='':
            moves = '9c1c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b9c)and Bboard.b7a==''\
           and board.s8b=='':
            moves = '9c7a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b9c)and Bboard.b7e==''\
           and board.s8d=='':
            moves = '9c7e+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b9c)and Bboard.b6f==''\
           and board.s8d+board.s7e=='':
            moves = '9c6f+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b9c)and Bboard.b5g==''\
           and board.s8d+board.s7e+board.s6f=='':
            moves = '9c5g+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b9c)and Bboard.b4h==''\
           and board.s8d+board.s7e+board.s6f+board.s5g=='':
            moves = '9c4h+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b9c)and Bboard.b3i==''\
           and board.s8d+board.s7e+board.s6f+board.s5g+board.s4h=='':
            moves = '9c3i+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b9c)and Bboard.b7a==''\
           and board.s8b=='':
            moves = '9c7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b9c)and Bboard.b7e==''\
           and board.s8d=='':
            moves = '9c7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b9c)and Bboard.b6f==''\
           and board.s8d+board.s7e=='':
            moves = '9c6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b9c)and Bboard.b5g==''\
           and board.s8d+board.s7e+board.s6f=='':
            moves = '9c5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b9c)and Bboard.b4h==''\
           and board.s8d+board.s7e+board.s6f+board.s5g=='':
            moves = '9c4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b9c)and Bboard.b3i==''\
           and board.s8d+board.s7e+board.s6f+board.s5g+board.s4h=='':
            moves = '9c3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b1d !='':
        if re.match(r'[LSGK+]',   Bboard.b1d)and Bboard.b1c=='':
            moves = '1d1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGK+]',    Bboard.b1d)and Bboard.b2c=='':
            moves = '1d2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b1d)and Bboard.b2d=='':
            moves = '1d2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b1d)and Bboard.b1e=='':
            moves = '1d1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b1d)and Bboard.b2e=='':
            moves = '1d2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[PLSR]',   Bboard.b1d)and Bboard.b1c=='':
            moves = '1d1c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',     Bboard.b1d)and Bboard.b2c=='':
            moves = '1d2c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('N',         Bboard.b1d)and Bboard.b2b=='':
            moves = '1d2b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b1d)and Bboard.b1a==''\
           and board.s1b+board.s1c=='':
            moves = '1d1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b1d)and Bboard.b1a==''\
           and board.s1b+board.s1c=='':
            moves = '1d1a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b1d)and Bboard.b1b==''\
           and board.s1c=='':
            moves = '1d1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b1d)and Bboard.b1b==''\
           and board.s1c=='':
            moves = '1d1b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b1d)and Bboard.b1f==''\
           and board.s1e=='':
            moves = '1d1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b1d)and Bboard.b1g==''\
           and board.s1e+board.s1f=='':
            moves = '1d1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b1d)and Bboard.b1h==''\
           and board.s1e+board.s1f+board.s1g=='':
            moves = '1d1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b1d)and Bboard.b1i==''\
           and board.s1e+board.s1f+board.s1g+board.s1h=='':
            moves = '1d1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b1d)and Bboard.b3d==''\
           and board.s2d=='':
            moves = '1d3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b1d)and Bboard.b4d==''\
           and board.s2d+board.s3d=='':
            moves = '1d4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b1d)and Bboard.b5d==''\
           and board.s2d+board.s3d+board.s4d=='':
            moves = '1d5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b1d)and Bboard.b6d==''\
           and board.s2d+board.s3d+board.s4d+board.s5d=='':
            moves = '1d6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b1d)and Bboard.b7d==''\
           and board.s2d+board.s3d+board.s4d+board.s5d+board.s6d=='':
            moves = '1d7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b1d)and Bboard.b8d==''\
           and board.s2d+board.s3d+board.s4d+board.s5d+board.s6d+board.s7d=='':
            moves = '1d8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b1d)and Bboard.b9d==''\
           and board.s2d+board.s3d+board.s4d+board.s5d+board.s6d+board.s7d+board.s8d=='':
            moves = '1d9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b1d)and Bboard.b3f==''\
           and board.s2e=='':
            moves = '1d3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b1d)and Bboard.b4g==''\
           and board.s2e+board.s3f=='':
            moves = '1d4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b1d)and Bboard.b5h==''\
           and board.s2e+board.s3f+board.s4g=='':
            moves = '1d5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b1d)and Bboard.b6i==''\
           and board.s2e+board.s3f+board.s4g+board.s5h=='':
            moves = '1d6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b1d)and Bboard.b4a==''\
           and board.s3b+board.s2c=='':
            moves = '1d4a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b1d)and Bboard.b3b==''\
           and board.s2c=='':
            moves = '1d3b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b1d)and Bboard.b4a==''\
           and board.s3b+board.s2c=='':
            moves = '1d4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b1d)and Bboard.b3b==''\
           and board.s2c=='':
            moves = '1d3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b2d !='':
        if re.match(r'[LSGK+]',   Bboard.b2d)and Bboard.b2c=='':
            moves = '2d2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGK+]',    Bboard.b2d)and Bboard.b1c=='':
            moves = '2d1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGK+]',    Bboard.b2d)and Bboard.b3c=='':
            moves = '2d3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b2d)and Bboard.b1d=='':
            moves = '2d1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b2d)and Bboard.b3d=='':
            moves = '2d3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b2d)and Bboard.b2e=='':
            moves = '2d2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b2d)and Bboard.b1e=='':
            moves = '2d1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b2d)and Bboard.b3e=='':
            moves = '2d3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[PLSR]',   Bboard.b2d)and Bboard.b2c=='':
            moves = '2d2c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',     Bboard.b2d)and Bboard.b1c=='':
            moves = '2d1c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'[BS]',     Bboard.b2d)and Bboard.b3c=='':
            moves = '2d3c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('N',         Bboard.b2d)and Bboard.b1b=='':
            moves = '2d1b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b2d)and Bboard.b3b=='':
            moves = '2d3b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b2d)and Bboard.b2a==''\
           and board.s2b+board.s2c=='':
            moves = '2d2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b2d)and Bboard.b2a==''\
           and board.s2b+board.s2c=='':
            moves = '2d2a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b2d)and Bboard.b2b==''\
           and board.s2c=='':
            moves = '2d2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b2d)and Bboard.b2b==''\
           and board.s2c=='':
            moves = '2d2b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b2d)and Bboard.b2f==''\
           and board.s2e=='':
            moves = '2d2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b2d)and Bboard.b2g==''\
           and board.s2e+board.s2f=='':
            moves = '2d2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b2d)and Bboard.b2h==''\
           and board.s2e+board.s2f+board.s2g=='':
            moves = '2d2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b2d)and Bboard.b2i==''\
           and board.s2e+board.s2f+board.s2g+board.s2h=='':
            moves = '2d2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b2d)and Bboard.b4d==''\
           and board.s3d=='':
            moves = '2d4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b2d)and Bboard.b5d==''\
           and board.s3d+board.s4d=='':
            moves = '2d5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b2d)and Bboard.b6d==''\
           and board.s3d+board.s4d+board.s5d=='':
            moves = '2d6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b2d)and Bboard.b7d==''\
           and board.s3d+board.s4d+board.s5d+board.s6d=='':
            moves = '2d7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b2d)and Bboard.b8d==''\
           and board.s3d+board.s4d+board.s5d+board.s6d+board.s7d=='':
            moves = '2d8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b2d)and Bboard.b9d==''\
           and board.s3d+board.s4d+board.s5d+board.s6d+board.s7d+board.s8d=='':
            moves = '2d9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b2d)and Bboard.b4f==''\
           and board.s3e=='':
            moves = '2d4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b2d)and Bboard.b5g==''\
           and board.s3e+board.s4f=='':
            moves = '2d5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b2d)and Bboard.b6h==''\
           and board.s3e+board.s4f+board.s5g=='':
            moves = '2d6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b2d)and Bboard.b7i==''\
           and board.s3e+board.s4f+board.s5g+board.s6h=='':
            moves = '2d7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b2d)and Bboard.b5a==''\
           and board.s4b+board.s3c=='':
            moves = '2d5a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b2d)and Bboard.b4b==''\
           and board.s3c=='':
            moves = '2d4b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b2d)and Bboard.b5a==''\
           and board.s4b+board.s3c=='':
            moves = '2d5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b2d)and Bboard.b4b==''\
           and board.s3c=='':
            moves = '2d4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b3d !='':
        if re.match(r'[LSGK+]',   Bboard.b3d)and Bboard.b3c=='':
            moves = '3d3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGK+]',    Bboard.b3d)and Bboard.b2c=='':
            moves = '3d2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGK+]',    Bboard.b3d)and Bboard.b4c=='':
            moves = '3d4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b3d)and Bboard.b2d=='':
            moves = '3d2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b3d)and Bboard.b4d=='':
            moves = '3d4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b3d)and Bboard.b3e=='':
            moves = '3d3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b3d)and Bboard.b2e=='':
            moves = '3d2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b3d)and Bboard.b4e=='':
            moves = '3d4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[PLSR]',   Bboard.b3d)and Bboard.b3c=='':
            moves = '3d3c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',     Bboard.b3d)and Bboard.b2c=='':
            moves = '3d2c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'[BS]',     Bboard.b3d)and Bboard.b4c=='':
            moves = '3d4c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('N',         Bboard.b3d)and Bboard.b2b=='':
            moves = '3d2b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b3d)and Bboard.b4b=='':
            moves = '3d4b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b3d)and Bboard.b3a==''\
           and board.s3b+board.s3c=='':
            moves = '3d3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b3d)and Bboard.b3a==''\
           and board.s3b+board.s3c=='':
            moves = '3d3a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b3d)and Bboard.b3b==''\
           and board.s3c=='':
            moves = '3d3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b3d)and Bboard.b3b==''\
           and board.s3c=='':
            moves = '3d3b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b3d)and Bboard.b3f==''\
           and board.s3e=='':
            moves = '3d3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b3d)and Bboard.b3g==''\
           and board.s3e+board.s3f=='':
            moves = '3d3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b3d)and Bboard.b3h==''\
           and board.s3e+board.s3f+board.s3g=='':
            moves = '3d3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b3d)and Bboard.b3i==''\
           and board.s3e+board.s3f+board.s3g+board.s3h=='':
            moves = '3d3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b3d)and Bboard.b1d==''\
           and board.s2d=='':
            moves = '3d1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b3d)and Bboard.b5d==''\
           and board.s4d=='':
            moves = '3d5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b3d)and Bboard.b6d==''\
           and board.s4d+board.s5d=='':
            moves = '3d6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b3d)and Bboard.b7d==''\
           and board.s4d+board.s5d+board.s6d=='':
            moves = '3d7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b3d)and Bboard.b8d==''\
           and board.s4d+board.s5d+board.s6d+board.s7d=='':
            moves = '3d8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b3d)and Bboard.b9d==''\
           and board.s4d+board.s5d+board.s6d+board.s7d+board.s8d=='':
            moves = '3d9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b3d)and Bboard.b1b==''\
           and board.s2c=='':
            moves = '3d1b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b3d)and Bboard.b1b==''\
           and board.s2c=='':
            moves = '3d1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b3d)and Bboard.b5f==''\
           and board.s4e=='':
            moves = '3d5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b3d)and Bboard.b6g==''\
           and board.s4e+board.s5f=='':
            moves = '3d6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b3d)and Bboard.b7h==''\
           and board.s4e+board.s5f+board.s6g=='':
            moves = '3d7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b3d)and Bboard.b8i==''\
           and board.s4e+board.s5f+board.s6g+board.s7h=='':
            moves = '3d8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b3d)and Bboard.b6a==''\
           and board.s5b+board.s4c=='':
            moves = '3d6a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b3d)and Bboard.b5b==''\
           and board.s4c=='':
            moves = '3d5b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b3d)and Bboard.b6a==''\
           and board.s5b+board.s4c=='':
            moves = '3d6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b3d)and Bboard.b5b==''\
           and board.s4c=='':
            moves = '3d5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b3d)and Bboard.b1f==''\
           and board.s2e=='':
            moves = '3d1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b4d !='':
        if re.match(r'[LSGK+]',   Bboard.b4d)and Bboard.b4c=='':
            moves = '4d4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGK+]',    Bboard.b4d)and Bboard.b3c=='':
            moves = '4d3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGK+]',    Bboard.b4d)and Bboard.b5c=='':
            moves = '4d5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b4d)and Bboard.b3d=='':
            moves = '4d3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b4d)and Bboard.b5d=='':
            moves = '4d5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b4d)and Bboard.b4e=='':
            moves = '4d4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b4d)and Bboard.b3e=='':
            moves = '4d3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b4d)and Bboard.b5e=='':
            moves = '4d5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[PLSR]',   Bboard.b4d)and Bboard.b4c=='':
            moves = '4d4c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',     Bboard.b4d)and Bboard.b3c=='':
            moves = '4d3c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'[BS]',     Bboard.b4d)and Bboard.b5c=='':
            moves = '4d5c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('N',         Bboard.b4d)and Bboard.b3b=='':
            moves = '4d3b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b4d)and Bboard.b5b=='':
            moves = '4d5b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b4d)and Bboard.b4a==''\
           and board.s4b+board.s4c=='':
            moves = '4d4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b4d)and Bboard.b4a==''\
           and board.s4b+board.s4c=='':
            moves = '4d4a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b4d)and Bboard.b4b==''\
           and board.s4c=='':
            moves = '4d4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b4d)and Bboard.b4b==''\
           and board.s4c=='':
            moves = '4d4b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b4d)and Bboard.b4f==''\
           and board.s4e=='':
            moves = '4d4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b4d)and Bboard.b4g==''\
           and board.s4e+board.s4f=='':
            moves = '4d4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b4d)and Bboard.b4h==''\
           and board.s4e+board.s4f+board.s4g=='':
            moves = '4d4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b4d)and Bboard.b4i==''\
           and board.s4e+board.s4f+board.s4g+board.s4h=='':
            moves = '4d4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b4d)and Bboard.b1d==''\
           and board.s2d+board.s3d=='':
            moves = '4d1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b4d)and Bboard.b2d==''\
           and board.s3d=='':
            moves = '4d2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b4d)and Bboard.b6d==''\
           and board.s5d=='':
            moves = '4d6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b4d)and Bboard.b7d==''\
           and board.s5d+board.s6d=='':
            moves = '4d7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b4d)and Bboard.b8d==''\
           and board.s5d+board.s6d+board.s7d=='':
            moves = '4d8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b4d)and Bboard.b9d==''\
           and board.s5d+board.s6d+board.s7d+board.s8d=='':
            moves = '4d9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b4d)and Bboard.b1a==''\
           and board.s2b+board.s3c=='':
            moves = '4d1a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b4d)and Bboard.b2b==''\
           and board.s3c=='':
            moves = '4d2b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b4d)and Bboard.b1a==''\
           and board.s2b+board.s3c=='':
            moves = '4d1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b4d)and Bboard.b2b==''\
           and board.s3c=='':
            moves = '4d2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b4d)and Bboard.b6f==''\
           and board.s5e=='':
            moves = '4d6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b4d)and Bboard.b7g==''\
           and board.s5e+board.s6f=='':
            moves = '4d7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b4d)and Bboard.b8h==''\
           and board.s5e+board.s6f+board.s7g=='':
            moves = '4d8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b4d)and Bboard.b9i==''\
           and board.s5e+board.s6f+board.s7g+board.s8h=='':
            moves = '4d9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b4d)and Bboard.b7a==''\
           and board.s6b+board.s5c=='':
            moves = '4d7a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b4d)and Bboard.b6b==''\
           and board.s5c=='':
            moves = '4d6b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b4d)and Bboard.b7a==''\
           and board.s6b+board.s5c=='':
            moves = '4d7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b4d)and Bboard.b6b==''\
           and board.s5c=='':
            moves = '4d6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b4d)and Bboard.b2f==''\
           and board.s3e=='':
            moves = '4d2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b4d)and Bboard.b1g==''\
           and board.s3e+board.s2f=='':
            moves = '4d1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b5d !='':
        if re.match(r'[LSGK+]',   Bboard.b5d)and Bboard.b5c=='':
            moves = '5d5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGK+]',    Bboard.b5d)and Bboard.b4c=='':
            moves = '5d4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGK+]',    Bboard.b5d)and Bboard.b6c=='':
            moves = '5d6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b5d)and Bboard.b4d=='':
            moves = '5d4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b5d)and Bboard.b6d=='':
            moves = '5d6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b5d)and Bboard.b5e=='':
            moves = '5d5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b5d)and Bboard.b4e=='':
            moves = '5d4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b5d)and Bboard.b6e=='':
            moves = '5d6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[PLSR]',   Bboard.b5d)and Bboard.b5c=='':
            moves = '5d5c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',     Bboard.b5d)and Bboard.b4c=='':
            moves = '5d4c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'[BS]',     Bboard.b5d)and Bboard.b6c=='':
            moves = '5d6c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('N',         Bboard.b5d)and Bboard.b4b=='':
            moves = '5d4b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b5d)and Bboard.b6b=='':
            moves = '5d6b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b5d)and Bboard.b5a==''\
           and board.s5b+board.s5c=='':
            moves = '5d5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b5d)and Bboard.b5a==''\
           and board.s5b+board.s5c=='':
            moves = '5d5a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b5d)and Bboard.b5b==''\
           and board.s5c=='':
            moves = '5d5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b5d)and Bboard.b5b==''\
           and board.s5c=='':
            moves = '5d5b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b5d)and Bboard.b5f==''\
           and board.s5e=='':
            moves = '5d5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b5d)and Bboard.b5g==''\
           and board.s5e+board.s5f=='':
            moves = '5d5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b5d)and Bboard.b5h==''\
           and board.s5e+board.s5f+board.s5g=='':
            moves = '5d5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b5d)and Bboard.b5i==''\
           and board.s5e+board.s5f+board.s5g+board.s5h=='':
            moves = '5d5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b5d)and Bboard.b1d==''\
           and board.s2d+board.s3d+board.s4d=='':
            moves = '5d1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b5d)and Bboard.b2d==''\
           and board.s3d+board.s4d=='':
            moves = '5d2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b5d)and Bboard.b3d==''\
           and board.s4d=='':
            moves = '5d3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b5d)and Bboard.b7d==''\
           and board.s6d=='':
            moves = '5d7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b5d)and Bboard.b8d==''\
           and board.s6d+board.s7d=='':
            moves = '5d8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b5d)and Bboard.b9d==''\
           and board.s6d+board.s7d+board.s8d=='':
            moves = '5d9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b5d)and Bboard.b2a==''\
          and board.s3b+board.s4c=='':
           moves ='5d2a+'
           kaihimore(moves)
           if oute.oute == 0:
              depth1.append(moves)
        if re.match('B',Bboard.b5d)and Bboard.b3b==''\
          and board.s4c=='':
           moves ='5d3b+'
           kaihimore(moves)
           if oute.oute == 0:
              depth1.append(moves)
        if re.match('\+B',  Bboard.b5d)and Bboard.b2a==''\
          and board.s3b+board.s4c=='':
           moves ='5d2a'
           kaihimore(moves)
           if oute.oute == 0:
              depth1.append(moves)
        if re.match('\+B',Bboard.b5d)and Bboard.b3b==''\
          and board.s4c=='':
           moves ='5d3b'
           kaihimore(moves)
           if oute.oute == 0:
              depth1.append(moves)
        if re.match(r'\+B|B',  Bboard.b5d)and Bboard.b7f==''\
          and board.s6e=='':
           moves ='5d7f'
           kaihimore(moves)
           if oute.oute == 0:
              depth1.append(moves)
        if re.match(r'\+B|B',  Bboard.b5d)and Bboard.b8g==''\
          and board.s6e+board.s7f=='':
           moves ='5d8g'
           kaihimore(moves)
           if oute.oute == 0:
              depth1.append(moves)
        if re.match(r'\+B|B',  Bboard.b5d)and Bboard.b9h==''\
          and board.s6e+board.s7f+board.s8g=='':
           moves ='5d9h'
           kaihimore(moves)
           if oute.oute == 0:
              depth1.append(moves)
        if re.match('B',Bboard.b5d)and Bboard.b8a==''\
          and board.s7b+board.s6c=='':
           moves ='5d8a+'
           kaihimore(moves)
           if oute.oute == 0:
              depth1.append(moves)
        if re.match('B',Bboard.b5d)and Bboard.b7b==''\
          and board.s6c=='':
           moves ='5d7b+'
           kaihimore(moves)
           if oute.oute == 0:
              depth1.append(moves)
        if re.match('\+B',  Bboard.b5d)and Bboard.b8a==''\
          and board.s7b+board.s6c=='':
           moves ='5d8a'
           kaihimore(moves)
           if oute.oute == 0:
              depth1.append(moves)
        if re.match('\+B',Bboard.b5d)and Bboard.b7b==''\
          and board.s6c=='':
           moves ='5d7b'
           kaihimore(moves)
           if oute.oute == 0:
              depth1.append(moves)
        if re.match(r'\+B|B',  Bboard.b5d)and Bboard.b3f==''\
          and board.s4e=='':
           moves ='5d3f'
           kaihimore(moves)
           if oute.oute == 0:
              depth1.append(moves)
        if re.match(r'\+B|B',  Bboard.b5d)and Bboard.b2g==''\
          and board.s4e+board.s3f=='':
           moves ='5d2g'
           kaihimore(moves)
           if oute.oute == 0:
              depth1.append(moves)

    if Bboard.b6d !='':
        if re.match(r'[LSGK+]',   Bboard.b6d)and Bboard.b6c=='':
            moves = '6d6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGK+]',    Bboard.b6d)and Bboard.b5c=='':
            moves = '6d5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGK+]',    Bboard.b6d)and Bboard.b7c=='':
            moves = '6d7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b6d)and Bboard.b5d=='':
            moves = '6d5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b6d)and Bboard.b7d=='':
            moves = '6d7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b6d)and Bboard.b6e=='':
            moves = '6d6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b6d)and Bboard.b5e=='':
            moves = '6d5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b6d)and Bboard.b7e=='':
            moves = '6d7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[PLSR]',   Bboard.b6d)and Bboard.b6c=='':
            moves = '6d6c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',     Bboard.b6d)and Bboard.b5c=='':
            moves = '6d5c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'[BS]',     Bboard.b6d)and Bboard.b7c=='':
            moves = '6d7c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('N',         Bboard.b6d)and Bboard.b5b=='':
            moves = '6d5b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b6d)and Bboard.b7b=='':
            moves = '6d7b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b6d)and Bboard.b6a==''\
           and board.s6b+board.s6c=='':
            moves = '6d6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b6d)and Bboard.b6a==''\
           and board.s6b+board.s6c=='':
            moves = '6d6a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b6d)and Bboard.b6b==''\
           and board.s6c=='':
            moves = '6d6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b6d)and Bboard.b6b==''\
           and board.s6c=='':
            moves = '6d6b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b6d)and Bboard.b6f==''\
           and board.s6e=='':
            moves = '6d6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b6d)and Bboard.b6g==''\
           and board.s6e+board.s6f=='':
            moves = '6d6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b6d)and Bboard.b6h==''\
           and board.s6e+board.s6f+board.s6g=='':
            moves = '6d6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b6d)and Bboard.b6i==''\
           and board.s6e+board.s6f+board.s6g+board.s6h=='':
            moves = '6d6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b6d)and Bboard.b9d==''\
           and board.s8d+board.s7d=='':
            moves = '6d9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b6d)and Bboard.b8d==''\
           and board.s7d=='':
            moves = '6d8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b6d)and Bboard.b4d==''\
           and board.s5d=='':
            moves = '6d4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b6d)and Bboard.b3d==''\
           and board.s5d+board.s4d=='':
            moves = '6d3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b6d)and Bboard.b2d==''\
           and board.s5d+board.s4d+board.s3d=='':
            moves = '6d2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b6d)and Bboard.b1d==''\
           and board.s5d+board.s4d+board.s3d+board.s2d=='':
            moves = '6d1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b6d)and Bboard.b9a==''\
           and board.s8b+board.s7c=='':
            moves = '6d9a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b6d)and Bboard.b8b==''\
           and board.s7c=='':
            moves = '6d8b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b6d)and Bboard.b9a==''\
           and board.s8b+board.s7c=='':
            moves = '6d9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b6d)and Bboard.b8b==''\
           and board.s7c=='':
            moves = '6d8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b6d)and Bboard.b4f==''\
           and board.s5e=='':
            moves = '6d4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b6d)and Bboard.b3g==''\
           and board.s5e+board.s4f=='':
            moves = '6d3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b6d)and Bboard.b2h==''\
           and board.s5e+board.s4f+board.s3g=='':
            moves = '6d2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b6d)and Bboard.b1i==''\
           and board.s5e+board.s4f+board.s3g+board.s2h=='':
            moves = '6d1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b6d)and Bboard.b3a==''\
           and board.s4b+board.s5c=='':
            moves = '6d3a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b6d)and Bboard.b4b==''\
           and board.s5c=='':
            moves = '6d4b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b6d)and Bboard.b3a==''\
           and board.s4b+board.s5c=='':
            moves = '6d3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b6d)and Bboard.b4b==''\
           and board.s5c=='':
            moves = '6d4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b6d)and Bboard.b8f==''\
           and board.s7e=='':
            moves = '6d8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b6d)and Bboard.b9g==''\
           and board.s7e+board.s8f=='':
            moves = '6d9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b7d !='':
        if re.match(r'[LSGK+]',   Bboard.b7d)and Bboard.b7c=='':
            moves = '7d7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGK+]',    Bboard.b7d)and Bboard.b6c=='':
            moves = '7d6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGK+]',    Bboard.b7d)and Bboard.b8c=='':
            moves = '7d8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b7d)and Bboard.b6d=='':
            moves = '7d6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b7d)and Bboard.b8d=='':
            moves = '7d8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b7d)and Bboard.b7e=='':
            moves = '7d7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b7d)and Bboard.b6e=='':
            moves = '7d6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b7d)and Bboard.b8e=='':
            moves = '7d8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[PLSR]',   Bboard.b7d)and Bboard.b7c=='':
            moves = '7d7c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',     Bboard.b7d)and Bboard.b6c=='':
            moves = '7d6c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'[BS]',     Bboard.b7d)and Bboard.b8c=='':
            moves = '7d8c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('N',         Bboard.b7d)and Bboard.b6b=='':
            moves = '7d6b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b7d)and Bboard.b8b=='':
            moves = '7d8b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b7d)and Bboard.b7a==''\
           and board.s7b+board.s7c=='':
            moves = '7d7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b7d)and Bboard.b7a==''\
           and board.s7b+board.s7c=='':
            moves = '7d7a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b7d)and Bboard.b7b==''\
           and board.s7c=='':
            moves = '7d7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b7d)and Bboard.b7b==''\
           and board.s7c=='':
            moves = '7d7b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b7d)and Bboard.b7f==''\
           and board.s7e=='':
            moves = '7d7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b7d)and Bboard.b7g==''\
           and board.s7e+board.s7f=='':
            moves = '7d7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b7d)and Bboard.b7h==''\
           and board.s7e+board.s7f+board.s7g=='':
            moves = '7d7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b7d)and Bboard.b7i==''\
           and board.s7e+board.s7f+board.s7g+board.s7h=='':
            moves = '7d7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b7d)and Bboard.b9d==''\
           and board.s8d=='':
            moves = '7d9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b7d)and Bboard.b5d==''\
           and board.s6d=='':
            moves = '7d5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b7d)and Bboard.b4d==''\
           and board.s6d+board.s5d=='':
            moves = '7d4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b7d)and Bboard.b3d==''\
           and board.s6d+board.s5d+board.s4d=='':
            moves = '7d3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b7d)and Bboard.b2d==''\
           and board.s6d+board.s5d+board.s4d+board.s3d=='':
            moves = '7d2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b7d)and Bboard.b1d==''\
           and board.s6d+board.s5d+board.s4d+board.s3d+board.s2d=='':
            moves = '7d1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b7d)and Bboard.b9b==''\
           and board.s8c=='':
            moves = '7d9b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b7d)and Bboard.b9b==''\
           and board.s8c=='':
            moves = '7d9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b7d)and Bboard.b5f==''\
           and board.s6e=='':
            moves = '7d5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b7d)and Bboard.b4g==''\
           and board.s6e+board.s5f=='':
            moves = '7d4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b7d)and Bboard.b3h==''\
           and board.s6e+board.s5f+board.s4g=='':
            moves = '7d3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b7d)and Bboard.b2i==''\
           and board.s6e+board.s5f+board.s4g+board.s3h=='':
            moves = '7d2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b7d)and Bboard.b4a==''\
           and board.s5b+board.s6c=='':
            moves = '7d4a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b7d)and Bboard.b5b==''\
           and board.s6c=='':
            moves = '7d5b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b7d)and Bboard.b4a==''\
           and board.s5b+board.s6c=='':
            moves = '7d4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b7d)and Bboard.b5b==''\
           and board.s6c=='':
            moves = '7d5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b7d)and Bboard.b9f==''\
           and board.s8e=='':
            moves = '7d9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b8d !='':
        if re.match(r'[LSGK+]',   Bboard.b8d)and Bboard.b8c=='':
            moves = '8d8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGK+]',    Bboard.b8d)and Bboard.b7c=='':
            moves = '8d7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGK+]',    Bboard.b8d)and Bboard.b9c=='':
            moves = '8d9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b8d)and Bboard.b7d=='':
            moves = '8d7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b8d)and Bboard.b9d=='':
            moves = '8d9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b8d)and Bboard.b8e=='':
            moves = '8d8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b8d)and Bboard.b7e=='':
            moves = '8d7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b8d)and Bboard.b9e=='':
            moves = '8d9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[PLSR]',   Bboard.b8d)and Bboard.b8c=='':
            moves = '8d8c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',     Bboard.b8d)and Bboard.b7c=='':
            moves = '8d7c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match(r'[BS]',     Bboard.b8d)and Bboard.b9c=='':
            moves = '8d9c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('N',         Bboard.b8d)and Bboard.b7b=='':
            moves = '8d7b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b8d)and Bboard.b9b=='':
            moves = '8d9b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b8d)and Bboard.b8a==''\
           and board.s8b+board.s8c=='':
            moves = '8d8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b8d)and Bboard.b8a==''\
           and board.s8b+board.s8c=='':
            moves = '8d8a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b8d)and Bboard.b8b==''\
           and board.s8c=='':
            moves = '8d8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b8d)and Bboard.b8b==''\
           and board.s8c=='':
            moves = '8d8b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b8d)and Bboard.b8f==''\
           and board.s8e=='':
            moves = '8d8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b8d)and Bboard.b8g==''\
           and board.s8e+board.s8f=='':
            moves = '8d8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b8d)and Bboard.b8h==''\
           and board.s8e+board.s8f+board.s8g=='':
            moves = '8d8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b8d)and Bboard.b8i==''\
           and board.s8e+board.s8f+board.s8g+board.s8h=='':
            moves = '8d8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b8d)and Bboard.b6d==''\
           and board.s7d=='':
            moves = '8d6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b8d)and Bboard.b5d==''\
           and board.s7d+board.s6d=='':
            moves = '8d5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b8d)and Bboard.b4d==''\
           and board.s7d+board.s6d+board.s5d=='':
            moves = '8d4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b8d)and Bboard.b3d==''\
           and board.s7d+board.s6d+board.s5d+board.s4d=='':
            moves = '8d3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b8d)and Bboard.b2d==''\
           and board.s7d+board.s6d+board.s5d+board.s4d+board.s3d=='':
            moves = '8d2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b8d)and Bboard.b1d==''\
           and board.s7d+board.s6d+board.s5d+board.s4d+board.s3d+board.s2d=='':
            moves = '8d1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b8d)and Bboard.b6f==''\
           and board.s7e=='':
            moves = '8d6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b8d)and Bboard.b5g==''\
           and board.s7e+board.s6f=='':
            moves = '8d5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b8d)and Bboard.b4h==''\
           and board.s7e+board.s6f+board.s5g=='':
            moves = '8d4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b8d)and Bboard.b3i==''\
           and board.s7e+board.s6f+board.s5g+board.s4h=='':
            moves = '8d3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b8d)and Bboard.b5a==''\
           and board.s6b+board.s7c=='':
            moves = '8d5a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b8d)and Bboard.b6b==''\
           and board.s7c=='':
            moves = '8d6b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b8d)and Bboard.b5a==''\
           and board.s6b+board.s7c=='':
            moves = '8d5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b8d)and Bboard.b6b==''\
           and board.s7c=='':
            moves = '8d6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b9d !='':
        if re.match(r'[LSGK+]',   Bboard.b9d)and Bboard.b9c=='':
            moves = '9d9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGK+]',    Bboard.b9d)and Bboard.b8c=='':
            moves = '9d8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b9d)and Bboard.b8d=='':
            moves = '9d8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GK+]',     Bboard.b9d)and Bboard.b9e=='':
            moves = '9d9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|S|K',Bboard.b9d)and Bboard.b8e=='':
            moves = '9d8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[PLSR]',   Bboard.b9d)and Bboard.b9c=='':
            moves = '9d9c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[BS]',     Bboard.b9d)and Bboard.b8c=='':
            moves = '9d8c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)        
        if re.match('N',         Bboard.b9d)and Bboard.b8b=='':
            moves = '9d8b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b9d)and Bboard.b9a==''\
           and board.s9b+board.s9c=='':
            moves = '9d9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b9d)and Bboard.b9a==''\
           and board.s9b+board.s9c=='':
            moves = '9d9a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b9d)and Bboard.b9b==''\
           and board.s9c=='':
            moves = '9d9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b9d)and Bboard.b9b==''\
           and board.s9c=='':
            moves = '9d9b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b9d)and Bboard.b9f==''\
           and board.s9e=='':
            moves = '9d9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b9d)and Bboard.b9g==''\
           and board.s9e+board.s9f=='':
            moves = '9d9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b9d)and Bboard.b9h==''\
           and board.s9e+board.s9f+board.s9g=='':
            moves = '9d9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b9d)and Bboard.b9i==''\
           and board.s9e+board.s9f+board.s9g+board.s9h=='':
            moves = '9d9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b9d)and Bboard.b7d==''\
           and board.s8d=='':
            moves = '9d7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b9d)and Bboard.b6d==''\
           and board.s8d+board.s7d=='':
            moves = '9d6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b9d)and Bboard.b5d==''\
           and board.s8d+board.s7d+board.s6d=='':
            moves = '9d5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b9d)and Bboard.b4d==''\
           and board.s8d+board.s7d+board.s6d+board.s5d=='':
            moves = '9d4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b9d)and Bboard.b3d==''\
           and board.s8d+board.s7d+board.s6d+board.s5d+board.s4d=='':
            moves = '9d3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b9d)and Bboard.b2d==''\
           and board.s8d+board.s7d+board.s6d+board.s5d+board.s4d+board.s3d=='':
            moves = '9d2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b9d)and Bboard.b1d==''\
           and board.s8d+board.s7d+board.s6d+board.s5d+board.s4d+board.s3d+board.s2d=='':
            moves = '9d1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b9d)and Bboard.b7f==''\
           and board.s8e=='':
            moves = '9d7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b9d)and Bboard.b6g==''\
           and board.s8e+board.s7f=='':
            moves = '9d6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b9d)and Bboard.b5h==''\
           and board.s8e+board.s7f+board.s6g=='':
            moves = '9d5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b9d)and Bboard.b4i==''\
           and board.s8e+board.s7f+board.s6g+board.s5h=='':
            moves = '9d4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b9d)and Bboard.b6a==''\
           and board.s7b+board.s8c=='':
            moves = '9d6a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b9d)and Bboard.b7b==''\
           and board.s8c=='':
            moves = '9d7b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b9d)and Bboard.b6a==''\
           and board.s7b+board.s8c=='':
            moves = '9d6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b9d)and Bboard.b7b==''\
           and board.s8c=='':
            moves = '9d7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b1e !='':
        if re.match(r'[PLSGRK+]',   Bboard.b1e)and Bboard.b1d=='':
            moves = '1e1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b1e)and Bboard.b2d=='':
            moves = '1e2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b1e)and Bboard.b2e=='':
            moves = '1e2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b1e)and Bboard.b1f=='':
            moves = '1e1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b1e)and Bboard.b2f=='':
            moves = '1e2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b1e)and Bboard.b2c=='':
            moves = '1e2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b1e)and Bboard.b2c=='':
            moves = '1e2c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b1e)and Bboard.b1a==''\
           and board.s1b+board.s1c+board.s1d=='':
            moves = '1e1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b1e)and Bboard.b1a==''\
           and board.s1b+board.s1c+board.s1d=='':
            moves = '1e1a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b1e)and Bboard.b1b==''\
           and board.s1c+board.s1d=='':
            moves = '1e1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b1e)and Bboard.b1b==''\
           and board.s1c+board.s1d=='':
            moves = '1e1b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|L',    Bboard.b1e)and Bboard.b1c==''\
           and board.s1d=='':
            moves = '1e1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b1e)and Bboard.b1c==''\
           and board.s1d=='':
            moves = '1e1c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b1e)and Bboard.b1g==''\
           and board.s1f=='':
            moves = '1e1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b1e)and Bboard.b1h==''\
           and board.s1f+board.s1g=='':
            moves = '1e1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b1e)and Bboard.b1i==''\
           and board.s1f+board.s1g+board.s1h=='':
            moves = '1e1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b1e)and Bboard.b3e==''\
           and board.s2e=='':
            moves = '1e3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b1e)and Bboard.b4e==''\
           and board.s2e+board.s3e=='':
            moves = '1e4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b1e)and Bboard.b5e==''\
           and board.s2e+board.s3e+board.s4e=='':
            moves = '1e5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b1e)and Bboard.b6e==''\
           and board.s2e+board.s3e+board.s4e+board.s5e=='':
            moves = '1e6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b1e)and Bboard.b7e==''\
           and board.s2e+board.s3e+board.s4e+board.s5e+board.s6e=='':
            moves = '1e7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b1e)and Bboard.b8e==''\
           and board.s2e+board.s3e+board.s4e+board.s5e+board.s6e+board.s7e=='':
            moves = '1e8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b1e)and Bboard.b9e==''\
           and board.s2e+board.s3e+board.s4e+board.s5e+board.s6e+board.s7e+board.s8e=='':
            moves = '1e9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b1e)and Bboard.b3g==''\
           and board.s2f=='':
            moves = '1e3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b1e)and Bboard.b4h==''\
           and board.s2f+board.s3g=='':
            moves = '1e4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b1e)and Bboard.b5i==''\
           and board.s2f+board.s3g+board.s4h=='':
            moves = '1e5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b1e)and Bboard.b5a==''\
           and board.s4b+board.s3c+board.s2d=='':
            moves = '1e5a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b1e)and Bboard.b4b==''\
           and board.s3c+board.s2d=='':
            moves = '1e4b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b1e)and Bboard.b3c==''\
           and board.s2d=='':
            moves = '1e3c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b1e)and Bboard.b5a==''\
           and board.s4b+board.s3c+board.s2d=='':
            moves = '1e5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b1e)and Bboard.b4b==''\
           and board.s3c+board.s2d=='':
            moves = '1e4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',Bboard.b1e)and Bboard.b3c==''\
           and board.s2d=='':
            moves = '1e3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b2e !='':
        if re.match(r'[PLSGRK+]',   Bboard.b2e)and Bboard.b2d=='':
            moves = '2e2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b2e)and Bboard.b1d=='':
            moves = '2e1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b2e)and Bboard.b3d=='':
            moves = '2e3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b2e)and Bboard.b1e=='':
            moves = '2e1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b2e)and Bboard.b3e=='':
            moves = '2e3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b2e)and Bboard.b2f=='':
            moves = '2e2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b2e)and Bboard.b1f=='':
            moves = '2e1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b2e)and Bboard.b3f=='':
            moves = '2e3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b2e)and Bboard.b1c=='':
            moves = '2e1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b2e)and Bboard.b3c=='':
            moves = '2e3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b2e)and Bboard.b1c=='':
            moves = '2e1c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b2e)and Bboard.b3c=='':
            moves = '2e3c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b2e)and Bboard.b2a==''\
           and board.s2b+board.s2c+board.s2d=='':
            moves = '2e2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b2e)and Bboard.b2a==''\
           and board.s2b+board.s2c+board.s2d=='':
            moves = '2e2a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b2e)and Bboard.b2b==''\
           and board.s2c+board.s2d=='':
            moves = '2e2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b2e)and Bboard.b2b==''\
           and board.s2c+board.s2d=='':
            moves = '2e2b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|L',    Bboard.b2e)and Bboard.b2c==''\
           and board.s2d=='':
            moves = '2e2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b2e)and Bboard.b2c==''\
           and board.s2d=='':
            moves = '2e2c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b2e)and Bboard.b2g==''\
           and board.s2f=='':
            moves = '2e2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b2e)and Bboard.b2h==''\
           and board.s2f+board.s2g=='':
            moves = '2e2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b2e)and Bboard.b2i==''\
           and board.s2f+board.s2g+board.s2h=='':
            moves = '2e2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b2e)and Bboard.b4e==''\
           and board.s3e=='':
            moves = '2e4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b2e)and Bboard.b5e==''\
           and board.s3e+board.s4e=='':
            moves = '2e5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b2e)and Bboard.b6e==''\
           and board.s3e+board.s4e+board.s5e=='':
            moves = '2e6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b2e)and Bboard.b7e==''\
           and board.s3e+board.s4e+board.s5e+board.s6e=='':
            moves = '2e7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b2e)and Bboard.b8e==''\
           and board.s3e+board.s4e+board.s5e+board.s6e+board.s7e=='':
            moves = '2e8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b2e)and Bboard.b9e==''\
           and board.s3e+board.s4e+board.s5e+board.s6e+board.s7e+board.s8e=='':
            moves = '2e9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b2e)and Bboard.b4g==''\
           and board.s3f=='':
            moves = '2e4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b2e)and Bboard.b5h==''\
           and board.s3f+board.s4g=='':
            moves = '2e5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b2e)and Bboard.b6i==''\
           and board.s3f+board.s4g+board.s5h=='':
            moves = '2e6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b2e)and Bboard.b6a==''\
           and board.s5b+board.s4c+board.s3d=='':
            moves = '2e6a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b2e)and Bboard.b5b==''\
           and board.s4c+board.s3d=='':
            moves = '2e5b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b2e)and Bboard.b4c==''\
           and board.s3d=='':
            moves = '2e4c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b2e)and Bboard.b6a==''\
           and board.s5b+board.s4c+board.s3d=='':
            moves = '2e6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b2e)and Bboard.b5b==''\
           and board.s4c+board.s3d=='':
            moves = '2e5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',Bboard.b2e)and Bboard.b4c==''\
           and board.s3d=='':
            moves = '2e4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b3e !='':
        if re.match(r'[PLSGRK+]',   Bboard.b3e)and Bboard.b3d=='':
            moves = '3e3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b3e)and Bboard.b2d=='':
            moves = '3e2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b3e)and Bboard.b4d=='':
            moves = '3e4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b3e)and Bboard.b2e=='':
            moves = '3e2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b3e)and Bboard.b4e=='':
            moves = '3e4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b3e)and Bboard.b3f=='':
            moves = '3e3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b3e)and Bboard.b2f=='':
            moves = '3e2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b3e)and Bboard.b4f=='':
            moves = '3e4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b3e)and Bboard.b2c=='':
            moves = '3e2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b3e)and Bboard.b4c=='':
            moves = '3e4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b3e)and Bboard.b2c=='':
            moves = '3e2c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b3e)and Bboard.b4c=='':
            moves = '3e4c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b3e)and Bboard.b3a==''\
           and board.s3b+board.s3c+board.s3d=='':
            moves = '3e3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b3e)and Bboard.b3a==''\
           and board.s3b+board.s3c+board.s3d=='':
            moves = '3e3a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b3e)and Bboard.b3b==''\
           and board.s3c+board.s3d=='':
            moves = '3e3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b3e)and Bboard.b3b==''\
           and board.s3c+board.s3d=='':
            moves = '3e3b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|L',    Bboard.b3e)and Bboard.b3c==''\
           and board.s3d=='':
            moves = '3e3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b3e)and Bboard.b3c==''\
           and board.s3d=='':
            moves = '3e3c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b3e)and Bboard.b3g==''\
           and board.s3f=='':
            moves = '3e3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b3e)and Bboard.b3h==''\
           and board.s3f+board.s3g=='':
            moves = '3e3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b3e)and Bboard.b3i==''\
           and board.s3f+board.s3g+board.s3h=='':
            moves = '3e3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b3e)and Bboard.b1e==''\
           and board.s2e=='':
            moves = '3e1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b3e)and Bboard.b5e==''\
           and board.s4e=='':
            moves = '3e5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b3e)and Bboard.b6e==''\
           and board.s4e+board.s5e=='':
            moves = '3e6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b3e)and Bboard.b7e==''\
           and board.s4e+board.s5e+board.s6e=='':
            moves = '3e7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b3e)and Bboard.b8e==''\
           and board.s4e+board.s5e+board.s6e+board.s7e=='':
            moves = '3e8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b3e)and Bboard.b9e==''\
           and board.s4e+board.s5e+board.s6e+board.s7e+board.s8e=='':
            moves = '3e9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b3e)and Bboard.b1c==''\
           and board.s2d=='':
            moves = '3e1c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',Bboard.b3e)and Bboard.b1c==''\
           and board.s2d=='':
            moves = '3e1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b3e)and Bboard.b5g==''\
           and board.s2f=='':
            moves = '3e5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b3e)and Bboard.b6h==''\
           and board.s2f+board.s5g=='':
            moves = '3e6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b3e)and Bboard.b7i==''\
           and board.s2f+board.s5g+board.s6h=='':
            moves = '3e7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b3e)and Bboard.b7a==''\
           and board.s6b+board.s5c+board.s4d=='':
            moves = '3e7a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b3e)and Bboard.b6b==''\
           and board.s5c+board.s4d=='':
            moves = '3e6b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b3e)and Bboard.b5c==''\
           and board.s4d=='':
            moves = '3e5c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b3e)and Bboard.b7a==''\
           and board.s6b+board.s5c+board.s4d=='':
            moves = '3e7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b3e)and Bboard.b6b==''\
           and board.s5c+board.s4d=='':
            moves = '3e6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',Bboard.b3e)and Bboard.b5c==''\
           and board.s4d=='':
            moves = '3e5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b3e)and Bboard.b1g==''\
           and board.s2f=='':
            moves = '3e1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b4e !='':
        if re.match(r'[PLSGRK+]',   Bboard.b4e)and Bboard.b4d=='':
            moves = '4e4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b4e)and Bboard.b3d=='':
            moves = '4e3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b4e)and Bboard.b5d=='':
            moves = '4e5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b4e)and Bboard.b3e=='':
            moves = '4e3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b4e)and Bboard.b5e=='':
            moves = '4e5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b4e)and Bboard.b4f=='':
            moves = '4e4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b4e)and Bboard.b3f=='':
            moves = '4e3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b4e)and Bboard.b5f=='':
            moves = '4e5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b4e)and Bboard.b3c=='':
            moves = '4e3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b4e)and Bboard.b5c=='':
            moves = '4e5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b4e)and Bboard.b3c=='':
            moves = '4e3c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b4e)and Bboard.b5c=='':
            moves = '4e5c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b4e)and Bboard.b4a==''\
           and board.s4b+board.s4c+board.s4d=='':
            moves = '4e4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b4e)and Bboard.b4a==''\
           and board.s4b+board.s4c+board.s4d=='':
            moves = '4e4a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b4e)and Bboard.b4b==''\
           and board.s4c+board.s4d=='':
            moves = '4e4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b4e)and Bboard.b4b==''\
           and board.s4c+board.s4d=='':
            moves = '4e4b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|L',    Bboard.b4e)and Bboard.b4c==''\
           and board.s4d=='':
            moves = '4e4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b4e)and Bboard.b4c==''\
           and board.s4d=='':
            moves = '4e4c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b4e)and Bboard.b4g==''\
           and board.s4f=='':
            moves = '4e4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b4e)and Bboard.b4h==''\
           and board.s4f+board.s4g=='':
            moves = '4e4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b4e)and Bboard.b4i==''\
           and board.s4f+board.s4g+board.s4h=='':
            moves = '4e4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b4e)and Bboard.b1e==''\
           and board.s2e+board.s3e=='':
            moves = '4e1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b4e)and Bboard.b2e==''\
           and board.s3e=='':
            moves = '4e2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b4e)and Bboard.b6e==''\
           and board.s5e=='':
            moves = '4e6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b4e)and Bboard.b7e==''\
           and board.s5e+board.s6e=='':
            moves = '4e7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b4e)and Bboard.b8e==''\
           and board.s5e+board.s6e+board.s7e=='':
            moves = '4e8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b4e)and Bboard.b9e==''\
           and board.s5e+board.s6e+board.s7e+board.s8e=='':
            moves = '4e9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b4e)and Bboard.b1b==''\
           and board.s2c+board.s3d=='':
            moves = '4e1b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b4e)and Bboard.b2c==''\
           and board.s3d=='':
            moves = '4e2c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b4e)and Bboard.b1b==''\
           and board.s2c+board.s3d=='':
            moves = '4e1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',Bboard.b4e)and Bboard.b2c==''\
           and board.s3d=='':
            moves = '4e2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b4e)and Bboard.b6g==''\
           and board.s5f=='':
            moves = '4e6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b4e)and Bboard.b7h==''\
           and board.s5f+board.s6g=='':
            moves = '4e7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b4e)and Bboard.b8i==''\
           and board.s5f+board.s6g+board.s7h=='':
            moves = '4e8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b4e)and Bboard.b8a==''\
           and board.s7b+board.s6c+board.s5d=='':
            moves = '4e8a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b4e)and Bboard.b7b==''\
           and board.s6c+board.s5d=='':
            moves = '4e7b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b4e)and Bboard.b6c==''\
           and board.s5d=='':
            moves = '4e6c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b4e)and Bboard.b8a==''\
           and board.s7b+board.s6c+board.s5d=='':
            moves = '4e8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b4e)and Bboard.b7b==''\
           and board.s6c+board.s5d=='':
            moves = '4e7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',Bboard.b4e)and Bboard.b6c==''\
           and board.s5d=='':
            moves = '4e6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b4e)and Bboard.b2g==''\
           and board.s3f=='':
            moves = '4e2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b4e)and Bboard.b1h==''\
           and board.s3f+board.s2g=='':
            moves = '4e1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b5e !='':
        if re.match(r'[PLSGRK+]',   Bboard.b5e)and Bboard.b5d=='':
            moves = '5e5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b5e)and Bboard.b4d=='':
            moves = '5e4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b5e)and Bboard.b6d=='':
            moves = '5e6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b5e)and Bboard.b4e=='':
            moves = '5e4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b5e)and Bboard.b6e=='':
            moves = '5e6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b5e)and Bboard.b5f=='':
            moves = '5e5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b5e)and Bboard.b4f=='':
            moves = '5e4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b5e)and Bboard.b6f=='':
            moves = '5e6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b5e)and Bboard.b4c=='':
            moves = '5e4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b5e)and Bboard.b6c=='':
            moves = '5e6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b5e)and Bboard.b4c=='':
            moves = '5e4c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b5e)and Bboard.b6c=='':
            moves = '5e6c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b5e)and Bboard.b5a==''\
           and board.s5b+board.s5c+board.s5d=='':
            moves = '5e5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b5e)and Bboard.b5a==''\
           and board.s5b+board.s5c+board.s5d=='':
            moves = '5e5a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b5e)and Bboard.b5b==''\
           and board.s5c+board.s5d=='':
            moves = '5e5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b5e)and Bboard.b5b==''\
           and board.s5c+board.s5d=='':
            moves = '5e5b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|L',    Bboard.b5e)and Bboard.b5c==''\
           and board.s5d=='':
            moves = '5e5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b5e)and Bboard.b5c==''\
           and board.s5d=='':
            moves = '5e5c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b5e)and Bboard.b5g==''\
           and board.s5f=='':
            moves = '5e5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b5e)and Bboard.b5h==''\
           and board.s5f+board.s5g=='':
            moves = '5e5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b5e)and Bboard.b5i==''\
           and board.s5f+board.s5g+board.s5h=='':
            moves = '5e5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b5e)and Bboard.b1e==''\
           and board.s2e+board.s3e+board.s4e=='':
            moves = '5e1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b5e)and Bboard.b2e==''\
           and board.s3e+board.s4e=='':
            moves = '5e2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b5e)and Bboard.b3e==''\
           and board.s4e=='':
            moves = '5e3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b5e)and Bboard.b7e==''\
           and board.s6e=='':
            moves = '5e7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b5e)and Bboard.b8e==''\
           and board.s6e+board.s7e=='':
            moves = '5e8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b5e)and Bboard.b9e==''\
           and board.s6e+board.s7e+board.s8e=='':
            moves = '5e9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b5e)and Bboard.b1a==''\
           and board.s2b+board.s3c+board.s4d=='':
            moves = '5e1a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b5e)and Bboard.b2b==''\
           and board.s3c+board.s4d=='':
            moves = '5e2b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b5e)and Bboard.b3c==''\
           and board.s4d=='':
            moves = '5e3c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b5e)and Bboard.b1a==''\
           and board.s2b+board.s3c+board.s4d=='':
            moves = '5e1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b5e)and Bboard.b2b==''\
           and board.s3c+board.s4d=='':
            moves = '5e2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',Bboard.b5e)and Bboard.b3c==''\
           and board.s4d=='':
            moves = '5e3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b5e)and Bboard.b7g==''\
           and board.s6f=='':
            moves = '5e7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b5e)and Bboard.b8h==''\
           and board.s6f+board.s7g=='':
            moves = '5e8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b5e)and Bboard.b9i==''\
           and board.s6f+board.s7g+board.s8h=='':
            moves = '5e9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b5e)and Bboard.b9a==''\
           and board.s8b+board.s7c+board.s6d=='':
            moves = '5e9a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b5e)and Bboard.b8b==''\
           and board.s7c+board.s6d=='':
            moves = '5e8b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b5e)and Bboard.b7c==''\
           and board.s6d=='':
            moves = '5e7c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b5e)and Bboard.b9a==''\
           and board.s8b+board.s7c+board.s6d=='':
            moves = '5e9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b5e)and Bboard.b8b==''\
           and board.s7c+board.s6d=='':
            moves = '5e8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',Bboard.b5e)and Bboard.b7c==''\
           and board.s6d=='':
            moves = '5e7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b5e)and Bboard.b3g==''\
           and board.s4f=='':
            moves = '5e3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b5e)and Bboard.b2h==''\
           and board.s4f+board.s3g=='':
            moves = '5e2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b5e)and Bboard.b1i==''\
           and board.s4f+board.s3g+board.s2h=='':
            moves = '5e1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b6e !='':
        if re.match(r'[PLSGRK+]',   Bboard.b6e)and Bboard.b6d=='':
            moves = '6e6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b6e)and Bboard.b5d=='':
            moves = '6e5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b6e)and Bboard.b7d=='':
            moves = '6e7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b6e)and Bboard.b5e=='':
            moves = '6e5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b6e)and Bboard.b7e=='':
            moves = '6e7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b6e)and Bboard.b6f=='':
            moves = '6e6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b6e)and Bboard.b5f=='':
            moves = '6e5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b6e)and Bboard.b7f=='':
            moves = '6e7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b6e)and Bboard.b5c=='':
            moves = '6e5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b6e)and Bboard.b7c=='':
            moves = '6e7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b6e)and Bboard.b5c=='':
            moves = '6e5c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b6e)and Bboard.b7c=='':
            moves = '6e7c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b6e)and Bboard.b6a==''\
           and board.s6b+board.s6c+board.s6d=='':
            moves = '6e6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b6e)and Bboard.b6a==''\
           and board.s6b+board.s6c+board.s6d=='':
            moves = '6e6a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b6e)and Bboard.b6b==''\
           and board.s6c+board.s6d=='':
            moves = '6e6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b6e)and Bboard.b6b==''\
           and board.s6c+board.s6d=='':
            moves = '6e6b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|L',    Bboard.b6e)and Bboard.b6c==''\
           and board.s6d=='':
            moves = '6e6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b6e)and Bboard.b6c==''\
           and board.s6d=='':
            moves = '6e6c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b6e)and Bboard.b6g==''\
           and board.s6f=='':
            moves = '6e6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b6e)and Bboard.b6h==''\
           and board.s6f+board.s6g=='':
            moves = '6e6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b6e)and Bboard.b6i==''\
           and board.s6f+board.s6g+board.s6h=='':
            moves = '6e6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b6e)and Bboard.b9e==''\
           and board.s8e+board.s7e=='':
            moves = '6e9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b6e)and Bboard.b8e==''\
           and board.s7e=='':
            moves = '6e8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b6e)and Bboard.b4e==''\
           and board.s5e=='':
            moves = '6e4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b6e)and Bboard.b3e==''\
           and board.s5e+board.s4e=='':
            moves = '6e3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b6e)and Bboard.b2e==''\
           and board.s5e+board.s4e+board.s3e=='':
            moves = '6e2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b6e)and Bboard.b1e==''\
           and board.s5e+board.s4e+board.s3e+board.s2e=='':
            moves = '6e1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b6e)and Bboard.b9b==''\
           and board.s8c+board.s7d=='':
            moves = '6e9b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b6e)and Bboard.b8c==''\
           and board.s7d=='':
            moves = '6e8c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b6e)and Bboard.b9b==''\
           and board.s8c+board.s7d=='':
            moves = '6e9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',Bboard.b6e)and Bboard.b8c==''\
           and board.s7d=='':
            moves = '6e8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b6e)and Bboard.b4g==''\
           and board.s5f=='':
            moves = '6e4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b6e)and Bboard.b3h==''\
           and board.s5f+board.s4g=='':
            moves = '6e3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b6e)and Bboard.b2i==''\
           and board.s5f+board.s4g+board.s3h=='':
            moves = '6e2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b6e)and Bboard.b2a==''\
           and board.s3b+board.s4c+board.s5d=='':
            moves = '6e2a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b6e)and Bboard.b3b==''\
           and board.s4c+board.s5d=='':
            moves = '6e3b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b6e)and Bboard.b4c==''\
           and board.s5d=='':
            moves = '6e4c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b6e)and Bboard.b2a==''\
           and board.s3b+board.s4c+board.s5d=='':
            moves = '6e2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b6e)and Bboard.b3b==''\
           and board.s4c+board.s5d=='':
            moves = '6e3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',Bboard.b6e)and Bboard.b4c==''\
           and board.s5d=='':
            moves = '6e4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b6e)and Bboard.b8g==''\
           and board.s7f=='':
            moves = '6e8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b6e)and Bboard.b9h==''\
           and board.s7f+board.s8g=='':
            moves = '6e9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b7e !='':
        if re.match(r'[PLSGRK+]',   Bboard.b7e)and Bboard.b7d=='':
            moves = '7e7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b7e)and Bboard.b6d=='':
            moves = '7e6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b7e)and Bboard.b8d=='':
            moves = '7e8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b7e)and Bboard.b6e=='':
            moves = '7e6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b7e)and Bboard.b8e=='':
            moves = '7e8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b7e)and Bboard.b7f=='':
            moves = '7e7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b7e)and Bboard.b6f=='':
            moves = '7e6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b7e)and Bboard.b8f=='':
            moves = '7e8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b7e)and Bboard.b6c=='':
            moves = '7e6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b7e)and Bboard.b8c=='':
            moves = '7e8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b7e)and Bboard.b6c=='':
            moves = '7e6c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b7e)and Bboard.b8c=='':
            moves = '7e8c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b7e)and Bboard.b7a==''\
           and board.s7b+board.s7c+board.s7d=='':
            moves = '7e7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b7e)and Bboard.b7a==''\
           and board.s7b+board.s7c+board.s7d=='':
            moves = '7e7a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b7e)and Bboard.b7b==''\
           and board.s7c+board.s7d=='':
            moves = '7e7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b7e)and Bboard.b7b==''\
           and board.s7c+board.s7d=='':
            moves = '7e7b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|L',    Bboard.b7e)and Bboard.b7c==''\
           and board.s7d=='':
            moves = '7e7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b7e)and Bboard.b7c==''\
           and board.s7d=='':
            moves = '7e7c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b7e)and Bboard.b7g==''\
           and board.s7f=='':
            moves = '7e7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b7e)and Bboard.b7h==''\
           and board.s7f+board.s7g=='':
            moves = '7e7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b7e)and Bboard.b7i==''\
           and board.s7f+board.s7g+board.s7h=='':
            moves = '7e7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b7e)and Bboard.b9e==''\
           and board.s8e=='':
            moves = '7e9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b7e)and Bboard.b5e==''\
           and board.s6e=='':
            moves = '7e5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b7e)and Bboard.b4e==''\
           and board.s6e+board.s5e=='':
            moves = '7e4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b7e)and Bboard.b3e==''\
           and board.s6e+board.s5e+board.s4e=='':
            moves = '7e3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b7e)and Bboard.b2e==''\
           and board.s6e+board.s5e+board.s4e+board.s3e=='':
            moves = '7e2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b7e)and Bboard.b1e==''\
           and board.s6e+board.s5e+board.s4e+board.s3e+board.s2e=='':
            moves = '7e1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b7e)and Bboard.b9c==''\
           and board.s8d=='':
            moves = '7e9c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',Bboard.b7e)and Bboard.b9c==''\
           and board.s8d=='':
            moves = '7e9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b7e)and Bboard.b5g==''\
           and board.s8f=='':
            moves = '7e5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b7e)and Bboard.b4h==''\
           and board.s8f+board.s5g=='':
            moves = '7e4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b7e)and Bboard.b3i==''\
           and board.s8f+board.s5g+board.s4h=='':
            moves = '7e3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b7e)and Bboard.b3a==''\
           and board.s4b+board.s5c+board.s6d=='':
            moves = '7e3a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b7e)and Bboard.b4b==''\
           and board.s5c+board.s6d=='':
            moves = '7e4b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b7e)and Bboard.b5c==''\
           and board.s6d=='':
            moves = '7e5c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b7e)and Bboard.b3a==''\
           and board.s4b+board.s5c+board.s6d=='':
            moves = '7e3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b7e)and Bboard.b4b==''\
           and board.s5c+board.s6d=='':
            moves = '7e4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',Bboard.b7e)and Bboard.b5c==''\
           and board.s6d=='':
            moves = '7e5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b7e)and Bboard.b9g==''\
           and board.s8f=='':
            moves = '7e9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b8e !='':
        if re.match(r'[PLSGRK+]',   Bboard.b8e)and Bboard.b8d=='':
            moves = '8e8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b8e)and Bboard.b7d=='':
            moves = '8e7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b8e)and Bboard.b9d=='':
            moves = '8e9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b8e)and Bboard.b7e=='':
            moves = '8e7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b8e)and Bboard.b9e=='':
            moves = '8e9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b8e)and Bboard.b8f=='':
            moves = '8e8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b8e)and Bboard.b7f=='':
            moves = '8e7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b8e)and Bboard.b9f=='':
            moves = '8e9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b8e)and Bboard.b7c=='':
            moves = '8e7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b8e)and Bboard.b9c=='':
            moves = '8e9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b8e)and Bboard.b7c=='':
            moves = '8e7c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b8e)and Bboard.b9c=='':
            moves = '8e9c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b8e)and Bboard.b8a==''\
           and board.s8b+board.s8c+board.s8d=='':
            moves = '8e8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b8e)and Bboard.b8a==''\
           and board.s8b+board.s8c+board.s8d=='':
            moves = '8e8a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b8e)and Bboard.b8b==''\
           and board.s8c+board.s8d=='':
            moves = '8e8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b8e)and Bboard.b8b==''\
           and board.s8c+board.s8d=='':
            moves = '8e8b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|L',    Bboard.b8e)and Bboard.b8c==''\
           and board.s8d=='':
            moves = '8e8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b8e)and Bboard.b8c==''\
           and board.s8d=='':
            moves = '8e8c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b8e)and Bboard.b8g==''\
           and board.s8f=='':
            moves = '8e8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b8e)and Bboard.b8h==''\
           and board.s8f+board.s8g=='':
            moves = '8e8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b8e)and Bboard.b8i==''\
           and board.s8f+board.s8g+board.s8h=='':
            moves = '8e8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b8e)and Bboard.b6e==''\
           and board.s7e=='':
            moves = '8e6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b8e)and Bboard.b5e==''\
           and board.s7e+board.s6e=='':
            moves = '8e5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b8e)and Bboard.b4e==''\
           and board.s7e+board.s6e+board.s5e=='':
            moves = '8e4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b8e)and Bboard.b3e==''\
           and board.s7e+board.s6e+board.s5e+board.s4e=='':
            moves = '8e3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b8e)and Bboard.b2e==''\
           and board.s7e+board.s6e+board.s5e+board.s4e+board.s3e=='':
            moves = '8e2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b8e)and Bboard.b1e==''\
           and board.s7e+board.s6e+board.s5e+board.s4e+board.s3e+board.s2e=='':
            moves = '8e1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b8e)and Bboard.b6g==''\
           and board.s7f=='':
            moves = '8e6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b8e)and Bboard.b5h==''\
           and board.s7f+board.s6g=='':
            moves = '8e5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b8e)and Bboard.b4i==''\
           and board.s7f+board.s6g+board.s5h=='':
            moves = '8e4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b8e)and Bboard.b4a==''\
           and board.s5b+board.s6c+board.s7d=='':
            moves = '8e4a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b8e)and Bboard.b5b==''\
           and board.s6c+board.s7d=='':
            moves = '8e5b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b8e)and Bboard.b6c==''\
           and board.s7d=='':
            moves = '8e6c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b8e)and Bboard.b4a==''\
           and board.s5b+board.s6c+board.s7d=='':
            moves = '8e4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b8e)and Bboard.b5b==''\
           and board.s6c+board.s7d=='':
            moves = '8e5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',Bboard.b8e)and Bboard.b6c==''\
           and board.s7d=='':
            moves = '8e6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b9e !='':
        if re.match(r'[PLSGRK+]',   Bboard.b9e)and Bboard.b9d=='':
            moves = '9e9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b9e)and Bboard.b8d=='':
            moves = '9e8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b9e)and Bboard.b8e=='':
            moves = '9e8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b9e)and Bboard.b9f=='':
            moves = '9e9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b9e)and Bboard.b8f=='':
            moves = '9e8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b9e)and Bboard.b8c=='':
            moves = '9e8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b9e)and Bboard.b8c=='':
            moves = '9e8c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b9e)and Bboard.b9a==''\
           and board.s9b+board.s9c+board.s9d=='':
            moves = '9e9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b9e)and Bboard.b9a==''\
           and board.s9b+board.s9c+board.s9d=='':
            moves = '9e9a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b9e)and Bboard.b9b==''\
           and board.s9c+board.s9d=='':
            moves = '9e9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b9e)and Bboard.b9b==''\
           and board.s9c+board.s9d=='':
            moves = '9e9b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|L',    Bboard.b9e)and Bboard.b9c==''\
           and board.s9d=='':
            moves = '9e9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b9e)and Bboard.b9c==''\
           and board.s9d=='':
            moves = '9e9c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b9e)and Bboard.b9g==''\
           and board.s9f=='':
            moves = '9e9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b9e)and Bboard.b9h==''\
           and board.s9f+board.s9g=='':
            moves = '9e9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b9e)and Bboard.b9i==''\
           and board.s9f+board.s9g+board.s9h=='':
            moves = '9e9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b9e)and Bboard.b9i==''\
           and board.s9f+board.s9g+board.s9h=='':
            moves = '9e9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b9e)and Bboard.b7e==''\
           and board.s8e=='':
            moves = '9e7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b9e)and Bboard.b6e==''\
           and board.s8e+board.s7e=='':
            moves = '9e6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b9e)and Bboard.b5e==''\
           and board.s8e+board.s7e+board.s6e=='':
            moves = '9e5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b9e)and Bboard.b4e==''\
           and board.s8e+board.s7e+board.s6e+board.s5e=='':
            moves = '9e4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b9e)and Bboard.b3e==''\
           and board.s8e+board.s7e+board.s6e+board.s5e+board.s4e=='':
            moves = '9e3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b9e)and Bboard.b2e==''\
           and board.s8e+board.s7e+board.s6e+board.s5e+board.s4e+board.s3e=='':
            moves = '9e2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b9e)and Bboard.b1e==''\
           and board.s8e+board.s7e+board.s6e+board.s5e+board.s4e+board.s3e+board.s2e=='':
            moves = '9e1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b9e)and Bboard.b7g==''\
           and board.s8f=='':
            moves = '9e7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b9e)and Bboard.b6h==''\
           and board.s8f+board.s7g=='':
            moves = '9e6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b9e)and Bboard.b5i==''\
           and board.s8f+board.s7g+board.s6h=='':
            moves = '9e5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b9e)and Bboard.b5a==''\
           and board.s6b+board.s7c+board.s8d=='':
            moves = '9e5a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b9e)and Bboard.b6b==''\
           and board.s7c+board.s8d=='':
            moves = '9e6b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b9e)and Bboard.b7c==''\
           and board.s8d=='':
            moves = '9e7c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b9e)and Bboard.b5a==''\
           and board.s6b+board.s7c+board.s8d=='':
            moves = '9e5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b9e)and Bboard.b6b==''\
           and board.s7c+board.s8d=='':
            moves = '9e6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',Bboard.b9e)and Bboard.b7c==''\
           and board.s8d=='':
            moves = '9e7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b1f !='':
        if re.match(r'[PLSGRK+]',   Bboard.b1f)and Bboard.b1e=='':
            moves = '1f1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b1f)and Bboard.b2e=='':
            moves = '1f2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b1f)and Bboard.b2f=='':
            moves = '1f2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b1f)and Bboard.b1g=='':
            moves = '1f1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b1f)and Bboard.b2g=='':
            moves = '1f2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b1f)and Bboard.b2d=='':
            moves = '1f2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b1f)and Bboard.b1a==''\
           and board.s1b+board.s1c+board.s1d+board.s1e=='':
            moves = '1f1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b1f)and Bboard.b1a==''\
           and board.s1b+board.s1c+board.s1d+board.s1e=='':
            moves = '1f1a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b1f)and Bboard.b1b==''\
           and board.s1c+board.s1d+board.s1e=='':
            moves = '1f1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b1f)and Bboard.b1b==''\
           and board.s1c+board.s1d+board.s1e=='':
            moves = '1f1b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|L',    Bboard.b1f)and Bboard.b1c==''\
           and board.s1d+board.s1e=='':
            moves = '1f1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b1f)and Bboard.b1c==''\
           and board.s1d+board.s1e=='':
            moves = '1f1c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b1f)and Bboard.b1d==''\
           and board.s1e=='':
            moves = '1f1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b1f)and Bboard.b1h==''\
           and board.s1g=='':
            moves = '1f1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b1f)and Bboard.b1i==''\
           and board.s1g+board.s1h=='':
            moves = '1f1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b1f)and Bboard.b3f==''\
           and board.s2f=='':
            moves = '1f3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b1f)and Bboard.b4f==''\
           and board.s2f+board.s3f=='':
            moves = '1f4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b1f)and Bboard.b5f==''\
           and board.s2f+board.s3f+board.s4f=='':
            moves = '1f5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b1f)and Bboard.b6f==''\
           and board.s2f+board.s3f+board.s4f+board.s5f=='':
            moves = '1f6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b1f)and Bboard.b7f==''\
           and board.s2f+board.s3f+board.s4f+board.s5f+board.s6f=='':
            moves = '1f7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b1f)and Bboard.b8f==''\
           and board.s2f+board.s3f+board.s4f+board.s5f+board.s6f+board.s7f=='':
            moves = '1f8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b1f)and Bboard.b9f==''\
           and board.s2f+board.s3f+board.s4f+board.s5f+board.s6f+board.s7f+board.s8f=='':
            moves = '1f9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b1f)and Bboard.b3d==''\
           and board.s2e=='':
            moves = '1f3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b1f)and Bboard.b4c==''\
           and board.s2e+board.s3d=='':
            moves = '1f4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b1f)and Bboard.b5b==''\
           and board.s2e+board.s3d+board.s4c=='':
            moves = '1f5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b1f)and Bboard.b6a==''\
           and board.s2e+board.s3d+board.s4c+board.s5b=='':
            moves = '1f6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b1f)and Bboard.b4i==''\
           and board.s3h+board.s2g=='':
            moves = '1f4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b1f)and Bboard.b3h==''\
           and board.s2g=='':
            moves = '1f3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b1f)and Bboard.b4c==''\
           and board.s2e+board.s3d=='':
            moves = '1f4c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b1f)and Bboard.b5b==''\
           and board.s2e+board.s3d+board.s4c=='':
            moves = '1f5b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b1f)and Bboard.b6a==''\
           and board.s2e+board.s3d+board.s4c+board.s5b=='':
            moves = '1f6a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b2f !='':
        if re.match(r'[PLSGRK+]',   Bboard.b2f)and Bboard.b2e=='':
            moves = '2f2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b2f)and Bboard.b1e=='':
            moves = '2f1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b2f)and Bboard.b3e=='':
            moves = '2f3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b2f)and Bboard.b1f=='':
            moves = '2f1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b2f)and Bboard.b3f=='':
            moves = '2f3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b2f)and Bboard.b2g=='':
            moves = '2f2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b2f)and Bboard.b1g=='':
            moves = '2f1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b2f)and Bboard.b3g=='':
            moves = '2f3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b2f)and Bboard.b1d=='':
            moves = '2f1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b2f)and Bboard.b3d=='':
            moves = '2f3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b2f)and Bboard.b2a==''\
           and board.s2b+board.s2c+board.s2d+board.s2e=='':
            moves = '2f2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b2f)and Bboard.b2a==''\
           and board.s2b+board.s2c+board.s2d+board.s2e=='':
            moves = '2f2a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b2f)and Bboard.b2b==''\
           and board.s2c+board.s2d+board.s2e=='':
            moves = '2f2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b2f)and Bboard.b2b==''\
           and board.s2c+board.s2d+board.s2e=='':
            moves = '2f2b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|L',    Bboard.b2f)and Bboard.b2c==''\
           and board.s2d+board.s2e=='':
            moves = '2f2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b2f)and Bboard.b2c==''\
           and board.s2d+board.s2e=='':
            moves = '2f2c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b2f)and Bboard.b2d==''\
           and board.s2e=='':
            moves = '2f2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b2f)and Bboard.b2h==''\
           and board.s2g=='':
            moves = '2f2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b2f)and Bboard.b2i==''\
           and board.s2g+board.s2h=='':
            moves = '2f2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b2f)and Bboard.b4f==''\
           and board.s3f=='':
            moves = '2f4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b2f)and Bboard.b5f==''\
           and board.s3f+board.s4f=='':
            moves = '2f5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b2f)and Bboard.b6f==''\
           and board.s3f+board.s4f+board.s5f=='':
            moves = '2f6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b2f)and Bboard.b7f==''\
           and board.s3f+board.s4f+board.s5f+board.s6f=='':
            moves = '2f7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b2f)and Bboard.b8f==''\
           and board.s3f+board.s4f+board.s5f+board.s6f+board.s7f=='':
            moves = '2f8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b2f)and Bboard.b9f==''\
           and board.s3f+board.s4f+board.s5f+board.s6f+board.s7f+board.s8f=='':
            moves = '2f9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b2f)and Bboard.b4d==''\
           and board.s3e=='':
            moves = '2f4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b2f)and Bboard.b5c==''\
           and board.s3e+board.s4d=='':
            moves = '2f5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b2f)and Bboard.b6b==''\
           and board.s3e+board.s4d+board.s5c=='':
            moves = '2f6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b2f)and Bboard.b7a==''\
           and board.s3e+board.s4d+board.s5c+board.s6b=='':
            moves = '2f7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b2f)and Bboard.b5i==''\
           and board.s4h+board.s3g=='':
            moves = '2f5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b2f)and Bboard.b4h==''\
           and board.s3g=='':
            moves = '2f4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b2f)and Bboard.b5c==''\
           and board.s3e+board.s4d=='':
            moves = '2f5c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b2f)and Bboard.b6b==''\
           and board.s3e+board.s4d+board.s5c=='':
            moves = '2f6b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b2f)and Bboard.b7a==''\
           and board.s3e+board.s4d+board.s5c+board.s6b=='':
            moves = '2f7a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b3f !='':
        if re.match(r'[PLSGRK+]',   Bboard.b3f)and Bboard.b3e=='':
            moves = '3f3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b3f)and Bboard.b2e=='':
            moves = '3f2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b3f)and Bboard.b4e=='':
            moves = '3f4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b3f)and Bboard.b2f=='':
            moves = '3f2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b3f)and Bboard.b4f=='':
            moves = '3f4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b3f)and Bboard.b3g=='':
            moves = '3f3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b3f)and Bboard.b2g=='':
            moves = '3f2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b3f)and Bboard.b4g=='':
            moves = '3f4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b3f)and Bboard.b2d=='':
            moves = '3f2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b3f)and Bboard.b4d=='':
            moves = '3f4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b3f)and Bboard.b3a==''\
           and board.s3b+board.s3c+board.s3d+board.s3e=='':
            moves = '3f3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b3f)and Bboard.b3a==''\
           and board.s3b+board.s3c+board.s3d+board.s3e=='':
            moves = '3f3a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b3f)and Bboard.b3b==''\
           and board.s3c+board.s3d+board.s3e=='':
            moves = '3f3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b3f)and Bboard.b3b==''\
           and board.s3c+board.s3d+board.s3e=='':
            moves = '3f3b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|L',    Bboard.b3f)and Bboard.b3c==''\
           and board.s3d+board.s3e=='':
            moves = '3f3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b3f)and Bboard.b3c==''\
           and board.s3d+board.s3e=='':
            moves = '3f3c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b3f)and Bboard.b3d==''\
           and board.s3e=='':
            moves = '3f3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b3f)and Bboard.b3h==''\
           and board.s3g=='':
            moves = '3f3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b3f)and Bboard.b3i==''\
           and board.s3g+board.s3h=='':
            moves = '3f3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b3f)and Bboard.b1f==''\
           and board.s2f=='':
            moves = '3f1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b3f)and Bboard.b5f==''\
           and board.s4f=='':
            moves = '3f5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b3f)and Bboard.b6f==''\
           and board.s4f+board.s5f=='':
            moves = '3f6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b3f)and Bboard.b7f==''\
           and board.s4f+board.s5f+board.s6f=='':
            moves = '3f7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b3f)and Bboard.b8f==''\
           and board.s4f+board.s5f+board.s6f+board.s7f=='':
            moves = '3f8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b3f)and Bboard.b9f==''\
           and board.s4f+board.s5f+board.s6f+board.s7f+board.s8f=='':
            moves = '3f9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b3f)and Bboard.b1h==''\
           and board.s2g=='':
            moves = '3f1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b3f)and Bboard.b5d==''\
           and board.s4e=='':
            moves = '3f5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b3f)and Bboard.b6c==''\
           and board.s4e+board.s5d=='':
            moves = '3f6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b3f)and Bboard.b7b==''\
           and board.s4e+board.s5d+board.s6c=='':
            moves = '3f7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b3f)and Bboard.b8a==''\
           and board.s4e+board.s5d+board.s6c+board.s7b=='':
            moves = '3f8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b3f)and Bboard.b6i==''\
           and board.s5h+board.s4g=='':
            moves = '3f6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b3f)and Bboard.b5h==''\
           and board.s4g=='':
            moves = '3f5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b3f)and Bboard.b1d==''\
           and board.s2e=='':
            moves = '3f1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b3f)and Bboard.b6c==''\
           and board.s4e+board.s5d=='':
            moves = '3f6c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b3f)and Bboard.b7b==''\
           and board.s4e+board.s5d+board.s6c=='':
            moves = '3f7b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b3f)and Bboard.b8a==''\
           and board.s4e+board.s5d+board.s6c+board.s7b=='':
            moves = '3f8a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b4f !='':
        if re.match(r'[PLSGRK+]',   Bboard.b4f)and Bboard.b4e=='':
            moves = '4f4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b4f)and Bboard.b3e=='':
            moves = '4f3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b4f)and Bboard.b5e=='':
            moves = '4f5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b4f)and Bboard.b3f=='':
            moves = '4f3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b4f)and Bboard.b5f=='':
            moves = '4f5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b4f)and Bboard.b4g=='':
            moves = '4f4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b4f)and Bboard.b3g=='':
            moves = '4f3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b4f)and Bboard.b5g=='':
            moves = '4f5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b4f)and Bboard.b3d=='':
            moves = '4f3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b4f)and Bboard.b5d=='':
            moves = '4f5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b4f)and Bboard.b4a==''\
           and board.s4b+board.s4c+board.s4d+board.s4e=='':
            moves = '4f4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b4f)and Bboard.b4a==''\
           and board.s4b+board.s4c+board.s4d+board.s4e=='':
            moves = '4f4a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b4f)and Bboard.b4b==''\
           and board.s4c+board.s4d+board.s4e=='':
            moves = '4f4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b4f)and Bboard.b4b==''\
           and board.s4c+board.s4d+board.s4e=='':
            moves = '4f4b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|L',    Bboard.b4f)and Bboard.b4c==''\
           and board.s4d+board.s4e=='':
            moves = '4f4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b4f)and Bboard.b4c==''\
           and board.s4d+board.s4e=='':
            moves = '4f4c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b4f)and Bboard.b4d==''\
           and board.s4e=='':
            moves = '4f4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b4f)and Bboard.b4h==''\
           and board.s4g=='':
            moves = '4f4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b4f)and Bboard.b4i==''\
           and board.s4g+board.s4h=='':
            moves = '4f4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b4f)and Bboard.b1f==''\
           and board.s2f+board.s3f=='':
            moves = '4f1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b4f)and Bboard.b2f==''\
           and board.s3f=='':
            moves = '4f2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b4f)and Bboard.b6f==''\
           and board.s5f=='':
            moves = '4f6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b4f)and Bboard.b7f==''\
           and board.s5f+board.s6f=='':
            moves = '4f7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b4f)and Bboard.b8f==''\
           and board.s5f+board.s6f+board.s7f=='':
            moves = '4f8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b4f)and Bboard.b9f==''\
           and board.s5f+board.s6f+board.s7f+board.s8f=='':
            moves = '4f9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b4f)and Bboard.b1i==''\
           and board.s2h+board.s3g=='':
            moves = '4f1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b4f)and Bboard.b2h==''\
           and board.s3g=='':
            moves = '4f2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b4f)and Bboard.b6d==''\
           and board.s5e=='':
            moves = '4f6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b4f)and Bboard.b7c==''\
           and board.s5e+board.s6d=='':
            moves = '4f7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b4f)and Bboard.b8b==''\
           and board.s5e+board.s6d+board.s7c=='':
            moves = '4f8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b4f)and Bboard.b9a==''\
           and board.s5e+board.s6d+board.s7c+board.s8b=='':
            moves = '4f9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b4f)and Bboard.b7i==''\
           and board.s6h+board.s5g=='':
            moves = '4f7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b4f)and Bboard.b6h==''\
           and board.s5g=='':
            moves = '4f6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b4f)and Bboard.b2d==''\
           and board.s3e=='':
            moves = '4f2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b4f)and Bboard.b1c==''\
           and board.s3e+board.s2d=='':
            moves = '4f1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b4f)and Bboard.b7c==''\
           and board.s5e+board.s6d=='':
            moves = '4f7c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b4f)and Bboard.b8b==''\
           and board.s5e+board.s6d+board.s7c=='':
            moves = '4f8b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b4f)and Bboard.b1c==''\
           and board.s3e+board.s2d=='':
            moves = '4f1c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b4f)and Bboard.b9a==''\
           and board.s5e+board.s6d+board.s7c+board.s8b=='':
            moves = '4f9a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b5f !='':
        if re.match(r'[PLSGRK+]',   Bboard.b5f)and Bboard.b5e=='':
            moves = '5f5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b5f)and Bboard.b4e=='':
            moves = '5f4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b5f)and Bboard.b6e=='':
            moves = '5f6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b5f)and Bboard.b4f=='':
            moves = '5f4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b5f)and Bboard.b6f=='':
            moves = '5f6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b5f)and Bboard.b5g=='':
            moves = '5f5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b5f)and Bboard.b4g=='':
            moves = '5f4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b5f)and Bboard.b6g=='':
            moves = '5f6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b5f)and Bboard.b4d=='':
            moves = '5f4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b5f)and Bboard.b6d=='':
            moves = '5f6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b5f)and Bboard.b5a==''\
           and board.s5b+board.s5c+board.s5d+board.s5e=='':
            moves = '5f5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b5f)and Bboard.b5a==''\
           and board.s5b+board.s5c+board.s5d+board.s5e=='':
            moves = '5f5a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b5f)and Bboard.b5b==''\
           and board.s5c+board.s5d+board.s5e=='':
            moves = '5f5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b5f)and Bboard.b5b==''\
           and board.s5c+board.s5d+board.s5e=='':
            moves = '5f5b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|L',    Bboard.b5f)and Bboard.b5c==''\
           and board.s5d+board.s5e=='':
            moves = '5f5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b5f)and Bboard.b5c==''\
           and board.s5d+board.s5e=='':
            moves = '5f5c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b5f)and Bboard.b5d==''\
           and board.s5e=='':
            moves = '5f5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b5f)and Bboard.b5h==''\
           and board.s5g=='':
            moves = '5f5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b5f)and Bboard.b5i==''\
           and board.s5g+board.s5h=='':
            moves = '5f5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b5f)and Bboard.b1f==''\
           and board.s2f+board.s3f+board.s4f=='':
            moves = '5f1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b5f)and Bboard.b2f==''\
           and board.s3f+board.s4f=='':
            moves = '5f2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b5f)and Bboard.b3f==''\
           and board.s4f=='':
            moves = '5f3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b5f)and Bboard.b7f==''\
           and board.s6f=='':
            moves = '5f7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b5f)and Bboard.b8f==''\
           and board.s6f+board.s7f=='':
            moves = '5f8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b5f)and Bboard.b9f==''\
           and board.s6f+board.s7f+board.s8f=='':
            moves = '5f9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',  Bboard.b5f)and Bboard.b2i==''\
          and board.s3h+board.s4g=='':
           moves ='5f2i'
           kaihimore(moves)
           if oute.oute == 0:
              depth1.append(moves)
        if re.match(r'\+B|B',Bboard.b5f)and Bboard.b3h==''\
          and board.s4g=='':
           moves ='5f3h'
           kaihimore(moves)
           if oute.oute == 0:
              depth1.append(moves)
        if re.match(r'\+B|B',  Bboard.b5f)and Bboard.b7d==''\
          and board.s6e=='':
           moves ='5f7d'
           kaihimore(moves)
           if oute.oute == 0:
              depth1.append(moves)
        if re.match('\+B',  Bboard.b5f)and Bboard.b8c==''\
          and board.s6e+board.s7d=='':
           moves ='5f8c'
           kaihimore(moves)
           if oute.oute == 0:
              depth1.append(moves)
        if re.match('\+B',  Bboard.b5f)and Bboard.b9b==''\
          and board.s6e+board.s7d+board.s8c=='':
           moves ='5f9b'
           kaihimore(moves)
           if oute.oute == 0:
              depth1.append(moves)
        if re.match(r'\+B|B',  Bboard.b5f)and Bboard.b8i==''\
          and board.s7h+board.s6g=='':
           moves ='5f8i'
           kaihimore(moves)
           if oute.oute == 0:
              depth1.append(moves)
        if re.match(r'\+B|B',Bboard.b5f)and Bboard.b7h==''\
          and board.s6g=='':
           moves ='5f7h'
           kaihimore(moves)
           if oute.oute == 0:
              depth1.append(moves)
        if re.match(r'\+B|B',  Bboard.b5f)and Bboard.b3d==''\
          and board.s4e=='':
           moves ='5f3d'
           kaihimore(moves)
           if oute.oute == 0:
              depth1.append(moves)
        if re.match('\+B',  Bboard.b5f)and Bboard.b2c==''\
          and board.s4e+board.s3d=='':
           moves ='5f2c'
           kaihimore(moves)
           if oute.oute == 0:
              depth1.append(moves)
        if re.match('B',  Bboard.b5f)and Bboard.b8c==''\
          and board.s6e+board.s7d=='':
           moves ='5f8c+'
           kaihimore(moves)
           if oute.oute == 0:
              depth1.append(moves)
        if re.match('B',  Bboard.b5f)and Bboard.b2c==''\
          and board.s4e+board.s3d=='':
           moves ='5f2c+'
           kaihimore(moves)
           if oute.oute == 0:
              depth1.append(moves)

    if Bboard.b6f !='':
        if re.match(r'[PLSGRK+]',   Bboard.b6f)and Bboard.b6e=='':
            moves = '6f6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b6f)and Bboard.b5e=='':
            moves = '6f5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b6f)and Bboard.b7e=='':
            moves = '6f7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b6f)and Bboard.b5f=='':
            moves = '6f5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b6f)and Bboard.b7f=='':
            moves = '6f7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b6f)and Bboard.b6g=='':
            moves = '6f6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b6f)and Bboard.b5g=='':
            moves = '6f5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b6f)and Bboard.b7g=='':
            moves = '6f7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b6f)and Bboard.b5d=='':
            moves = '6f5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b6f)and Bboard.b7d=='':
            moves = '6f7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b6f)and Bboard.b6a==''\
           and board.s6b+board.s6c+board.s6d+board.s6e=='':
            moves = '6f6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b6f)and Bboard.b6a==''\
           and board.s6b+board.s6c+board.s6d+board.s6e=='':
            moves = '6f6a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b6f)and Bboard.b6b==''\
           and board.s6c+board.s6d+board.s6e=='':
            moves = '6f6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b6f)and Bboard.b6b==''\
           and board.s6c+board.s6d+board.s6e=='':
            moves = '6f6b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|L',    Bboard.b6f)and Bboard.b6c==''\
           and board.s6d+board.s6e=='':
            moves = '6f6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b6f)and Bboard.b6c==''\
           and board.s6d+board.s6e=='':
            moves = '6f6c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b6f)and Bboard.b6d==''\
           and board.s6e=='':
            moves = '6f6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b6f)and Bboard.b6h==''\
           and board.s6g=='':
            moves = '6f6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b6f)and Bboard.b6i==''\
           and board.s6g+board.s6h=='':
            moves = '6f6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b6f)and Bboard.b9f==''\
           and board.s8f+board.s7f=='':
            moves = '6f9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b6f)and Bboard.b8f==''\
           and board.s7f=='':
            moves = '6f8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b6f)and Bboard.b4f==''\
           and board.s5f=='':
            moves = '6f4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b6f)and Bboard.b3f==''\
           and board.s5f+board.s4f=='':
            moves = '6f3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b6f)and Bboard.b2f==''\
           and board.s5f+board.s4f+board.s3f=='':
            moves = '6f2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b6f)and Bboard.b1f==''\
           and board.s5f+board.s4f+board.s3f+board.s2f=='':
            moves = '6f1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b6f)and Bboard.b9i==''\
           and board.s8h+board.s7g=='':
            moves = '6f9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b6f)and Bboard.b8h==''\
           and board.s7g=='':
            moves = '6f8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b6f)and Bboard.b4d==''\
           and board.s5e=='':
            moves = '6f4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b6f)and Bboard.b3c==''\
           and board.s5e+board.s4d=='':
            moves = '6f3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b6f)and Bboard.b2b==''\
           and board.s5e+board.s4d+board.s3c=='':
            moves = '6f2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b6f)and Bboard.b1a==''\
           and board.s5e+board.s4d+board.s3c+board.s2b=='':
            moves = '6f1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b6f)and Bboard.b3i==''\
           and board.s4h+board.s5g=='':
            moves = '6f3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b6f)and Bboard.b4h==''\
           and board.s5g=='':
            moves = '6f4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b6f)and Bboard.b8d==''\
           and board.s7e=='':
            moves = '6f8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b6f)and Bboard.b9c==''\
           and board.s7e+board.s8d=='':
            moves = '6f9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b6f)and Bboard.b3c==''\
           and board.s5e+board.s4d=='':
            moves = '6f3c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b6f)and Bboard.b2b==''\
           and board.s5e+board.s4d+board.s3c=='':
            moves = '6f2b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b6f)and Bboard.b9c==''\
           and board.s7e+board.s8d=='':
            moves = '6f9c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b6f)and Bboard.b1a==''\
           and board.s5e+board.s4d+board.s3c+board.s2b=='':
            moves = '6f1a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b7f !='':
        if re.match(r'[PLSGRK+]',   Bboard.b7f)and Bboard.b7e=='':
            moves = '7f7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b7f)and Bboard.b6e=='':
            moves = '7f6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b7f)and Bboard.b8e=='':
            moves = '7f8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b7f)and Bboard.b6f=='':
            moves = '7f6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b7f)and Bboard.b8f=='':
            moves = '7f8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b7f)and Bboard.b7g=='':
            moves = '7f7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b7f)and Bboard.b6g=='':
            moves = '7f6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b7f)and Bboard.b8g=='':
            moves = '7f8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b7f)and Bboard.b6d=='':
            moves = '7f6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b7f)and Bboard.b8d=='':
            moves = '7f8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b7f)and Bboard.b7a==''\
           and board.s7b+board.s7c+board.s7d+board.s7e=='':
            moves = '7f7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b7f)and Bboard.b7a==''\
           and board.s7b+board.s7c+board.s7d+board.s7e=='':
            moves = '7f7a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b7f)and Bboard.b7b==''\
           and board.s7c+board.s7d+board.s7e=='':
            moves = '7f7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b7f)and Bboard.b7b==''\
           and board.s7c+board.s7d+board.s7e=='':
            moves = '7f7b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|L',    Bboard.b7f)and Bboard.b7c==''\
           and board.s7d+board.s7e=='':
            moves = '7f7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b7f)and Bboard.b7c==''\
           and board.s7d+board.s7e=='':
            moves = '7f7c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b7f)and Bboard.b7d==''\
           and board.s7e=='':
            moves = '7f7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b7f)and Bboard.b7h==''\
           and board.s7g=='':
            moves = '7f7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b7f)and Bboard.b7i==''\
           and board.s7g+board.s7h=='':
            moves = '7f7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b7f)and Bboard.b9f==''\
           and board.s8f=='':
            moves = '7f9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b7f)and Bboard.b5f==''\
           and board.s6f=='':
            moves = '7f5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b7f)and Bboard.b4f==''\
           and board.s6f+board.s5f=='':
            moves = '7f4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b7f)and Bboard.b3f==''\
           and board.s6f+board.s5f+board.s4f=='':
            moves = '7f3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b7f)and Bboard.b2f==''\
           and board.s6f+board.s5f+board.s4f+board.s3f=='':
            moves = '7f2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b7f)and Bboard.b1f==''\
           and board.s6f+board.s5f+board.s4f+board.s3f+board.s2f=='':
            moves = '7f1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b7f)and Bboard.b9h==''\
           and board.s8g=='':
            moves = '7f9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b7f)and Bboard.b5d==''\
           and board.s6e=='':
            moves = '7f5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b7f)and Bboard.b4c==''\
           and board.s6e+board.s5d=='':
            moves = '7f4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b7f)and Bboard.b3b==''\
           and board.s6e+board.s5d+board.s4c=='':
            moves = '7f3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b7f)and Bboard.b2a==''\
           and board.s6e+board.s5d+board.s4c+board.s3b=='':
            moves = '7f2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b7f)and Bboard.b4i==''\
           and board.s5h+board.s6g=='':
            moves = '7f4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b7f)and Bboard.b5h==''\
           and board.s6g=='':
            moves = '7f5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b7f)and Bboard.b9d==''\
           and board.s8e=='':
            moves = '7f9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b7f)and Bboard.b4c==''\
           and board.s6e+board.s5d=='':
            moves = '7f4c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b7f)and Bboard.b3b==''\
           and board.s6e+board.s5d+board.s4c=='':
            moves = '7f3b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b7f)and Bboard.b2a==''\
           and board.s6e+board.s5d+board.s4c+board.s3b=='':
            moves = '7f2a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b8f !='':
        if re.match(r'[PLSGRK+]',   Bboard.b8f)and Bboard.b8e=='':
            moves = '8f8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b8f)and Bboard.b7e=='':
            moves = '8f7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b8f)and Bboard.b9e=='':
            moves = '8f9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b8f)and Bboard.b7f=='':
            moves = '8f7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b8f)and Bboard.b9f=='':
            moves = '8f9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b8f)and Bboard.b8g=='':
            moves = '8f8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b8f)and Bboard.b7g=='':
            moves = '8f7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b8f)and Bboard.b9g=='':
            moves = '8f9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b8f)and Bboard.b7d=='':
            moves = '8f7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b8f)and Bboard.b9d=='':
            moves = '8f9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b8f)and Bboard.b8a==''\
           and board.s8b+board.s8c+board.s8d+board.s8e=='':
            moves = '8f8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b8f)and Bboard.b8a==''\
           and board.s8b+board.s8c+board.s8d+board.s8e=='':
            moves = '8f8a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b8f)and Bboard.b8b==''\
           and board.s8c+board.s8d+board.s8e=='':
            moves = '8f8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b8f)and Bboard.b8b==''\
           and board.s8c+board.s8d+board.s8e=='':
            moves = '8f8b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|L',    Bboard.b8f)and Bboard.b8c==''\
           and board.s8d+board.s8e=='':
            moves = '8f8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b8f)and Bboard.b8c==''\
           and board.s8d+board.s8e=='':
            moves = '8f8c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b8f)and Bboard.b8d==''\
           and board.s8e=='':
            moves = '8f8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b8f)and Bboard.b8h==''\
           and board.s8g=='':
            moves = '8f8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b8f)and Bboard.b8i==''\
           and board.s8g+board.s8h=='':
            moves = '8f8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b8f)and Bboard.b6f==''\
           and board.s7f=='':
            moves = '8f6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b8f)and Bboard.b5f==''\
           and board.s7f+board.s6f=='':
            moves = '8f5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b8f)and Bboard.b4f==''\
           and board.s7f+board.s6f+board.s5f=='':
            moves = '8f4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b8f)and Bboard.b3f==''\
           and board.s7f+board.s6f+board.s5f+board.s4f=='':
            moves = '8f3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b8f)and Bboard.b2f==''\
           and board.s7f+board.s6f+board.s5f+board.s4f+board.s3f=='':
            moves = '8f2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b8f)and Bboard.b1f==''\
           and board.s7f+board.s6f+board.s5f+board.s4f+board.s3f+board.s2f=='':
            moves = '8f1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b8f)and Bboard.b6d==''\
           and board.s7e=='':
            moves = '8f6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b8f)and Bboard.b5c==''\
           and board.s7e+board.s6d=='':
            moves = '8f5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b8f)and Bboard.b4b==''\
           and board.s7e+board.s6d+board.s5c=='':
            moves = '8f4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b8f)and Bboard.b3a==''\
           and board.s7e+board.s6d+board.s5c+board.s4b=='':
            moves = '8f3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b8f)and Bboard.b5i==''\
           and board.s6h+board.s7g=='':
            moves = '8f5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b8f)and Bboard.b6h==''\
           and board.s7g=='':
            moves = '8f6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b8f)and Bboard.b5c==''\
           and board.s7e+board.s6d=='':
            moves = '8f5c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b8f)and Bboard.b4b==''\
           and board.s7e+board.s6d+board.s5c=='':
            moves = '8f4b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b8f)and Bboard.b3a==''\
           and board.s7e+board.s6d+board.s5c+board.s4b=='':
            moves = '8f3a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b9f !='':
        if re.match(r'[PLSGRK+]',   Bboard.b9f)and Bboard.b9e=='':
            moves = '9f9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b9f)and Bboard.b8e=='':
            moves = '9f8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b9f)and Bboard.b8f=='':
            moves = '9f8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b9f)and Bboard.b9g=='':
            moves = '9f9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b9f)and Bboard.b8g=='':
            moves = '9f8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b9f)and Bboard.b8d=='':
            moves = '9f8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b9f)and Bboard.b9a==''\
           and board.s9b+board.s9c+board.s9d+board.s9e=='':
            moves = '9f9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b9f)and Bboard.b9a==''\
           and board.s9b+board.s9c+board.s9d+board.s9e=='':
            moves = '9f9a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b9f)and Bboard.b9b==''\
           and board.s9c+board.s9d+board.s9e=='':
            moves = '9f9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b9f)and Bboard.b9b==''\
           and board.s9c+board.s9d+board.s9e=='':
            moves = '9f9b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|L',    Bboard.b9f)and Bboard.b9c==''\
           and board.s9d+board.s9e=='':
            moves = '9f9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b9f)and Bboard.b9c==''\
           and board.s9d+board.s9e=='':
            moves = '9f9c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b9f)and Bboard.b9d==''\
           and board.s9e=='':
            moves = '9f9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b9f)and Bboard.b9h==''\
           and board.s9g=='':
            moves = '9f9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b9f)and Bboard.b9i==''\
           and board.s9g+board.s9h=='':
            moves = '9f9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b9f)and Bboard.b7f==''\
           and board.s8f=='':
            moves = '9f7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b9f)and Bboard.b6f==''\
           and board.s8f+board.s7f=='':
            moves = '9f6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b9f)and Bboard.b5f==''\
           and board.s8f+board.s7f+board.s6f=='':
            moves = '9f5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b9f)and Bboard.b4f==''\
           and board.s8f+board.s7f+board.s6f+board.s5f=='':
            moves = '9f4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b9f)and Bboard.b3f==''\
           and board.s8f+board.s7f+board.s6f+board.s5f+board.s4f=='':
            moves = '9f3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b9f)and Bboard.b2f==''\
           and board.s8f+board.s7f+board.s6f+board.s5f+board.s4f+board.s3f=='':
            moves = '9f2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b9f)and Bboard.b1f==''\
           and board.s8f+board.s7f+board.s6f+board.s5f+board.s4f+board.s3f+board.s2f=='':
            moves = '9f1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b9f)and Bboard.b7d==''\
           and board.s8e=='':
            moves = '9f7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b9f)and Bboard.b6c==''\
           and board.s8e+board.s7d=='':
            moves = '9f6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b9f)and Bboard.b5b==''\
           and board.s8e+board.s7d+board.s6c=='':
            moves = '9f5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b9f)and Bboard.b4a==''\
           and board.s8e+board.s7d+board.s6c+board.s5b=='':
            moves = '9f4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b9f)and Bboard.b6i==''\
           and board.s7h+board.s8g=='':
            moves = '9f6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b9f)and Bboard.b7h==''\
           and board.s8g=='':
            moves = '9f7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b9f)and Bboard.b6c==''\
           and board.s8e+board.s7d=='':
            moves = '9f6c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b9f)and Bboard.b5b==''\
           and board.s8e+board.s7d+board.s6c=='':
            moves = '9f5b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b9f)and Bboard.b4a==''\
           and board.s8e+board.s7d+board.s6c+board.s5b=='':
            moves = '9f4a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b1g !='':
        if re.match(r'[PLSGRK+]',   Bboard.b1g)and Bboard.b1f=='':
            moves = '1g1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b1g)and Bboard.b2f=='':
            moves = '1g2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b1g)and Bboard.b2g=='':
            moves = '1g2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b1g)and Bboard.b1h=='':
            moves = '1g1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b1g)and Bboard.b2h=='':
            moves = '1g2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b1g)and Bboard.b2e=='':
            moves = '1g2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b1g)and Bboard.b1a==''\
           and board.s1b+board.s1c+board.s1d+board.s1e+board.s1f=='':
            moves = '1g1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b1g)and Bboard.b1a==''\
           and board.s1b+board.s1c+board.s1d+board.s1e+board.s1f=='':
            moves = '1g1a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b1g)and Bboard.b1b==''\
           and board.s1c+board.s1d+board.s1e+board.s1f=='':
            moves = '1g1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b1g)and Bboard.b1b==''\
           and board.s1c+board.s1d+board.s1e+board.s1f=='':
            moves = '1g1b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|L',    Bboard.b1g)and Bboard.b1c==''\
           and board.s1d+board.s1e+board.s1f=='':
            moves = '1g1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b1g)and Bboard.b1c==''\
           and board.s1d+board.s1e+board.s1f=='':
            moves = '1g1c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b1g)and Bboard.b1d==''\
           and board.s1e+board.s1f=='':
            moves = '1g1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b1g)and Bboard.b1e==''\
           and board.s1f=='':
            moves = '1g1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b1g)and Bboard.b1i==''\
           and board.s1h=='':
            moves = '1g1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b1g)and Bboard.b3g==''\
           and board.s2g=='':
            moves = '1g3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b1g)and Bboard.b4g==''\
           and board.s2g+board.s3g=='':
            moves = '1g4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b1g)and Bboard.b5g==''\
           and board.s2g+board.s3g+board.s4g=='':
            moves = '1g5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b1g)and Bboard.b6g==''\
           and board.s2g+board.s3g+board.s4g+board.s5g=='':
            moves = '1g6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b1g)and Bboard.b7g==''\
           and board.s2g+board.s3g+board.s4g+board.s5g+board.s6g=='':
            moves = '1g7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b1g)and Bboard.b8g==''\
           and board.s2g+board.s3g+board.s4g+board.s5g+board.s6g+board.s7g=='':
            moves = '1g8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b1g)and Bboard.b9g==''\
           and board.s2g+board.s3g+board.s4g+board.s5g+board.s6g+board.s7g+board.s8g=='':
            moves = '1g9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b1g)and Bboard.b5c==''\
           and board.s2f+board.s3e+board.s4d=='':
            moves = '1g5c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b1g)and Bboard.b6b==''\
           and board.s2f+board.s3e+board.s4d+board.s5c=='':
            moves = '1g6b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b1g)and Bboard.b7a==''\
           and board.s2f+board.s3e+board.s4d+board.s5c+board.s6b=='':
            moves = '1g7a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b1g)and Bboard.b3i==''\
           and board.s2h=='':
            moves = '1g3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b1g)and Bboard.b3e==''\
           and board.s2f=='':
            moves = '1g3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b1g)and Bboard.b4d==''\
           and board.s2f+board.s3e=='':
            moves = '1g4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b1g)and Bboard.b5c==''\
           and board.s2f+board.s3e+board.s4d=='':
            moves = '1g5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b1g)and Bboard.b6b==''\
           and board.s2f+board.s3e+board.s4d+board.s5c=='':
            moves = '1g6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b1g)and Bboard.b7a==''\
           and board.s2f+board.s3e+board.s4d+board.s5c+board.s6b=='':
            moves = '1g7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b2g !='':
        if re.match(r'[PLSGRK+]',   Bboard.b2g)and Bboard.b2f=='':
            moves = '2g2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b2g)and Bboard.b1f=='':
            moves = '2g1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b2g)and Bboard.b3f=='':
            moves = '2g3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b2g)and Bboard.b1g=='':
            moves = '2g1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b2g)and Bboard.b3g=='':
            moves = '2g3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b2g)and Bboard.b2h=='':
            moves = '2g2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b2g)and Bboard.b1h=='':
            moves = '2g1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b2g)and Bboard.b3h=='':
            moves = '2g3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b2g)and Bboard.b1e=='':
            moves = '2g1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b2g)and Bboard.b3e=='':
            moves = '2g3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b2g)and Bboard.b2a==''\
           and board.s2b+board.s2c+board.s2d+board.s2e+board.s2f=='':
            moves = '2g2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b2g)and Bboard.b2a==''\
           and board.s2b+board.s2c+board.s2d+board.s2e+board.s2f=='':
            moves = '2g2a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b2g)and Bboard.b2b==''\
           and board.s2c+board.s2d+board.s2e+board.s2f=='':
            moves = '2g2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b2g)and Bboard.b2b==''\
           and board.s2c+board.s2d+board.s2e+board.s2f=='':
            moves = '2g2b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|L',    Bboard.b2g)and Bboard.b2c==''\
           and board.s2d+board.s2e+board.s2f=='':
            moves = '2g2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b2g)and Bboard.b2c==''\
           and board.s2d+board.s2e+board.s2f=='':
            moves = '2g2c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b2g)and Bboard.b2d==''\
           and board.s2e+board.s2f=='':
            moves = '2g2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b2g)and Bboard.b2e==''\
           and board.s2f=='':
            moves = '2g2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b2g)and Bboard.b2i==''\
           and board.s2h=='':
            moves = '2g2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b2g)and Bboard.b4g==''\
           and board.s3g=='':
            moves = '2g4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b2g)and Bboard.b5g==''\
           and board.s3g+board.s4g=='':
            moves = '2g5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b2g)and Bboard.b6g==''\
           and board.s3g+board.s4g+board.s5g=='':
            moves = '2g6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b2g)and Bboard.b7g==''\
           and board.s3g+board.s4g+board.s5g+board.s6g=='':
            moves = '2g7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b2g)and Bboard.b8g==''\
           and board.s3g+board.s4g+board.s5g+board.s6g+board.s7g=='':
            moves = '2g8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b2g)and Bboard.b9g==''\
           and board.s3g+board.s4g+board.s5g+board.s6g+board.s7g+board.s8g=='':
            moves = '2g9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b2g)and Bboard.b6c==''\
           and board.s3f+board.s4e+board.s5d=='':
            moves = '2g6c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b2g)and Bboard.b7b==''\
           and board.s3f+board.s4e+board.s5d+board.s6c=='':
            moves = '2g7b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b2g)and Bboard.b8a==''\
           and board.s3f+board.s4e+board.s5d+board.s6c+board.s7b=='':
            moves = '2g8a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b2g)and Bboard.b4e==''\
           and board.s3f=='':
            moves = '2g4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b2g)and Bboard.b5d==''\
           and board.s3f+board.s4e=='':
            moves = '2g5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b2g)and Bboard.b6c==''\
           and board.s3f+board.s4e+board.s5d=='':
            moves = '2g6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b2g)and Bboard.b7b==''\
           and board.s3f+board.s4e+board.s5d+board.s6c=='':
            moves = '2g7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b2g)and Bboard.b8a==''\
           and board.s3f+board.s4e+board.s5d+board.s6c+board.s7b=='':
            moves = '2g8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b2g)and Bboard.b4i==''\
           and board.s3h=='':
            moves = '2g4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b3g !='':
        if re.match(r'[PLSGRK+]',   Bboard.b3g)and Bboard.b3f=='':
            moves = '3g3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b3g)and Bboard.b2f=='':
            moves = '3g2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b3g)and Bboard.b4f=='':
            moves = '3g4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b3g)and Bboard.b2g=='':
            moves = '3g2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b3g)and Bboard.b4g=='':
            moves = '3g4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b3g)and Bboard.b3h=='':
            moves = '3g3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b3g)and Bboard.b2h=='':
            moves = '3g2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b3g)and Bboard.b4h=='':
            moves = '3g4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b3g)and Bboard.b2e=='':
            moves = '3g2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b3g)and Bboard.b4e=='':
            moves = '3g4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b3g)and Bboard.b3a==''\
           and board.s3b+board.s3c+board.s3d+board.s3e+board.s3f=='':
            moves = '3g3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b3g)and Bboard.b3a==''\
           and board.s3b+board.s3c+board.s3d+board.s3e+board.s3f=='':
            moves = '3g3a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b3g)and Bboard.b3b==''\
           and board.s3c+board.s3d+board.s3e+board.s3f=='':
            moves = '3g3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b3g)and Bboard.b3b==''\
           and board.s3c+board.s3d+board.s3e+board.s3f=='':
            moves = '3g3b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|L',    Bboard.b3g)and Bboard.b3c==''\
           and board.s3d+board.s3e+board.s3f=='':
            moves = '3g3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b3g)and Bboard.b3c==''\
           and board.s3d+board.s3e+board.s3f=='':
            moves = '3g3c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b3g)and Bboard.b3d==''\
           and board.s3e+board.s3f=='':
            moves = '3g3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b3g)and Bboard.b3e==''\
           and board.s3f=='':
            moves = '3g3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b3g)and Bboard.b3i==''\
           and board.s3h=='':
            moves = '3g3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b3g)and Bboard.b1g==''\
           and board.s2g=='':
            moves = '3g1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b3g)and Bboard.b5g==''\
           and board.s4g=='':
            moves = '3g5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b3g)and Bboard.b6g==''\
           and board.s4g+board.s5g=='':
            moves = '3g6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b3g)and Bboard.b7g==''\
           and board.s4g+board.s5g+board.s6g=='':
            moves = '3g7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b3g)and Bboard.b8g==''\
           and board.s4g+board.s5g+board.s6g+board.s7g=='':
            moves = '3g8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b3g)and Bboard.b9g==''\
           and board.s4g+board.s5g+board.s6g+board.s7g+board.s8g=='':
            moves = '3g9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b3g)and Bboard.b7c==''\
           and board.s4f+board.s5e+board.s6d=='':
            moves = '3g7c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b3g)and Bboard.b8b==''\
           and board.s4f+board.s5e+board.s6d+board.s7c=='':
            moves = '3g8b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b3g)and Bboard.b9a==''\
           and board.s4f+board.s5e+board.s6d+board.s7c+board.s8b=='':
            moves = '3g9a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b3g)and Bboard.b1i==''\
           and board.s2h=='':
            moves = '3g1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b3g)and Bboard.b5e==''\
           and board.s4f=='':
            moves = '3g5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b3g)and Bboard.b6d==''\
           and board.s4f+board.s5e=='':
            moves = '3g6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b3g)and Bboard.b7c==''\
           and board.s4f+board.s5e+board.s6d=='':
            moves = '3g7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b3g)and Bboard.b8b==''\
           and board.s4f+board.s5e+board.s6d+board.s7c=='':
            moves = '3g8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b3g)and Bboard.b9a==''\
           and board.s4f+board.s5e+board.s6d+board.s7c+board.s8b=='':
            moves = '3g9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b3g)and Bboard.b5i==''\
           and board.s4h=='':
            moves = '3g5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b3g)and Bboard.b1e==''\
           and board.s2f=='':
            moves = '3g1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b4g !='':
        if re.match(r'[PLSGRK+]',   Bboard.b4g)and Bboard.b4f=='':
            moves = '4g4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b4g)and Bboard.b3f=='':
            moves = '4g3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b4g)and Bboard.b5f=='':
            moves = '4g5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b4g)and Bboard.b3g=='':
            moves = '4g3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b4g)and Bboard.b5g=='':
            moves = '4g5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b4g)and Bboard.b4h=='':
            moves = '4g4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b4g)and Bboard.b3h=='':
            moves = '4g3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b4g)and Bboard.b5h=='':
            moves = '4g5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b4g)and Bboard.b3e=='':
            moves = '4g3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b4g)and Bboard.b5e=='':
            moves = '4g5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b4g)and Bboard.b4a==''\
           and board.s4b+board.s4c+board.s4d+board.s4e+board.s4f=='':
            moves = '4g4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b4g)and Bboard.b4a==''\
           and board.s4b+board.s4c+board.s4d+board.s4e+board.s4f=='':
            moves = '4g4a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b4g)and Bboard.b4b==''\
           and board.s4c+board.s4d+board.s4e+board.s4f=='':
            moves = '4g4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b4g)and Bboard.b4b==''\
           and board.s4c+board.s4d+board.s4e+board.s4f=='':
            moves = '4g4b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|L',    Bboard.b4g)and Bboard.b4c==''\
           and board.s4d+board.s4e+board.s4f=='':
            moves = '4g4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b4g)and Bboard.b4c==''\
           and board.s4d+board.s4e+board.s4f=='':
            moves = '4g4c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b4g)and Bboard.b4d==''\
           and board.s4e+board.s4f=='':
            moves = '4g4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b4g)and Bboard.b4e==''\
           and board.s4f=='':
            moves = '4g4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b4g)and Bboard.b4i==''\
           and board.s4h=='':
            moves = '4g4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b4g)and Bboard.b1g==''\
           and board.s2g+board.s3g=='':
            moves = '4g1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b4g)and Bboard.b2g==''\
           and board.s3g=='':
            moves = '4g2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b4g)and Bboard.b6g==''\
           and board.s5g=='':
            moves = '4g6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b4g)and Bboard.b7g==''\
           and board.s5g+board.s6g=='':
            moves = '4g7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b4g)and Bboard.b8g==''\
           and board.s5g+board.s6g+board.s7g=='':
            moves = '4g8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b4g)and Bboard.b9g==''\
           and board.s5g+board.s6g+board.s7g+board.s8g=='':
            moves = '4g9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b4g)and Bboard.b6e==''\
           and board.s5f=='':
            moves = '4g6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b4g)and Bboard.b7d==''\
           and board.s5f+board.s6e=='':
            moves = '4g7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b4g)and Bboard.b8c==''\
           and board.s5f+board.s6e+board.s7d=='':
            moves = '4g8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b4g)and Bboard.b9b==''\
           and board.s5f+board.s6e+board.s7d+board.s8c=='':
            moves = '4g9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b4g)and Bboard.b8c==''\
           and board.s5f+board.s6e+board.s7d=='':
            moves = '4g8c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b4g)and Bboard.b9b==''\
           and board.s5f+board.s6e+board.s7d+board.s8c=='':
            moves = '4g9b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b4g)and Bboard.b1d==''\
           and board.s2e+board.s3f=='':
            moves = '4g1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b4g)and Bboard.b2e==''\
           and board.s3f=='':
            moves = '4g2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b4g)and Bboard.b2i==''\
           and board.s3h=='':
            moves = '4g2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b4g)and Bboard.b6i==''\
           and board.s5h=='':
            moves = '4g6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b5g !='':
        if re.match(r'[PLSGRK+]',   Bboard.b5g)and Bboard.b5f=='':
            moves = '5g5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b5g)and Bboard.b4f=='':
            moves = '5g4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b5g)and Bboard.b6f=='':
            moves = '5g6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b5g)and Bboard.b4g=='':
            moves = '5g4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b5g)and Bboard.b6g=='':
            moves = '5g6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b5g)and Bboard.b5h=='':
            moves = '5g5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b5g)and Bboard.b4h=='':
            moves = '5g4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b5g)and Bboard.b6h=='':
            moves = '5g6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b5g)and Bboard.b4e=='':
            moves = '5g4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b5g)and Bboard.b6e=='':
            moves = '5g6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b5g)and Bboard.b5a==''\
           and board.s5b+board.s5c+board.s5d+board.s5e+board.s5f=='':
            moves = '5g5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b5g)and Bboard.b5a==''\
           and board.s5b+board.s5c+board.s5d+board.s5e+board.s5f=='':
            moves = '5g5a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b5g)and Bboard.b5b==''\
           and board.s5c+board.s5d+board.s5e+board.s5f=='':
            moves = '5g5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b5g)and Bboard.b5b==''\
           and board.s5c+board.s5d+board.s5e+board.s5f=='':
            moves = '5g5b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|L',    Bboard.b5g)and Bboard.b5c==''\
           and board.s5d+board.s5e+board.s5f=='':
            moves = '5g5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b5g)and Bboard.b5c==''\
           and board.s5d+board.s5e+board.s5f=='':
            moves = '5g5c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b5g)and Bboard.b5d==''\
           and board.s5e+board.s5f=='':
            moves = '5g5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b5g)and Bboard.b5e==''\
           and board.s5f=='':
            moves = '5g5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b5g)and Bboard.b5i==''\
           and board.s5h=='':
            moves = '5g5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b5g)and Bboard.b1g==''\
           and board.s2g+board.s3g+board.s4g=='':
            moves = '5g1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b5g)and Bboard.b2g==''\
           and board.s3g+board.s4g=='':
            moves = '5g2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b5g)and Bboard.b3g==''\
           and board.s4g=='':
            moves = '5g3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b5g)and Bboard.b7g==''\
           and board.s6g=='':
            moves = '5g7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b5g)and Bboard.b8g==''\
           and board.s6g+board.s7g=='':
            moves = '5g8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b5g)and Bboard.b9g==''\
           and board.s6g+board.s7g+board.s8g=='':
            moves = '5g9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b5g)and Bboard.b7e==''\
           and board.s6f=='':
            moves = '5g7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b5g)and Bboard.b8d==''\
           and board.s6f+board.s7e=='':
            moves = '5g8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b5g)and Bboard.b9c==''\
           and board.s6f+board.s7e+board.s8d=='':
            moves = '5g9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b5g)and Bboard.b9c==''\
           and board.s6f+board.s7e+board.s8d=='':
            moves = '5g9c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b5g)and Bboard.b2d==''\
           and board.s3e+board.s4f=='':
            moves = '5g2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b5g)and Bboard.b3e==''\
           and board.s4f=='':
            moves = '5g3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b5g)and Bboard.b1c==''\
           and board.s4f+board.s3e+board.s2d=='':
            moves = '5g1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b5g)and Bboard.b1c==''\
           and board.s4f+board.s3e+board.s2d=='':
            moves = '5g1c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b5g)and Bboard.b3i==''\
           and board.s4h=='':
            moves = '5g3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b5g)and Bboard.b7i==''\
           and board.s6h=='':
            moves = '5g7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b6g !='':
        if re.match(r'[PLSGRK+]',   Bboard.b6g)and Bboard.b6f=='':
            moves = '6g6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b6g)and Bboard.b5f=='':
            moves = '6g5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b6g)and Bboard.b7f=='':
            moves = '6g7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b6g)and Bboard.b5g=='':
            moves = '6g5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b6g)and Bboard.b7g=='':
            moves = '6g7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b6g)and Bboard.b6h=='':
            moves = '6g6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b6g)and Bboard.b5h=='':
            moves = '6g5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b6g)and Bboard.b7h=='':
            moves = '6g7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b6g)and Bboard.b5e=='':
            moves = '6g5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b6g)and Bboard.b7e=='':
            moves = '6g7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b6g)and Bboard.b6a==''\
           and board.s6b+board.s6c+board.s6d+board.s6e+board.s6f=='':
            moves = '6g6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b6g)and Bboard.b6a==''\
           and board.s6b+board.s6c+board.s6d+board.s6e+board.s6f=='':
            moves = '6g6a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b6g)and Bboard.b6b==''\
           and board.s6c+board.s6d+board.s6e+board.s6f=='':
            moves = '6g6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b6g)and Bboard.b6b==''\
           and board.s6c+board.s6d+board.s6e+board.s6f=='':
            moves = '6g6b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|L',    Bboard.b6g)and Bboard.b6c==''\
           and board.s6d+board.s6e+board.s6f=='':
            moves = '6g6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b6g)and Bboard.b6c==''\
           and board.s6d+board.s6e+board.s6f=='':
            moves = '6g6c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b6g)and Bboard.b6d==''\
           and board.s6e+board.s6f=='':
            moves = '6g6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b6g)and Bboard.b6e==''\
           and board.s6f=='':
            moves = '6g6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b6g)and Bboard.b6i==''\
           and board.s6h=='':
            moves = '6g6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b6g)and Bboard.b9g==''\
           and board.s8g+board.s7g=='':
            moves = '6g9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b6g)and Bboard.b8g==''\
           and board.s7g=='':
            moves = '6g8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b6g)and Bboard.b4g==''\
           and board.s5g=='':
            moves = '6g4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b6g)and Bboard.b3g==''\
           and board.s5g+board.s4g=='':
            moves = '6g3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b6g)and Bboard.b2g==''\
           and board.s5g+board.s4g+board.s3g=='':
            moves = '6g2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b6g)and Bboard.b1g==''\
           and board.s5g+board.s4g+board.s3g+board.s2g=='':
            moves = '6g1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b6g)and Bboard.b4e==''\
           and board.s5f=='':
            moves = '6g4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b6g)and Bboard.b3d==''\
           and board.s5f+board.s4e=='':
            moves = '6g3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b6g)and Bboard.b2c==''\
           and board.s5f+board.s4e+board.s3d=='':
            moves = '6g2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b6g)and Bboard.b1b==''\
           and board.s5f+board.s4e+board.s3d+board.s2c=='':
            moves = '6g1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b6g)and Bboard.b2c==''\
           and board.s5f+board.s4e+board.s3d=='':
            moves = '6g2c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b6g)and Bboard.b1b==''\
           and board.s5f+board.s4e+board.s3d+board.s2c=='':
            moves = '6g1b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b6g)and Bboard.b9d==''\
           and board.s8e+board.s7f=='':
            moves = '6g9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b6g)and Bboard.b8e==''\
           and board.s7f=='':
            moves = '6g8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b6g)and Bboard.b8i==''\
           and board.s7h=='':
            moves = '6g8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b6g)and Bboard.b4i==''\
           and board.s5h=='':
            moves = '6g4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b7g !='':
        if re.match(r'[PLSGRK+]',   Bboard.b7g)and Bboard.b7f=='':
            moves = '7g7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b7g)and Bboard.b6f=='':
            moves = '7g6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b7g)and Bboard.b8f=='':
            moves = '7g8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b7g)and Bboard.b6g=='':
            moves = '7g6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b7g)and Bboard.b8g=='':
            moves = '7g8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b7g)and Bboard.b7h=='':
            moves = '7g7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b7g)and Bboard.b6h=='':
            moves = '7g6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b7g)and Bboard.b8h=='':
            moves = '7g8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b7g)and Bboard.b6e=='':
            moves = '7g6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b7g)and Bboard.b8e=='':
            moves = '7g8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b7g)and Bboard.b7a==''\
           and board.s7b+board.s7c+board.s7d+board.s7e+board.s7f=='':
            moves = '7g7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b7g)and Bboard.b7a==''\
           and board.s7b+board.s7c+board.s7d+board.s7e+board.s7f=='':
            moves = '7g7a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b7g)and Bboard.b7b==''\
           and board.s7c+board.s7d+board.s7e+board.s7f=='':
            moves = '7g7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b7g)and Bboard.b7b==''\
           and board.s7c+board.s7d+board.s7e+board.s7f=='':
            moves = '7g7b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|L',    Bboard.b7g)and Bboard.b7c==''\
           and board.s7d+board.s7e+board.s7f=='':
            moves = '7g7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b7g)and Bboard.b7c==''\
           and board.s7d+board.s7e+board.s7f=='':
            moves = '7g7c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b7g)and Bboard.b7d==''\
           and board.s7e+board.s7f=='':
            moves = '7g7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b7g)and Bboard.b7e==''\
           and board.s7f=='':
            moves = '7g7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b7g)and Bboard.b7i==''\
           and board.s7h=='':
            moves = '7g7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b7g)and Bboard.b9g==''\
           and board.s8g=='':
            moves = '7g9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b7g)and Bboard.b5g==''\
           and board.s6g=='':
            moves = '7g5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b7g)and Bboard.b4g==''\
           and board.s6g+board.s5g=='':
            moves = '7g4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b7g)and Bboard.b3g==''\
           and board.s6g+board.s5g+board.s4g=='':
            moves = '7g3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b7g)and Bboard.b2g==''\
           and board.s6g+board.s5g+board.s4g+board.s3g=='':
            moves = '7g2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b7g)and Bboard.b1g==''\
           and board.s6g+board.s5g+board.s4g+board.s3g+board.s2g=='':
            moves = '7g1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b7g)and Bboard.b3c==''\
           and board.s6f+board.s5e+board.s4d=='':
            moves = '7g3c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b7g)and Bboard.b2b==''\
           and board.s6f+board.s5e+board.s4d+board.s3c=='':
            moves = '7g2b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b7g)and Bboard.b1a==''\
           and board.s6f+board.s5e+board.s4d+board.s3c+board.s2b=='':
            moves = '7g1a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b7g)and Bboard.b9i==''\
           and board.s8h=='':
            moves = '7g9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b7g)and Bboard.b5e==''\
           and board.s6f=='':
            moves = '7g5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b7g)and Bboard.b4d==''\
           and board.s6f+board.s5e=='':
            moves = '7g4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b7g)and Bboard.b3c==''\
           and board.s6f+board.s5e+board.s4d=='':
            moves = '7g3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b7g)and Bboard.b2b==''\
           and board.s6f+board.s5e+board.s4d+board.s3c=='':
            moves = '7g2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b7g)and Bboard.b1a==''\
           and board.s6f+board.s5e+board.s4d+board.s3c+board.s2b=='':
            moves = '7g1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b7g)and Bboard.b5i==''\
           and board.s6h=='':
            moves = '7g5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b7g)and Bboard.b9e==''\
           and board.s8f=='':
            moves = '7g9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b8g !='':
        if re.match(r'[PLSGRK+]',   Bboard.b8g)and Bboard.b8f=='':
            moves = '8g8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b8g)and Bboard.b7f=='':
            moves = '8g7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b8g)and Bboard.b9f=='':
            moves = '8g9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b8g)and Bboard.b7g=='':
            moves = '8g7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b8g)and Bboard.b9g=='':
            moves = '8g9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b8g)and Bboard.b8h=='':
            moves = '8g8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b8g)and Bboard.b7h=='':
            moves = '8g7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b8g)and Bboard.b9h=='':
            moves = '8g9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b8g)and Bboard.b7e=='':
            moves = '8g7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b8g)and Bboard.b9e=='':
            moves = '8g9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b8g)and Bboard.b8a==''\
           and board.s8b+board.s8c+board.s8d+board.s8e+board.s8f=='':
            moves = '8g8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b8g)and Bboard.b8a==''\
           and board.s8b+board.s8c+board.s8d+board.s8e+board.s8f=='':
            moves = '8g8a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b8g)and Bboard.b8b==''\
           and board.s8c+board.s8d+board.s8e+board.s8f=='':
            moves = '8g8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b8g)and Bboard.b8b==''\
           and board.s8c+board.s8d+board.s8e+board.s8f=='':
            moves = '8g8b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|L',    Bboard.b8g)and Bboard.b8c==''\
           and board.s8d+board.s8e+board.s8f=='':
            moves = '8g8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b8g)and Bboard.b8c==''\
           and board.s8d+board.s8e+board.s8f=='':
            moves = '8g8c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b8g)and Bboard.b8d==''\
           and board.s8e+board.s8f=='':
            moves = '8g8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b8g)and Bboard.b8e==''\
           and board.s8f=='':
            moves = '8g8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b8g)and Bboard.b8i==''\
           and board.s8h=='':
            moves = '8g8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b8g)and Bboard.b6g==''\
           and board.s7g=='':
            moves = '8g6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b8g)and Bboard.b5g==''\
           and board.s7g+board.s6g=='':
            moves = '8g5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b8g)and Bboard.b4g==''\
           and board.s7g+board.s6g+board.s5g=='':
            moves = '8g4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b8g)and Bboard.b3g==''\
           and board.s7g+board.s6g+board.s5g+board.s4g=='':
            moves = '8g3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b8g)and Bboard.b2g==''\
           and board.s7g+board.s6g+board.s5g+board.s4g+board.s3g=='':
            moves = '8g2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b8g)and Bboard.b1g==''\
           and board.s7g+board.s6g+board.s5g+board.s4g+board.s3g+board.s2g=='':
            moves = '8g1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b8g)and Bboard.b4c==''\
           and board.s7f+board.s6e+board.s5d=='':
            moves = '8g4c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b8g)and Bboard.b3b==''\
           and board.s7f+board.s6e+board.s5d+board.s4c=='':
            moves = '8g3b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b8g)and Bboard.b2a==''\
           and board.s7f+board.s6e+board.s5d+board.s4c+board.s3b=='':
            moves = '8g2a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b8g)and Bboard.b6e==''\
           and board.s7f=='':
            moves = '8g6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b8g)and Bboard.b5d==''\
           and board.s7f+board.s6e=='':
            moves = '8g5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b8g)and Bboard.b4c==''\
           and board.s7f+board.s6e+board.s5d=='':
            moves = '8g4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b8g)and Bboard.b3b==''\
           and board.s7f+board.s6e+board.s5d+board.s4c=='':
            moves = '8g3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b8g)and Bboard.b2a==''\
           and board.s7f+board.s6e+board.s5d+board.s4c+board.s3b=='':
            moves = '8g2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b8g)and Bboard.b6i==''\
           and board.s7h=='':
            moves = '8g6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b9g !='':
        if re.match(r'[PLSGRK+]',   Bboard.b9g)and Bboard.b9f=='':
            moves = '9g9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b9g)and Bboard.b8f=='':
            moves = '9g8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b9g)and Bboard.b8g=='':
            moves = '9g8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b9g)and Bboard.b9h=='':
            moves = '9g9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b9g)and Bboard.b8h=='':
            moves = '9g8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b9g)and Bboard.b8e=='':
            moves = '9g8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b9g)and Bboard.b9a==''\
           and board.s9b+board.s9c+board.s9d+board.s9e+board.s9f=='':
            moves = '9g9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b9g)and Bboard.b9a==''\
           and board.s9b+board.s9c+board.s9d+board.s9e+board.s9f=='':
            moves = '9g9a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b9g)and Bboard.b9b==''\
           and board.s9c+board.s9d+board.s9e+board.s9f=='':
            moves = '9g9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b9g)and Bboard.b9b==''\
           and board.s9c+board.s9d+board.s9e+board.s9f=='':
            moves = '9g9b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|L',    Bboard.b9g)and Bboard.b9c==''\
           and board.s9d+board.s9e+board.s9f=='':
            moves = '9g9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b9g)and Bboard.b9c==''\
           and board.s9d+board.s9e+board.s9f=='':
            moves = '9g9c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b9g)and Bboard.b9d==''\
           and board.s9e+board.s9f=='':
            moves = '9g9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b9g)and Bboard.b9e==''\
           and board.s9f=='':
            moves = '9g9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b9g)and Bboard.b9i==''\
           and board.s9h=='':
            moves = '9g9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b9g)and Bboard.b7g==''\
           and board.s8g=='':
            moves = '9g7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b9g)and Bboard.b6g==''\
           and board.s8g+board.s7g=='':
            moves = '9g6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b9g)and Bboard.b5g==''\
           and board.s8g+board.s7g+board.s6g=='':
            moves = '9g5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b9g)and Bboard.b4g==''\
           and board.s8g+board.s7g+board.s6g+board.s5g=='':
            moves = '9g4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b9g)and Bboard.b3g==''\
           and board.s8g+board.s7g+board.s6g+board.s5g+board.s4g=='':
            moves = '9g3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b9g)and Bboard.b2g==''\
           and board.s8g+board.s7g+board.s6g+board.s5g+board.s4g+board.s3g=='':
            moves = '9g2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b9g)and Bboard.b1g==''\
           and board.s8g+board.s7g+board.s6g+board.s5g+board.s4g+board.s3g+board.s2g=='':
            moves = '9g1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b9g)and Bboard.b5c==''\
           and board.s8f+board.s7e+board.s6d=='':
            moves = '9g5c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b9g)and Bboard.b4b==''\
           and board.s8f+board.s7e+board.s6d+board.s5c=='':
            moves = '9g4b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b9g)and Bboard.b3a==''\
           and board.s8f+board.s7e+board.s6d+board.s5c+board.s4b=='':
            moves = '9g3a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b9g)and Bboard.b7i==''\
           and board.s8h=='':
            moves = '9g7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b9g)and Bboard.b7e==''\
           and board.s8f=='':
            moves = '9g7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b9g)and Bboard.b6d==''\
           and board.s8f+board.s7e=='':
            moves = '9g6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b9g)and Bboard.b5c==''\
           and board.s8f+board.s7e+board.s6d=='':
            moves = '9g5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b9g)and Bboard.b4b==''\
           and board.s8f+board.s7e+board.s6d+board.s5c=='':
            moves = '9g4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b9g)and Bboard.b3a==''\
           and board.s8f+board.s7e+board.s6d+board.s5c+board.s4b=='':
            moves = '9g3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b1h !='':
        if re.match(r'[PLSGRK+]',   Bboard.b1h)and Bboard.b1g=='':
            moves = '1h1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b1h)and Bboard.b2g=='':
            moves = '1h2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b1h)and Bboard.b2h=='':
            moves = '1h2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b1h)and Bboard.b1i=='':
            moves = '1h1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b1h)and Bboard.b2i=='':
            moves = '1h2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b1h)and Bboard.b2f=='':
            moves = '1h2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b1h)and Bboard.b1a==''\
           and board.s1b+board.s1c+board.s1d+board.s1e+board.s1f+board.s1g=='':
            moves = '1h1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b1h)and Bboard.b1a==''\
           and board.s1b+board.s1c+board.s1d+board.s1e+board.s1f+board.s1g=='':
            moves = '1h1a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b1h)and Bboard.b1b==''\
           and board.s1c+board.s1d+board.s1e+board.s1f+board.s1g=='':
            moves = '1h1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b1h)and Bboard.b1b==''\
           and board.s1c+board.s1d+board.s1e+board.s1f+board.s1g=='':
            moves = '1h1b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|L',    Bboard.b1h)and Bboard.b1c==''\
           and board.s1d+board.s1e+board.s1f+board.s1g=='':
            moves = '1h1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b1h)and Bboard.b1c==''\
           and board.s1d+board.s1e+board.s1f+board.s1g=='':
            moves = '1h1c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b1h)and Bboard.b1d==''\
           and board.s1e+board.s1f+board.s1g=='':
            moves = '1h1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b1h)and Bboard.b1e==''\
           and board.s1f+board.s1g=='':
            moves = '1h1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b1h)and Bboard.b1f==''\
           and board.s1g=='':
            moves = '1h1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b1h)and Bboard.b3h==''\
           and board.s2h=='':
            moves = '1h3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b1h)and Bboard.b4h==''\
           and board.s2h+board.s3h=='':
            moves = '1h4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b1h)and Bboard.b5h==''\
           and board.s2h+board.s3h+board.s4h=='':
            moves = '1h5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b1h)and Bboard.b6h==''\
           and board.s2h+board.s3h+board.s4h+board.s5h=='':
            moves = '1h6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b1h)and Bboard.b7h==''\
           and board.s2h+board.s3h+board.s4h+board.s5h+board.s6h=='':
            moves = '1h7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b1h)and Bboard.b8h==''\
           and board.s2h+board.s3h+board.s4h+board.s5h+board.s6h+board.s7h=='':
            moves = '1h8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b1h)and Bboard.b9h==''\
           and board.s2h+board.s3h+board.s4h+board.s5h+board.s6h+board.s7h+board.s8h=='':
            moves = '1h9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b1h)and Bboard.b6c==''\
           and board.s2g+board.s3f+board.s4e+board.s5d=='':
            moves = '1h6c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b1h)and Bboard.b7b==''\
           and board.s2g+board.s3f+board.s4e+board.s5d+board.s6c=='':
            moves = '1h7b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b1h)and Bboard.b8a==''\
           and board.s2g+board.s3f+board.s4e+board.s5d+board.s6c+board.s7b=='':
            moves = '1h8a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b1h)and Bboard.b3f==''\
           and board.s2g=='':
            moves = '1h3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b1h)and Bboard.b4e==''\
           and board.s2g+board.s3f=='':
            moves = '1h4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b1h)and Bboard.b5d==''\
           and board.s2g+board.s3f+board.s4e=='':
            moves = '1h5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b1h)and Bboard.b6c==''\
           and board.s2g+board.s3f+board.s4e+board.s5d=='':
            moves = '1h6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b1h)and Bboard.b7b==''\
           and board.s2g+board.s3f+board.s4e+board.s5d+board.s6c=='':
            moves = '1h7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b1h)and Bboard.b8a==''\
           and board.s2g+board.s3f+board.s4e+board.s5d+board.s6c+board.s7b=='':
            moves = '1h8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b2h !='':
        if re.match(r'[PLSGRK+]',   Bboard.b2h)and Bboard.b2g=='':
            moves = '2h2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b2h)and Bboard.b1g=='':
            moves = '2h1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b2h)and Bboard.b3g=='':
            moves = '2h3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b2h)and Bboard.b1h=='':
            moves = '2h1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b2h)and Bboard.b3h=='':
            moves = '2h3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b2h)and Bboard.b2i=='':
            moves = '2h2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b2h)and Bboard.b1i=='':
            moves = '2h1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b2h)and Bboard.b3i=='':
            moves = '2h3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b2h)and Bboard.b1f=='':
            moves = '2h1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b2h)and Bboard.b3f=='':
            moves = '2h3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b2h)and Bboard.b2a==''\
           and board.s2b+board.s2c+board.s2d+board.s2e+board.s2f+board.s2g=='':
            moves = '2h2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b2h)and Bboard.b2a==''\
           and board.s2b+board.s2c+board.s2d+board.s2e+board.s2f+board.s2g=='':
            moves = '2h2a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b2h)and Bboard.b2b==''\
           and board.s2c+board.s2d+board.s2e+board.s2f+board.s2g=='':
            moves = '2h2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b2h)and Bboard.b2b==''\
           and board.s2c+board.s2d+board.s2e+board.s2f+board.s2g=='':
            moves = '2h2b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|L',    Bboard.b2h)and Bboard.b2c==''\
           and board.s2d+board.s2e+board.s2f+board.s2g=='':
            moves = '2h2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b2h)and Bboard.b2c==''\
           and board.s2d+board.s2e+board.s2f+board.s2g=='':
            moves = '2h2c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b2h)and Bboard.b2d==''\
           and board.s2e+board.s2f+board.s2g=='':
            moves = '2h2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b2h)and Bboard.b2e==''\
           and board.s2f+board.s2g=='':
            moves = '2h2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b2h)and Bboard.b2f==''\
           and board.s2g=='':
            moves = '2h2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b2h)and Bboard.b4h==''\
           and board.s3h=='':
            moves = '2h4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b2h)and Bboard.b5h==''\
           and board.s3h+board.s4h=='':
            moves = '2h5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b2h)and Bboard.b6h==''\
           and board.s3h+board.s4h+board.s5h=='':
            moves = '2h6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b2h)and Bboard.b7h==''\
           and board.s3h+board.s4h+board.s5h+board.s6h=='':
            moves = '2h7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b2h)and Bboard.b8h==''\
           and board.s3h+board.s4h+board.s5h+board.s6h+board.s7h=='':
            moves = '2h8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b2h)and Bboard.b9h==''\
           and board.s3h+board.s4h+board.s5h+board.s6h+board.s7h+board.s8h=='':
            moves = '2h9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b2h)and Bboard.b7c==''\
           and board.s3g+board.s4f+board.s5e+board.s6d=='':
            moves = '2h7c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b2h)and Bboard.b8b==''\
           and board.s3g+board.s4f+board.s5e+board.s6d+board.s7c=='':
            moves = '2h8b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b2h)and Bboard.b9a==''\
           and board.s3g+board.s4f+board.s5e+board.s6d+board.s7c+board.s8b=='':
            moves = '2h9a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b2h)and Bboard.b4f==''\
           and board.s3g=='':
            moves = '2h4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b2h)and Bboard.b5e==''\
           and board.s3g+board.s4f=='':
            moves = '2h5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b2h)and Bboard.b6d==''\
           and board.s3g+board.s4f+board.s5e=='':
            moves = '2h6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b2h)and Bboard.b7c==''\
           and board.s3g+board.s4f+board.s5e+board.s6d=='':
            moves = '2h7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b2h)and Bboard.b8b==''\
           and board.s3g+board.s4f+board.s5e+board.s6d+board.s7c=='':
            moves = '2h8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b2h)and Bboard.b9a==''\
           and board.s3g+board.s4f+board.s5e+board.s6d+board.s7c+board.s8b=='':
            moves = '2h9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b3h !='':
        if re.match(r'[PLSGRK+]',   Bboard.b3h)and Bboard.b3g=='':
            moves = '3h3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b3h)and Bboard.b2g=='':
            moves = '3h2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b3h)and Bboard.b4g=='':
            moves = '3h4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b3h)and Bboard.b2h=='':
            moves = '3h2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b3h)and Bboard.b4h=='':
            moves = '3h4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b3h)and Bboard.b3i=='':
            moves = '3h3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b3h)and Bboard.b2i=='':
            moves = '3h2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b3h)and Bboard.b4i=='':
            moves = '3h4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b3h)and Bboard.b2f=='':
            moves = '3h2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b3h)and Bboard.b4f=='':
            moves = '3h4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b3h)and Bboard.b3a==''\
           and board.s3b+board.s3c+board.s3d+board.s3e+board.s3f+board.s3g=='':
            moves = '3h3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b3h)and Bboard.b3a==''\
           and board.s3b+board.s3c+board.s3d+board.s3e+board.s3f+board.s3g=='':
            moves = '3h3a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b3h)and Bboard.b3b==''\
           and board.s3c+board.s3d+board.s3e+board.s3f+board.s3g=='':
            moves = '3h3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b3h)and Bboard.b3b==''\
           and board.s3c+board.s3d+board.s3e+board.s3f+board.s3g=='':
            moves = '3h3b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|L',    Bboard.b3h)and Bboard.b3c==''\
           and board.s3d+board.s3e+board.s3f+board.s3g=='':
            moves = '3h3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b3h)and Bboard.b3c==''\
           and board.s3d+board.s3e+board.s3f+board.s3g=='':
            moves = '3h3c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b3h)and Bboard.b3d==''\
           and board.s3e+board.s3f+board.s3g=='':
            moves = '3h3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b3h)and Bboard.b3e==''\
           and board.s3f+board.s3g=='':
            moves = '3h3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b3h)and Bboard.b3f==''\
           and board.s3g=='':
            moves = '3h3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b3h)and Bboard.b1h==''\
           and board.s2h=='':
            moves = '3h1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b3h)and Bboard.b5h==''\
           and board.s4h=='':
            moves = '3h5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b3h)and Bboard.b6h==''\
           and board.s4h+board.s5h=='':
            moves = '3h6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b3h)and Bboard.b7h==''\
           and board.s4h+board.s5h+board.s6h=='':
            moves = '3h7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b3h)and Bboard.b8h==''\
           and board.s4h+board.s5h+board.s6h+board.s7h=='':
            moves = '3h8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b3h)and Bboard.b9h==''\
           and board.s4h+board.s5h+board.s6h+board.s7h+board.s8h=='':
            moves = '3h9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b3h)and Bboard.b8c==''\
           and board.s4g+board.s5f+board.s6e+board.s7d=='':
            moves = '3h8c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b3h)and Bboard.b9b==''\
           and board.s4g+board.s5f+board.s6e+board.s7d+board.s8c=='':
            moves = '3h9b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b3h)and Bboard.b5f==''\
           and board.s4g=='':
            moves = '3h5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b3h)and Bboard.b6e==''\
           and board.s4g+board.s5f=='':
            moves = '3h6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b3h)and Bboard.b7d==''\
           and board.s4g+board.s5f+board.s6e=='':
            moves = '3h7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b3h)and Bboard.b8c==''\
           and board.s4g+board.s5f+board.s6e+board.s7d=='':
            moves = '3h8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b3h)and Bboard.b9b==''\
           and board.s4g+board.s5f+board.s6e+board.s7d+board.s8c=='':
            moves = '3h9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b3h)and Bboard.b1f==''\
           and board.s2g=='':
            moves = '3h1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b4h !='':
        if re.match(r'[PLSGRK+]',   Bboard.b4h)and Bboard.b4g=='':
            moves = '4h4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b4h)and Bboard.b3g=='':
            moves = '4h3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b4h)and Bboard.b5g=='':
            moves = '4h5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b4h)and Bboard.b3h=='':
            moves = '4h3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b4h)and Bboard.b5h=='':
            moves = '4h5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b4h)and Bboard.b4i=='':
            moves = '4h4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b4h)and Bboard.b3i=='':
            moves = '4h3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b4h)and Bboard.b5i=='':
            moves = '4h5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b4h)and Bboard.b3f=='':
            moves = '4h3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b4h)and Bboard.b5f=='':
            moves = '4h5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b4h)and Bboard.b4a==''\
           and board.s4b+board.s4c+board.s4d+board.s4e+board.s4f+board.s4g=='':
            moves = '4h4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b4h)and Bboard.b4a==''\
           and board.s4b+board.s4c+board.s4d+board.s4e+board.s4f+board.s4g=='':
            moves = '4h4a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b4h)and Bboard.b4b==''\
           and board.s4c+board.s4d+board.s4e+board.s4f+board.s4g=='':
            moves = '4h4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b4h)and Bboard.b4b==''\
           and board.s4c+board.s4d+board.s4e+board.s4f+board.s4g=='':
            moves = '4h4b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|L',    Bboard.b4h)and Bboard.b4c==''\
           and board.s4d+board.s4e+board.s4f+board.s4g=='':
            moves = '4h4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b4h)and Bboard.b4c==''\
           and board.s4d+board.s4e+board.s4f+board.s4g=='':
            moves = '4h4c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b4h)and Bboard.b4d==''\
           and board.s4e+board.s4f+board.s4g=='':
            moves = '4h4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b4h)and Bboard.b4e==''\
           and board.s4f+board.s4g=='':
            moves = '4h4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b4h)and Bboard.b4f==''\
           and board.s4g=='':
            moves = '4h4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b4h)and Bboard.b1h==''\
           and board.s2h+board.s3h=='':
            moves = '4h1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b4h)and Bboard.b2h==''\
           and board.s3h=='':
            moves = '4h2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b4h)and Bboard.b6h==''\
           and board.s5h=='':
            moves = '4h6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b4h)and Bboard.b7h==''\
           and board.s5h+board.s6h=='':
            moves = '4h7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b4h)and Bboard.b8h==''\
           and board.s5h+board.s6h+board.s7h=='':
            moves = '4h8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b4h)and Bboard.b9h==''\
           and board.s5h+board.s6h+board.s7h+board.s8h=='':
            moves = '4h9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b4h)and Bboard.b6f==''\
           and board.s5g=='':
            moves = '4h6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b4h)and Bboard.b7e==''\
           and board.s5g+board.s6f=='':
            moves = '4h7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b4h)and Bboard.b8d==''\
           and board.s5g+board.s6f+board.s7e=='':
            moves = '4h8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b4h)and Bboard.b9c==''\
           and board.s5g+board.s6f+board.s7e+board.s8d=='':
            moves = '4h9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b4h)and Bboard.b9c==''\
           and board.s5g+board.s6f+board.s7e+board.s8d=='':
            moves = '4h9c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b4h)and Bboard.b1e==''\
           and board.s2f+board.s3g=='':
            moves = '4h1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b4h)and Bboard.b2f==''\
           and board.s3g=='':
            moves = '4h2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b5h !='':
        if re.match(r'[PLSGRK+]',   Bboard.b5h)and Bboard.b5g=='':
            moves = '5h5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b5h)and Bboard.b4g=='':
            moves = '5h4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b5h)and Bboard.b6g=='':
            moves = '5h6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b5h)and Bboard.b4h=='':
            moves = '5h4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b5h)and Bboard.b6h=='':
            moves = '5h6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b5h)and Bboard.b5i=='':
            moves = '5h5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b5h)and Bboard.b4i=='':
            moves = '5h4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b5h)and Bboard.b6i=='':
            moves = '5h6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b5h)and Bboard.b4f=='':
            moves = '5h4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b5h)and Bboard.b6f=='':
            moves = '5h6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b5h)and Bboard.b5a==''\
           and board.s5b+board.s5c+board.s5d+board.s5e+board.s5f+board.s5g=='':
            moves = '5h5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b5h)and Bboard.b5a==''\
           and board.s5b+board.s5c+board.s5d+board.s5e+board.s5f+board.s5g=='':
            moves = '5h5a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b5h)and Bboard.b5b==''\
           and board.s5c+board.s5d+board.s5e+board.s5f+board.s5g=='':
            moves = '5h5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b5h)and Bboard.b5b==''\
           and board.s5c+board.s5d+board.s5e+board.s5f+board.s5g=='':
            moves = '5h5b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|L',    Bboard.b5h)and Bboard.b5c==''\
           and board.s5d+board.s5e+board.s5f+board.s5g=='':
            moves = '5h5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b5h)and Bboard.b5c==''\
           and board.s5d+board.s5e+board.s5f+board.s5g=='':
            moves = '5h5c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b5h)and Bboard.b5d==''\
           and board.s5e+board.s5f+board.s5g=='':
            moves = '5h5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b5h)and Bboard.b5e==''\
           and board.s5f+board.s5g=='':
            moves = '5h5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b5h)and Bboard.b5f==''\
           and board.s5g=='':
            moves = '5h5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b5h)and Bboard.b1h==''\
           and board.s2h+board.s3h+board.s4h=='':
            moves = '5h1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b5h)and Bboard.b2h==''\
           and board.s3h+board.s4h=='':
            moves = '5h2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b5h)and Bboard.b3h==''\
           and board.s4h=='':
            moves = '5h3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b5h)and Bboard.b7h==''\
           and board.s6h=='':
            moves = '5h7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b5h)and Bboard.b8h==''\
           and board.s6h+board.s7h=='':
            moves = '5h8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b5h)and Bboard.b9h==''\
           and board.s6h+board.s7h+board.s8h=='':
            moves = '5h9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b5h)and Bboard.b7f==''\
           and board.s6g=='':
            moves = '5h7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b5h)and Bboard.b8e==''\
           and board.s6g+board.s7f=='':
            moves = '5h8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b5h)and Bboard.b9d==''\
           and board.s6g+board.s7f+board.s8e=='':
            moves = '5h9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b5h)and Bboard.b2e==''\
           and board.s3f+board.s4g=='':
            moves = '5h2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b5h)and Bboard.b3f==''\
           and board.s4g=='':
            moves = '5h3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b5h)and Bboard.b1d==''\
           and board.s4g+board.s3f+board.s2e=='':
            moves = '5h1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b6h !='':
        if re.match(r'[PLSGRK+]',   Bboard.b6h)and Bboard.b6g=='':
            moves = '6h6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b6h)and Bboard.b5g=='':
            moves = '6h5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b6h)and Bboard.b7g=='':
            moves = '6h7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b6h)and Bboard.b5h=='':
            moves = '6h5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b6h)and Bboard.b7h=='':
            moves = '6h7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b6h)and Bboard.b6i=='':
            moves = '6h6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b6h)and Bboard.b5i=='':
            moves = '6h5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b6h)and Bboard.b7i=='':
            moves = '6h7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b6h)and Bboard.b5f=='':
            moves = '6h5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b6h)and Bboard.b7f=='':
            moves = '6h7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b6h)and Bboard.b6a==''\
           and board.s6b+board.s6c+board.s6d+board.s6e+board.s6f+board.s6g=='':
            moves = '6h6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b6h)and Bboard.b6a==''\
           and board.s6b+board.s6c+board.s6d+board.s6e+board.s6f+board.s6g=='':
            moves = '6h6a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b6h)and Bboard.b6b==''\
           and board.s6c+board.s6d+board.s6e+board.s6f+board.s6g=='':
            moves = '6h6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b6h)and Bboard.b6b==''\
           and board.s6c+board.s6d+board.s6e+board.s6f+board.s6g=='':
            moves = '6h6b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|L',    Bboard.b6h)and Bboard.b6c==''\
           and board.s6d+board.s6e+board.s6f+board.s6g=='':
            moves = '6h6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b6h)and Bboard.b6c==''\
           and board.s6d+board.s6e+board.s6f+board.s6g=='':
            moves = '6h6c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b6h)and Bboard.b6d==''\
           and board.s6e+board.s6f+board.s6g=='':
            moves = '6h6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b6h)and Bboard.b6e==''\
           and board.s6f+board.s6g=='':
            moves = '6h6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b6h)and Bboard.b6f==''\
           and board.s6g=='':
            moves = '6h6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b6h)and Bboard.b9h==''\
           and board.s8h+board.s7h=='':
            moves = '6h9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b6h)and Bboard.b8h==''\
           and board.s7h=='':
            moves = '6h8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b6h)and Bboard.b4h==''\
           and board.s5h=='':
            moves = '6h4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b6h)and Bboard.b3h==''\
           and board.s5h+board.s4h=='':
            moves = '6h3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b6h)and Bboard.b2h==''\
           and board.s5h+board.s4h+board.s3h=='':
            moves = '6h2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b6h)and Bboard.b1h==''\
           and board.s5h+board.s4h+board.s3h+board.s2h=='':
            moves = '6h1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b6h)and Bboard.b4f==''\
           and board.s5g=='':
            moves = '6h4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b6h)and Bboard.b3e==''\
           and board.s5g+board.s4f=='':
            moves = '6h3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b6h)and Bboard.b2d==''\
           and board.s5g+board.s4f+board.s3e=='':
            moves = '6h2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b6h)and Bboard.b1c==''\
           and board.s5g+board.s4f+board.s3e+board.s2d=='':
            moves = '6h1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',   Bboard.b6h)and Bboard.b1c==''\
           and board.s5g+board.s4f+board.s3e+board.s2d=='':
            moves = '6h1c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b6h)and Bboard.b9e==''\
           and board.s8f+board.s7g=='':
            moves = '6h9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b6h)and Bboard.b8f==''\
           and board.s7g=='':
            moves = '6h8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b7h !='':
        if re.match(r'[PLSGRK+]',   Bboard.b7h)and Bboard.b7g=='':
            moves = '7h7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b7h)and Bboard.b6g=='':
            moves = '7h6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b7h)and Bboard.b8g=='':
            moves = '7h8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b7h)and Bboard.b6h=='':
            moves = '7h6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b7h)and Bboard.b8h=='':
            moves = '7h8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b7h)and Bboard.b7i=='':
            moves = '7h7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b7h)and Bboard.b6i=='':
            moves = '7h6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b7h)and Bboard.b8i=='':
            moves = '7h8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b7h)and Bboard.b6f=='':
            moves = '7h6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b7h)and Bboard.b8f=='':
            moves = '7h8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b7h)and Bboard.b7a==''\
           and board.s7b+board.s7c+board.s7d+board.s7e+board.s7f+board.s7g=='':
            moves = '7h7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b7h)and Bboard.b7a==''\
           and board.s7b+board.s7c+board.s7d+board.s7e+board.s7f+board.s7g=='':
            moves = '7h7a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b7h)and Bboard.b7b==''\
           and board.s7c+board.s7d+board.s7e+board.s7f+board.s7g=='':
            moves = '7h7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b7h)and Bboard.b7b==''\
           and board.s7c+board.s7d+board.s7e+board.s7f+board.s7g=='':
            moves = '7h7b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|L',    Bboard.b7h)and Bboard.b7c==''\
           and board.s7d+board.s7e+board.s7f+board.s7g=='':
            moves = '7h7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b7h)and Bboard.b7c==''\
           and board.s7d+board.s7e+board.s7f+board.s7g=='':
            moves = '7h7c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b7h)and Bboard.b7d==''\
           and board.s7e+board.s7f+board.s7g=='':
            moves = '7h7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b7h)and Bboard.b7e==''\
           and board.s7f+board.s7g=='':
            moves = '7h7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b7h)and Bboard.b7f==''\
           and board.s7g=='':
            moves = '7h7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b7h)and Bboard.b9h==''\
           and board.s8h=='':
            moves = '7h9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b7h)and Bboard.b5h==''\
           and board.s6h=='':
            moves = '7h5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b7h)and Bboard.b4h==''\
           and board.s6h+board.s5h=='':
            moves = '7h4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b7h)and Bboard.b3h==''\
           and board.s6h+board.s5h+board.s4h=='':
            moves = '7h3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b7h)and Bboard.b2h==''\
           and board.s6h+board.s5h+board.s4h+board.s3h=='':
            moves = '7h2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b7h)and Bboard.b1h==''\
           and board.s6h+board.s5h+board.s4h+board.s3h+board.s2h=='':
            moves = '7h1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b7h)and Bboard.b2c==''\
           and board.s6g+board.s5f+board.s4e+board.s3d=='':
            moves = '7h2c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b7h)and Bboard.b1b==''\
           and board.s6g+board.s5f+board.s4e+board.s3d+board.s2c=='':
            moves = '7h1b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b7h)and Bboard.b5f==''\
           and board.s6g=='':
            moves = '7h5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b7h)and Bboard.b4e==''\
           and board.s6g+board.s5f=='':
            moves = '7h4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b7h)and Bboard.b3d==''\
           and board.s6g+board.s5f+board.s4e=='':
            moves = '7h3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b7h)and Bboard.b2c==''\
           and board.s6g+board.s5f+board.s4e+board.s3d=='':
            moves = '7h2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b7h)and Bboard.b1b==''\
           and board.s6g+board.s5f+board.s4e+board.s3d+board.s2c=='':
            moves = '7h1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b7h)and Bboard.b9f==''\
           and board.s8g=='':
            moves = '7h9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b8h !='':
        if re.match(r'[PLSGRK+]',   Bboard.b8h)and Bboard.b8g=='':
            moves = '8h8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b8h)and Bboard.b7g=='':
            moves = '8h7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b8h)and Bboard.b9g=='':
            moves = '8h9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b8h)and Bboard.b7h=='':
            moves = '8h7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b8h)and Bboard.b9h=='':
            moves = '8h9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b8h)and Bboard.b8i=='':
            moves = '8h8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b8h)and Bboard.b7i=='':
            moves = '8h7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b8h)and Bboard.b9i=='':
            moves = '8h9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b8h)and Bboard.b7f=='':
            moves = '8h7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b8h)and Bboard.b9f=='':
            moves = '8h9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b8h)and Bboard.b8a==''\
           and board.s8b+board.s8c+board.s8d+board.s8e+board.s8f+board.s8g=='':
            moves = '8h8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b8h)and Bboard.b8a==''\
           and board.s8b+board.s8c+board.s8d+board.s8e+board.s8f+board.s8g=='':
            moves = '8h8a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b8h)and Bboard.b8b==''\
           and board.s8c+board.s8d+board.s8e+board.s8f+board.s8g=='':
            moves = '8h8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b8h)and Bboard.b8b==''\
           and board.s8c+board.s8d+board.s8e+board.s8f+board.s8g=='':
            moves = '8h8b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|L',    Bboard.b8h)and Bboard.b8c==''\
           and board.s8d+board.s8e+board.s8f+board.s8g=='':
            moves = '8h8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b8h)and Bboard.b8c==''\
           and board.s8d+board.s8e+board.s8f+board.s8g=='':
            moves = '8h8c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b8h)and Bboard.b8d==''\
           and board.s8e+board.s8f+board.s8g=='':
            moves = '8h8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b8h)and Bboard.b8e==''\
           and board.s8f+board.s8g=='':
            moves = '8h8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b8h)and Bboard.b8f==''\
           and board.s8g=='':
            moves = '8h8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b8h)and Bboard.b6h==''\
           and board.s7h=='':
            moves = '8h6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b8h)and Bboard.b5h==''\
           and board.s7h+board.s6h=='':
            moves = '8h5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b8h)and Bboard.b4h==''\
           and board.s7h+board.s6h+board.s5h=='':
            moves = '8h4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b8h)and Bboard.b3h==''\
           and board.s7h+board.s6h+board.s5h+board.s4h=='':
            moves = '8h3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b8h)and Bboard.b2h==''\
           and board.s7h+board.s6h+board.s5h+board.s4h+board.s3h=='':
            moves = '8h2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b8h)and Bboard.b1h==''\
           and board.s7h+board.s6h+board.s5h+board.s4h+board.s3h+board.s2h=='':
            moves = '8h1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b8h)and Bboard.b3c==''\
           and board.s7g+board.s6f+board.s5e+board.s4d=='':
            moves = '8h3c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b8h)and Bboard.b2b==''\
           and board.s7g+board.s6f+board.s5e+board.s4d+board.s3c=='':
            moves = '8h2b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b8h)and Bboard.b1a==''\
           and board.s7g+board.s6f+board.s5e+board.s4d+board.s3c+board.s2b=='':
            moves = '8h1a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b8h)and Bboard.b6f==''\
           and board.s7g=='':
            moves = '8h6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b8h)and Bboard.b5e==''\
           and board.s7g+board.s6f=='':
            moves = '8h5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b8h)and Bboard.b4d==''\
           and board.s7g+board.s6f+board.s5e=='':
            moves = '8h4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b8h)and Bboard.b3c==''\
           and board.s7g+board.s6f+board.s5e+board.s4d=='':
            moves = '8h3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b8h)and Bboard.b2b==''\
           and board.s7g+board.s6f+board.s5e+board.s4d+board.s3c=='':
            moves = '8h2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b8h)and Bboard.b1a==''\
           and board.s7g+board.s6f+board.s5e+board.s4d+board.s3c+board.s2b=='':
            moves = '8h1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b9h !='':
        if re.match(r'[PLSGRK+]',   Bboard.b9h)and Bboard.b9g=='':
            moves = '9h9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b9h)and Bboard.b8g=='':
            moves = '9h8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b9h)and Bboard.b8h=='':
            moves = '9h8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b9h)and Bboard.b9i=='':
            moves = '9h9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|\+B|B|S|K',Bboard.b9h)and Bboard.b8i=='':
            moves = '9h8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b9h)and Bboard.b8f=='':
            moves = '9h8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b9h)and Bboard.b9a==''\
           and board.s9b+board.s9c+board.s9d+board.s9e+board.s9f+board.s9g=='':
            moves = '9h9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b9h)and Bboard.b9a==''\
           and board.s9b+board.s9c+board.s9d+board.s9e+board.s9f+board.s9g=='':
            moves = '9h9a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b9h)and Bboard.b9b==''\
           and board.s9c+board.s9d+board.s9e+board.s9f+board.s9g=='':
            moves = '9h9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b9h)and Bboard.b9b==''\
           and board.s9c+board.s9d+board.s9e+board.s9f+board.s9g=='':
            moves = '9h9b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|L',    Bboard.b9h)and Bboard.b9c==''\
           and board.s9d+board.s9e+board.s9f+board.s9g=='':
            moves = '9h9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b9h)and Bboard.b9c==''\
           and board.s9d+board.s9e+board.s9f+board.s9g=='':
            moves = '9h9c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b9h)and Bboard.b9d==''\
           and board.s9e+board.s9f+board.s9g=='':
            moves = '9h9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b9h)and Bboard.b9e==''\
           and board.s9f+board.s9g=='':
            moves = '9h9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b9h)and Bboard.b9f==''\
           and board.s9g=='':
            moves = '9h9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b9h)and Bboard.b7h==''\
           and board.s8h=='':
            moves = '9h7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b9h)and Bboard.b6h==''\
           and board.s8h+board.s7h=='':
            moves = '9h6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b9h)and Bboard.b5h==''\
           and board.s8h+board.s7h+board.s6h=='':
            moves = '9h5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b9h)and Bboard.b4h==''\
           and board.s8h+board.s7h+board.s6h+board.s5h=='':
            moves = '9h4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b9h)and Bboard.b3h==''\
           and board.s8h+board.s7h+board.s6h+board.s5h+board.s4h=='':
            moves = '9h3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b9h)and Bboard.b2h==''\
           and board.s8h+board.s7h+board.s6h+board.s5h+board.s4h+board.s3h=='':
            moves = '9h2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b9h)and Bboard.b1h==''\
           and board.s8h+board.s7h+board.s6h+board.s5h+board.s4h+board.s3h+board.s2h=='':
            moves = '9h1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b9h)and Bboard.b4c==''\
           and board.s8g+board.s7f+board.s6e+board.s5d=='':
            moves = '9h4c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b9h)and Bboard.b3b==''\
           and board.s8g+board.s7f+board.s6e+board.s5d+board.s4c=='':
            moves = '9h3b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b9h)and Bboard.b2a==''\
           and board.s8g+board.s7f+board.s6e+board.s5d+board.s4c+board.s3b=='':
            moves = '9h2a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b9h)and Bboard.b7f==''\
           and board.s8g=='':
            moves = '9h7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b9h)and Bboard.b6e==''\
           and board.s8g+board.s7f=='':
            moves = '9h6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b9h)and Bboard.b5d==''\
           and board.s8g+board.s7f+board.s6e=='':
            moves = '9h5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b9h)and Bboard.b4c==''\
           and board.s8g+board.s7f+board.s6e+board.s5d=='':
            moves = '9h4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b9h)and Bboard.b3b==''\
           and board.s8g+board.s7f+board.s6e+board.s5d+board.s4c=='':
            moves = '9h3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b9h)and Bboard.b2a==''\
           and board.s8g+board.s7f+board.s6e+board.s5d+board.s4c+board.s3b=='':
            moves = '9h2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b1i !='':
        if re.match(r'[PLSGRK+]',   Bboard.b1i)and Bboard.b1h=='':
            moves = '1i1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b1i)and Bboard.b2h=='':
            moves = '1i2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b1i)and Bboard.b2i=='':
            moves = '1i2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b1i)and Bboard.b2g=='':
            moves = '1i2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b1i)and Bboard.b1a==''\
           and board.s1b+board.s1c+board.s1d+board.s1e+board.s1f+board.s1g+board.s1h=='':
            moves = '1i1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b1i)and Bboard.b1a==''\
           and board.s1b+board.s1c+board.s1d+board.s1e+board.s1f+board.s1g+board.s1h=='':
            moves = '1i1a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b1i)and Bboard.b1b==''\
           and board.s1c+board.s1d+board.s1e+board.s1f+board.s1g+board.s1h=='':
            moves = '1i1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b1i)and Bboard.b1b==''\
           and board.s1c+board.s1d+board.s1e+board.s1f+board.s1g+board.s1h=='':
            moves = '1i1b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|L',    Bboard.b1i)and Bboard.b1c==''\
           and board.s1d+board.s1e+board.s1f+board.s1g+board.s1h=='':
            moves = '1i1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b1i)and Bboard.b1c==''\
           and board.s1d+board.s1e+board.s1f+board.s1g+board.s1h=='':
            moves = '1i1c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b1i)and Bboard.b1d==''\
           and board.s1e+board.s1f+board.s1g+board.s1h=='':
            moves = '1i1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b1i)and Bboard.b1e==''\
           and board.s1f+board.s1g+board.s1h=='':
            moves = '1i1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b1i)and Bboard.b1f==''\
           and board.s1g+board.s1h=='':
            moves = '1i1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b1i)and Bboard.b1g==''\
           and board.s1h=='':
            moves = '1i1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b1i)and Bboard.b3i==''\
           and board.s2i=='':
            moves = '1i3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b1i)and Bboard.b4i==''\
           and board.s2i+board.s3i=='':
            moves = '1i4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b1i)and Bboard.b5i==''\
           and board.s2i+board.s3i+board.s4i=='':
            moves = '1i5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b1i)and Bboard.b6i==''\
           and board.s2i+board.s3i+board.s4i+board.s5i=='':
            moves = '1i6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b1i)and Bboard.b7i==''\
           and board.s2i+board.s3i+board.s4i+board.s5i+board.s6i=='':
            moves = '1i7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b1i)and Bboard.b8i==''\
           and board.s2i+board.s3i+board.s4i+board.s5i+board.s6i+board.s7i=='':
            moves = '1i8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b1i)and Bboard.b9i==''\
           and board.s2i+board.s3i+board.s4i+board.s5i+board.s6i+board.s7i+board.s8i=='':
            moves = '1i9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b1i)and Bboard.b7c==''\
           and board.s2h+board.s3g+board.s4f+board.s5e+board.s6d=='':
            moves = '1i7c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b1i)and Bboard.b8b==''\
           and board.s2h+board.s3g+board.s4f+board.s5e+board.s6d+board.s7c=='':
            moves = '1i8b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b1i)and Bboard.b9a==''\
           and board.s2h+board.s3g+board.s4f+board.s5e+board.s6d+board.s7c+board.s8b=='':
            moves = '1i9a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b1i)and Bboard.b3g==''\
           and board.s2h=='':
            moves = '1i3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b1i)and Bboard.b4f==''\
           and board.s2h+board.s3g=='':
            moves = '1i4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b1i)and Bboard.b5e==''\
           and board.s2h+board.s3g+board.s4f=='':
            moves = '1i5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b1i)and Bboard.b6d==''\
           and board.s2h+board.s3g+board.s4f+board.s5e=='':
            moves = '1i6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b1i)and Bboard.b7c==''\
           and board.s2h+board.s3g+board.s4f+board.s5e+board.s6d=='':
            moves = '1i7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b1i)and Bboard.b8b==''\
           and board.s2h+board.s3g+board.s4f+board.s5e+board.s6d+board.s7c=='':
            moves = '1i8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b1i)and Bboard.b9a==''\
           and board.s2h+board.s3g+board.s4f+board.s5e+board.s6d+board.s7c+board.s8b=='':
            moves = '1i9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b2i !='':
        if re.match(r'[PLSGRK+]',   Bboard.b2i)and Bboard.b2h=='':
            moves = '2i2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b2i)and Bboard.b1h=='':
            moves = '2i1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b2i)and Bboard.b3h=='':
            moves = '2i3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b2i)and Bboard.b1i=='':
            moves = '2i1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b2i)and Bboard.b3i=='':
            moves = '2i3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b2i)and Bboard.b1g=='':
            moves = '2i1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b2i)and Bboard.b3g=='':
            moves = '2i3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b2i)and Bboard.b2a==''\
           and board.s2b+board.s2c+board.s2d+board.s2e+board.s2f+board.s2g+board.s2h=='':
            moves = '2i2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b2i)and Bboard.b2a==''\
           and board.s2b+board.s2c+board.s2d+board.s2e+board.s2f+board.s2g+board.s2h=='':
            moves = '2i2a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b2i)and Bboard.b2b==''\
           and board.s2c+board.s2d+board.s2e+board.s2f+board.s2g+board.s2h=='':
            moves = '2i2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b2i)and Bboard.b2b==''\
           and board.s2c+board.s2d+board.s2e+board.s2f+board.s2g+board.s2h=='':
            moves = '2i2b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|L',    Bboard.b2i)and Bboard.b2c==''\
           and board.s2d+board.s2e+board.s2f+board.s2g+board.s2h=='':
            moves = '2i2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b2i)and Bboard.b2c==''\
           and board.s2d+board.s2e+board.s2f+board.s2g+board.s2h=='':
            moves = '2i2c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b2i)and Bboard.b2d==''\
           and board.s2e+board.s2f+board.s2g+board.s2h=='':
            moves = '2i2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b2i)and Bboard.b2e==''\
           and board.s2f+board.s2g+board.s2h=='':
            moves = '2i2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b2i)and Bboard.b2f==''\
           and board.s2g+board.s2h=='':
            moves = '2i2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b2i)and Bboard.b2g==''\
           and board.s2h=='':
            moves = '2i2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b2i)and Bboard.b4i==''\
           and board.s3i=='':
            moves = '2i4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b2i)and Bboard.b5i==''\
           and board.s3i+board.s4i=='':
            moves = '2i5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b2i)and Bboard.b6i==''\
           and board.s3i+board.s4i+board.s5i=='':
            moves = '2i6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b2i)and Bboard.b7i==''\
           and board.s3i+board.s4i+board.s5i+board.s6i=='':
            moves = '2i7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b2i)and Bboard.b8i==''\
           and board.s3i+board.s4i+board.s5i+board.s6i+board.s7i=='':
            moves = '2i8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b2i)and Bboard.b9i==''\
           and board.s3i+board.s4i+board.s5i+board.s6i+board.s7i+board.s8i=='':
            moves = '2i9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b2i)and Bboard.b8c==''\
           and board.s3h+board.s4g+board.s5f+board.s6e+board.s7d=='':
            moves = '2i8c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b2i)and Bboard.b9b==''\
           and board.s3h+board.s4g+board.s5f+board.s6e+board.s7d+board.s8c=='':
            moves = '2i9b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b2i)and Bboard.b4g==''\
           and board.s3h=='':
            moves = '2i4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b2i)and Bboard.b5f==''\
           and board.s3h+board.s4g=='':
            moves = '2i5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b2i)and Bboard.b6e==''\
           and board.s3h+board.s4g+board.s5f=='':
            moves = '2i6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b2i)and Bboard.b7d==''\
           and board.s3h+board.s4g+board.s5f+board.s6e=='':
            moves = '2i7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b2i)and Bboard.b8c==''\
           and board.s3h+board.s4g+board.s5f+board.s6e+board.s7d=='':
            moves = '2i8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b2i)and Bboard.b9b==''\
           and board.s3h+board.s4g+board.s5f+board.s6e+board.s7d+board.s8c=='':
            moves = '2i9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b3i !='':
        if re.match(r'[PLSGRK+]',   Bboard.b3i)and Bboard.b3h=='':
            moves = '3i3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b3i)and Bboard.b2h=='':
            moves = '3i2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b3i)and Bboard.b4h=='':
            moves = '3i4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b3i)and Bboard.b2i=='':
            moves = '3i2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b3i)and Bboard.b4i=='':
            moves = '3i4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b3i)and Bboard.b2g=='':
            moves = '3i2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b3i)and Bboard.b4g=='':
            moves = '3i4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b3i)and Bboard.b3a==''\
           and board.s3b+board.s3c+board.s3d+board.s3e+board.s3f+board.s3g+board.s3h=='':
            moves = '3i3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b3i)and Bboard.b3a==''\
           and board.s3b+board.s3c+board.s3d+board.s3e+board.s3f+board.s3g+board.s3h=='':
            moves = '3i3a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b3i)and Bboard.b3b==''\
           and board.s3c+board.s3d+board.s3e+board.s3f+board.s3g+board.s3h=='':
            moves = '3i3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b3i)and Bboard.b3b==''\
           and board.s3c+board.s3d+board.s3e+board.s3f+board.s3g+board.s3h=='':
            moves = '3i3b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|L',    Bboard.b3i)and Bboard.b3c==''\
           and board.s3d+board.s3e+board.s3f+board.s3g+board.s3h=='':
            moves = '3i3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b3i)and Bboard.b3c==''\
           and board.s3d+board.s3e+board.s3f+board.s3g+board.s3h=='':
            moves = '3i3c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b3i)and Bboard.b3d==''\
           and board.s3e+board.s3f+board.s3g+board.s3h=='':
            moves = '3i3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b3i)and Bboard.b3e==''\
           and board.s3f+board.s3g+board.s3h=='':
            moves = '3i3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b3i)and Bboard.b3f==''\
           and board.s3g+board.s3h=='':
            moves = '3i3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b3i)and Bboard.b3g==''\
           and board.s3h=='':
            moves = '3i3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b3i)and Bboard.b1i==''\
           and board.s2i=='':
            moves = '3i1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b3i)and Bboard.b5i==''\
           and board.s4i=='':
            moves = '3i5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b3i)and Bboard.b6i==''\
           and board.s4i+board.s5i=='':
            moves = '3i6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b3i)and Bboard.b7i==''\
           and board.s4i+board.s5i+board.s6i=='':
            moves = '3i7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b3i)and Bboard.b8i==''\
           and board.s4i+board.s5i+board.s6i+board.s7i=='':
            moves = '3i8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b3i)and Bboard.b9i==''\
           and board.s4i+board.s5i+board.s6i+board.s7i+board.s8i=='':
            moves = '3i9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b3i)and Bboard.b9c==''\
           and board.s4h+board.s5g+board.s6f+board.s7e+board.s8d=='':
            moves = '3i9c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b3i)and Bboard.b1g==''\
           and board.s2h=='':
            moves = '3i1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b3i)and Bboard.b5g==''\
           and board.s4h=='':
            moves = '3i5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b3i)and Bboard.b6f==''\
           and board.s4h+board.s5g=='':
            moves = '3i6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b3i)and Bboard.b6e==''\
           and board.s4h+board.s5g+board.s6f=='':
            moves = '3i7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b3i)and Bboard.b7d==''\
           and board.s4h+board.s5g+board.s6f+board.s7e=='':
            moves = '3i8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b3i)and Bboard.b9c==''\
           and board.s4h+board.s5g+board.s6f+board.s7e+board.s8d=='':
            moves = '3i9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b4i !='':
        if re.match(r'[PLSGRK+]',   Bboard.b4i)and Bboard.b4h=='':
            moves = '4i4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b4i)and Bboard.b3h=='':
            moves = '4i3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b4i)and Bboard.b5h=='':
            moves = '4i5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b4i)and Bboard.b3i=='':
            moves = '4i3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b4i)and Bboard.b5i=='':
            moves = '4i5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b4i)and Bboard.b3g=='':
            moves = '4i3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b4i)and Bboard.b5g=='':
            moves = '4i5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b4i)and Bboard.b4a==''\
           and board.s4b+board.s4c+board.s4d+board.s4e+board.s4f+board.s4g+board.s4h=='':
            moves = '4i4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b4i)and Bboard.b4a==''\
           and board.s4b+board.s4c+board.s4d+board.s4e+board.s4f+board.s4g+board.s4h=='':
            moves = '4i4a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b4i)and Bboard.b4b==''\
           and board.s4c+board.s4d+board.s4e+board.s4f+board.s4g+board.s4h=='':
            moves = '4i4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b4i)and Bboard.b4b==''\
           and board.s4c+board.s4d+board.s4e+board.s4f+board.s4g+board.s4h=='':
            moves = '4i4b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|L',    Bboard.b4i)and Bboard.b4c==''\
           and board.s4d+board.s4e+board.s4f+board.s4g+board.s4h=='':
            moves = '4i4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b4i)and Bboard.b4c==''\
           and board.s4d+board.s4e+board.s4f+board.s4g+board.s4h=='':
            moves = '4i4c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b4i)and Bboard.b4d==''\
           and board.s4e+board.s4f+board.s4g+board.s4h=='':
            moves = '4i4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b4i)and Bboard.b4e==''\
           and board.s4f+board.s4g+board.s4h=='':
            moves = '4i4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b4i)and Bboard.b4f==''\
           and board.s4g+board.s4h=='':
            moves = '4i4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b4i)and Bboard.b4g==''\
           and board.s4h=='':
            moves = '4i4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b4i)and Bboard.b1i==''\
           and board.s2i+board.s3i=='':
            moves = '4i1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b4i)and Bboard.b2i==''\
           and board.s3i=='':
            moves = '4i2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b4i)and Bboard.b6i==''\
           and board.s5i=='':
            moves = '4i6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b4i)and Bboard.b7i==''\
           and board.s5i+board.s6i=='':
            moves = '4i7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b4i)and Bboard.b8i==''\
           and board.s5i+board.s6i+board.s7i=='':
            moves = '4i8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b4i)and Bboard.b9i==''\
           and board.s5i+board.s6i+board.s7i+board.s8i=='':
            moves = '4i9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b4i)and Bboard.b6g==''\
           and board.s5h=='':
            moves = '4i6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b4i)and Bboard.b7f==''\
           and board.s5h+board.s6g=='':
            moves = '4i7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b4i)and Bboard.b8e==''\
           and board.s5h+board.s6g+board.s7f=='':
            moves = '4i8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b4i)and Bboard.b9d==''\
           and board.s5h+board.s6g+board.s7f+board.s8e=='':
            moves = '4i9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b4i)and Bboard.b1f==''\
           and board.s2g+board.s3h=='':
            moves = '4i1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b4i)and Bboard.b2g==''\
           and board.s3h=='':
            moves = '4i2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b5i !='':
        if re.match(r'[PLSGRK+]',   Bboard.b5i)and Bboard.b5h=='':
            moves = '5i5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b5i)and Bboard.b4h=='':
            moves = '5i4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b5i)and Bboard.b6h=='':
            moves = '5i6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b5i)and Bboard.b4i=='':
            moves = '5i4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b5i)and Bboard.b6i=='':
            moves = '5i6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b5i)and Bboard.b4g=='':
            moves = '5i4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b5i)and Bboard.b6g=='':
            moves = '5i6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b5i)and Bboard.b5a==''\
           and board.s5b+board.s5c+board.s5d+board.s5e+board.s5f+board.s5g+board.s5h=='':
            moves = '5i5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b5i)and Bboard.b5a==''\
           and board.s5b+board.s5c+board.s5d+board.s5e+board.s5f+board.s5g+board.s5h=='':
            moves = '5i5a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b5i)and Bboard.b5b==''\
           and board.s5c+board.s5d+board.s5e+board.s5f+board.s5g+board.s5h=='':
            moves = '5i5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b5i)and Bboard.b5b==''\
           and board.s5c+board.s5d+board.s5e+board.s5f+board.s5g+board.s5h=='':
            moves = '5i5b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|L',    Bboard.b5i)and Bboard.b5c==''\
           and board.s5d+board.s5e+board.s5f+board.s5g+board.s5h=='':
            moves = '5i5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b5i)and Bboard.b5c==''\
           and board.s5d+board.s5e+board.s5f+board.s5g+board.s5h=='':
            moves = '5i5c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b5i)and Bboard.b5d==''\
           and board.s5e+board.s5f+board.s5g+board.s5h=='':
            moves = '5i5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b5i)and Bboard.b5e==''\
           and board.s5f+board.s5g+board.s5h=='':
            moves = '5i5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b5i)and Bboard.b5f==''\
           and board.s5g+board.s5h=='':
            moves = '5i5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b5i)and Bboard.b5g==''\
           and board.s5h=='':
            moves = '5i5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b5i)and Bboard.b1i==''\
           and board.s2i+board.s3i+board.s4i=='':
            moves = '5i1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b5i)and Bboard.b2i==''\
           and board.s3i+board.s4i=='':
            moves = '5i2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b5i)and Bboard.b3i==''\
           and board.s4i=='':
            moves = '5i3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b5i)and Bboard.b7i==''\
           and board.s6i=='':
            moves = '5i7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b5i)and Bboard.b8i==''\
           and board.s6i+board.s7i=='':
            moves = '5i8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b5i)and Bboard.b9i==''\
           and board.s6i+board.s7i+board.s8i=='':
            moves = '5i9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b5i)and Bboard.b7g==''\
           and board.s6h=='':
            moves = '5i7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b5i)and Bboard.b8f==''\
           and board.s6h+board.s7g=='':
            moves = '5i8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b5i)and Bboard.b9e==''\
           and board.s6h+board.s7g+board.s8f=='':
            moves = '5i9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b5i)and Bboard.b2f==''\
           and board.s3g+board.s4h=='':
            moves = '5i2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b5i)and Bboard.b3g==''\
           and board.s4h=='':
            moves = '5i3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b5i)and Bboard.b1e==''\
           and board.s4h+board.s3g+board.s2f=='':
            moves = '5i1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b6i !='':
        if re.match(r'[PLSGRK+]',   Bboard.b6i)and Bboard.b6h=='':
            moves = '6i6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b6i)and Bboard.b5h=='':
            moves = '6i5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b6i)and Bboard.b7h=='':
            moves = '6i7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b6i)and Bboard.b5i=='':
            moves = '6i5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b6i)and Bboard.b7i=='':
            moves = '6i7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b6i)and Bboard.b5g=='':
            moves = '6i5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b6i)and Bboard.b7g=='':
            moves = '6i7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b6i)and Bboard.b6a==''\
           and board.s6b+board.s6c+board.s6d+board.s6e+board.s6f+board.s6g+board.s6h=='':
            moves = '6i6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b6i)and Bboard.b6a==''\
           and board.s6b+board.s6c+board.s6d+board.s6e+board.s6f+board.s6g+board.s6h=='':
            moves = '6i6a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b6i)and Bboard.b6b==''\
           and board.s6c+board.s6d+board.s6e+board.s6f+board.s6g+board.s6h=='':
            moves = '6i6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b6i)and Bboard.b6b==''\
           and board.s6c+board.s6d+board.s6e+board.s6f+board.s6g+board.s6h=='':
            moves = '6i6b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|L',    Bboard.b6i)and Bboard.b6c==''\
           and board.s6d+board.s6e+board.s6f+board.s6g+board.s6h=='':
            moves = '6i6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b6i)and Bboard.b6c==''\
           and board.s6d+board.s6e+board.s6f+board.s6g+board.s6h=='':
            moves = '6i6c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b6i)and Bboard.b6d==''\
           and board.s6e+board.s6f+board.s6g+board.s6h=='':
            moves = '6i6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b6i)and Bboard.b6e==''\
           and board.s6f+board.s6g+board.s6h=='':
            moves = '6i6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b6i)and Bboard.b6f==''\
           and board.s6g+board.s6h=='':
            moves = '6i6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b6i)and Bboard.b6g==''\
           and board.s6h=='':
            moves = '6i6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b6i)and Bboard.b9i==''\
           and board.s8i+board.s7i=='':
            moves = '6i9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b6i)and Bboard.b8i==''\
           and board.s7i=='':
            moves = '6i8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b6i)and Bboard.b4i==''\
           and board.s5i=='':
            moves = '6i4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b6i)and Bboard.b3i==''\
           and board.s5i+board.s4i=='':
            moves = '6i3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b6i)and Bboard.b2i==''\
           and board.s5i+board.s4i+board.s3i=='':
            moves = '6i2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b6i)and Bboard.b1i==''\
           and board.s5i+board.s4i+board.s3i+board.s2i=='':
            moves = '6i1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b6i)and Bboard.b4g==''\
           and board.s5h=='':
            moves = '6i4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b6i)and Bboard.b3f==''\
           and board.s5h+board.s4g=='':
            moves = '6i3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b6i)and Bboard.b2e==''\
           and board.s5h+board.s4g+board.s3f=='':
            moves = '6i2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b6i)and Bboard.b1d==''\
           and board.s5h+board.s4g+board.s3f+board.s2e=='':
            moves = '6i1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b6i)and Bboard.b9f==''\
           and board.s8g+board.s7h=='':
            moves = '6i9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b6i)and Bboard.b8g==''\
           and board.s7h=='':
            moves = '6i8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b7i !='':
        if re.match(r'[PLSGRK+]',   Bboard.b7i)and Bboard.b7h=='':
            moves = '7i7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b7i)and Bboard.b6h=='':
            moves = '7i6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b7i)and Bboard.b8h=='':
            moves = '7i8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b7i)and Bboard.b6i=='':
            moves = '7i6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b7i)and Bboard.b8i=='':
            moves = '7i8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b7i)and Bboard.b6g=='':
            moves = '7i6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b7i)and Bboard.b8g=='':
            moves = '7i8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b7i)and Bboard.b7a==''\
           and board.s7b+board.s7c+board.s7d+board.s7e+board.s7f+board.s7g+board.s7h=='':
            moves = '7i7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b7i)and Bboard.b7a==''\
           and board.s7b+board.s7c+board.s7d+board.s7e+board.s7f+board.s7g+board.s7h=='':
            moves = '7i7a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b7i)and Bboard.b7b==''\
           and board.s7c+board.s7d+board.s7e+board.s7f+board.s7g+board.s7h=='':
            moves = '7i7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b7i)and Bboard.b7b==''\
           and board.s7c+board.s7d+board.s7e+board.s7f+board.s7g+board.s7h=='':
            moves = '7i7b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|L',    Bboard.b7i)and Bboard.b7c==''\
           and board.s7d+board.s7e+board.s7f+board.s7g+board.s7h=='':
            moves = '7i7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b7i)and Bboard.b7c==''\
           and board.s7d+board.s7e+board.s7f+board.s7g+board.s7h=='':
            moves = '7i7c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b7i)and Bboard.b7d==''\
           and board.s7e+board.s7f+board.s7g+board.s7h=='':
            moves = '7i7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b7i)and Bboard.b7e==''\
           and board.s7f+board.s7g+board.s7h=='':
            moves = '7i7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b7i)and Bboard.b7f==''\
           and board.s7g+board.s7h=='':
            moves = '7i7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b7i)and Bboard.b7g==''\
           and board.s7h=='':
            moves = '7i7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b7i)and Bboard.b9i==''\
           and board.s8i=='':
            moves = '7i9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b7i)and Bboard.b5i==''\
           and board.s6i=='':
            moves = '7i5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b7i)and Bboard.b4i==''\
           and board.s6i+board.s5i=='':
            moves = '7i4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b7i)and Bboard.b3i==''\
           and board.s6i+board.s5i+board.s4i=='':
            moves = '7i3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b7i)and Bboard.b2i==''\
           and board.s6i+board.s5i+board.s4i+board.s3i=='':
            moves = '7i2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b7i)and Bboard.b1i==''\
           and board.s6i+board.s5i+board.s4i+board.s3i+board.s2i=='':
            moves = '7i1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b7i)and Bboard.b1c==''\
           and board.s6h+board.s5g+board.s4f+board.s3e+board.s2d=='':
            moves = '7i1c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b7i)and Bboard.b9g==''\
           and board.s8h=='':
            moves = '7i9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b7i)and Bboard.b5g==''\
           and board.s6h=='':
            moves = '7i5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b7i)and Bboard.b4f==''\
           and board.s6h+board.s5g=='':
            moves = '7i4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b7i)and Bboard.b4e==''\
           and board.s6h+board.s5g+board.s4f=='':
            moves = '7i3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b7i)and Bboard.b3d==''\
           and board.s6h+board.s5g+board.s4f+board.s3e=='':
            moves = '7i2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b7i)and Bboard.b1c==''\
           and board.s6h+board.s5g+board.s4f+board.s3e+board.s2d=='':
            moves = '7i1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b8i !='':
        if re.match(r'[PLSGRK+]',   Bboard.b8i)and Bboard.b8h=='':
            moves = '8i8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b8i)and Bboard.b7h=='':
            moves = '8i7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b8i)and Bboard.b9h=='':
            moves = '8i9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b8i)and Bboard.b7i=='':
            moves = '8i7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b8i)and Bboard.b9i=='':
            moves = '8i9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b8i)and Bboard.b7g=='':
            moves = '8i7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b8i)and Bboard.b9g=='':
            moves = '8i9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b8i)and Bboard.b8a==''\
           and board.s8b+board.s8c+board.s8d+board.s8e+board.s8f+board.s8g+board.s8h=='':
            moves = '8i8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b8i)and Bboard.b8a==''\
           and board.s8b+board.s8c+board.s8d+board.s8e+board.s8f+board.s8g+board.s8h=='':
            moves = '8i8a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b8i)and Bboard.b8b==''\
           and board.s8c+board.s8d+board.s8e+board.s8f+board.s8g+board.s8h=='':
            moves = '8i8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b8i)and Bboard.b8b==''\
           and board.s8c+board.s8d+board.s8e+board.s8f+board.s8g+board.s8h=='':
            moves = '8i8b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|L',    Bboard.b8i)and Bboard.b8c==''\
           and board.s8d+board.s8e+board.s8f+board.s8g+board.s8h=='':
            moves = '8i8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b8i)and Bboard.b8c==''\
           and board.s8d+board.s8e+board.s8f+board.s8g+board.s8h=='':
            moves = '8i8c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b8i)and Bboard.b8d==''\
           and board.s8e+board.s8f+board.s8g+board.s8h=='':
            moves = '8i8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b8i)and Bboard.b8e==''\
           and board.s8f+board.s8g+board.s8h=='':
            moves = '8i8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b8i)and Bboard.b8f==''\
           and board.s8g+board.s8h=='':
            moves = '8i8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b8i)and Bboard.b8g==''\
           and board.s8h=='':
            moves = '8i8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b8i)and Bboard.b6i==''\
           and board.s7i=='':
            moves = '8i6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b8i)and Bboard.b5i==''\
           and board.s7i+board.s6i=='':
            moves = '8i5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b8i)and Bboard.b4i==''\
           and board.s7i+board.s6i+board.s5i=='':
            moves = '8i4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b8i)and Bboard.b3i==''\
           and board.s7i+board.s6i+board.s5i+board.s4i=='':
            moves = '8i3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b8i)and Bboard.b2i==''\
           and board.s7i+board.s6i+board.s5i+board.s4i+board.s3i=='':
            moves = '8i2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b8i)and Bboard.b1i==''\
           and board.s7i+board.s6i+board.s5i+board.s4i+board.s3i+board.s2i=='':
            moves = '8i1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b8i)and Bboard.b2c==''\
           and board.s7h+board.s6g+board.s5f+board.s4e+board.s3d=='':
            moves = '8i2c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b8i)and Bboard.b1b==''\
           and board.s7h+board.s6g+board.s5f+board.s4e+board.s3d+board.s2c=='':
            moves = '8i1b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b8i)and Bboard.b6g==''\
           and board.s7h=='':
            moves = '8i6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b8i)and Bboard.b5f==''\
           and board.s7h+board.s6g=='':
            moves = '8i5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b8i)and Bboard.b4e==''\
           and board.s7h+board.s6g+board.s5f=='':
            moves = '8i4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b8i)and Bboard.b3d==''\
           and board.s7h+board.s6g+board.s5f+board.s4e=='':
            moves = '8i3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b8i)and Bboard.b2c==''\
           and board.s7h+board.s6g+board.s5f+board.s4e+board.s3d=='':
            moves = '8i2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b8i)and Bboard.b1b==''\
           and board.s7h+board.s6g+board.s5f+board.s4e+board.s3d+board.s2c=='':
            moves = '8i1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if Bboard.b9i !='':
        if re.match(r'[PLSGRK+]',   Bboard.b9i)and Bboard.b9h=='':
            moves = '9i9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[SGBK+]',    Bboard.b9i)and Bboard.b8h=='':
            moves = '9i8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'[GRK+]',     Bboard.b9i)and Bboard.b8i=='':
            moves = '9i8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('N',         Bboard.b9i)and Bboard.b8g=='':
            moves = '9i8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b9i)and Bboard.b9a==''\
           and board.s9b+board.s9c+board.s9d+board.s9e+board.s9f+board.s9g+board.s9h=='':
            moves = '9i9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b9i)and Bboard.b9a==''\
           and board.s9b+board.s9c+board.s9d+board.s9e+board.s9f+board.s9g+board.s9h=='':
            moves = '9i9a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+R',        Bboard.b9i)and Bboard.b9b==''\
           and board.s9c+board.s9d+board.s9e+board.s9f+board.s9g+board.s9h=='':
            moves = '9i9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b9i)and Bboard.b9b==''\
           and board.s9c+board.s9d+board.s9e+board.s9f+board.s9g+board.s9h=='':
            moves = '9i9b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|L',    Bboard.b9i)and Bboard.b9c==''\
           and board.s9d+board.s9e+board.s9f+board.s9g+board.s9h=='':
            moves = '9i9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'R|L',      Bboard.b9i)and Bboard.b9c==''\
           and board.s9d+board.s9e+board.s9f+board.s9g+board.s9h=='':
            moves = '9i9c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b9i)and Bboard.b9d==''\
           and board.s9e+board.s9f+board.s9g+board.s9h=='':
            moves = '9i9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b9i)and Bboard.b9e==''\
           and board.s9f+board.s9g+board.s9h=='':
            moves = '9i9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b9i)and Bboard.b9f==''\
           and board.s9g+board.s9h=='':
            moves = '9i9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R|L',   Bboard.b9i)and Bboard.b9g==''\
           and board.s9h=='':
            moves = '9i9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b9i)and Bboard.b7i==''\
           and board.s8i=='':
            moves = '9i7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b9i)and Bboard.b6i==''\
           and board.s8i+board.s7i=='':
            moves = '9i6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b9i)and Bboard.b5i==''\
           and board.s8i+board.s7i+board.s6i=='':
            moves = '9i5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',   Bboard.b9i)and Bboard.b4i==''\
           and board.s8i+board.s7i+board.s6i+board.s5i=='':
            moves = '9i4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b9i)and Bboard.b3i==''\
           and board.s8i+board.s7i+board.s6i+board.s5i+board.s4i=='':
            moves = '9i3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b9i)and Bboard.b2i==''\
           and board.s8i+board.s7i+board.s6i+board.s5i+board.s4i+board.s3i=='':
            moves = '9i2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+R|R',      Bboard.b9i)and Bboard.b1i==''\
           and board.s8i+board.s7i+board.s6i+board.s5i+board.s4i+board.s3i+board.s2i=='':
            moves = '9i1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b9i)and Bboard.b3c==''\
           and board.s8h+board.s7g+board.s6f+board.s5e+board.s4d=='':
            moves = '9i3c+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b9i)and Bboard.b2b==''\
           and board.s8h+board.s7g+board.s6f+board.s5e+board.s4d+board.s3c=='':
            moves = '9i2b+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('B',Bboard.b9i)and Bboard.b1a==''\
           and board.s8h+board.s7g+board.s6f+board.s5e+board.s4d+board.s3c+board.s2b=='':
            moves = '9i1a+'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b9i)and Bboard.b7g==''\
           and board.s8h=='':
            moves = '9i7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b9i)and Bboard.b6f==''\
           and board.s8h+board.s7g=='':
            moves = '9i6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b9i)and Bboard.b5e==''\
           and board.s8h+board.s7g+board.s6f=='':
            moves = '9i5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match(r'\+B|B',   Bboard.b9i)and Bboard.b4d==''\
           and board.s8h+board.s7g+board.s6f+board.s5e=='':
            moves = '9i4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b9i)and Bboard.b3c==''\
           and board.s8h+board.s7g+board.s6f+board.s5e+board.s4d=='':
            moves = '9i3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b9i)and Bboard.b2b==''\
           and board.s8h+board.s7g+board.s6f+board.s5e+board.s4d+board.s3c=='':
            moves = '9i2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if re.match('\+B',   Bboard.b9i)and Bboard.b1a==''\
           and board.s8h+board.s7g+board.s6f+board.s5e+board.s4d+board.s3c+board.s2b=='':
            moves = '9i1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s1a =='':
        if Bboard.S>0:
            moves = 'S*1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*1a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s1b =='':
        if Bboard.P>0 and (Bboard.b1b !='P' and Bboard.b1c !='P' and Bboard.b1d !='P' and Bboard.b1e !='P' and Bboard.b1f !='P' and Bboard.b1g !='P' and Bboard.b1h !='P' and Bboard.b1i !='P'):
            moves = 'P*1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*1b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s1c =='':
        if Bboard.P>0 and (Bboard.b1b !='P' and Bboard.b1c !='P' and Bboard.b1d !='P' and Bboard.b1e !='P' and Bboard.b1f !='P' and Bboard.b1g !='P' and Bboard.b1h !='P' and Bboard.b1i !='P'):
            moves = 'P*1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*1c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s1d =='':
        if Bboard.P>0 and (Bboard.b1b !='P' and Bboard.b1c !='P' and Bboard.b1d !='P' and Bboard.b1e !='P' and Bboard.b1f !='P' and Bboard.b1g !='P' and Bboard.b1h !='P' and Bboard.b1i !='P'):
            moves = 'P*1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*1d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s1e =='':
        if Bboard.P>0 and (Bboard.b1b !='P' and Bboard.b1c !='P' and Bboard.b1d !='P' and Bboard.b1e !='P' and Bboard.b1f !='P' and Bboard.b1g !='P' and Bboard.b1h !='P' and Bboard.b1i !='P'):
            moves = 'P*1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*1e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s1f =='':
        if Bboard.P>0 and (Bboard.b1b !='P' and Bboard.b1c !='P' and Bboard.b1d !='P' and Bboard.b1e !='P' and Bboard.b1f !='P' and Bboard.b1g !='P' and Bboard.b1h !='P' and Bboard.b1i !='P'):
            moves = 'P*1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*1f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s1g =='':
        if Bboard.P>0 and (Bboard.b1b !='P' and Bboard.b1c !='P' and Bboard.b1d !='P' and Bboard.b1e !='P' and Bboard.b1f !='P' and Bboard.b1g !='P' and Bboard.b1h !='P' and Bboard.b1i !='P'):
            moves = 'P*1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*1g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s1h =='':
        if Bboard.P>0 and (Bboard.b1b !='P' and Bboard.b1c !='P' and Bboard.b1d !='P' and Bboard.b1e !='P' and Bboard.b1f !='P' and Bboard.b1g !='P' and Bboard.b1h !='P' and Bboard.b1i !='P'):
            moves = 'P*1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*1h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s1i =='':
        if Bboard.P>0 and (Bboard.b1b !='P' and Bboard.b1c !='P' and Bboard.b1d !='P' and Bboard.b1e !='P' and Bboard.b1f !='P' and Bboard.b1g !='P' and Bboard.b1h !='P' and Bboard.b1i !='P'):
            moves = 'P*1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*1i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s2a =='':
        if Bboard.S>0:
            moves = 'S*2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*2a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s2b =='':
        if Bboard.P>0 and (Bboard.b2b !='P' and Bboard.b2c !='P' and Bboard.b2d !='P' and Bboard.b2e !='P' and Bboard.b2f !='P' and Bboard.b2g !='P' and Bboard.b2h !='P' and Bboard.b2i !='P'):
            moves = 'P*2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*2b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s2c =='':
        if Bboard.P>0 and (Bboard.b2b !='P' and Bboard.b2c !='P' and Bboard.b2d !='P' and Bboard.b2e !='P' and Bboard.b2f !='P' and Bboard.b2g !='P' and Bboard.b2h !='P' and Bboard.b2i !='P'):
            moves = 'P*2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*2c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s2d =='':
        if Bboard.P>0 and (Bboard.b2b !='P' and Bboard.b2c !='P' and Bboard.b2d !='P' and Bboard.b2e !='P' and Bboard.b2f !='P' and Bboard.b2g !='P' and Bboard.b2h !='P' and Bboard.b2i !='P'):
            moves = 'P*2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*2d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s2e =='':
        if Bboard.P>0 and (Bboard.b2b !='P' and Bboard.b2c !='P' and Bboard.b2d !='P' and Bboard.b2e !='P' and Bboard.b2f !='P' and Bboard.b2g !='P' and Bboard.b2h !='P' and Bboard.b2i !='P'):
            moves = 'P*2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*2e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s2f =='':
        if Bboard.P>0 and (Bboard.b2b !='P' and Bboard.b2c !='P' and Bboard.b2d !='P' and Bboard.b2e !='P' and Bboard.b2f !='P' and Bboard.b2g !='P' and Bboard.b2h !='P' and Bboard.b2i !='P'):
            moves = 'P*2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*2f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s2g =='':
        if Bboard.P>0 and (Bboard.b2b !='P' and Bboard.b2c !='P' and Bboard.b2d !='P' and Bboard.b2e !='P' and Bboard.b2f !='P' and Bboard.b2g !='P' and Bboard.b2h !='P' and Bboard.b2i !='P'):
            moves = 'P*2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*2g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s2h =='':
        if Bboard.P>0 and (Bboard.b2b !='P' and Bboard.b2c !='P' and Bboard.b2d !='P' and Bboard.b2e !='P' and Bboard.b2f !='P' and Bboard.b2g !='P' and Bboard.b2h !='P' and Bboard.b2i !='P'):
            moves = 'P*2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*2h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s2i =='':
        if Bboard.P>0 and (Bboard.b2b !='P' and Bboard.b2c !='P' and Bboard.b2d !='P' and Bboard.b2e !='P' and Bboard.b2f !='P' and Bboard.b2g !='P' and Bboard.b2h !='P' and Bboard.b2i !='P'):
            moves = 'P*2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*2i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s3a =='':
        if Bboard.S>0:
            moves = 'S*3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*3a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s3b =='':
        if Bboard.P>0 and (Bboard.b3b !='P' and Bboard.b3c !='P' and Bboard.b3d !='P' and Bboard.b3e !='P' and Bboard.b3f !='P' and Bboard.b3g !='P' and Bboard.b3h !='P' and Bboard.b3i !='P'):
            moves = 'P*3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*3b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s3c =='':
        if Bboard.P>0 and (Bboard.b3b !='P' and Bboard.b3c !='P' and Bboard.b3d !='P' and Bboard.b3e !='P' and Bboard.b3f !='P' and Bboard.b3g !='P' and Bboard.b3h !='P' and Bboard.b3i !='P'):
            moves = 'P*3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*3c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s3d =='':
        if Bboard.P>0 and (Bboard.b3b !='P' and Bboard.b3c !='P' and Bboard.b3d !='P' and Bboard.b3e !='P' and Bboard.b3f !='P' and Bboard.b3g !='P' and Bboard.b3h !='P' and Bboard.b3i !='P'):
            moves = 'P*3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*3d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s3e =='':
        if Bboard.P>0 and (Bboard.b3b !='P' and Bboard.b3c !='P' and Bboard.b3d !='P' and Bboard.b3e !='P' and Bboard.b3f !='P' and Bboard.b3g !='P' and Bboard.b3h !='P' and Bboard.b3i !='P'):
            moves = 'P*3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*3e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s3f =='':
        if Bboard.P>0 and (Bboard.b3b !='P' and Bboard.b3c !='P' and Bboard.b3d !='P' and Bboard.b3e !='P' and Bboard.b3f !='P' and Bboard.b3g !='P' and Bboard.b3h !='P' and Bboard.b3i !='P'):
            moves = 'P*3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*3f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s3g =='':
        if Bboard.P>0 and (Bboard.b3b !='P' and Bboard.b3c !='P' and Bboard.b3d !='P' and Bboard.b3e !='P' and Bboard.b3f !='P' and Bboard.b3g !='P' and Bboard.b3h !='P' and Bboard.b3i !='P'):
            moves = 'P*3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*3g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s3h =='':
        if Bboard.P>0 and (Bboard.b3b !='P' and Bboard.b3c !='P' and Bboard.b3d !='P' and Bboard.b3e !='P' and Bboard.b3f !='P' and Bboard.b3g !='P' and Bboard.b3h !='P' and Bboard.b3i !='P'):
            moves = 'P*3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*3h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s3i =='':
        if Bboard.P>0 and (Bboard.b3b !='P' and Bboard.b3c !='P' and Bboard.b3d !='P' and Bboard.b3e !='P' and Bboard.b3f !='P' and Bboard.b3g !='P' and Bboard.b3h !='P' and Bboard.b3i !='P'):
            moves = 'P*3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*3i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s4a =='':
        if Bboard.S>0:
            moves = 'S*4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*4a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s4b =='':
        if Bboard.P>0 and (Bboard.b4b !='P' and Bboard.b4c !='P' and Bboard.b4d !='P' and Bboard.b4e !='P' and Bboard.b4f !='P' and Bboard.b4g !='P' and Bboard.b4h !='P' and Bboard.b4i !='P'):
            moves = 'P*4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*4b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s4c =='':
        if Bboard.P>0 and (Bboard.b4b !='P' and Bboard.b4c !='P' and Bboard.b4d !='P' and Bboard.b4e !='P' and Bboard.b4f !='P' and Bboard.b4g !='P' and Bboard.b4h !='P' and Bboard.b4i !='P'):
            moves = 'P*4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*4c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s4d =='':
        if Bboard.P>0 and (Bboard.b4b !='P' and Bboard.b4c !='P' and Bboard.b4d !='P' and Bboard.b4e !='P' and Bboard.b4f !='P' and Bboard.b4g !='P' and Bboard.b4h !='P' and Bboard.b4i !='P'):
            moves = 'P*4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*4d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s4e =='':
        if Bboard.P>0 and (Bboard.b4b !='P' and Bboard.b4c !='P' and Bboard.b4d !='P' and Bboard.b4e !='P' and Bboard.b4f !='P' and Bboard.b4g !='P' and Bboard.b4h !='P' and Bboard.b4i !='P'):
            moves = 'P*4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*4e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s4f =='':
        if Bboard.P>0 and (Bboard.b4b !='P' and Bboard.b4c !='P' and Bboard.b4d !='P' and Bboard.b4e !='P' and Bboard.b4f !='P' and Bboard.b4g !='P' and Bboard.b4h !='P' and Bboard.b4i !='P'):
            moves = 'P*4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*4f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s4g =='':
        if Bboard.P>0 and (Bboard.b4b !='P' and Bboard.b4c !='P' and Bboard.b4d !='P' and Bboard.b4e !='P' and Bboard.b4f !='P' and Bboard.b4g !='P' and Bboard.b4h !='P' and Bboard.b4i !='P'):
            moves = 'P*4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*4g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s4h =='':
        if Bboard.P>0 and (Bboard.b4b !='P' and Bboard.b4c !='P' and Bboard.b4d !='P' and Bboard.b4e !='P' and Bboard.b4f !='P' and Bboard.b4g !='P' and Bboard.b4h !='P' and Bboard.b4i !='P'):
            moves = 'P*4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*4h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s4i =='':
        if Bboard.P>0 and (Bboard.b4b !='P' and Bboard.b4c !='P' and Bboard.b4d !='P' and Bboard.b4e !='P' and Bboard.b4f !='P' and Bboard.b4g !='P' and Bboard.b4h !='P' and Bboard.b4i !='P'):
            moves = 'P*4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*4i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s9a =='':
        if Bboard.S>0:
            moves = 'S*9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*9a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s9b =='':
        if Bboard.P>0 and (Bboard.b9b !='P' and Bboard.b9c !='P' and Bboard.b9d !='P' and Bboard.b9e !='P' and Bboard.b9f !='P' and Bboard.b9g !='P' and Bboard.b9h !='P' and Bboard.b9i !='P'):
            moves = 'P*9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*9b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s9c =='':
        if Bboard.P>0 and (Bboard.b9b !='P' and Bboard.b9c !='P' and Bboard.b9d !='P' and Bboard.b9e !='P' and Bboard.b9f !='P' and Bboard.b9g !='P' and Bboard.b9h !='P' and Bboard.b9i !='P'):
            moves = 'P*9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*9c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s9d =='':
        if Bboard.P>0 and (Bboard.b9b !='P' and Bboard.b9c !='P' and Bboard.b9d !='P' and Bboard.b9e !='P' and Bboard.b9f !='P' and Bboard.b9g !='P' and Bboard.b9h !='P' and Bboard.b9i !='P'):
            moves = 'P*9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*9d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s9e =='':
        if Bboard.P>0 and (Bboard.b9b !='P' and Bboard.b9c !='P' and Bboard.b9d !='P' and Bboard.b9e !='P' and Bboard.b9f !='P' and Bboard.b9g !='P' and Bboard.b9h !='P' and Bboard.b9i !='P'):
            moves = 'P*9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*9e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s9f =='':
        if Bboard.P>0 and (Bboard.b9b !='P' and Bboard.b9c !='P' and Bboard.b9d !='P' and Bboard.b9e !='P' and Bboard.b9f !='P' and Bboard.b9g !='P' and Bboard.b9h !='P' and Bboard.b9i !='P'):
            moves = 'P*9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*9f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s9g =='':
        if Bboard.P>0 and (Bboard.b9b !='P' and Bboard.b9c !='P' and Bboard.b9d !='P' and Bboard.b9e !='P' and Bboard.b9f !='P' and Bboard.b9g !='P' and Bboard.b9h !='P' and Bboard.b9i !='P'):
            moves = 'P*9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*9g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s9h =='':
        if Bboard.P>0 and (Bboard.b9b !='P' and Bboard.b9c !='P' and Bboard.b9d !='P' and Bboard.b9e !='P' and Bboard.b9f !='P' and Bboard.b9g !='P' and Bboard.b9h !='P' and Bboard.b9i !='P'):
            moves = 'P*9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*9h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s9i =='':
        if Bboard.P>0 and (Bboard.b9b !='P' and Bboard.b9c !='P' and Bboard.b9d !='P' and Bboard.b9e !='P' and Bboard.b9f !='P' and Bboard.b9g !='P' and Bboard.b9h !='P' and Bboard.b9i !='P'):
            moves = 'P*9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*9i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s8a =='':
        if Bboard.S>0:
            moves = 'S*8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*8a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s8b =='':
        if Bboard.P>0 and (Bboard.b8b !='P' and Bboard.b8c !='P' and Bboard.b8d !='P' and Bboard.b8e !='P' and Bboard.b8f !='P' and Bboard.b8g !='P' and Bboard.b8h !='P' and Bboard.b8i !='P'):
            moves = 'P*8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*8b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s8c =='':
        if Bboard.P>0 and (Bboard.b8b !='P' and Bboard.b8c !='P' and Bboard.b8d !='P' and Bboard.b8e !='P' and Bboard.b8f !='P' and Bboard.b8g !='P' and Bboard.b8h !='P' and Bboard.b8i !='P'):
            moves = 'P*8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*8c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s8d =='':
        if Bboard.P>0 and (Bboard.b8b !='P' and Bboard.b8c !='P' and Bboard.b8d !='P' and Bboard.b8e !='P' and Bboard.b8f !='P' and Bboard.b8g !='P' and Bboard.b8h !='P' and Bboard.b8i !='P'):
            moves = 'P*8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*8d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s8e =='':
        if Bboard.P>0 and (Bboard.b8b !='P' and Bboard.b8c !='P' and Bboard.b8d !='P' and Bboard.b8e !='P' and Bboard.b8f !='P' and Bboard.b8g !='P' and Bboard.b8h !='P' and Bboard.b8i !='P'):
            moves = 'P*8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*8e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s8f =='':
        if Bboard.P>0 and (Bboard.b8b !='P' and Bboard.b8c !='P' and Bboard.b8d !='P' and Bboard.b8e !='P' and Bboard.b8f !='P' and Bboard.b8g !='P' and Bboard.b8h !='P' and Bboard.b8i !='P'):
            moves = 'P*8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*8f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s8g =='':
        if Bboard.P>0 and (Bboard.b8b !='P' and Bboard.b8c !='P' and Bboard.b8d !='P' and Bboard.b8e !='P' and Bboard.b8f !='P' and Bboard.b8g !='P' and Bboard.b8h !='P' and Bboard.b8i !='P'):
            moves = 'P*8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*8g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s8h =='':
        if Bboard.P>0 and (Bboard.b8b !='P' and Bboard.b8c !='P' and Bboard.b8d !='P' and Bboard.b8e !='P' and Bboard.b8f !='P' and Bboard.b8g !='P' and Bboard.b8h !='P' and Bboard.b8i !='P'):
            moves = 'P*8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*8h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s8i =='':
        if Bboard.P>0 and (Bboard.b8b !='P' and Bboard.b8c !='P' and Bboard.b8d !='P' and Bboard.b8e !='P' and Bboard.b8f !='P' and Bboard.b8g !='P' and Bboard.b8h !='P' and Bboard.b8i !='P'):
            moves = 'P*8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*8i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s7a =='':
        if Bboard.S>0:
            moves = 'S*7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*7a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s7b =='':
        if Bboard.P>0 and (Bboard.b7b !='P' and Bboard.b7c !='P' and Bboard.b7d !='P' and Bboard.b7e !='P' and Bboard.b7f !='P' and Bboard.b7g !='P' and Bboard.b7h !='P' and Bboard.b7i !='P'):
            moves = 'P*7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*7b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s7c =='':
        if Bboard.P>0 and (Bboard.b7b !='P' and Bboard.b7c !='P' and Bboard.b7d !='P' and Bboard.b7e !='P' and Bboard.b7f !='P' and Bboard.b7g !='P' and Bboard.b7h !='P' and Bboard.b7i !='P'):
            moves = 'P*7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*7c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s7d =='':
        if Bboard.P>0 and (Bboard.b7b !='P' and Bboard.b7c !='P' and Bboard.b7d !='P' and Bboard.b7e !='P' and Bboard.b7f !='P' and Bboard.b7g !='P' and Bboard.b7h !='P' and Bboard.b7i !='P'):
            moves = 'P*7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*7d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s7e =='':
        if Bboard.P>0 and (Bboard.b7b !='P' and Bboard.b7c !='P' and Bboard.b7d !='P' and Bboard.b7e !='P' and Bboard.b7f !='P' and Bboard.b7g !='P' and Bboard.b7h !='P' and Bboard.b7i !='P'):
            moves = 'P*7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*7e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s7f =='':
        if Bboard.P>0 and (Bboard.b7b !='P' and Bboard.b7c !='P' and Bboard.b7d !='P' and Bboard.b7e !='P' and Bboard.b7f !='P' and Bboard.b7g !='P' and Bboard.b7h !='P' and Bboard.b7i !='P'):
            moves = 'P*7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*7f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s7g =='':
        if Bboard.P>0 and (Bboard.b7b !='P' and Bboard.b7c !='P' and Bboard.b7d !='P' and Bboard.b7e !='P' and Bboard.b7f !='P' and Bboard.b7g !='P' and Bboard.b7h !='P' and Bboard.b7i !='P'):
            moves = 'P*7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*7g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s7h =='':
        if Bboard.P>0 and (Bboard.b7b !='P' and Bboard.b7c !='P' and Bboard.b7d !='P' and Bboard.b7e !='P' and Bboard.b7f !='P' and Bboard.b7g !='P' and Bboard.b7h !='P' and Bboard.b7i !='P'):
            moves = 'P*7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*7h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s7i =='':
        if Bboard.P>0 and (Bboard.b7b !='P' and Bboard.b7c !='P' and Bboard.b7d !='P' and Bboard.b7e !='P' and Bboard.b7f !='P' and Bboard.b7g !='P' and Bboard.b7h !='P' and Bboard.b7i !='P'):
            moves = 'P*7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*7i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s6a =='':
        if Bboard.S>0:
            moves = 'S*6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*6a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s6b =='':
        if Bboard.P>0 and (Bboard.b6b !='P' and Bboard.b6c !='P' and Bboard.b6d !='P' and Bboard.b6e !='P' and Bboard.b6f !='P' and Bboard.b6g !='P' and Bboard.b6h !='P' and Bboard.b6i !='P'):
            moves = 'P*6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*6b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s6c =='':
        if Bboard.P>0 and (Bboard.b6b !='P' and Bboard.b6c !='P' and Bboard.b6d !='P' and Bboard.b6e !='P' and Bboard.b6f !='P' and Bboard.b6g !='P' and Bboard.b6h !='P' and Bboard.b6i !='P'):
            moves = 'P*6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*6c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s6d =='':
        if Bboard.P>0 and (Bboard.b6b !='P' and Bboard.b6c !='P' and Bboard.b6d !='P' and Bboard.b6e !='P' and Bboard.b6f !='P' and Bboard.b6g !='P' and Bboard.b6h !='P' and Bboard.b6i !='P'):
            moves = 'P*6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*6d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s6e =='':
        if Bboard.P>0 and (Bboard.b6b !='P' and Bboard.b6c !='P' and Bboard.b6d !='P' and Bboard.b6e !='P' and Bboard.b6f !='P' and Bboard.b6g !='P' and Bboard.b6h !='P' and Bboard.b6i !='P'):
            moves = 'P*6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*6e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s6f =='':
        if Bboard.P>0 and (Bboard.b6b !='P' and Bboard.b6c !='P' and Bboard.b6d !='P' and Bboard.b6e !='P' and Bboard.b6f !='P' and Bboard.b6g !='P' and Bboard.b6h !='P' and Bboard.b6i !='P'):
            moves = 'P*6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*6f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s6g =='':
        if Bboard.P>0 and (Bboard.b6b !='P' and Bboard.b6c !='P' and Bboard.b6d !='P' and Bboard.b6e !='P' and Bboard.b6f !='P' and Bboard.b6g !='P' and Bboard.b6h !='P' and Bboard.b6i !='P'):
            moves = 'P*6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*6g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s6h =='':
        if Bboard.P>0 and (Bboard.b6b !='P' and Bboard.b6c !='P' and Bboard.b6d !='P' and Bboard.b6e !='P' and Bboard.b6f !='P' and Bboard.b6g !='P' and Bboard.b6h !='P' and Bboard.b6i !='P'):
            moves = 'P*6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*6h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s6i =='':
        if Bboard.P>0 and (Bboard.b6b !='P' and Bboard.b6c !='P' and Bboard.b6d !='P' and Bboard.b6e !='P' and Bboard.b6f !='P' and Bboard.b6g !='P' and Bboard.b6h !='P' and Bboard.b6i !='P'):
            moves = 'P*6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*6i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s5a =='':
        if Bboard.S>0:
            moves = 'S*5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*5a'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s5b =='':
        if Bboard.P>0 and (Bboard.b5b !='P' and Bboard.b5c !='P' and Bboard.b5d !='P' and Bboard.b5e !='P' and Bboard.b5f !='P' and Bboard.b5g !='P' and Bboard.b5h !='P' and Bboard.b5i !='P'):
            moves = 'P*5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*5b'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s5c =='':
        if Bboard.P>0 and (Bboard.b5b !='P' and Bboard.b5c !='P' and Bboard.b5d !='P' and Bboard.b5e !='P' and Bboard.b5f !='P' and Bboard.b5g !='P' and Bboard.b5h !='P' and Bboard.b5i !='P'):
            moves = 'P*5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*5c'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s5d =='':
        if Bboard.P>0 and (Bboard.b5b !='P' and Bboard.b5c !='P' and Bboard.b5d !='P' and Bboard.b5e !='P' and Bboard.b5f !='P' and Bboard.b5g !='P' and Bboard.b5h !='P' and Bboard.b5i !='P'):
            moves = 'P*5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*5d'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s5e =='':
        if Bboard.P>0 and (Bboard.b5b !='P' and Bboard.b5c !='P' and Bboard.b5d !='P' and Bboard.b5e !='P' and Bboard.b5f !='P' and Bboard.b5g !='P' and Bboard.b5h !='P' and Bboard.b5i !='P'):
            moves = 'P*5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*5e'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s5f =='':
        if Bboard.P>0 and (Bboard.b5b !='P' and Bboard.b5c !='P' and Bboard.b5d !='P' and Bboard.b5e !='P' and Bboard.b5f !='P' and Bboard.b5g !='P' and Bboard.b5h !='P' and Bboard.b5i !='P'):
            moves = 'P*5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*5f'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s5g =='':
        if Bboard.P>0 and (Bboard.b5b !='P' and Bboard.b5c !='P' and Bboard.b5d !='P' and Bboard.b5e !='P' and Bboard.b5f !='P' and Bboard.b5g !='P' and Bboard.b5h !='P' and Bboard.b5i !='P'):
            moves = 'P*5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*5g'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s5h =='':
        if Bboard.P>0 and (Bboard.b5b !='P' and Bboard.b5c !='P' and Bboard.b5d !='P' and Bboard.b5e !='P' and Bboard.b5f !='P' and Bboard.b5g !='P' and Bboard.b5h !='P' and Bboard.b5i !='P'):
            moves = 'P*5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*5h'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)

    if board.s5i =='':
        if Bboard.P>0 and (Bboard.b5b !='P' and Bboard.b5c !='P' and Bboard.b5d !='P' and Bboard.b5e !='P' and Bboard.b5f !='P' and Bboard.b5g !='P' and Bboard.b5h !='P' and Bboard.b5i !='P'):
            moves = 'P*5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.L>0:
            moves = 'L*5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.N>0:
            moves = 'N*5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.S>0:
            moves = 'S*5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.G>0:
            moves = 'G*5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.B>0:
            moves = 'B*5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
        if Bboard.R>0:
            moves = 'R*5i'
            kaihimore(moves)
            if oute.oute == 0:
                depth1.append(moves)
