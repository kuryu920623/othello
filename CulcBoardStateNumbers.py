from Reserved6561Tuples.TurnableRange_ForBlack import TurnableRange_ForBlack
from Reserved6561Tuples.TurnableRange_ForWhite import TurnableRange_ForWhite
from Reserved6561Tuples.PutablePositions_ForBlack import PutablePositions_ForBlack
from Reserved6561Tuples.PutablePositions_ForWhite import PutablePositions_ForWhite
import copy

#入力したBoardStateNumbersの状態でcolorの石を置ける位置のSetを返す。
def MakePutablePositionList(BoardStateNumbers,color):
    PutablePositionSet = set([])
    PutablePositions = PutablePositions_ForBlack if color == 1 else PutablePositions_ForWhite

    #横方向で見てひっくり返せる場合
    for i in range(8):
        PutablePositionTuple_i = PutablePositions[BoardStateNumbers[0][i]]
        for j in PutablePositionTuple_i:
            PutablePositionSet.add((i,j))

    #縦方向で見てひっくり返せる場合
    for j in range(8):
        PutablePositionTuple_j = PutablePositions[BoardStateNumbers[1][j]]
        for i in PutablePositionTuple_j:
            PutablePositionSet.add((i,j))

    #右上→左下方向で見てひっくり返せる場合
    for i in range(6): #indexは(-5+i,7)→(-5+i+j,7-j)
        PutablePositionTuple_i = PutablePositions[BoardStateNumbers[2][i]]
        for j in PutablePositionTuple_i:
            if -5+i+j >= 0:
                PutablePositionSet.add((-5+i+j,7-j))
    for i in range(5): #indexは(0,i+7)→(j,7+i-j)
        PutablePositionTuple_i = PutablePositions[BoardStateNumbers[2][i+6]]
        for j in PutablePositionTuple_i:
            if 8+i-j <= 7:
                 PutablePositionSet.add((j,8+i-j))

    #右下→左上方向で見てひっくり返せる場合
    for i in range(6): #indexは(12-i,7)→(12-i-j,7-j)
        PutablePositionTuple_i = PutablePositions[BoardStateNumbers[3][i]]
        for j in PutablePositionTuple_i:
            if 12-i-j <= 7:
                PutablePositionSet.add((12-i-j,7-j))
    for i in range(5): #indexは(7,7+i)→(7-j,7+i-j)
        PutablePositionTuple_i = PutablePositions[BoardStateNumbers[3][i+6]]
        for j in PutablePositionTuple_i:
            if 8+i-j<=7:
                PutablePositionSet.add((7-j,8+i-j))

    return PutablePositionSet

#BoardStateNumberの状態で(i,j)に石を置くまたは(i,j)の石をひっくり返した時のBoardStateNumberの変化を計算して出力
#引数deltaは石の数値の変化量(白→黒なら-1,空に白を置いたら+2)
def CuclBoardStateNumber_OneStone(BoardStateNumbers,i,j,delta):

    NewBoardStateNumbers = copy.deepcopy(BoardStateNumbers) #新しい変数名を用意しないとなぜかグローバル変数が置き換わってしまう。

    #(1)横方向
    NewBoardStateNumbers[0][i] += delta * 3 ** (7-j)

    #(2)横方向
    NewBoardStateNumbers[1][j] += delta * 3 ** (7-i)

    #(3)右上→左下方向
    if 2<=i+j<=7: # 変更のあるマスが 2<=i+j<=7 (左上側)の位置の場合
        NewBoardStateNumbers[2][i+j-2] += delta * 3 ** j
    elif 8<=i+j<=12: # 変更のあるマスが 8<=i+j<=12 (右下側)の位置の場合
        NewBoardStateNumbers[2][i+j-2] += delta * 3 ** (7-i)

    #(4)右下→左上方向
    if 0<=i-j<=5: #変更のあるマスが 0<=i-j<=5 (左下側)の位置にある場合
        NewBoardStateNumbers[3][5-i+j] += delta * 3 ** j
    elif -5<=i-j<=-1: #変更のあるマスが -5<=i-j<=-1 (右上側)の位置にある場合
        NewBoardStateNumbers[3][5-i+j] += delta * 3 ** i

    return NewBoardStateNumbers

#BoardStateNumbersの状態で(i,j)にcolorの石を置き、ひっくり返し終わった後のBoardStateNumbersを計算して出力
def CuclBoardStateNumber_OnePut(BoardStateNumbers,i,j,color):

    delta = 2*color - 3  # color=black=1なら白→黒なので-1,color=white=2なら+1が代入される
    TurnStones = set([]) #返す石の位置Tuple(i,j)をSetで格納、先に返す石の確定をしないと変化したBoardStateNumbersに対して返せる石を探してしまう。

    TurnableRange = TurnableRange_ForBlack if color == 1 else TurnableRange_ForWhite

    #TurnStonesを探す処理
    #(1)横方向
    BoardStateNumber = BoardStateNumbers[0][i]
    TurnableRangeTuple = TurnableRange[BoardStateNumber][j]
    [TurnStones.add((i,j+k)) for k in TurnableRangeTuple]

    #(2)縦方向
    BoardStateNumber = BoardStateNumbers[1][j]
    TurnableRangeTuple = TurnableRange[BoardStateNumber][i]
    [TurnStones.add((i+k,j)) for k in TurnableRangeTuple]

    #(3)右上→左下方向
    if 2<=i+j<=7: #石を置いたマスが 2<=i+j<=7 (左上側)の位置の場合
        BoardStateNumber = BoardStateNumbers[2][i+j-2]
        TurnableRangeTuple = TurnableRange[BoardStateNumber][7-j]
        [TurnStones.add((i+k,j-k)) for k in TurnableRangeTuple]
    elif 8<=i+j<=12: #石を置いたマスが 8<=i+j<=12 (右下側)の位置の場合
        BoardStateNumber = BoardStateNumbers[2][i+j-2]
        TurnableRangeTuple = TurnableRange[BoardStateNumber][i]
        [TurnStones.add((i+k,j-k)) for k in TurnableRangeTuple]

    #(4)右下→左上方向

    if 0<=i-j<=5: #石を置いたマスが j<=i (左下側)の位置にある場合
        BoardStateNumber = BoardStateNumbers[3][5-i+j]
        TurnableRangeTuple = TurnableRange[BoardStateNumber][7-j]
        [TurnStones.add((i-k,j-k)) for k in TurnableRangeTuple]
    elif -5<=i-j<=-1: #石を置いたマスが i<j (右上側)の位置の場合
        BoardStateNumber = BoardStateNumbers[3][5-i+j]
        TurnableRangeTuple = TurnableRange[BoardStateNumber][7-i]
        [TurnStones.add((i-k,j-k)) for k in TurnableRangeTuple]

    NewBoardStateNumbers = copy.deepcopy(BoardStateNumbers) #新しい変数名を用意しないとなぜかグローバル変数が置き換わってしまう。

    #(1)置いた石の分のBoardStateNumbersの変化計算
    NewBoardStateNumbers = CuclBoardStateNumber_OneStone(NewBoardStateNumbers,i,j,color)

    #(2)ひっくり返す分のBoardStateNumbersの変化計算
    for StonePosition in TurnStones:
        NewBoardStateNumbers = CuclBoardStateNumber_OneStone(NewBoardStateNumbers,*StonePosition,delta)

    return NewBoardStateNumbers
