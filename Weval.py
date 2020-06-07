import Bboard
import Wboard
import board
import Bboardbak
import Wboardbak
import Bboardbak2
import Wboardbak2
import Wkiki1
import Wkiki2
import Bkiki1
import Bkiki2
import Bkikimoves1
import gc

def torare():
    torare=0
    torare2=0
    for j in range(80):
        b = 0
        w = 0
        b = Bkiki2.kikilist1[j]
        w = Wkiki2.kikilist1[j]
        if Wkiki2.kikilist2[j] =='p':
            torare -= b*150-w*10
            if torare<0:
                torare2+=torare
        if Wkiki2.kikilist2[j] =='l':
            torare -= b*800-w*10
            if torare<0:
                torare2+=torare
        if Wkiki2.kikilist2[j] =='n':
            torare -= b*800-w*10
            if torare<0:
                torare2+=torare
        if Wkiki2.kikilist2[j] =='g' or Wkiki2.kikilist2[j] =='s' or Wkiki2.kikilist2[j] =='+p' or Wkiki2.kikilist2[j] =='+l' or Wkiki2.kikilist2[j] =='+n' or Wkiki2.kikilist2[j] =='+s':
            torare -= b*1000-w*10
            if torare<0:
                torare2+=torare
        if Wkiki2.kikilist2[j] =='b':
            torare -= b*2500
            if torare<0:
                torare2+=torare
        if Wkiki2.kikilist2[j] =='r':
            torare -= b*3000
            if torare<0:
                torare2+=torare
        if Wkiki2.kikilist2[j] =='+r' or Wkiki2.kikilist2[j] =='+b':
            torare -= b*3200
            if torare<0:
                torare2+=torare
    return torare2


def eval(sfen):
    global sashite,score
    score =[]
    for i in range(len(sfen)):
        Bboardbak.yobidashi()
        Wboardbak.yobidashi()
        mae = sfen[i][0:2]
        ushiro = sfen[i][2:4]
        nari = sfen[i][4:5]
        if mae[1:2]=='*':
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
        Bboardbak2.kioku()
        Wboardbak2.kioku()
        board.synth()
        Bkikimoves1.move1()
        if Bkikimoves1.depth1 == [] and sfen[i][0:2] != 'P*':
            print('bestmove '+sfen[i])
            return
        Wkiki1.culc()
        Wkiki2.culc()
        Bkiki2.culc()
        torare2=torare()
        Wboardbak2.yobidashi()
        koma=Wboard.p*350+Wboard.l*850+Wboard.n*850+Wboard.s*1250+Wboard.g*1250+Wboard.b*20000+Wboard.r*30000
        point=0
        point=Wkiki1.kiki1*2+Wkiki2.kiki2*3+torare2+koma
        score.append(point)
        Bkiki2.kikilist1.clear()
        Bkiki2.kikilist2.clear()
        Wkiki2.kikilist1.clear()
        Wkiki2.kikilist2.clear()
    sashite = score.index(max(score))
