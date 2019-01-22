from Othello_OneMatch import OppositeColor
from CulcBoardStateNumbers import *

'''
点数計算は常に黒の点数を計算することにする。
というのも、今回の得点計算方法では常に「黒の点数」+「白の点数」=0
という関係が成り立つようになっており、MinMax法を使うと
点数が黒の点数であろうが白の点数であろうが同じ結果が出るから。

「黒の点数」+「白の点数」=0 関係が成り立たない得点計算をする場合、
AIが白の場合の得点/AIが黒の場合の得点の計算を分ける必要がある。
'''

# Point = PointA(各マスの点数による点数) + t(係数) * PointB(置くことができるマスの数による点数)

def Base_10toN(X,n):
    if (int(X/n)):
        return Base_10toN(int(X/n), n)+str(X%n)
    return str(X%n)

def Make6561PointA_Tuple(PointArray2D):
    PointA6561List = []
    color_to_point = (0,1,-1) #colorのindexを取ると得点の係数になる
    for i in range(3**8):
        i_Base3 = Base_10toN(i,3).zfill(8)
        PointList_i = []
        for row in range(4): #ちゃんとやると8列目まで必要だけど、上下対称なので4まででよい(5列目=4列目、6列目=3列目・・・)
            point_row = 0
            for j in range(8):
                point_row += PointArray2D[row][j] * color_to_point[int(i_Base3[j:j+1])]
            PointList_i.append(point_row)
        PointA6561List.append(tuple(PointList_i))
    return tuple(PointA6561List)

point_array1 =   ((68,-12,53,-8,-8,53,-12,68)
                ,(-12,-62,-33,-7,-7,-33,-62,-12)
                ,(53,-33,26,8,8,26,-33,53)
                ,(-8,-7,8,-18,-18,8,-7,-8)
                ,(-8,-7,8,-18,-18,8,-7,-8)
                ,(53,-33,26,8,8,26,-33,53)
                ,(-12,-62,-33,-7,-7,-33,-62,-12)
                ,(68,-12,53,-8,-8,53,-12,68))


