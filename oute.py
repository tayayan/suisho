import re
import board

#王手がかかっているかを判定。玉の位置は1一から5五まで。
def soute():
    global oute
    oute = 0
    if board.s1a == 'K':
        if re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s2a)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s1b)\
           or re.search(r'[bk]',board.s2b)or board.s2b=='s'or board.s2b=='+r'\
           or (re.search('r',board.s1c) and board.s1b=='')\
           or (re.search('r',board.s1d) and board.s1b+board.s1c=='')\
           or (re.search('r',board.s1e) and board.s1b+board.s1c+board.s1d=='')\
           or (re.search('r',board.s1f) and board.s1b+board.s1c+board.s1d+board.s1e=='')\
           or (re.search('r',board.s1g) and board.s1b+board.s1c+board.s1d+board.s1e+board.s1f=='')\
           or (re.search('r',board.s1h) and board.s1b+board.s1c+board.s1d+board.s1e+board.s1f+board.s1g=='')\
           or (re.search('r',board.s1i) and board.s1b+board.s1c+board.s1d+board.s1e+board.s1f+board.s1g+board.s1h=='')\
           or (re.search('r',board.s3a) and board.s2a=='')\
           or (re.search('r',board.s4a) and board.s2a+board.s3a=='')\
           or (re.search('r',board.s5a) and board.s2a+board.s3a+board.s4a=='')\
           or (re.search('r',board.s6a) and board.s2a+board.s3a+board.s4a+board.s5a=='')\
           or (re.search('r',board.s7a) and board.s2a+board.s3a+board.s4a+board.s5a+board.s6a=='')\
           or (re.search('r',board.s8a) and board.s2a+board.s3a+board.s4a+board.s5a+board.s6a+board.s7a=='')\
           or (re.search('r',board.s9a) and board.s2a+board.s3a+board.s4a+board.s5a+board.s6a+board.s7a+board.s8a=='')\
           or (re.search('b',board.s3c) and board.s2b=='')\
           or (re.search('b',board.s4d) and board.s2b+board.s3c=='')\
           or (re.search('b',board.s5e) and board.s2b+board.s3c+board.s4d=='')\
           or (re.search('b',board.s6f) and board.s2b+board.s3c+board.s4d+board.s5e=='')\
           or (re.search('b',board.s7g) and board.s2b+board.s3c+board.s4d+board.s5e+board.s6f=='')\
           or (re.search('b',board.s8h) and board.s2b+board.s3c+board.s4d+board.s5e+board.s6f+board.s7g=='')\
           or (re.search('b',board.s9i) and board.s2b+board.s3c+board.s4d+board.s5e+board.s6f+board.s7g+board.s8h=='')\
           :
            oute=1

    if board.s1b == 'K':
        if re.search(r'[plsgrk]|\+n|\+b',board.s1a)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s2a)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s2b)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s1c)\
           or re.search(r'[bk]',board.s2c)or board.s2c=='s'or board.s2c=='+r'\
           or (re.search('r',board.s1d) and board.s1c=='')\
           or (re.search('r',board.s1e) and board.s1c+board.s1d=='')\
           or (re.search('r',board.s1f) and board.s1c+board.s1d+board.s1e=='')\
           or (re.search('r',board.s1g) and board.s1c+board.s1d+board.s1e+board.s1f=='')\
           or (re.search('r',board.s1h) and board.s1c+board.s1d+board.s1e+board.s1f+board.s1g=='')\
           or (re.search('r',board.s1i) and board.s1c+board.s1d+board.s1e+board.s1f+board.s1g+board.s1h=='')\
           or (re.search('r',board.s3b) and board.s2b=='')\
           or (re.search('r',board.s4b) and board.s2b+board.s3b=='')\
           or (re.search('r',board.s5b) and board.s2b+board.s3b+board.s4b=='')\
           or (re.search('r',board.s6b) and board.s2b+board.s3b+board.s4b+board.s5b=='')\
           or (re.search('r',board.s7b) and board.s2b+board.s3b+board.s4b+board.s5b+board.s6b=='')\
           or (re.search('r',board.s8b) and board.s2b+board.s3b+board.s4b+board.s5b+board.s6b+board.s7b=='')\
           or (re.search('r',board.s9b) and board.s2b+board.s3b+board.s4b+board.s5b+board.s6b+board.s7b+board.s8b=='')\
           or (re.search('b',board.s3d) and board.s2c=='')\
           or (re.search('b',board.s4e) and board.s2c+board.s3d=='')\
           or (re.search('b',board.s5f) and board.s2c+board.s3d+board.s4e=='')\
           or (re.search('b',board.s6g) and board.s2c+board.s3d+board.s4e+board.s5f=='')\
           or (re.search('b',board.s7h) and board.s2c+board.s3d+board.s4e+board.s5f+board.s6g=='')\
           or (re.search('b',board.s8i) and board.s2c+board.s3d+board.s4e+board.s5f+board.s6g+board.s7h=='')\
           :
            oute=1
            
    if board.s1c == 'K':
        if re.search(r'[plsgrk]|\+n|\+b',board.s1b)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s2b)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s2c)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s1d)\
           or re.search(r'[bk]',board.s2d)or board.s2d=='s'or board.s2d=='+r'\
           or ((re.search('r',board.s1a)or board.s1a=='l')and board.s1b=='')\
           or (re.search('r',board.s1e) and board.s1d=='')\
           or (re.search('r',board.s1f) and board.s1d+board.s1e=='')\
           or (re.search('r',board.s1g) and board.s1d+board.s1e+board.s1f=='')\
           or (re.search('r',board.s1h) and board.s1d+board.s1e+board.s1f+board.s1g=='')\
           or (re.search('r',board.s1i) and board.s1d+board.s1e+board.s1f+board.s1g+board.s1h=='')\
           or (re.search('r',board.s3c) and board.s2c=='')\
           or (re.search('r',board.s4c) and board.s2c+board.s3c=='')\
           or (re.search('r',board.s5c) and board.s2c+board.s3c+board.s4c=='')\
           or (re.search('r',board.s6c) and board.s2c+board.s3c+board.s4c+board.s5c=='')\
           or (re.search('r',board.s7c) and board.s2c+board.s3c+board.s4c+board.s5c+board.s6c=='')\
           or (re.search('r',board.s8c) and board.s2c+board.s3c+board.s4c+board.s5c+board.s6c+board.s7c=='')\
           or (re.search('r',board.s9c) and board.s2c+board.s3c+board.s4c+board.s5c+board.s6c+board.s7c+board.s8c=='')\
           or (re.search('b',board.s3a) and board.s2b=='')\
           or (re.search('b',board.s3e) and board.s2d=='')\
           or (re.search('b',board.s4f) and board.s2d+board.s3e=='')\
           or (re.search('b',board.s5g) and board.s2d+board.s3e+board.s4f=='')\
           or (re.search('b',board.s6h) and board.s2d+board.s3e+board.s4f+board.s5g=='')\
           or (re.search('b',board.s7i) and board.s2d+board.s3e+board.s4f+board.s5g+board.s6h=='')\
           or board.s2a =='n'\
           :
            oute=1

    if board.s1d == 'K':
        if re.search(r'[plsgrk]|\+n|\+b',board.s1c)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s2c)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s2d)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s1e)\
           or re.search(r'[bk]',board.s2e)or board.s2e=='s'or board.s2e=='+r'\
           or ((re.search('r',board.s1a)or board.s1a=='l') and board.s1b+board.s1c=='')\
           or ((re.search('r',board.s1b)or board.s1b=='l') and board.s1c=='')\
           or (re.search('r',board.s1f) and board.s1e=='')\
           or (re.search('r',board.s1g) and board.s1e+board.s1f=='')\
           or (re.search('r',board.s1h) and board.s1e+board.s1f+board.s1g=='')\
           or (re.search('r',board.s1i) and board.s1e+board.s1f+board.s1g+board.s1h=='')\
           or (re.search('r',board.s3d) and board.s2d=='')\
           or (re.search('r',board.s4d) and board.s2d+board.s3d=='')\
           or (re.search('r',board.s5d) and board.s2d+board.s3d+board.s4d=='')\
           or (re.search('r',board.s6d) and board.s2d+board.s3d+board.s4d+board.s5d=='')\
           or (re.search('r',board.s7d) and board.s2d+board.s3d+board.s4d+board.s5d+board.s6d=='')\
           or (re.search('r',board.s8d) and board.s2d+board.s3d+board.s4d+board.s5d+board.s6d+board.s7d=='')\
           or (re.search('r',board.s9d) and board.s2d+board.s3d+board.s4d+board.s5d+board.s6d+board.s7d+board.s8d=='')\
           or (re.search('b',board.s4a) and board.s3b+board.s2c=='')\
           or (re.search('b',board.s3b) and board.s2c=='')\
           or (re.search('b',board.s3f) and board.s2e=='')\
           or (re.search('b',board.s4g) and board.s2e+board.s3f=='')\
           or (re.search('b',board.s5h) and board.s2e+board.s3f+board.s4g=='')\
           or (re.search('b',board.s6i) and board.s2e+board.s3f+board.s4g+board.s5h=='')\
           or board.s2b =='n'\
           :
            oute=1

    if board.s1e == 'K':
        if re.search(r'[plsgrk]|\+n|\+b',board.s1d)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s2d)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s2e)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s1f)\
           or re.search(r'[bk]',board.s2f)or board.s2f=='s'or board.s2f=='+r'\
           or ((re.search('r',board.s1a)or board.s1a=='l') and board.s1b+board.s1c+board.s1d=='')\
           or ((re.search('r',board.s1b)or board.s1b=='l') and board.s1c+board.s1d=='')\
           or ((re.search('r',board.s1c)or board.s1c=='l') and board.s1d=='')\
           or (re.search('r',board.s1g) and board.s1e=='')\
           or (re.search('r',board.s1h) and board.s1e+board.s1f=='')\
           or (re.search('r',board.s1i) and board.s1e+board.s1f+board.s1g=='')\
           or (re.search('r',board.s3e) and board.s2e=='')\
           or (re.search('r',board.s4e) and board.s2e+board.s3e=='')\
           or (re.search('r',board.s5e) and board.s2e+board.s3e+board.s4e=='')\
           or (re.search('r',board.s6e) and board.s2e+board.s3e+board.s4e+board.s5e=='')\
           or (re.search('r',board.s7e) and board.s2e+board.s3e+board.s4e+board.s5e+board.s6e=='')\
           or (re.search('r',board.s8e) and board.s2e+board.s3e+board.s4e+board.s5e+board.s6e+board.s7e=='')\
           or (re.search('r',board.s9e) and board.s2e+board.s3e+board.s4e+board.s5e+board.s6e+board.s7e+board.s8e=='')\
           or (re.search('b',board.s5a) and board.s4b+board.s3c+board.s2d=='')\
           or (re.search('b',board.s4b) and board.s3c+board.s2d=='')\
           or (re.search('b',board.s3c) and board.s2d=='')\
           or (re.search('b',board.s3g) and board.s2f=='')\
           or (re.search('b',board.s4h) and board.s2f+board.s3g=='')\
           or (re.search('b',board.s5i) and board.s2f+board.s3g+board.s4h=='')\
           or board.s2c =='n'\
           :
            oute=1

    if board.s1f == 'K':
        if re.search(r'[plsgrk]|\+n|\+b',board.s1e)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s2e)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s2f)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s1g)\
           or re.search(r'[bk]',board.s2g)or board.s2g=='s'or board.s2g=='+r'\
           or (re.search('r',board.s1i) and board.s1g+board.s1h=='')\
           or (re.search('r',board.s1h) and board.s1g=='')\
           or ((re.search('r',board.s1d)or board.s1d=='l') and board.s1e=='')\
           or ((re.search('r',board.s1c)or board.s1c=='l') and board.s1e+board.s1d=='')\
           or ((re.search('r',board.s1b)or board.s1b=='l') and board.s1e+board.s1d+board.s1c=='')\
           or ((re.search('r',board.s1a)or board.s1a=='l') and board.s1e+board.s1d+board.s1c+board.s1b=='')\
           or (re.search('r',board.s3f) and board.s2f=='')\
           or (re.search('r',board.s4f) and board.s2f+board.s3f=='')\
           or (re.search('r',board.s5f) and board.s2f+board.s3f+board.s4f=='')\
           or (re.search('r',board.s6f) and board.s2f+board.s3f+board.s4f+board.s5f=='')\
           or (re.search('r',board.s7f) and board.s2f+board.s3f+board.s4f+board.s5f+board.s6f=='')\
           or (re.search('r',board.s8f) and board.s2f+board.s3f+board.s4f+board.s5f+board.s6f+board.s7f=='')\
           or (re.search('r',board.s9f) and board.s2f+board.s3f+board.s4f+board.s5f+board.s6f+board.s7f+board.s8f=='')\
           or (re.search('b',board.s4i) and board.s3h+board.s2g=='')\
           or (re.search('b',board.s3h) and board.s2g=='')\
           or (re.search('b',board.s3d) and board.s2e=='')\
           or (re.search('b',board.s4c) and board.s2e+board.s3d=='')\
           or (re.search('b',board.s5b) and board.s2e+board.s3d+board.s4c=='')\
           or (re.search('b',board.s6a) and board.s2e+board.s3d+board.s4c+board.s5b=='')\
           or board.s2d =='n'\
           :
            oute=1

    if board.s1g == 'K':
        if re.search(r'[plsgrk]|\+n|\+b',board.s1f)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s2f)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s2g)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s1h)\
           or re.search(r'[bk]',board.s2h)or board.s2h=='s'or board.s2h=='+r'\
           or (re.search('r',board.s1i) and board.s1h=='')\
           or ((re.search('r',board.s1e)or board.s1e=='l') and board.s1f=='')\
           or ((re.search('r',board.s1d)or board.s1d=='l') and board.s1f+board.s1e=='')\
           or ((re.search('r',board.s1c)or board.s1c=='l') and board.s1f+board.s1e+board.s1d=='')\
           or ((re.search('r',board.s1b)or board.s1b=='l') and board.s1f+board.s1e+board.s1d+board.s1c=='')\
           or ((re.search('r',board.s1a)or board.s1a=='l') and board.s1f+board.s1e+board.s1d+board.s1c+board.s1b=='')\
           or (re.search('r',board.s3g) and board.s2g=='')\
           or (re.search('r',board.s4g) and board.s2g+board.s3g=='')\
           or (re.search('r',board.s5g) and board.s2g+board.s3g+board.s4g=='')\
           or (re.search('r',board.s6g) and board.s2g+board.s3g+board.s4g+board.s5g=='')\
           or (re.search('r',board.s7g) and board.s2g+board.s3g+board.s4g+board.s5g+board.s6g=='')\
           or (re.search('r',board.s8g) and board.s2g+board.s3g+board.s4g+board.s5g+board.s6g+board.s7g=='')\
           or (re.search('r',board.s9g) and board.s2g+board.s3g+board.s4g+board.s5g+board.s6g+board.s7g+board.s8g=='')\
           or (re.search('b',board.s3i) and board.s2h=='')\
           or (re.search('b',board.s3e) and board.s2f=='')\
           or (re.search('b',board.s4d) and board.s2f+board.s3e=='')\
           or (re.search('b',board.s5c) and board.s2f+board.s3e+board.s4d=='')\
           or (re.search('b',board.s6b) and board.s2f+board.s3e+board.s4d+board.s5c=='')\
           or (re.search('b',board.s7a) and board.s2f+board.s3e+board.s4d+board.s5c+board.s6b=='')\
           or board.s2e =='n'\
           :
            oute=1

    if board.s1h == 'K':
        if re.search(r'[plsgrk]|\+n|\+b',board.s1g)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s2g)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s2h)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s1i)\
           or re.search(r'[bk]',board.s2i)or board.s2i=='s'or board.s2i=='+r'\
           or ((re.search('r',board.s1f)or board.s1f=='l') and board.s1g=='')\
           or ((re.search('r',board.s1e)or board.s1e=='l') and board.s1g+board.s1f=='')\
           or ((re.search('r',board.s1d)or board.s1d=='l') and board.s1g+board.s1f+board.s1e=='')\
           or ((re.search('r',board.s1c)or board.s1c=='l') and board.s1g+board.s1f+board.s1e+board.s1d=='')\
           or ((re.search('r',board.s1b)or board.s1b=='l') and board.s1g+board.s1f+board.s1e+board.s1d+board.s1c=='')\
           or ((re.search('r',board.s1a)or board.s1a=='l') and board.s1g+board.s1f+board.s1e+board.s1d+board.s1c+board.s1b=='')\
           or (re.search('r',board.s3h) and board.s2h=='')\
           or (re.search('r',board.s4h) and board.s2h+board.s3h=='')\
           or (re.search('r',board.s5h) and board.s2h+board.s3h+board.s4h=='')\
           or (re.search('r',board.s6h) and board.s2h+board.s3h+board.s4h+board.s5h=='')\
           or (re.search('r',board.s7h) and board.s2h+board.s3h+board.s4h+board.s5h+board.s6h=='')\
           or (re.search('r',board.s8h) and board.s2h+board.s3h+board.s4h+board.s5h+board.s6h+board.s7h=='')\
           or (re.search('r',board.s9h) and board.s2h+board.s3h+board.s4h+board.s5h+board.s6h+board.s7h+board.s8h=='')\
           or (re.search('b',board.s3f) and board.s2g=='')\
           or (re.search('b',board.s4e) and board.s2g+board.s3f=='')\
           or (re.search('b',board.s5d) and board.s2g+board.s3f+board.s4e=='')\
           or (re.search('b',board.s6c) and board.s2g+board.s3f+board.s4e+board.s5d=='')\
           or (re.search('b',board.s7b) and board.s2g+board.s3f+board.s4e+board.s5d+board.s6c=='')\
           or (re.search('b',board.s8a) and board.s2g+board.s3f+board.s4e+board.s5d+board.s6c+board.s7b=='')\
           or board.s2f =='n'\
           :
            oute=1

    if board.s1i == 'K':
        if re.search(r'[plsgrk]|\+n|\+b',board.s1h)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s2h)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s2i)\
           or ((re.search('r',board.s1g)or board.s1g=='l') and board.s1h=='')\
           or ((re.search('r',board.s1h)or board.s1f=='l') and board.s1h+board.s1g=='')\
           or ((re.search('r',board.s1e)or board.s1e=='l') and board.s1h+board.s1g+board.s1f=='')\
           or ((re.search('r',board.s1d)or board.s1d=='l') and board.s1h+board.s1g+board.s1f+board.s1e=='')\
           or ((re.search('r',board.s1c)or board.s1c=='l') and board.s1h+board.s1g+board.s1f+board.s1e+board.s1d=='')\
           or ((re.search('r',board.s1b)or board.s1b=='l') and board.s1h+board.s1g+board.s1f+board.s1e+board.s1d+board.s1c=='')\
           or ((re.search('r',board.s1a)or board.s1a=='l') and board.s1h+board.s1g+board.s1f+board.s1e+board.s1d+board.s1c+board.s1b=='')\
           or (re.search('r',board.s3i) and board.s2i=='')\
           or (re.search('r',board.s4i) and board.s2i+board.s3i=='')\
           or (re.search('r',board.s5i) and board.s2i+board.s3i+board.s4i=='')\
           or (re.search('r',board.s6i) and board.s2i+board.s3i+board.s4i+board.s5i=='')\
           or (re.search('r',board.s7i) and board.s2i+board.s3i+board.s4i+board.s5i+board.s6i=='')\
           or (re.search('r',board.s8i) and board.s2i+board.s3i+board.s4i+board.s5i+board.s6i+board.s7i=='')\
           or (re.search('r',board.s9i) and board.s2i+board.s3i+board.s4i+board.s5i+board.s6i+board.s7i+board.s8i=='')\
           or (re.search('b',board.s3g) and board.s2h=='')\
           or (re.search('b',board.s4f) and board.s2h+board.s3g=='')\
           or (re.search('b',board.s5e) and board.s2h+board.s3g+board.s4f=='')\
           or (re.search('b',board.s6d) and board.s2h+board.s3g+board.s4f+board.s5e=='')\
           or (re.search('b',board.s7c) and board.s2h+board.s3g+board.s4f+board.s5e+board.s6d=='')\
           or (re.search('b',board.s8b) and board.s2h+board.s3g+board.s4f+board.s5e+board.s6d+board.s7c=='')\
           or (re.search('b',board.s9a) and board.s2h+board.s3g+board.s4f+board.s5e+board.s6d+board.s7c+board.s8b=='')\
           or board.s2g =='n'\
           :
            oute=1

    if board.s2a == 'K':
        if re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s1a)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s3a)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s2b)\
           or re.search(r'[bk]',board.s1b)or board.s1b=='s'or board.s1b=='+r'\
           or re.search(r'[bk]',board.s3b)or board.s3b=='s'or board.s3b=='+r'\
           or (re.search('r',board.s2c) and board.s2b=='')\
           or (re.search('r',board.s2d) and board.s2b+board.s2c=='')\
           or (re.search('r',board.s2e) and board.s2b+board.s2c+board.s2d=='')\
           or (re.search('r',board.s2f) and board.s2b+board.s2c+board.s2d+board.s2e=='')\
           or (re.search('r',board.s2g) and board.s2b+board.s2c+board.s2d+board.s2e+board.s2f=='')\
           or (re.search('r',board.s2h) and board.s2b+board.s2c+board.s2d+board.s2e+board.s2f+board.s2g=='')\
           or (re.search('r',board.s2i) and board.s2b+board.s2c+board.s2d+board.s2e+board.s2f+board.s2g+board.s2h=='')\
           or (re.search('r',board.s4a) and board.s3a=='')\
           or (re.search('r',board.s5a) and board.s3a+board.s4a=='')\
           or (re.search('r',board.s6a) and board.s3a+board.s4a+board.s5a=='')\
           or (re.search('r',board.s7a) and board.s3a+board.s4a+board.s5a+board.s6a=='')\
           or (re.search('r',board.s8a) and board.s3a+board.s4a+board.s5a+board.s6a+board.s7a=='')\
           or (re.search('r',board.s9a) and board.s3a+board.s4a+board.s5a+board.s6a+board.s7a+board.s8a=='')\
           or (re.search('b',board.s4c) and board.s3b=='')\
           or (re.search('b',board.s5d) and board.s3b+board.s4c=='')\
           or (re.search('b',board.s6e) and board.s3b+board.s4c+board.s5d=='')\
           or (re.search('b',board.s7f) and board.s3b+board.s4c+board.s5d+board.s6e=='')\
           or (re.search('b',board.s8g) and board.s3b+board.s4c+board.s5d+board.s6e+board.s7f=='')\
           or (re.search('b',board.s9h) and board.s3b+board.s4c+board.s5d+board.s6e+board.s7f+board.s8g=='')\
           :
            oute=1

    if board.s2b == 'K':
        if re.search(r'[plsgrk]|\+n|\+b',board.s2a)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s1a)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s3a)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s1b)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s3b)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s2c)\
           or re.search(r'[bk]',board.s1c)or board.s1c=='s'or board.s1c=='+r'\
           or re.search(r'[bk]',board.s3c)or board.s3c=='s'or board.s3c=='+r'\
           or (re.search('r',board.s2d) and board.s2c=='')\
           or (re.search('r',board.s2e) and board.s2c+board.s2d=='')\
           or (re.search('r',board.s2f) and board.s2c+board.s2d+board.s2e=='')\
           or (re.search('r',board.s2g) and board.s2c+board.s2d+board.s2e+board.s2f=='')\
           or (re.search('r',board.s2h) and board.s2c+board.s2d+board.s2e+board.s2f+board.s2g=='')\
           or (re.search('r',board.s2i) and board.s2c+board.s2d+board.s2e+board.s2f+board.s2g+board.s2h=='')\
           or (re.search('r',board.s4b) and board.s3b=='')\
           or (re.search('r',board.s5b) and board.s3b+board.s4b=='')\
           or (re.search('r',board.s6b) and board.s3b+board.s4b+board.s5b=='')\
           or (re.search('r',board.s7b) and board.s3b+board.s4b+board.s5b+board.s6b=='')\
           or (re.search('r',board.s8b) and board.s3b+board.s4b+board.s5b+board.s6b+board.s7b=='')\
           or (re.search('r',board.s9b) and board.s3b+board.s4b+board.s5b+board.s6b+board.s7b+board.s8b=='')\
           or (re.search('b',board.s4d) and board.s3c=='')\
           or (re.search('b',board.s5e) and board.s3c+board.s4d=='')\
           or (re.search('b',board.s6f) and board.s3c+board.s4d+board.s5e=='')\
           or (re.search('b',board.s7g) and board.s3c+board.s4d+board.s5e+board.s6f=='')\
           or (re.search('b',board.s8h) and board.s3c+board.s4d+board.s5e+board.s6f+board.s7g=='')\
           or (re.search('b',board.s9i) and board.s3c+board.s4d+board.s5e+board.s6f+board.s7g+board.s8h=='')\
           :
            oute=1

    if board.s2c == 'K':
        if re.search(r'[plsgrk]|\+n|\+b',board.s2b)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s1b)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s3b)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s1c)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s3c)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s2d)\
           or re.search(r'[bk]',board.s1d)or board.s1d=='s'or board.s1d=='+r'\
           or re.search(r'[bk]',board.s3d)or board.s3d=='s'or board.s3d=='+r'\
           or ((re.search('r',board.s2a)or board.s2a=='l') and board.s2b=='')\
           or (re.search('r',board.s2e) and board.s2d=='')\
           or (re.search('r',board.s2f) and board.s2d+board.s2e=='')\
           or (re.search('r',board.s2g) and board.s2d+board.s2e+board.s2f=='')\
           or (re.search('r',board.s2h) and board.s2d+board.s2e+board.s2f+board.s2g=='')\
           or (re.search('r',board.s2i) and board.s2d+board.s2e+board.s2f+board.s2g+board.s2h=='')\
           or (re.search('r',board.s4c) and board.s3c=='')\
           or (re.search('r',board.s5c) and board.s3c+board.s4c=='')\
           or (re.search('r',board.s6c) and board.s3c+board.s4c+board.s5c=='')\
           or (re.search('r',board.s7c) and board.s3c+board.s4c+board.s5c+board.s6c=='')\
           or (re.search('r',board.s8c) and board.s3c+board.s4c+board.s5c+board.s6c+board.s7c=='')\
           or (re.search('r',board.s9c) and board.s3c+board.s4c+board.s5c+board.s6c+board.s7c+board.s8c=='')\
           or (re.search('b',board.s4a) and board.s3b=='')\
           or (re.search('b',board.s4e) and board.s3d=='')\
           or (re.search('b',board.s5f) and board.s3d+board.s4e=='')\
           or (re.search('b',board.s6g) and board.s3d+board.s4e+board.s5f=='')\
           or (re.search('b',board.s7h) and board.s3d+board.s4e+board.s5f+board.s6g=='')\
           or (re.search('b',board.s8i) and board.s3d+board.s4e+board.s5f+board.s6g+board.s7h=='')\
           or board.s1a =='n'or board.s3a =='n'\
           :
            oute=1

    if board.s2d == 'K':
        if re.search(r'[plsgrk]|\+n|\+b',board.s2c)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s1c)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s3c)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s1d)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s3d)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s2e)\
           or re.search(r'[bk]',board.s1e)or board.s1e=='s'or board.s1e=='+r'\
           or re.search(r'[bk]',board.s3e)or board.s3e=='s'or board.s3e=='+r'\
           or ((re.search('r',board.s2a)or board.s2a=='l') and board.s2b+board.s2c=='')\
           or ((re.search('r',board.s2b)or board.s2b=='l') and board.s2c=='')\
           or (re.search('r',board.s2f) and board.s2e=='')\
           or (re.search('r',board.s2g) and board.s2e+board.s2f=='')\
           or (re.search('r',board.s2h) and board.s2e+board.s2f+board.s2g=='')\
           or (re.search('r',board.s2i) and board.s2e+board.s2f+board.s2g+board.s2h=='')\
           or (re.search('r',board.s4d) and board.s3d=='')\
           or (re.search('r',board.s5d) and board.s3d+board.s4d=='')\
           or (re.search('r',board.s6d) and board.s3d+board.s4d+board.s5d=='')\
           or (re.search('r',board.s7d) and board.s3d+board.s4d+board.s5d+board.s6d=='')\
           or (re.search('r',board.s8d) and board.s3d+board.s4d+board.s5d+board.s6d+board.s7d=='')\
           or (re.search('r',board.s9d) and board.s3d+board.s4d+board.s5d+board.s6d+board.s7d+board.s8d=='')\
           or (re.search('b',board.s5a) and board.s4b+board.s3c=='')\
           or (re.search('b',board.s4b) and board.s3c=='')\
           or (re.search('b',board.s4f) and board.s3e=='')\
           or (re.search('b',board.s5g) and board.s3e+board.s4f=='')\
           or (re.search('b',board.s6h) and board.s3e+board.s4f+board.s5g=='')\
           or (re.search('b',board.s7i) and board.s3e+board.s4f+board.s5g+board.s6h=='')\
           or board.s1b =='n'or board.s3b =='n'\
           :
            oute=1

    if board.s2e == 'K':
        if re.search(r'[plsgrk]|\+n|\+b',board.s2d)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s1d)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s3d)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s1e)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s3e)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s2f)\
           or re.search(r'[bk]',board.s1f)or board.s1f=='s'or board.s1f=='+r'\
           or re.search(r'[bk]',board.s3f)or board.s3f=='s'or board.s3f=='+r'\
           or ((re.search('r',board.s2a)or board.s2a=='l') and board.s2b+board.s2c+board.s2d=='')\
           or ((re.search('r',board.s2b)or board.s2b=='l') and board.s2c+board.s2d=='')\
           or ((re.search('r',board.s2c)or board.s2c=='l') and board.s2d=='')\
           or (re.search('r',board.s2g) and board.s2e=='')\
           or (re.search('r',board.s2h) and board.s2e+board.s2f=='')\
           or (re.search('r',board.s2i) and board.s2e+board.s2f+board.s2g=='')\
           or (re.search('r',board.s4e) and board.s3e=='')\
           or (re.search('r',board.s5e) and board.s3e+board.s4e=='')\
           or (re.search('r',board.s6e) and board.s3e+board.s4e+board.s5e=='')\
           or (re.search('r',board.s7e) and board.s3e+board.s4e+board.s5e+board.s6e=='')\
           or (re.search('r',board.s8e) and board.s3e+board.s4e+board.s5e+board.s6e+board.s7e=='')\
           or (re.search('r',board.s9e) and board.s3e+board.s4e+board.s5e+board.s6e+board.s7e+board.s8e=='')\
           or (re.search('b',board.s6a) and board.s5b+board.s4c+board.s3d=='')\
           or (re.search('b',board.s5b) and board.s4c+board.s3d=='')\
           or (re.search('b',board.s4c) and board.s3d=='')\
           or (re.search('b',board.s4g) and board.s3f=='')\
           or (re.search('b',board.s5h) and board.s3f+board.s4g=='')\
           or (re.search('b',board.s6i) and board.s3f+board.s4g+board.s5h=='')\
           or board.s1c =='n'or board.s3c =='n'\
           :
            oute=1

    if board.s2f == 'K':
        if re.search(r'[plsgrk]|\+n|\+b',board.s2e)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s1e)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s3e)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s1f)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s3f)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s2g)\
           or re.search(r'[bk]',board.s1g)or board.s1g=='s'or board.s1g=='+r'\
           or re.search(r'[bk]',board.s3g)or board.s3g=='s'or board.s3g=='+r'\
           or (re.search('r',board.s2i) and board.s2g+board.s2h=='')\
           or (re.search('r',board.s2h) and board.s2g=='')\
           or ((re.search('r',board.s2d)or board.s2d=='l') and board.s2e=='')\
           or ((re.search('r',board.s2c)or board.s2c=='l') and board.s2e+board.s2d=='')\
           or ((re.search('r',board.s2b)or board.s2b=='l') and board.s2e+board.s2d+board.s2c=='')\
           or ((re.search('r',board.s2a)or board.s2a=='l') and board.s2e+board.s2d+board.s2c+board.s2b=='')\
           or (re.search('r',board.s4f) and board.s3f=='')\
           or (re.search('r',board.s5f) and board.s3f+board.s4f=='')\
           or (re.search('r',board.s6f) and board.s3f+board.s4f+board.s5f=='')\
           or (re.search('r',board.s7f) and board.s3f+board.s4f+board.s5f+board.s6f=='')\
           or (re.search('r',board.s8f) and board.s3f+board.s4f+board.s5f+board.s6f+board.s7f=='')\
           or (re.search('r',board.s9f) and board.s3f+board.s4f+board.s5f+board.s6f+board.s7f+board.s8f=='')\
           or (re.search('b',board.s5i) and board.s4h+board.s3g=='')\
           or (re.search('b',board.s4h) and board.s3g=='')\
           or (re.search('b',board.s4d) and board.s3e=='')\
           or (re.search('b',board.s5c) and board.s3e+board.s4d=='')\
           or (re.search('b',board.s6b) and board.s3e+board.s4d+board.s5c=='')\
           or (re.search('b',board.s7a) and board.s3e+board.s4d+board.s5c+board.s6b=='')\
           or board.s1d =='n'or board.s3d =='n'\
           :
            oute=1

    if board.s2g == 'K':
        if re.search(r'[plsgrk]|\+n|\+b',board.s2f)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s1f)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s3f)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s1g)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s3g)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s2h)\
           or re.search(r'[bk]',board.s1h)or board.s1h=='s'or board.s1h=='+r'\
           or re.search(r'[bk]',board.s3h)or board.s3h=='s'or board.s3h=='+r'\
           or (re.search('r',board.s2i) and board.s2h=='')\
           or ((re.search('r',board.s2e)or board.s2e=='l') and board.s2f=='')\
           or ((re.search('r',board.s2d)or board.s2d=='l') and board.s2f+board.s2e=='')\
           or ((re.search('r',board.s2c)or board.s2c=='l') and board.s2f+board.s2e+board.s2d=='')\
           or ((re.search('r',board.s2b)or board.s2b=='l') and board.s2f+board.s2e+board.s2d+board.s2c=='')\
           or ((re.search('r',board.s2a)or board.s2a=='l') and board.s2f+board.s2e+board.s2d+board.s2c+board.s2b=='')\
           or (re.search('r',board.s4g) and board.s3g=='')\
           or (re.search('r',board.s5g) and board.s3g+board.s4g=='')\
           or (re.search('r',board.s6g) and board.s3g+board.s4g+board.s5g=='')\
           or (re.search('r',board.s7g) and board.s3g+board.s4g+board.s5g+board.s6g=='')\
           or (re.search('r',board.s8g) and board.s3g+board.s4g+board.s5g+board.s6g+board.s7g=='')\
           or (re.search('r',board.s9g) and board.s3g+board.s4g+board.s5g+board.s6g+board.s7g+board.s8g=='')\
           or (re.search('b',board.s4i) and board.s3h=='')\
           or (re.search('b',board.s4e) and board.s3f=='')\
           or (re.search('b',board.s5d) and board.s3f+board.s4e=='')\
           or (re.search('b',board.s6c) and board.s3f+board.s4e+board.s5d=='')\
           or (re.search('b',board.s7b) and board.s3f+board.s4e+board.s5d+board.s6c=='')\
           or (re.search('b',board.s8a) and board.s3f+board.s4e+board.s5d+board.s6c+board.s7b=='')\
           or board.s1e =='n'or board.s3e =='n'\
           :
            oute=1

    if board.s2h == 'K':
        if re.search(r'[plsgrk]|\+n|\+b',board.s2g)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s1g)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s3g)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s1h)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s3h)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s2i)\
           or re.search(r'[bk]',board.s1i)or board.s1i=='s'or board.s1i=='+r'\
           or re.search(r'[bk]',board.s3i)or board.s3i=='s'or board.s3i=='+r'\
           or ((re.search('r',board.s2f)or board.s2f=='l') and board.s2g=='')\
           or ((re.search('r',board.s2e)or board.s2e=='l') and board.s2g+board.s2f=='')\
           or ((re.search('r',board.s2d)or board.s2d=='l') and board.s2g+board.s2f+board.s2e=='')\
           or ((re.search('r',board.s2c)or board.s2c=='l') and board.s2g+board.s2f+board.s2e+board.s2d=='')\
           or ((re.search('r',board.s2b)or board.s2b=='l') and board.s2g+board.s2f+board.s2e+board.s2d+board.s2c=='')\
           or ((re.search('r',board.s2a)or board.s2a=='l') and board.s2g+board.s2f+board.s2e+board.s2d+board.s2c+board.s2b=='')\
           or (re.search('r',board.s4h) and board.s3h=='')\
           or (re.search('r',board.s5h) and board.s3h+board.s4h=='')\
           or (re.search('r',board.s6h) and board.s3h+board.s4h+board.s5h=='')\
           or (re.search('r',board.s7h) and board.s3h+board.s4h+board.s5h+board.s6h=='')\
           or (re.search('r',board.s8h) and board.s3h+board.s4h+board.s5h+board.s6h+board.s7h=='')\
           or (re.search('r',board.s9h) and board.s3h+board.s4h+board.s5h+board.s6h+board.s7h+board.s8h=='')\
           or (re.search('b',board.s4f) and board.s3g=='')\
           or (re.search('b',board.s5e) and board.s3g+board.s4f=='')\
           or (re.search('b',board.s6d) and board.s3g+board.s4f+board.s5e=='')\
           or (re.search('b',board.s7c) and board.s3g+board.s4f+board.s5e+board.s6d=='')\
           or (re.search('b',board.s8b) and board.s3g+board.s4f+board.s5e+board.s6d+board.s7c=='')\
           or (re.search('b',board.s9a) and board.s3g+board.s4f+board.s5e+board.s6d+board.s7c+board.s8b=='')\
           or board.s1f =='n'or board.s3f =='n'\
           :
            oute=1

    if board.s2i == 'K':
        if re.search(r'[plsgrk]|\+n|\+b',board.s2h)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s1h)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s3h)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s1i)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s3i)\
           or ((re.search('r',board.s2g)or board.s2g=='l') and board.s2h=='')\
           or ((re.search('r',board.s2h)or board.s2f=='l') and board.s2h+board.s2g=='')\
           or ((re.search('r',board.s2e)or board.s2e=='l') and board.s2h+board.s2g+board.s2f=='')\
           or ((re.search('r',board.s2d)or board.s2d=='l') and board.s2h+board.s2g+board.s2f+board.s2e=='')\
           or ((re.search('r',board.s2c)or board.s2c=='l') and board.s2h+board.s2g+board.s2f+board.s2e+board.s2d=='')\
           or ((re.search('r',board.s2b)or board.s2b=='l') and board.s2h+board.s2g+board.s2f+board.s2e+board.s2d+board.s2c=='')\
           or ((re.search('r',board.s2a)or board.s2a=='l') and board.s2h+board.s2g+board.s2f+board.s2e+board.s2d+board.s2c+board.s2b=='')\
           or (re.search('r',board.s4i) and board.s3i=='')\
           or (re.search('r',board.s5i) and board.s3i+board.s4i=='')\
           or (re.search('r',board.s6i) and board.s3i+board.s4i+board.s5i=='')\
           or (re.search('r',board.s7i) and board.s3i+board.s4i+board.s5i+board.s6i=='')\
           or (re.search('r',board.s8i) and board.s3i+board.s4i+board.s5i+board.s6i+board.s7i=='')\
           or (re.search('r',board.s9i) and board.s3i+board.s4i+board.s5i+board.s6i+board.s7i+board.s8i=='')\
           or (re.search('b',board.s4g) and board.s3h=='')\
           or (re.search('b',board.s5f) and board.s3h+board.s4g=='')\
           or (re.search('b',board.s6e) and board.s3h+board.s4g+board.s5f=='')\
           or (re.search('b',board.s7d) and board.s3h+board.s4g+board.s5f+board.s6e=='')\
           or (re.search('b',board.s8c) and board.s3h+board.s4g+board.s5f+board.s6e+board.s7d=='')\
           or (re.search('b',board.s9b) and board.s3h+board.s4g+board.s5f+board.s6e+board.s7d+board.s8c=='')\
           or board.s2g =='n'\
           :
            oute=1

    if board.s3a == 'K':
        if re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s2a)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s4a)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s3b)\
           or re.search(r'[bk]',board.s2b)or board.s2b=='s'or board.s2b=='+r'\
           or re.search(r'[bk]',board.s4b)or board.s4b=='s'or board.s4b=='+r'\
           or (re.search('r',board.s3c) and board.s3b=='')\
           or (re.search('r',board.s3d) and board.s3b+board.s3c=='')\
           or (re.search('r',board.s3e) and board.s3b+board.s3c+board.s3d=='')\
           or (re.search('r',board.s3f) and board.s3b+board.s3c+board.s3d+board.s3e=='')\
           or (re.search('r',board.s3g) and board.s3b+board.s3c+board.s3d+board.s3e+board.s3f=='')\
           or (re.search('r',board.s3h) and board.s3b+board.s3c+board.s3d+board.s3e+board.s3f+board.s3g=='')\
           or (re.search('r',board.s3i) and board.s3b+board.s3c+board.s3d+board.s3e+board.s3f+board.s3g+board.s3h=='')\
           or (re.search('r',board.s1a) and board.s2a=='')\
           or (re.search('r',board.s5a) and board.s4a=='')\
           or (re.search('r',board.s6a) and board.s4a+board.s5a=='')\
           or (re.search('r',board.s7a) and board.s4a+board.s5a+board.s6a=='')\
           or (re.search('r',board.s8a) and board.s4a+board.s5a+board.s6a+board.s7a=='')\
           or (re.search('r',board.s9a) and board.s4a+board.s5a+board.s6a+board.s7a+board.s8a=='')\
           or (re.search('b',board.s1c) and board.s2b=='')\
           or (re.search('b',board.s5c) and board.s4b=='')\
           or (re.search('b',board.s6d) and board.s4b+board.s5c=='')\
           or (re.search('b',board.s7e) and board.s4b+board.s5c+board.s6d=='')\
           or (re.search('b',board.s8f) and board.s4b+board.s5c+board.s6d+board.s7e=='')\
           or (re.search('b',board.s9g) and board.s4b+board.s5c+board.s6d+board.s7e+board.s8f=='')\
           :
            oute=1

    if board.s3b == 'K':
        if re.search(r'[plsgrk]|\+n|\+b',board.s3a)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s2a)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s4a)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s2b)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s4b)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s3c)\
           or re.search(r'[bk]',board.s2c)or board.s2c=='s'or board.s2c=='+r'\
           or re.search(r'[bk]',board.s4c)or board.s4c=='s'or board.s4c=='+r'\
           or (re.search('r',board.s3d) and board.s3c=='')\
           or (re.search('r',board.s3e) and board.s3c+board.s3d=='')\
           or (re.search('r',board.s3f) and board.s3c+board.s3d+board.s3e=='')\
           or (re.search('r',board.s3g) and board.s3c+board.s3d+board.s3e+board.s3f=='')\
           or (re.search('r',board.s3h) and board.s3c+board.s3d+board.s3e+board.s3f+board.s3g=='')\
           or (re.search('r',board.s3i) and board.s3c+board.s3d+board.s3e+board.s3f+board.s3g+board.s3h=='')\
           or (re.search('r',board.s1b) and board.s2b=='')\
           or (re.search('r',board.s5b) and board.s4b=='')\
           or (re.search('r',board.s6b) and board.s4b+board.s5b=='')\
           or (re.search('r',board.s7b) and board.s4b+board.s5b+board.s6b=='')\
           or (re.search('r',board.s8b) and board.s4b+board.s5b+board.s6b+board.s7b=='')\
           or (re.search('r',board.s9b) and board.s4b+board.s5b+board.s6b+board.s7b+board.s8b=='')\
           or (re.search('b',board.s1d) and board.s2c=='')\
           or (re.search('b',board.s5d) and board.s4c=='')\
           or (re.search('b',board.s6e) and board.s4c+board.s5d=='')\
           or (re.search('b',board.s7f) and board.s4c+board.s5d+board.s6e=='')\
           or (re.search('b',board.s8g) and board.s4c+board.s5d+board.s6e+board.s7f=='')\
           or (re.search('b',board.s9h) and board.s4c+board.s5d+board.s6e+board.s7f+board.s8g=='')\
           :
            oute=1

    if board.s3c == 'K':
        if re.search(r'[plsgrk]|\+n|\+b',board.s3b)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s2b)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s4b)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s2c)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s4c)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s3d)\
           or re.search(r'[bk]',board.s2d)or board.s2d=='s'or board.s2d=='+r'\
           or re.search(r'[bk]',board.s4d)or board.s4d=='s'or board.s4d=='+r'\
           or ((re.search('r',board.s3a)or board.s3a=='l') and board.s3b=='')\
           or (re.search('r',board.s3e) and board.s3d=='')\
           or (re.search('r',board.s3f) and board.s3d+board.s3e=='')\
           or (re.search('r',board.s3g) and board.s3d+board.s3e+board.s3f=='')\
           or (re.search('r',board.s3h) and board.s3d+board.s3e+board.s3f+board.s3g=='')\
           or (re.search('r',board.s3i) and board.s3d+board.s3e+board.s3f+board.s3g+board.s3h=='')\
           or (re.search('r',board.s1c) and board.s2c=='')\
           or (re.search('r',board.s5c) and board.s4c=='')\
           or (re.search('r',board.s6c) and board.s4c+board.s5c=='')\
           or (re.search('r',board.s7c) and board.s4c+board.s5c+board.s6c=='')\
           or (re.search('r',board.s8c) and board.s4c+board.s5c+board.s6c+board.s7c=='')\
           or (re.search('r',board.s9c) and board.s4c+board.s5c+board.s6c+board.s7c+board.s8c=='')\
           or (re.search('b',board.s1a) and board.s2b=='')\
           or (re.search('b',board.s1e) and board.s2d=='')\
           or (re.search('b',board.s5a) and board.s4b=='')\
           or (re.search('b',board.s5e) and board.s4d=='')\
           or (re.search('b',board.s6f) and board.s4d+board.s5e=='')\
           or (re.search('b',board.s7g) and board.s4d+board.s5e+board.s6f=='')\
           or (re.search('b',board.s8h) and board.s4d+board.s5e+board.s6f+board.s7g=='')\
           or (re.search('b',board.s9i) and board.s4d+board.s5e+board.s6f+board.s7g+board.s8h=='')\
           or board.s2a =='n'or board.s4a =='n'\
           :
            oute=1


    if board.s3d == 'K':
        if re.search(r'[plsgrk]|\+n|\+b',board.s3c)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s2c)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s4c)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s2d)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s4d)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s3e)\
           or re.search(r'[bk]',board.s2e)or board.s2e=='s'or board.s2e=='+r'\
           or re.search(r'[bk]',board.s4e)or board.s4e=='s'or board.s4e=='+r'\
           or ((re.search('r',board.s3a)or board.s3a=='l') and board.s3b+board.s3c=='')\
           or ((re.search('r',board.s3b)or board.s3b=='l') and board.s3c=='')\
           or (re.search('r',board.s3f) and board.s3e=='')\
           or (re.search('r',board.s3g) and board.s3e+board.s3f=='')\
           or (re.search('r',board.s3h) and board.s3e+board.s3f+board.s3g=='')\
           or (re.search('r',board.s3i) and board.s3e+board.s3f+board.s3g+board.s3h=='')\
           or (re.search('r',board.s1d) and board.s2d=='')\
           or (re.search('r',board.s5d) and board.s4d=='')\
           or (re.search('r',board.s6d) and board.s4d+board.s5d=='')\
           or (re.search('r',board.s7d) and board.s4d+board.s5d+board.s6d=='')\
           or (re.search('r',board.s8d) and board.s4d+board.s5d+board.s6d+board.s7d=='')\
           or (re.search('r',board.s9d) and board.s4d+board.s5d+board.s6d+board.s7d+board.s8d=='')\
           or (re.search('b',board.s1b) and board.s2c=='')\
           or (re.search('b',board.s1f) and board.s2e=='')\
           or (re.search('b',board.s6a) and board.s5b+board.s4c=='')\
           or (re.search('b',board.s5b) and board.s4c=='')\
           or (re.search('b',board.s5f) and board.s4e=='')\
           or (re.search('b',board.s6g) and board.s4e+board.s5f=='')\
           or (re.search('b',board.s7h) and board.s4e+board.s5f+board.s6g=='')\
           or (re.search('b',board.s8i) and board.s4e+board.s5f+board.s6g+board.s7h=='')\
           or board.s2b =='n'or board.s4b =='n'\
           :
            oute=1

    if board.s3e == 'K':
        if re.search(r'[plsgrk]|\+n|\+b',board.s3d)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s2d)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s4d)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s2e)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s4e)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s3f)\
           or re.search(r'[bk]',board.s2f)or board.s2f=='s'or board.s2f=='+r'\
           or re.search(r'[bk]',board.s4f)or board.s4f=='s'or board.s4f=='+r'\
           or ((re.search('r',board.s3a)or board.s3a=='l') and board.s3b+board.s3c+board.s3d=='')\
           or ((re.search('r',board.s3b)or board.s3b=='l') and board.s3c+board.s3d=='')\
           or ((re.search('r',board.s3c)or board.s3c=='l') and board.s3d=='')\
           or (re.search('r',board.s3g) and board.s3e=='')\
           or (re.search('r',board.s3h) and board.s3e+board.s3f=='')\
           or (re.search('r',board.s3i) and board.s3e+board.s3f+board.s3g=='')\
           or (re.search('r',board.s1e) and board.s2e=='')\
           or (re.search('r',board.s5e) and board.s4e=='')\
           or (re.search('r',board.s6e) and board.s4e+board.s5e=='')\
           or (re.search('r',board.s7e) and board.s4e+board.s5e+board.s6e=='')\
           or (re.search('r',board.s8e) and board.s4e+board.s5e+board.s6e+board.s7e=='')\
           or (re.search('r',board.s9e) and board.s4e+board.s5e+board.s6e+board.s7e+board.s8e=='')\
           or (re.search('b',board.s1c) and board.s2d=='')\
           or (re.search('b',board.s1g) and board.s2f=='')\
           or (re.search('b',board.s7a) and board.s6b+board.s5c+board.s4d=='')\
           or (re.search('b',board.s6b) and board.s5c+board.s4d=='')\
           or (re.search('b',board.s5c) and board.s4d=='')\
           or (re.search('b',board.s5g) and board.s4f=='')\
           or (re.search('b',board.s6h) and board.s4f+board.s5g=='')\
           or (re.search('b',board.s7i) and board.s4f+board.s5g+board.s6h=='')\
           or board.s2c =='n'or board.s4c =='n'\
           :
            oute=1

    if board.s3f == 'K':
        if re.search(r'[plsgrk]|\+n|\+b',board.s3e)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s2e)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s4e)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s2f)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s4f)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s3g)\
           or re.search(r'[bk]',board.s2g)or board.s2g=='s'or board.s2g=='+r'\
           or re.search(r'[bk]',board.s4g)or board.s4g=='s'or board.s4g=='+r'\
           or (re.search('r',board.s3i) and board.s3g+board.s3h=='')\
           or (re.search('r',board.s3h) and board.s3g=='')\
           or ((re.search('r',board.s3d)or board.s3d=='l') and board.s3e=='')\
           or ((re.search('r',board.s3c)or board.s3c=='l') and board.s3e+board.s3d=='')\
           or ((re.search('r',board.s3b)or board.s3b=='l') and board.s3e+board.s3d+board.s3c=='')\
           or ((re.search('r',board.s3a)or board.s3a=='l') and board.s3e+board.s3d+board.s3c+board.s3b=='')\
           or (re.search('r',board.s1f) and board.s2f=='')\
           or (re.search('r',board.s5f) and board.s4f=='')\
           or (re.search('r',board.s6f) and board.s4f+board.s5f=='')\
           or (re.search('r',board.s7f) and board.s4f+board.s5f+board.s6f=='')\
           or (re.search('r',board.s8f) and board.s4f+board.s5f+board.s6f+board.s7f=='')\
           or (re.search('r',board.s9f) and board.s4f+board.s5f+board.s6f+board.s7f+board.s8f=='')\
           or (re.search('b',board.s1d) and board.s2e=='')\
           or (re.search('b',board.s1h) and board.s2g=='')\
           or (re.search('b',board.s6i) and board.s5h+board.s4g=='')\
           or (re.search('b',board.s5h) and board.s4g=='')\
           or (re.search('b',board.s5d) and board.s4e=='')\
           or (re.search('b',board.s6c) and board.s4e+board.s5d=='')\
           or (re.search('b',board.s7b) and board.s4e+board.s5d+board.s6c=='')\
           or (re.search('b',board.s8a) and board.s4e+board.s5d+board.s6c+board.s7b=='')\
           or board.s2d =='n'or board.s4d =='n'\
           :
            oute=1

    if board.s3g == 'K':
        if re.search(r'[plsgrk]|\+n|\+b',board.s3f)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s2f)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s4f)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s2g)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s4g)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s3h)\
           or re.search(r'[bk]',board.s2h)or board.s2h=='s'or board.s2h=='+r'\
           or re.search(r'[bk]',board.s4h)or board.s4h=='s'or board.s4h=='+r'\
           or (re.search('r',board.s3i) and board.s3h=='')\
           or ((re.search('r',board.s3e)or board.s3e=='l') and board.s3f=='')\
           or ((re.search('r',board.s3d)or board.s3d=='l') and board.s3f+board.s3e=='')\
           or ((re.search('r',board.s3c)or board.s3c=='l') and board.s3f+board.s3e+board.s3d=='')\
           or ((re.search('r',board.s3b)or board.s3b=='l') and board.s3f+board.s3e+board.s3d+board.s3c=='')\
           or ((re.search('r',board.s3a)or board.s3a=='l') and board.s3f+board.s3e+board.s3d+board.s3c+board.s3b=='')\
           or (re.search('r',board.s1g) and board.s2g=='')\
           or (re.search('r',board.s5g) and board.s4g=='')\
           or (re.search('r',board.s6g) and board.s4g+board.s5g=='')\
           or (re.search('r',board.s7g) and board.s4g+board.s5g+board.s6g=='')\
           or (re.search('r',board.s8g) and board.s4g+board.s5g+board.s6g+board.s7g=='')\
           or (re.search('r',board.s9g) and board.s4g+board.s5g+board.s6g+board.s7g+board.s8g=='')\
           or (re.search('b',board.s1e) and board.s2f=='')\
           or (re.search('b',board.s1i) and board.s2h=='')\
           or (re.search('b',board.s5i) and board.s4h=='')\
           or (re.search('b',board.s5e) and board.s4f=='')\
           or (re.search('b',board.s6d) and board.s4f+board.s5e=='')\
           or (re.search('b',board.s7c) and board.s4f+board.s5e+board.s6d=='')\
           or (re.search('b',board.s8b) and board.s4f+board.s5e+board.s6d+board.s7c=='')\
           or (re.search('b',board.s9a) and board.s4f+board.s5e+board.s6d+board.s7c+board.s8b=='')\
           or board.s2e =='n'or board.s4e =='n'\
           :
            oute=1

    if board.s3h == 'K':
        if re.search(r'[plsgrk]|\+n|\+b',board.s3g)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s2g)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s4g)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s2h)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s4h)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s3i)\
           or re.search(r'[bk]',board.s2i)or board.s2i=='s'or board.s2i=='+r'\
           or re.search(r'[bk]',board.s4i)or board.s4i=='s'or board.s4i=='+r'\
           or ((re.search('r',board.s3f)or board.s3f=='l') and board.s3g=='')\
           or ((re.search('r',board.s3e)or board.s3e=='l') and board.s3g+board.s3f=='')\
           or ((re.search('r',board.s3d)or board.s3d=='l') and board.s3g+board.s3f+board.s3e=='')\
           or ((re.search('r',board.s3c)or board.s3c=='l') and board.s3g+board.s3f+board.s3e+board.s3d=='')\
           or ((re.search('r',board.s3b)or board.s3b=='l') and board.s3g+board.s3f+board.s3e+board.s3d+board.s3c=='')\
           or ((re.search('r',board.s3a)or board.s3a=='l') and board.s3g+board.s3f+board.s3e+board.s3d+board.s3c+board.s3b=='')\
           or (re.search('r',board.s1h) and board.s2h=='')\
           or (re.search('r',board.s5h) and board.s4h=='')\
           or (re.search('r',board.s6h) and board.s4h+board.s5h=='')\
           or (re.search('r',board.s7h) and board.s4h+board.s5h+board.s6h=='')\
           or (re.search('r',board.s8h) and board.s4h+board.s5h+board.s6h+board.s7h=='')\
           or (re.search('r',board.s9h) and board.s4h+board.s5h+board.s6h+board.s7h+board.s8h=='')\
           or (re.search('b',board.s1f) and board.s2g=='')\
           or (re.search('b',board.s5f) and board.s4g=='')\
           or (re.search('b',board.s6e) and board.s4g+board.s5f=='')\
           or (re.search('b',board.s7d) and board.s4g+board.s5f+board.s6e=='')\
           or (re.search('b',board.s8c) and board.s4g+board.s5f+board.s6e+board.s7d=='')\
           or (re.search('b',board.s9b) and board.s4g+board.s5f+board.s6e+board.s7d+board.s8c=='')\
           or board.s2f =='n'or board.s4f =='n'\
           :
            oute=1

    if board.s3i == 'K':
        if re.search(r'[plsgrk]|\+n|\+b',board.s3h)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s2h)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s4h)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s2i)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s4i)\
           or ((re.search('r',board.s3g)or board.s3g=='l') and board.s3h=='')\
           or ((re.search('r',board.s3h)or board.s3f=='l') and board.s3h+board.s3g=='')\
           or ((re.search('r',board.s3e)or board.s3e=='l') and board.s3h+board.s3g+board.s3f=='')\
           or ((re.search('r',board.s3d)or board.s3d=='l') and board.s3h+board.s3g+board.s3f+board.s3e=='')\
           or ((re.search('r',board.s3c)or board.s3c=='l') and board.s3h+board.s3g+board.s3f+board.s3e+board.s3d=='')\
           or ((re.search('r',board.s3b)or board.s3b=='l') and board.s3h+board.s3g+board.s3f+board.s3e+board.s3d+board.s3c=='')\
           or ((re.search('r',board.s3a)or board.s3a=='l') and board.s3h+board.s3g+board.s3f+board.s3e+board.s3d+board.s3c+board.s3b=='')\
           or (re.search('r',board.s1i) and board.s2i=='')\
           or (re.search('r',board.s5i) and board.s4i=='')\
           or (re.search('r',board.s6i) and board.s4i+board.s5i=='')\
           or (re.search('r',board.s7i) and board.s4i+board.s5i+board.s6i=='')\
           or (re.search('r',board.s8i) and board.s4i+board.s5i+board.s6i+board.s7i=='')\
           or (re.search('r',board.s9i) and board.s4i+board.s5i+board.s6i+board.s7i+board.s8i=='')\
           or (re.search('b',board.s1g) and board.s2h=='')\
           or (re.search('b',board.s5g) and board.s4h=='')\
           or (re.search('b',board.s6f) and board.s4h+board.s5g=='')\
           or (re.search('b',board.s7e) and board.s4h+board.s5g+board.s6f=='')\
           or (re.search('b',board.s8d) and board.s4h+board.s5g+board.s6f+board.s7e=='')\
           or (re.search('b',board.s9c) and board.s4h+board.s5g+board.s6f+board.s7e+board.s8d=='')\
           or board.s2g =='n'or board.s4g =='n'\
           :
            oute=1

    if board.s4a == 'K':
        if re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s3a)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s5a)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s4b)\
           or re.search(r'[bk]',board.s3b)or board.s3b=='s'or board.s3b=='+r'\
           or re.search(r'[bk]',board.s5b)or board.s5b=='s'or board.s5b=='+r'\
           or (re.search('r',board.s4c) and board.s4b=='')\
           or (re.search('r',board.s4d) and board.s4b+board.s4c=='')\
           or (re.search('r',board.s4e) and board.s4b+board.s4c+board.s4d=='')\
           or (re.search('r',board.s4f) and board.s4b+board.s4c+board.s4d+board.s4e=='')\
           or (re.search('r',board.s4g) and board.s4b+board.s4c+board.s4d+board.s4e+board.s4f=='')\
           or (re.search('r',board.s4h) and board.s4b+board.s4c+board.s4d+board.s4e+board.s4f+board.s4g=='')\
           or (re.search('r',board.s4i) and board.s4b+board.s4c+board.s4d+board.s4e+board.s4f+board.s4g+board.s4h=='')\
           or (re.search('r',board.s1a) and board.s2a+board.s3a=='')\
           or (re.search('r',board.s2a) and board.s3a=='')\
           or (re.search('r',board.s6a) and board.s5a=='')\
           or (re.search('r',board.s7a) and board.s5a+board.s6a=='')\
           or (re.search('r',board.s8a) and board.s5a+board.s6a+board.s7a=='')\
           or (re.search('r',board.s9a) and board.s5a+board.s6a+board.s7a+board.s8a=='')\
           or (re.search('b',board.s1d) and board.s3b+board.s2c=='')\
           or (re.search('b',board.s2c) and board.s3b=='')\
           or (re.search('b',board.s6c) and board.s5b=='')\
           or (re.search('b',board.s7d) and board.s5b+board.s6c=='')\
           or (re.search('b',board.s8e) and board.s5b+board.s6c+board.s7d=='')\
           or (re.search('b',board.s9f) and board.s5b+board.s6c+board.s7d+board.s8e=='')\
           :
            oute=1

    if board.s4b == 'K':
        if re.search(r'[plsgrk]|\+n|\+b',board.s4a)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s3a)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s5a)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s3b)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s5b)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s4c)\
           or re.search(r'[bk]',board.s3c)or board.s3c=='s'or board.s3c=='+r'\
           or re.search(r'[bk]',board.s5c)or board.s5c=='s'or board.s5c=='+r'\
           or (re.search('r',board.s4d) and board.s4c=='')\
           or (re.search('r',board.s4e) and board.s4c+board.s4d=='')\
           or (re.search('r',board.s4f) and board.s4c+board.s4d+board.s4e=='')\
           or (re.search('r',board.s4g) and board.s4c+board.s4d+board.s4e+board.s4f=='')\
           or (re.search('r',board.s4h) and board.s4c+board.s4d+board.s4e+board.s4f+board.s4g=='')\
           or (re.search('r',board.s4i) and board.s4c+board.s4d+board.s4e+board.s4f+board.s4g+board.s4h=='')\
           or (re.search('r',board.s1b) and board.s2b+board.s3b=='')\
           or (re.search('r',board.s2b) and board.s3b=='')\
           or (re.search('r',board.s6b) and board.s5b=='')\
           or (re.search('r',board.s7b) and board.s5b+board.s6b=='')\
           or (re.search('r',board.s8b) and board.s5b+board.s6b+board.s7b=='')\
           or (re.search('r',board.s9b) and board.s5b+board.s6b+board.s7b+board.s8b=='')\
           or (re.search('b',board.s1e) and board.s3c+board.s2d=='')\
           or (re.search('b',board.s2d) and board.s3c=='')\
           or (re.search('b',board.s6d) and board.s5c=='')\
           or (re.search('b',board.s7e) and board.s5c+board.s6d=='')\
           or (re.search('b',board.s8f) and board.s5c+board.s6d+board.s7e=='')\
           or (re.search('b',board.s9g) and board.s5c+board.s6d+board.s7e+board.s8f=='')\
           :
            oute=1

    if board.s4c == 'K':
        if re.search(r'[plsgrk]|\+n|\+b',board.s4b)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s3b)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s5b)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s3c)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s5c)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s4d)\
           or re.search(r'[bk]',board.s3d)or board.s3d=='s'or board.s3d=='+r'\
           or re.search(r'[bk]',board.s5d)or board.s5d=='s'or board.s5d=='+r'\
           or ((re.search('r',board.s4a)or board.s4a=='l') and board.s4b=='')\
           or (re.search('r',board.s4e) and board.s4d=='')\
           or (re.search('r',board.s4f) and board.s4d+board.s4e=='')\
           or (re.search('r',board.s4g) and board.s4d+board.s4e+board.s4f=='')\
           or (re.search('r',board.s4h) and board.s4d+board.s4e+board.s4f+board.s4g=='')\
           or (re.search('r',board.s4i) and board.s4d+board.s4e+board.s4f+board.s4g+board.s4h=='')\
           or (re.search('r',board.s1c) and board.s2c+board.s3c=='')\
           or (re.search('r',board.s2c) and board.s3c=='')\
           or (re.search('r',board.s6c) and board.s5c=='')\
           or (re.search('r',board.s7c) and board.s5c+board.s6c=='')\
           or (re.search('r',board.s8c) and board.s5c+board.s6c+board.s7c=='')\
           or (re.search('r',board.s9c) and board.s5c+board.s6c+board.s7c+board.s8c=='')\
           or (re.search('b',board.s1f) and board.s3d+board.s2e=='')\
           or (re.search('b',board.s2a) and board.s3b=='')\
           or (re.search('b',board.s2e) and board.s3d=='')\
           or (re.search('b',board.s6a) and board.s5b=='')\
           or (re.search('b',board.s6e) and board.s5d=='')\
           or (re.search('b',board.s7f) and board.s5d+board.s6e=='')\
           or (re.search('b',board.s8g) and board.s5d+board.s6e+board.s7f=='')\
           or (re.search('b',board.s9h) and board.s5d+board.s6e+board.s7f+board.s8g=='')\
           or board.s3a =='n'or board.s5a =='n'\
           :
            oute=1

    if board.s4d == 'K':
        if re.search(r'[plsgrk]|\+n|\+b',board.s4c)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s3c)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s5c)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s3d)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s5d)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s4e)\
           or re.search(r'[bk]',board.s3e)or board.s3e=='s'or board.s3e=='+r'\
           or re.search(r'[bk]',board.s5e)or board.s5e=='s'or board.s5e=='+r'\
           or ((re.search('r',board.s4a)or board.s4a=='l') and board.s4b+board.s4c=='')\
           or ((re.search('r',board.s4b)or board.s4b=='l') and board.s4c=='')\
           or (re.search('r',board.s4f) and board.s4e=='')\
           or (re.search('r',board.s4g) and board.s4e+board.s4f=='')\
           or (re.search('r',board.s4h) and board.s4e+board.s4f+board.s4g=='')\
           or (re.search('r',board.s4i) and board.s4e+board.s4f+board.s4g+board.s4h=='')\
           or (re.search('r',board.s1d) and board.s2d+board.s3d=='')\
           or (re.search('r',board.s2d) and board.s3d=='')\
           or (re.search('r',board.s6d) and board.s5d=='')\
           or (re.search('r',board.s7d) and board.s5d+board.s6d=='')\
           or (re.search('r',board.s8d) and board.s5d+board.s6d+board.s7d=='')\
           or (re.search('r',board.s9d) and board.s5d+board.s6d+board.s7d+board.s8d=='')\
           or (re.search('b',board.s1a) and board.s2b+board.s3c=='')\
           or (re.search('b',board.s1g) and board.s2f+board.s3e=='')\
           or (re.search('b',board.s2b) and board.s3c=='')\
           or (re.search('b',board.s2f) and board.s3e=='')\
           or (re.search('b',board.s7a) and board.s6b+board.s5c=='')\
           or (re.search('b',board.s6b) and board.s5c=='')\
           or (re.search('b',board.s6f) and board.s5e=='')\
           or (re.search('b',board.s7g) and board.s5e+board.s6f=='')\
           or (re.search('b',board.s8h) and board.s5e+board.s6f+board.s7g=='')\
           or (re.search('b',board.s9i) and board.s5e+board.s6f+board.s7g+board.s8h=='')\
           or board.s3b =='n'or board.s5b =='n'\
           :
            oute=1

    if board.s4e == 'K':
        if re.search(r'[plsgrk]|\+n|\+b',board.s4d)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s3d)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s5d)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s3e)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s5e)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s4f)\
           or re.search(r'[bk]',board.s3f)or board.s3f=='s'or board.s3f=='+r'\
           or re.search(r'[bk]',board.s5f)or board.s5f=='s'or board.s5f=='+r'\
           or ((re.search('r',board.s4a)or board.s4a=='l') and board.s4b+board.s4c+board.s4d=='')\
           or ((re.search('r',board.s4b)or board.s4b=='l') and board.s4c+board.s4d=='')\
           or ((re.search('r',board.s4c)or board.s4c=='l') and board.s4d=='')\
           or (re.search('r',board.s4g) and board.s4e=='')\
           or (re.search('r',board.s4h) and board.s4e+board.s4f=='')\
           or (re.search('r',board.s4i) and board.s4e+board.s4f+board.s4g=='')\
           or (re.search('r',board.s1e) and board.s2e+board.s3e=='')\
           or (re.search('r',board.s2e) and board.s3e=='')\
           or (re.search('r',board.s6e) and board.s5e=='')\
           or (re.search('r',board.s7e) and board.s5e+board.s6e=='')\
           or (re.search('r',board.s8e) and board.s5e+board.s6e+board.s7e=='')\
           or (re.search('r',board.s9e) and board.s5e+board.s6e+board.s7e+board.s8e=='')\
           or (re.search('b',board.s1b) and board.s2c+board.s3d=='')\
           or (re.search('b',board.s1h) and board.s2g+board.s3f=='')\
           or (re.search('b',board.s2c) and board.s3d=='')\
           or (re.search('b',board.s2g) and board.s3f=='')\
           or (re.search('b',board.s8a) and board.s7b+board.s6c+board.s5d=='')\
           or (re.search('b',board.s7b) and board.s6c+board.s5d=='')\
           or (re.search('b',board.s6c) and board.s5d=='')\
           or (re.search('b',board.s6g) and board.s5f=='')\
           or (re.search('b',board.s7h) and board.s5f+board.s6g=='')\
           or (re.search('b',board.s8i) and board.s5f+board.s6g+board.s7h=='')\
           or board.s3c =='n'or board.s5c =='n'\
           :
            oute=1

    if board.s4f == 'K':
        if re.search(r'[plsgrk]|\+n|\+b',board.s4e)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s3e)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s5e)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s3f)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s5f)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s4g)\
           or re.search(r'[bk]',board.s3g)or board.s3g=='s'or board.s3g=='+r'\
           or re.search(r'[bk]',board.s5g)or board.s5g=='s'or board.s5g=='+r'\
           or (re.search('r',board.s4i) and board.s4g+board.s4h=='')\
           or (re.search('r',board.s4h) and board.s4g=='')\
           or ((re.search('r',board.s4d)or board.s4d=='l') and board.s4e=='')\
           or ((re.search('r',board.s4c)or board.s4c=='l') and board.s4e+board.s4d=='')\
           or ((re.search('r',board.s4b)or board.s4b=='l') and board.s4e+board.s4d+board.s4c=='')\
           or ((re.search('r',board.s4a)or board.s4a=='l') and board.s4e+board.s4d+board.s4c+board.s4b=='')\
           or (re.search('r',board.s1f) and board.s2f+board.s3f=='')\
           or (re.search('r',board.s2f) and board.s3f=='')\
           or (re.search('r',board.s6f) and board.s5f=='')\
           or (re.search('r',board.s7f) and board.s5f+board.s6f=='')\
           or (re.search('r',board.s8f) and board.s5f+board.s6f+board.s7f=='')\
           or (re.search('r',board.s9f) and board.s5f+board.s6f+board.s7f+board.s8f=='')\
           or (re.search('b',board.s1i) and board.s2h+board.s3g=='')\
           or (re.search('b',board.s1c) and board.s2d+board.s3e=='')\
           or (re.search('b',board.s2d) and board.s3e=='')\
           or (re.search('b',board.s2h) and board.s3g=='')\
           or (re.search('b',board.s7i) and board.s6h+board.s5g=='')\
           or (re.search('b',board.s6h) and board.s5g=='')\
           or (re.search('b',board.s6d) and board.s5e=='')\
           or (re.search('b',board.s7c) and board.s5e+board.s6d=='')\
           or (re.search('b',board.s8b) and board.s5e+board.s6d+board.s7c=='')\
           or (re.search('b',board.s9a) and board.s5e+board.s6d+board.s7c+board.s8b=='')\
           or board.s3d =='n'or board.s5d =='n'\
           :
            oute=1

    if board.s4g == 'K':
        if re.search(r'[plsgrk]|\+n|\+b',board.s4f)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s3f)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s5f)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s3g)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s5g)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s4h)\
           or re.search(r'[bk]',board.s3h)or board.s3h=='s'or board.s3h=='+r'\
           or re.search(r'[bk]',board.s5h)or board.s5h=='s'or board.s5h=='+r'\
           or (re.search('r',board.s4i) and board.s4h=='')\
           or ((re.search('r',board.s4e)or board.s4e=='l') and board.s4f=='')\
           or ((re.search('r',board.s4d)or board.s4d=='l') and board.s4f+board.s4e=='')\
           or ((re.search('r',board.s4c)or board.s4c=='l') and board.s4f+board.s4e+board.s4d=='')\
           or ((re.search('r',board.s4b)or board.s4b=='l') and board.s4f+board.s4e+board.s4d+board.s4c=='')\
           or ((re.search('r',board.s4a)or board.s4a=='l') and board.s4f+board.s4e+board.s4d+board.s4c+board.s4b=='')\
           or (re.search('r',board.s1g) and board.s2g+board.s3g=='')\
           or (re.search('r',board.s2g) and board.s3g=='')\
           or (re.search('r',board.s6g) and board.s5g=='')\
           or (re.search('r',board.s7g) and board.s5g+board.s6g=='')\
           or (re.search('r',board.s8g) and board.s5g+board.s6g+board.s7g=='')\
           or (re.search('r',board.s9g) and board.s5g+board.s6g+board.s7g+board.s8g=='')\
           or (re.search('b',board.s1d) and board.s3f+board.s2e=='')\
           or (re.search('b',board.s2e) and board.s3f=='')\
           or (re.search('b',board.s2i) and board.s3h=='')\
           or (re.search('b',board.s6i) and board.s5h=='')\
           or (re.search('b',board.s6e) and board.s5f=='')\
           or (re.search('b',board.s7d) and board.s5f+board.s6e=='')\
           or (re.search('b',board.s8c) and board.s5f+board.s6e+board.s7d=='')\
           or (re.search('b',board.s9b) and board.s5f+board.s6e+board.s7d+board.s8c=='')\
           or board.s3e =='n'or board.s5e =='n'\
           :
            oute=1

    if board.s4h == 'K':
        if re.search(r'[plsgrk]|\+n|\+b',board.s4g)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s3g)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s5g)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s3h)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s5h)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s4i)\
           or re.search(r'[bk]',board.s3i)or board.s3i=='s'or board.s3i=='+r'\
           or re.search(r'[bk]',board.s5i)or board.s5i=='s'or board.s5i=='+r'\
           or ((re.search('r',board.s4f)or board.s4f=='l') and board.s4g=='')\
           or ((re.search('r',board.s4e)or board.s4e=='l') and board.s4g+board.s4f=='')\
           or ((re.search('r',board.s4d)or board.s4d=='l') and board.s4g+board.s4f+board.s4e=='')\
           or ((re.search('r',board.s4c)or board.s4c=='l') and board.s4g+board.s4f+board.s4e+board.s4d=='')\
           or ((re.search('r',board.s4b)or board.s4b=='l') and board.s4g+board.s4f+board.s4e+board.s4d+board.s4c=='')\
           or ((re.search('r',board.s4a)or board.s4a=='l') and board.s4g+board.s4f+board.s4e+board.s4d+board.s4c+board.s4b=='')\
           or (re.search('r',board.s1h) and board.s2h+board.s3h=='')\
           or (re.search('r',board.s2h) and board.s3h=='')\
           or (re.search('r',board.s6h) and board.s5h=='')\
           or (re.search('r',board.s7h) and board.s5h+board.s6h=='')\
           or (re.search('r',board.s8h) and board.s5h+board.s6h+board.s7h=='')\
           or (re.search('r',board.s9h) and board.s5h+board.s6h+board.s7h+board.s8h=='')\
           or (re.search('b',board.s1e) and board.s3g+board.s2f=='')\
           or (re.search('b',board.s2f) and board.s3g=='')\
           or (re.search('b',board.s6f) and board.s5g=='')\
           or (re.search('b',board.s7e) and board.s5g+board.s6f=='')\
           or (re.search('b',board.s8d) and board.s5g+board.s6f+board.s7e=='')\
           or (re.search('b',board.s9c) and board.s5g+board.s6f+board.s7e+board.s8d=='')\
           or board.s3f =='n'or board.s5f =='n'\
           :
            oute=1

    if board.s4i == 'K':
        if re.search(r'[plsgrk]|\+n|\+b',board.s4h)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s3h)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s5h)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s3i)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s5i)\
           or ((re.search('r',board.s4g)or board.s4g=='l') and board.s4h=='')\
           or ((re.search('r',board.s4h)or board.s4f=='l') and board.s4h+board.s4g=='')\
           or ((re.search('r',board.s4e)or board.s4e=='l') and board.s4h+board.s4g+board.s4f=='')\
           or ((re.search('r',board.s4d)or board.s4d=='l') and board.s4h+board.s4g+board.s4f+board.s4e=='')\
           or ((re.search('r',board.s4c)or board.s4c=='l') and board.s4h+board.s4g+board.s4f+board.s4e+board.s4d=='')\
           or ((re.search('r',board.s4b)or board.s4b=='l') and board.s4h+board.s4g+board.s4f+board.s4e+board.s4d+board.s4c=='')\
           or ((re.search('r',board.s4a)or board.s4a=='l') and board.s4h+board.s4g+board.s4f+board.s4e+board.s4d+board.s4c+board.s4b=='')\
           or (re.search('r',board.s1i) and board.s2i+board.s3i=='')\
           or (re.search('r',board.s2i) and board.s3i=='')\
           or (re.search('r',board.s6i) and board.s5i=='')\
           or (re.search('r',board.s7i) and board.s5i+board.s6i=='')\
           or (re.search('r',board.s8i) and board.s5i+board.s6i+board.s7i=='')\
           or (re.search('r',board.s9i) and board.s5i+board.s6i+board.s7i+board.s8i=='')\
           or (re.search('b',board.s1f) and board.s3h+board.s2g=='')\
           or (re.search('b',board.s2g) and board.s3h=='')\
           or (re.search('b',board.s6g) and board.s5h=='')\
           or (re.search('b',board.s7f) and board.s5h+board.s6g=='')\
           or (re.search('b',board.s8e) and board.s5h+board.s6g+board.s7f=='')\
           or (re.search('b',board.s9d) and board.s5h+board.s6g+board.s7f+board.s8e=='')\
           or board.s3g =='n'or board.s5g =='n'\
           :
            oute=1

    if board.s5a == 'K':
        if re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s4a)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s6a)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s5b)\
           or re.search(r'[bk]',board.s4b)or board.s4b=='s'or board.s4b=='+r'\
           or re.search(r'[bk]',board.s6b)or board.s6b=='s'or board.s6b=='+r'\
           or (re.search('r',board.s5c) and board.s5b=='')\
           or (re.search('r',board.s5d) and board.s5b+board.s5c=='')\
           or (re.search('r',board.s5e) and board.s5b+board.s5c+board.s5d=='')\
           or (re.search('r',board.s5f) and board.s5b+board.s5c+board.s5d+board.s5e=='')\
           or (re.search('r',board.s5g) and board.s5b+board.s5c+board.s5d+board.s5e+board.s5f=='')\
           or (re.search('r',board.s5h) and board.s5b+board.s5c+board.s5d+board.s5e+board.s5f+board.s5g=='')\
           or (re.search('r',board.s5i) and board.s5b+board.s5c+board.s5d+board.s5e+board.s5f+board.s5g+board.s5h=='')\
           or (re.search('r',board.s1a) and board.s2a+board.s3a+board.s4a=='')\
           or (re.search('r',board.s2a) and board.s3a+board.s4a=='')\
           or (re.search('r',board.s3a) and board.s4a=='')\
           or (re.search('r',board.s7a) and board.s6a=='')\
           or (re.search('r',board.s8a) and board.s6a+board.s7a=='')\
           or (re.search('r',board.s9a) and board.s6a+board.s7a+board.s8a=='')\
           or (re.search('b',board.s1e) and board.s4b+board.s3c+board.s2d=='')\
           or (re.search('b',board.s2d) and board.s4b+board.s3c=='')\
           or (re.search('b',board.s3c) and board.s4b=='')\
           or (re.search('b',board.s7c) and board.s6b=='')\
           or (re.search('b',board.s8d) and board.s6b+board.s7c=='')\
           or (re.search('b',board.s9e) and board.s6b+board.s7c+board.s8d=='')\
           :
            oute=1

    if board.s5b == 'K':
        if re.search(r'[plsgrk]|\+n|\+b',board.s5a)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s4a)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s6a)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s4b)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s6b)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s5c)\
           or re.search(r'[bk]',board.s4c)or board.s4c=='s'or board.s4c=='+r'\
           or re.search(r'[bk]',board.s6c)or board.s6c=='s'or board.s6c=='+r'\
           or (re.search('r',board.s5d) and board.s5c=='')\
           or (re.search('r',board.s5e) and board.s5c+board.s5d=='')\
           or (re.search('r',board.s5f) and board.s5c+board.s5d+board.s5e=='')\
           or (re.search('r',board.s5g) and board.s5c+board.s5d+board.s5e+board.s5f=='')\
           or (re.search('r',board.s5h) and board.s5c+board.s5d+board.s5e+board.s5f+board.s5g=='')\
           or (re.search('r',board.s5i) and board.s5c+board.s5d+board.s5e+board.s5f+board.s5g+board.s5h=='')\
           or (re.search('r',board.s1b) and board.s2b+board.s3b+board.s4b=='')\
           or (re.search('r',board.s2b) and board.s3b+board.s4b=='')\
           or (re.search('r',board.s3b) and board.s4b=='')\
           or (re.search('r',board.s7b) and board.s6b=='')\
           or (re.search('r',board.s8b) and board.s6b+board.s7b=='')\
           or (re.search('r',board.s9b) and board.s6b+board.s7b+board.s8b=='')\
           or (re.search('b',board.s1f) and board.s4c+board.s3d+board.s2e=='')\
           or (re.search('b',board.s2e) and board.s4c+board.s3d=='')\
           or (re.search('b',board.s3d) and board.s4c=='')\
           or (re.search('b',board.s7d) and board.s6c=='')\
           or (re.search('b',board.s8e) and board.s6c+board.s7d=='')\
           or (re.search('b',board.s9f) and board.s6c+board.s7d+board.s8e=='')\
           :
            oute=1

    if board.s5c == 'K':
        if re.search(r'[plsgrk]|\+n|\+b',board.s5b)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s4b)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s6b)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s4c)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s6c)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s5d)\
           or re.search(r'[bk]',board.s4d)or board.s4d=='s'or board.s4d=='+r'\
           or re.search(r'[bk]',board.s6d)or board.s6d=='s'or board.s6d=='+r'\
           or ((re.search('r',board.s5a)or board.s5a=='l') and board.s5b=='')\
           or (re.search('r',board.s5e) and board.s5d=='')\
           or (re.search('r',board.s5f) and board.s5d+board.s5e=='')\
           or (re.search('r',board.s5g) and board.s5d+board.s5e+board.s5f=='')\
           or (re.search('r',board.s5h) and board.s5d+board.s5e+board.s5f+board.s5g=='')\
           or (re.search('r',board.s5i) and board.s5d+board.s5e+board.s5f+board.s5g+board.s5h=='')\
           or (re.search('r',board.s1c) and board.s2c+board.s3c+board.s4c=='')\
           or (re.search('r',board.s2c) and board.s3c+board.s4c=='')\
           or (re.search('r',board.s3c) and board.s4c=='')\
           or (re.search('r',board.s7c) and board.s6c=='')\
           or (re.search('r',board.s8c) and board.s6c+board.s7c=='')\
           or (re.search('r',board.s9c) and board.s6c+board.s7c+board.s8c=='')\
           or (re.search('b',board.s1g) and board.s4d+board.s3e+board.s2f=='')\
           or (re.search('b',board.s2f) and board.s4d+board.s3e=='')\
           or (re.search('b',board.s3a) and board.s4b=='')\
           or (re.search('b',board.s3e) and board.s4d=='')\
           or (re.search('b',board.s7a) and board.s6b=='')\
           or (re.search('b',board.s7e) and board.s6d=='')\
           or (re.search('b',board.s8f) and board.s6d+board.s7e=='')\
           or (re.search('b',board.s9g) and board.s6d+board.s7e+board.s8f=='')\
           or board.s4a =='n'or board.s6a =='n'\
           :
            oute=1

    if board.s5d == 'K':
        if re.search(r'[plsgrk]|\+n|\+b',board.s5c)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s4c)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s6c)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s4d)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s6d)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s5e)\
           or re.search(r'[bk]',board.s4e)or board.s4e=='s'or board.s4e=='+r'\
           or re.search(r'[bk]',board.s6e)or board.s6e=='s'or board.s6e=='+r'\
           or ((re.search('r',board.s5a)or board.s5a=='l') and board.s5b+board.s5c=='')\
           or ((re.search('r',board.s5b)or board.s5b=='l') and board.s5c=='')\
           or (re.search('r',board.s5f) and board.s5e=='')\
           or (re.search('r',board.s5g) and board.s5e+board.s5f=='')\
           or (re.search('r',board.s5h) and board.s5e+board.s5f+board.s5g=='')\
           or (re.search('r',board.s5i) and board.s5e+board.s5f+board.s5g+board.s5h=='')\
           or (re.search('r',board.s1d) and board.s2d+board.s3d+board.s4d=='')\
           or (re.search('r',board.s2d) and board.s3d+board.s4d=='')\
           or (re.search('r',board.s3d) and board.s4d=='')\
           or (re.search('r',board.s7d) and board.s6d=='')\
           or (re.search('r',board.s8d) and board.s6d+board.s7d=='')\
           or (re.search('r',board.s9d) and board.s6d+board.s7d+board.s8d=='')\
           or (re.search('b',board.s1h) and board.s4e+board.s3f+board.s2g=='')\
           or (re.search('b',board.s2a) and board.s3b+board.s4c=='')\
           or (re.search('b',board.s2g) and board.s3f+board.s4e=='')\
           or (re.search('b',board.s3b) and board.s4c=='')\
           or (re.search('b',board.s3f) and board.s4e=='')\
           or (re.search('b',board.s8a) and board.s7b+board.s6c=='')\
           or (re.search('b',board.s7b) and board.s6c=='')\
           or (re.search('b',board.s7f) and board.s6e=='')\
           or (re.search('b',board.s8g) and board.s6e+board.s7f=='')\
           or (re.search('b',board.s9h) and board.s6e+board.s7f+board.s8g=='')\
           or board.s4b =='n'or board.s6b =='n'\
           :
            oute=1

    if board.s5e == 'K':
        if re.search(r'[plsgrk]|\+n|\+b',board.s5d)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s4d)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s6d)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s4e)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s6e)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s5f)\
           or re.search(r'[bk]',board.s4f)or board.s4f=='s'or board.s4f=='+r'\
           or re.search(r'[bk]',board.s6f)or board.s6f=='s'or board.s6f=='+r'\
           or ((re.search('r',board.s5a)or board.s5a=='l') and board.s5b+board.s5c+board.s5d=='')\
           or ((re.search('r',board.s5b)or board.s5b=='l') and board.s5c+board.s5d=='')\
           or ((re.search('r',board.s5c)or board.s5c=='l') and board.s5d=='')\
           or (re.search('r',board.s5g) and board.s5e=='')\
           or (re.search('r',board.s5h) and board.s5e+board.s5f=='')\
           or (re.search('r',board.s5i) and board.s5e+board.s5f+board.s5g=='')\
           or (re.search('r',board.s1e) and board.s2e+board.s3e+board.s4e=='')\
           or (re.search('r',board.s2e) and board.s3e+board.s4e=='')\
           or (re.search('r',board.s3e) and board.s4e=='')\
           or (re.search('r',board.s7e) and board.s6e=='')\
           or (re.search('r',board.s8e) and board.s6e+board.s7e=='')\
           or (re.search('r',board.s9e) and board.s6e+board.s7e+board.s8e=='')\
           or (re.search('b',board.s1a) and board.s2b+board.s3c+board.s4d=='')\
           or (re.search('b',board.s1i) and board.s2h+board.s3g+board.s4f=='')\
           or (re.search('b',board.s2b) and board.s3c+board.s4d=='')\
           or (re.search('b',board.s2h) and board.s3g+board.s4f=='')\
           or (re.search('b',board.s3c) and board.s4d=='')\
           or (re.search('b',board.s3g) and board.s4f=='')\
           or (re.search('b',board.s9a) and board.s8b+board.s7c+board.s6d=='')\
           or (re.search('b',board.s8b) and board.s7c+board.s6d=='')\
           or (re.search('b',board.s7c) and board.s6d=='')\
           or (re.search('b',board.s7g) and board.s6f=='')\
           or (re.search('b',board.s8h) and board.s6f+board.s7g=='')\
           or (re.search('b',board.s9i) and board.s6f+board.s7g+board.s8h=='')\
           or board.s4c =='n'or board.s6c =='n'\
           :
            oute=1

    if board.s5f == 'K':
        if re.search(r'[plsgrk]|\+n|\+b',board.s5e)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s4e)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s6e)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s4f)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s6f)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s5g)\
           or re.search(r'[bk]',board.s4g)or board.s4g=='s'or board.s4g=='+r'\
           or re.search(r'[bk]',board.s6g)or board.s6g=='s'or board.s6g=='+r'\
           or (re.search('r',board.s5i) and board.s5g+board.s5h=='')\
           or (re.search('r',board.s5h) and board.s5g=='')\
           or ((re.search('r',board.s5d)or board.s5d=='l') and board.s5e=='')\
           or ((re.search('r',board.s5c)or board.s5c=='l') and board.s5e+board.s5d=='')\
           or ((re.search('r',board.s5b)or board.s5b=='l') and board.s5e+board.s5d+board.s5c=='')\
           or ((re.search('r',board.s5a)or board.s5a=='l') and board.s5e+board.s5d+board.s5c+board.s5b=='')\
           or (re.search('r',board.s1f) and board.s2f+board.s3f+board.s4f=='')\
           or (re.search('r',board.s2f) and board.s3f+board.s4f=='')\
           or (re.search('r',board.s3f) and board.s4f=='')\
           or (re.search('r',board.s7f) and board.s6f=='')\
           or (re.search('r',board.s8f) and board.s6f+board.s7f=='')\
           or (re.search('r',board.s9f) and board.s6f+board.s7f+board.s8f=='')\
           or (re.search('b',board.s1b) and board.s2c+board.s3d+board.s4e=='')\
           or (re.search('b',board.s2i) and board.s3h+board.s4g=='')\
           or (re.search('b',board.s2c) and board.s3d+board.s4e=='')\
           or (re.search('b',board.s3d) and board.s4e=='')\
           or (re.search('b',board.s3h) and board.s4g=='')\
           or (re.search('b',board.s8i) and board.s7h+board.s6g=='')\
           or (re.search('b',board.s7h) and board.s6g=='')\
           or (re.search('b',board.s7d) and board.s6e=='')\
           or (re.search('b',board.s8c) and board.s6e+board.s7d=='')\
           or (re.search('b',board.s9b) and board.s6e+board.s7d+board.s8c=='')\
           or board.s4d =='n'or board.s6d =='n'\
           :
            oute=1

    if board.s5g == 'K':
        if re.search(r'[plsgrk]|\+n|\+b',board.s5f)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s4f)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s6f)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s4g)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s6g)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s5h)\
           or re.search(r'[bk]',board.s4h)or board.s4h=='s'or board.s4h=='+r'\
           or re.search(r'[bk]',board.s6h)or board.s6h=='s'or board.s6h=='+r'\
           or (re.search('r',board.s5i) and board.s5h=='')\
           or ((re.search('r',board.s5e)or board.s5e=='l') and board.s5f=='')\
           or ((re.search('r',board.s5d)or board.s5d=='l') and board.s5f+board.s5e=='')\
           or ((re.search('r',board.s5c)or board.s5c=='l') and board.s5f+board.s5e+board.s5d=='')\
           or ((re.search('r',board.s5b)or board.s5b=='l') and board.s5f+board.s5e+board.s5d+board.s5c=='')\
           or ((re.search('r',board.s5a)or board.s5a=='l') and board.s5f+board.s5e+board.s5d+board.s5c+board.s5b=='')\
           or (re.search('r',board.s1g) and board.s2g+board.s3g+board.s4g=='')\
           or (re.search('r',board.s2g) and board.s3g+board.s4g=='')\
           or (re.search('r',board.s3g) and board.s4g=='')\
           or (re.search('r',board.s7g) and board.s6g=='')\
           or (re.search('r',board.s8g) and board.s6g+board.s7g=='')\
           or (re.search('r',board.s9g) and board.s6g+board.s7g+board.s8g=='')\
           or (re.search('b',board.s1c) and board.s4f+board.s3e+board.s2d=='')\
           or (re.search('b',board.s2d) and board.s4f+board.s3e=='')\
           or (re.search('b',board.s3e) and board.s4f=='')\
           or (re.search('b',board.s3i) and board.s4h=='')\
           or (re.search('b',board.s7i) and board.s6h=='')\
           or (re.search('b',board.s7e) and board.s6f=='')\
           or (re.search('b',board.s8d) and board.s6f+board.s7e=='')\
           or (re.search('b',board.s9c) and board.s6f+board.s7e+board.s8d=='')\
           or board.s4e =='n'or board.s6e =='n'\
           :
            oute=1

    if board.s5h == 'K':
        if re.search(r'[plsgrk]|\+n|\+b',board.s5g)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s4g)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s6g)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s4h)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s6h)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s5i)\
           or re.search(r'[bk]',board.s4i)or board.s4i=='s'or board.s4i=='+r'\
           or re.search(r'[bk]',board.s6i)or board.s6i=='s'or board.s6i=='+r'\
           or ((re.search('r',board.s5f)or board.s5f=='l') and board.s5g=='')\
           or ((re.search('r',board.s5e)or board.s5e=='l') and board.s5g+board.s5f=='')\
           or ((re.search('r',board.s5d)or board.s5d=='l') and board.s5g+board.s5f+board.s5e=='')\
           or ((re.search('r',board.s5c)or board.s5c=='l') and board.s5g+board.s5f+board.s5e+board.s5d=='')\
           or ((re.search('r',board.s5b)or board.s5b=='l') and board.s5g+board.s5f+board.s5e+board.s5d+board.s5c=='')\
           or ((re.search('r',board.s5a)or board.s5a=='l') and board.s5g+board.s5f+board.s5e+board.s5d+board.s5c+board.s5b=='')\
           or (re.search('r',board.s1h) and board.s2h+board.s3h+board.s4h=='')\
           or (re.search('r',board.s2h) and board.s3h+board.s4h=='')\
           or (re.search('r',board.s3h) and board.s4h=='')\
           or (re.search('r',board.s7h) and board.s6h=='')\
           or (re.search('r',board.s8h) and board.s6h+board.s7h=='')\
           or (re.search('r',board.s9h) and board.s6h+board.s7h+board.s8h=='')\
           or (re.search('b',board.s1d) and board.s4g+board.s3f+board.s2e=='')\
           or (re.search('b',board.s2e) and board.s4g+board.s3f=='')\
           or (re.search('b',board.s3f) and board.s4g=='')\
           or (re.search('b',board.s7f) and board.s6g=='')\
           or (re.search('b',board.s8e) and board.s6g+board.s7f=='')\
           or (re.search('b',board.s9d) and board.s6g+board.s7f+board.s8e=='')\
           or board.s4f =='n'or board.s6f =='n'\
           :
            oute=1

    if board.s5i == 'K':
        if re.search(r'[plsgrk]|\+n|\+b',board.s5h)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s4h)\
           or re.search(r'[sgbk]|\+p|\+l|\+n|\+r',board.s6h)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s4i)\
           or re.search(r'[rgk]|\+p|\+l|\+n|\+s|\+b',board.s6i)\
           or ((re.search('r',board.s5g)or board.s5g=='l') and board.s5h=='')\
           or ((re.search('r',board.s5h)or board.s5f=='l') and board.s5h+board.s5g=='')\
           or ((re.search('r',board.s5e)or board.s5e=='l') and board.s5h+board.s5g+board.s5f=='')\
           or ((re.search('r',board.s5d)or board.s5d=='l') and board.s5h+board.s5g+board.s5f+board.s5e=='')\
           or ((re.search('r',board.s5c)or board.s5c=='l') and board.s5h+board.s5g+board.s5f+board.s5e+board.s5d=='')\
           or ((re.search('r',board.s5b)or board.s5b=='l') and board.s5h+board.s5g+board.s5f+board.s5e+board.s5d+board.s5c=='')\
           or ((re.search('r',board.s5a)or board.s5a=='l') and board.s5h+board.s5g+board.s5f+board.s5e+board.s5d+board.s5c+board.s5b=='')\
           or (re.search('r',board.s2i) and board.s3i+board.s4i=='')\
           or (re.search('r',board.s3i) and board.s3i=='')\
           or (re.search('r',board.s7i) and board.s6i=='')\
           or (re.search('r',board.s8i) and board.s6i+board.s7i=='')\
           or (re.search('r',board.s9i) and board.s6i+board.s7i+board.s8i=='')\
           or (re.search('b',board.s1e) and board.s4h+board.s3g+board.s2f=='')\
           or (re.search('b',board.s2f) and board.s4h+board.s3g=='')\
           or (re.search('b',board.s3g) and board.s4h=='')\
           or (re.search('b',board.s7g) and board.s6h=='')\
           or (re.search('b',board.s8f) and board.s6h+board.s7g=='')\
           or (re.search('b',board.s9e) and board.s6h+board.s7g+board.s8f=='')\
           or board.s4g =='n'or board.s6g =='n'\
           :
            oute=1


#先手玉に王手がかかっているか
def boute():
    global oute
    board.synth()
    soute()
    if oute==1:
        return
    board.mirror()
    soute()

#後手玉に王手がかかっているか
def woute():
    global oute
    board.rotate()
    soute()
    if oute==1:
        return
    board.romirror()
    soute()
