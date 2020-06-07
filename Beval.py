import Bboard
import Wboard
import board
import Bboardbak
import Wboardbak
import Bboardbak2
import Wboardbak2
import Bkiki1
import Bkiki2
import Wkiki1
import Wkiki2
import Wkikimoves1
import gc

def torare():
    torare=0
    torare2=0
    for j in range(80):
        b = 0
        w = 0
        b = Bkiki2.kikilist1[j]
        w = Wkiki2.kikilist1[j]
        if Bkiki2.kikilist2[j] =='P':
            torare -= w*100-b*20
            if torare<0:
                torare2+=torare
        if Bkiki2.kikilist2[j] =='L':
            torare -= w*800-b*20
            if torare<0:
                torare2+=torare
        if Bkiki2.kikilist2[j] =='N':
            torare -= w*800-b*20
            if torare<0:
                torare2+=torare
        if Bkiki2.kikilist2[j] =='G' or Bkiki2.kikilist2[j] =='S' or Bkiki2.kikilist2[j] =='+P' or Bkiki2.kikilist2[j] =='+L' or Bkiki2.kikilist2[j] =='+N' or Bkiki2.kikilist2[j] =='+S':
            torare -= w*1000-b*20
            if torare<0:
                torare2+=torare
        if Bkiki2.kikilist2[j] =='B':
            torare -= w*2500
            if torare<0:
                torare2+=torare
        if Bkiki2.kikilist2[j] =='R':
            torare -= w*3000
            if torare<0:
                torare2+=torare
        if Bkiki2.kikilist2[j] =='+R' or Bkiki2.kikilist2[j] =='+B':
            torare -= w*3200
            if torare<0:
                torare2+=torare
    return torare2

def eval(sfen):
    global sashite,score,torare,koma
    score =[]
    for i in range(len(sfen)):
        Bboardbak.yobidashi()
        Wboardbak.yobidashi()
        mae = sfen[i][0:2]
        ushiro = sfen[i][2:4]
        nari = sfen[i][4:5]
        if mae[1:2]=='*':
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
        Bboardbak2.kioku()
        Wboardbak2.kioku()
        board.synth()
        Wkikimoves1.move1()
        if Wkikimoves1.depth1 == [] and sfen[i][0:2] != 'P*':
            print('bestmove '+sfen[i])
            return
        Bkiki1.culc()
        Bkiki2.culc()
        Wkiki2.culc()
        torare2=int(torare())
        Bboardbak2.yobidashi()
        koma=Bboard.P*450+Bboard.L*850+Bboard.N*850+Bboard.S*1250+Bboard.G*1250+Bboard.B*20000+Bboard.R*30000
        point=0
        point= Bkiki1.kiki1 + Bkiki2.kiki2*2 + koma + torare2
        score.append(point)
        Bkiki2.kikilist1.clear()
        Bkiki2.kikilist2.clear()
        Wkiki2.kikilist1.clear()
        Wkiki2.kikilist2.clear()
    sashite = score.index(max(score))
