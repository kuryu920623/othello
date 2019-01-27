from CulcBoardStateNumbers import *
from Convert_StateNumbers_Board2D import *
from PC_Choice import *

import time

blank, black, white = 0,1,2
HumanTurn,PCTurn = 0,1

#BoardStateNUmbers:盤面の状態を表すための数字
BoardStateNumbers =  [[0,0,0,189,135,0,0,0] #横方向、一番右の石が1桁目を表す
                    , [0,0,0,189,135,0,0,0] #縦方向、一番下の石が1桁目を表す
                    , [0,0,0,0,54,108,54,0,0,0,0] #左下→右上方向、左下が一桁目
                    , [0,0,0,0,27,216,27,0,0,0,0]] #左上→右下方向、左上が一桁目

#白黒逆の色を返す。
def OppositeColor(color):
    return {1:2,2:1}[color]

def end(BoardStateNumbers):
    Board2D = BoardStateNumbers_to_Board2D(BoardStateNumbers)
    BlackNum,WhiteNum = 0,0
    for i in Board2D:
        BlackNum += i.count(1)
        WhiteNum += i.count(2)
    return BlackNum,WhiteNum

def printBoard_2D(BoardStateNumbers):
    Board2D = BoardStateNumbers_to_Board2D(BoardStateNumbers)
    board_forPrint = [[0 for t in range(8)]for s in range(8)]
    for i in range(8):
        for j in range(8):
            board_forPrint[i][j] = [str(i)+str(j),"●","○"][Board2D[i][j]]
        print(" ".join(board_forPrint[i]))

def printPutablePositions(PutablePositionSet,CurrentTurnColor):
    print("Next" + [0,"●","○"][CurrentTurnColor])
    PositionList = list(PutablePositionSet)
    PositionList = [str(Tuple[0])+str(Tuple[1]) for Tuple in PositionList]
    PositionList.sort()
    print(" ".join(PositionList))


#PCBlack/PCWhiteは本来ならPC_Choiceインスタンス。しかし人間のターンなら使用されないためなんでもよい。
#返り値を設定してよいものだろうか・・・またごちゃごちゃしてしまいそう
def OneMatch(blackTurn,whiteTurn,PCBlack=0,PCWhite=0):
    #初期設定
    BlackTurn = blackTurn # 黒番：0なら人間、1ならPC
    WhiteTurn = whiteTurn # 白版：0なら人間、1ならPC
    HumanOrPlayerTurn = [0,BlackTurn,WhiteTurn]
    CurrentTurnNumber = 0 #経過ターン数
    CurrentTurnColor = 1 #CurrentTurnColorはその時の手番の色(数字)、初手は黒
    BoardStateNumbers =  [[0,0,0,189,135,0,0,0] #横方向、一番右の石が1桁目を表す
                        , [0,0,0,189,135,0,0,0] #縦方向、一番下の石が1桁目を表す
                        , [0,0,0,0,54,108,54,0,0,0,0] #左下→右上方向、左下が一桁目
                        , [0,0,0,0,27,216,27,0,0,0,0]] #左上→右下方向、左上が一桁目
    StartTime = time.time()

    #対戦開始
    while True:
        PutablePositionSet = MakePutablePositionList(BoardStateNumbers,CurrentTurnColor)
        if PutablePositionSet == set([]):
            CurrentTurnColor = OppositeColor(CurrentTurnColor)
            PutablePositionSet = MakePutablePositionList(BoardStateNumbers,CurrentTurnColor)
            if PutablePositionSet == set([]): #双方置く場所がないので終了
                EndTime = time.time()
                return list(end(BoardStateNumbers)) + [round(EndTime-StartTime,2)] #関数化したのでreturnの時点で終了
                break
        CurrentTurnNumber += 1

        # printBoard_2D(BoardStateNumbers)
        # printPutablePositions(PutablePositionSet,CurrentTurnColor)
        # print()

        if HumanOrPlayerTurn[CurrentTurnColor] == 0: #人間のターン
            while True:
                PutPosition = input()
                if PutPosition == "exit":
                    exit()
                PutPosition_Tuple = (int(PutPosition[0:1]),int(PutPosition[1:2]))
                if PutPosition_Tuple in PutablePositionSet:
                    break
        else: #PCのターン
            PC = (0,PCBlack,PCWhite)[CurrentTurnColor]
            CurrentDepthPoint = float("inf") if CurrentTurnColor == 1 else -float("inf")
            if CurrentTurnNumber >= 50:
                PutPosition_Tuple = PC.MinMaxChoice(BoardStateNumbers,OppositeColor(CurrentTurnColor),0,7,CurrentDepthPoint,CurrentTurnNumber)
            else:
                PutPosition_Tuple = PC.MinMaxChoice(BoardStateNumbers,OppositeColor(CurrentTurnColor),0,3,CurrentDepthPoint,CurrentTurnNumber)

        BoardStateNumbers = CuclBoardStateNumber_OnePut(BoardStateNumbers,*PutPosition_Tuple,CurrentTurnColor)
        CurrentTurnColor = OppositeColor(CurrentTurnColor)

#PCインスタンス生成
PC1 = PC_Choice(40,10,point_array1,point_array1)
PC2 = PC_Choice(1000,1000,point_array1,point_array1)

OneMatch(1,1,PC1,PC2)
