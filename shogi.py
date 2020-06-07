import re
import random
import Bboard
import Wboard
import board
import Bmoves
import Wmoves
import Beval
import Weval
import Bkikimoves1
import Wkikimoves1

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
            moves = Bmoves.depth1
            #合法手がなければ投了
            if Bmoves.depth1==[]:
                print('bestmove resign')
            #合法手があればランダムで選択
            else:
                Beval.eval(moves)
                if Wkikimoves1.depth1 == []:
                    break
                print('info score cp '+ str(max(Beval.score)))
                print('bestmove '+Bmoves.depth1[Beval.sashite])
        #後手番も同じ
        else:
            Wmoves.move1()
            print(f'{Wmoves.depth1=}')
            moves = Wmoves.depth1
            if Wmoves.depth1==[]:
                print('bestmove resign')
            else:
                Weval.eval(moves)
                if Bkikimoves1.depth1 == []:
                    break
                print('info score cp '+str(max(Weval.score)))
                print('bestmove '+Wmoves.depth1[Weval.sashite])
