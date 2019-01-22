"""
各BoardStateNumber(0~6560の数字)の状態に対して、i(0~7)番目の位置に石を置いた時に
左右それぞれ、何枚の石を返すことができるかをtupleで格納した表を作成。
tuple(左に返せる枚数,右に返せる枚数)が6561(3^8)*8(石を置くindex)個入った三次元tupleを生成
一度作成して以降は白/黒それぞれテキストファイルとして保存して、毎回それを読み込ませる。

例
    BoardStateNumber=135は---wb---という列の状態を表す
    この時左から3番目(index=2)に黒を置くと右に一枚返すことができるので
    TurnableRange_ForBlack[135] = ((0,0),(0,0),(0,1),(0,0),(0,0),(0,0),(0,0),(0,0))
    となる
"""

import random

def OppositeColor(color):
    return {1:2,2:1}[color]

#10進法表記の数字xをN進法表記の文字列に変換して返す。
def Base_10toN(X,n):
    if (int(X/n)):
        return Base_10toN(int(X/n), n)+str(X%n)
    return str(X%n)

#i_Base3(空/黒/白=0/1/2 とした8桁の文字列)の時、index=jの位置にcolorの石を置いた時、置いた石の左方向に石を返す数。
#例えば"12201220"の時、index=3(左から4番目)の位置に黒(=1)の石を置いた場合、2枚返せるので返り値は2
def TurnStoneRange_Left(color,i_Base3,j):
    if j <= 1:
        return 0
    if i_Base3[j:j+1] != "0":
        return 0
    if i_Base3[j-1:j] != str(OppositeColor(color)):
        return 0

    depth = 1
    while j - depth >= 0 and i_Base3[j-depth:j-depth+1] == str(OppositeColor(color)):
        depth += 1
    if j - depth == -1: #端まで白で埋まっていた場合(wwww----)
        return 0
    elif i_Base3[j-depth] == "0": #左の白の端が空だった場合(--ww----)
        return 0
    else:
        return depth - 1

#i_Base3(空/黒/白=0/1/2 とした8桁の文字列)の時、index=jの位置にcolorの石を置いた時、置いた石の右方向に石を返す数。
#例えば"12202120"の時、index=3(左から4番目)の位置に黒(=1)の石を置いた場合、右方向に1枚返せるので返り値は1
def TurnStoneRange_Right(color,i_Base3,j):
    if j >= 6:
        return 0
    if i_Base3[j:j+1] != "0":
        return 0
    if i_Base3[j+1:j+2] != str(OppositeColor(color)):
        return 0

    depth = 1
    while j + depth <= 7 and i_Base3[j+depth:j+depth+1] == str(OppositeColor(color)):
        depth += 1
    if j + depth == 8: #端まで白で埋まっていた場合(----wwww)
        return 0
    elif i_Base3[j+depth] == "0": #左の白の端が空だった場合(----ww--)
        return 0
    else:
        return depth - 1

blank,black,white = 0,1,2
TurnableRange_ForBlack = [] #BoardStateNum = i(0~6560) の状態で黒石をindex = j(0~7)に置いた時の左右のひっくり返せる石の位置を格納。3次元タプル。
TurnableRange_ForWhite = []
PutablePositionNumbers_ForBlack = [] #BoardStateNum = i(0~6560) の状態で黒石を置ける位置の数をint型で格納。1次元タプル。
PutablePositionNumbers_ForWhite = []
PutablePositions_ForBlack = [] #BoardStateNum = i(0~6560) の状態で黒石を置けるindex(左が0)をタプルで格納。おける位置がない場合空のタプルを格納。2次元タプル。
PutablePositions_ForWhite = []

