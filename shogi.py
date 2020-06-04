import re
import random
import Bboard
import Wboard
import board
import oute
import Bmoves
import Wmoves

#usiコマンドに対応する根幹部分
sfen =''
i = 0
while i < 5:
    command = input()
    if command == 'usi':
        print('id name suisui') 
        print('usiok')
    if command == 'isready':
        print('readyok')
    if re.match('position', command):
        sfen = command
    if re.match('go', command):
        #初期局面にする
        Bboard.shoki()
        Wboard.shoki()
        #startposを読み込み、現局面を表示する
        board.position(sfen)
        board.synth()
        board.kyokumen()
        print(f'{board.turn = }')
        #以下合法手生成
        if board.turn == 1:
            Bmoves.move1()
            print(f'{Bmoves.depth1=}')
            #合法手がなければ投了
            if Bmoves.depth1==[]:
                print('bestmove resign')
            #合法手があればランダムで選択
            else:
                print('bestmove '+Bmoves.depth1[random.randint(0,len(Bmoves.depth1)-1)])
        #後手番も同じ
        else:
            Wmoves.move1()
            print(f'{Wmoves.depth1=}')
            if Wmoves.depth1==[]:
                print('bestmove resign')
            else:
                print('bestmove '+Wmoves.depth1[random.randint(0,len(Wmoves.depth1)-1)])