class PC_Choice():
    def __init__(self,ID,t1,t2,PointArray2D_1,PointArray2D_2):
        self.ID = ID
        self.t1 = t1
        self.t2 = t2
        self.PointA6561Tuple_1 = Make6561PointA_Tuple(PointArray2D_1)
        self.PointA6561Tuple_2 = Make6561PointA_Tuple(PointArray2D_2)

    def CulcBlackPoint(self,BoardStateNumbers,CurrentTurnNumber):
        PutablePositionNum_Black = len(MakePutablePositionList(BoardStateNumbers,1)) #この部分の計算が重くなりそうなので前半だけでいいかも
        PutablePositionNum_White = len(MakePutablePositionList(BoardStateNumbers,2))
        PointB = PutablePositionNum_Black - PutablePositionNum_White

        PointA = 0
        if CurrentTurnNumber <= 25:
            for row in range(8):
                i = row if row<=3 else 7-row #iは0~3
                PointA += self.PointA6561Tuple_1[BoardStateNumbers[0][row]][i]
            return PointA + self.t1 * PointB
        elif CurrentTurnNumber <= 50: #最初に4枚置いてあるので、残りマス数が10になるまで
            for row in range(8):
                i = row if row<=3 else 7-row
                PointA += self.PointA6561Tuple_2[BoardStateNumbers[0][i]][i]
            return PointA + self.t2 * PointB

    def MinMaxChoice(self,BoardStateNumbers,PreviousTurnColor,CurrentDepth,EndDepth,UpperDepthPoint,CurrentTurnNumber):
        CurrentDepth += 1

        #次の番になる色の確定
        TurnColor = OppositeColor(PreviousTurnColor)
        PutablePositionSet = MakePutablePositionList(BoardStateNumbers,TurnColor)
        alphabeta = True
        if PutablePositionSet == set([]):
            TurnColor = OppositeColor(TurnColor)
            PutablePositionSet = MakePutablePositionList(BoardStateNumbers,TurnColor)
            alphabeta = False
            if PutablePositionSet == set([]):
                return self.CulcBlackPoint(BoardStateNumbers,CurrentTurnNumber)
        if CurrentDepth ==  1: #最後は置く位置を返すので、PutablePositionsを(順序が関係ない)セットにしてしまうと返せなくなる。そのため整列してListにする必要がある
            PutablePositionSet = sorted(PutablePositionSet)
        #次の番の色確定完了

        PointList = []
        CurrentDepthPoint = -float("inf") if TurnColor == 1 else float("inf")
        if alphabeta: #前の番の色≠今回の番の色なので、αβ法適用
            for PutPosition in PutablePositionSet:
                NewBoardStateNumbers = CuclBoardStateNumber_OnePut(BoardStateNumbers,*PutPosition,TurnColor)
                if CurrentDepth == EndDepth:
                    Point = self.CulcBlackPoint(NewBoardStateNumbers,CurrentTurnNumber)
                else:
                    Point = self.MinMaxChoice(NewBoardStateNumbers,TurnColor,CurrentDepth,EndDepth,CurrentDepthPoint,CurrentTurnNumber)
                    CurrentDepthPoint = max(Point,CurrentDepthPoint) if TurnColor == 1 else min(Point,CurrentDepthPoint)
                #αβ法適用できるか判断
                if (Point < UpperDepthPoint and TurnColor == 2) or (Point > UpperDepthPoint and TurnColor == 1):
                    return Point #上の階層に値を返してPointListの作成を終了,関数は一度returnするとfor内であろうと処理を停止する。
                else:
                    PointList.append(Point)

            #PointListの作成が完了したので、上のレベルにPointを返す処理
            if CurrentDepth == 1: #CurrentDepth=1 の時は点数でなく石を置く位置(i,j)を返す必要がある。
                if TurnColor == 1: #PutablePositionSetが黒番の場合
                    FinalPoint = max(PointList)
                else: #PutablePositionSetが白番の場合
                    FinalPoint = min(PointList)
                return PutablePositionSet[PointList.index(FinalPoint)]
            else: #CurrentDepth!=1 なので上のレベルに点数を返す
                if TurnColor == 1: #PutablePositionSetが黒番の場合
                    return max(PointList)
                else: #PutablePositionSetが白番の場合
                    return min(PointList)


        else: #前の番の色=今回の番の色なので、αβ法適用不可、この場合CurrentDepth=1 となることはありえない
            for PutPosition in PutablePositionSet:
                NewBoardStateNumbers = CuclBoardStateNumber_OnePut(BoardStateNumbers,*PutPosition,TurnColor)
                if CurrentDepth == EndDepth:
                    PointList.append(self.CulcBlackPoint(NewBoardStateNumbers,CurrentTurnNumber))
                else:
                    PointList.append(self.MinMaxChoice(NewBoardStateNumbers,TurnColor,CurrentDepth,EndDepth,CurrentDepthPoint,CurrentTurnNumber))
                    CurrentDepthPoint = max(PointList[-1],CurrentDepthPoint) if TurnColor == 1 else min(Point,CurrentDepthPoint)
            if TurnColor == 1: #PutablePositionSetが黒番の場合
                return max(PointList)
            else: #PutablePositionSetが白番の場合
                return min(PointList)


PC1 = PC_Choice(1,10,23,point_array1,point_array1)
BoardStateNumbers =  [[0,0,0,189,135,0,0,0] #横方向、一番右の石が1桁目を表す
                    , [0,0,0,189,135,0,0,0] #縦方向、一番下の石が1桁目を表す
                    , [0,0,0,0,54,108,54,0,0,0,0] #左下→右上方向、左下が一桁目
                    , [0,0,0,0,27,216,27,0,0,0,0]] #左上→右下方向、左上が一桁目
print(PC1.CulcBlackPoint(BoardStateNumbers,0))
print(PC1.MinMaxChoice(BoardStateNumbers,2,0,8,float("inf"),0))