for i in range(3**8):
    RangeList_ForBlack_i = [] #BoardStateNumber=iの各位置に黒石を置いた場合の返せる石の数tuple(左、右)が計8個入る
    RangeList_ForWhite_i = [] #BoardStateNumber=iの各位置に白石を置いた場合の返せる石の数tuple(左、右)が計8個入る
    PositionList_ForBlack_i = [] #BoardStateNumber=iの状態で黒石がおける位置のindex(0~7)を入れる。おける位置がない場合は空のまま
    PositionList_ForWhite_i = []
    i_Base3 = Base_10toN(i,3).zfill(8)
    for j in range(8): #jは石を置く位置
        RangeTuple_ij_ForBlack = []
        [RangeTuple_ij_ForBlack.append(k) for k in range(-TurnStoneRange_Left(black,i_Base3,j), TurnStoneRange_Right(black,i_Base3,j)+1) if k != 0]
        RangeList_ForBlack_i.append(tuple(RangeTuple_ij_ForBlack))
        if RangeList_ForBlack_i[-1] != ():
            PositionList_ForBlack_i.append(j)
        RangeTuple_ij_ForWhite = []
        [RangeTuple_ij_ForWhite.append(k) for k in range(-TurnStoneRange_Left(white,i_Base3,j), TurnStoneRange_Right(white,i_Base3,j)+1) if k != 0]
        RangeList_ForWhite_i.append(tuple(RangeTuple_ij_ForWhite))
        if RangeList_ForWhite_i[-1] != ():
            PositionList_ForWhite_i.append(j)
    TurnableRange_ForBlack.append(tuple(RangeList_ForBlack_i))
    PutablePositions_ForBlack.append(tuple(PositionList_ForBlack_i))
    PutablePositionNumbers_ForBlack.append(8-RangeList_ForBlack_i.count(()))
    TurnableRange_ForWhite.append(tuple(RangeList_ForWhite_i))
    PutablePositions_ForWhite.append(tuple(PositionList_ForWhite_i))
    PutablePositionNumbers_ForWhite.append(8-RangeList_ForWhite_i.count(()))
    # if i%100 == 0: #黒、動作確認用
    #     print(i_Base3,RangeList_ForBlack_i)
    #     print()
    # if i%101 == 0: #白、動作確認用
    #     print(i_Base3,RangeList_ForWhite_i)
    #     print()
    # if i%100 == 0: #黒、動作確認用
    #     print(i_Base3,PutablePositionNumbers_ForBlack[-1])
    #     print()
    # if i%107 == 0: #白、動作確認用
    #     print(i_Base3,PutablePositionNumbers_ForWhite[-1])
    #     print()
    # if i%103 == 0: #黒、動作確認用
    #     print(i_Base3,PutablePositions_ForBlack[-1])
    #     print()
    # if i%110 == 0: #白、動作確認用
    #     print(i_Base3,PutablePositions_ForWhite[-1])
    #     print()

#TurnableRangeをpythonファイルとして保存。
TurnableRange_ForBlack_file = open("TurnableRange_ForBlack.py","w+")
TurnableRange_ForBlack_file.write("TurnableRange_ForBlack" + "=" + str(tuple(TurnableRange_ForBlack)))
TurnableRange_ForBlack_file.close()
TurnableRange_ForWhite_file = open("TurnableRange_ForWhite.py","w+")
TurnableRange_ForWhite_file.write("TurnableRange_ForWhite" + "=" + str(tuple(TurnableRange_ForWhite)))
TurnableRange_ForWhite_file.close()

#PutablePositionNumbersをpythonファイルとして保存。
PutablePositionNumbers_file = open("PutablePositionNumbers_ForBlack.py","w+")
PutablePositionNumbers_file.write("PutablePositionNumbers_ForBlack" + "=" + str(tuple(PutablePositionNumbers_ForBlack)))
PutablePositionNumbers_file.close()
PutablePositionNumbers_file = open("PutablePositionNumbers_ForWhite.py","w+")
PutablePositionNumbers_file.write("PutablePositionNumbers_ForWhite" + "=" + str(tuple(PutablePositionNumbers_ForWhite)))
PutablePositionNumbers_file.close()

#PutablePositionsをpythonファイルとして保存。
PutablePositions_file = open("PutablePositions_ForBlack.py","w+")
PutablePositions_file.write("PutablePositions_ForBlack" + "=" + str(tuple(PutablePositions_ForBlack)))
PutablePositions_file.close()
PutablePositions_file = open("PutablePositions_ForWhite.py","w+")
PutablePositions_file.write("PutablePositions_ForWhite" + "=" + str(tuple(PutablePositions_ForWhite)))
PutablePositions_file.close()
