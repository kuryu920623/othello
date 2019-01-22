'''
BaordStateNumbersとBoard2D(盤面の空黒白をそのまま表す二次元List)を相互に変換する。
基本的にはデバック用として使用?
'''

from CulcBoardStateNumbers import *

def Board2D_to_BoardStateNumbers(Board2D):
    BoardStateNumbers = [[],[],[],[]]

    #(1)横方向
    for i in range(8):
        Num_i = 0
        for j in range(8):
            Num_i += Board2D[i][7-j] * 3 ** j
        BoardStateNumbers[0].append(Num_i)

    #(2)横方向
    for i in range(8):
        Num_i = 0
        for j in range(8):
            Num_i += Board2D[7-j][i] * 3 ** j
        BoardStateNumbers[1].append(Num_i)

    #(3)右上→左下方向
    for i in range(6):
        Num_i = 0
        for j in range(i+3):
            Num_i += Board2D[i-j+2][j] * 3 ** j
        BoardStateNumbers[2].append(Num_i)
    for i in range(5):
        Num_i = 0
        for j in range(7-i):
            Num_i += Board2D[7-j][1+i+j] * 3 ** j
        BoardStateNumbers[2].append(Num_i)

    #(4)右下→左上方向
    for i in range(6):
        Num_i = 0
        for j in range(i+3):
            Num_i += Board2D[5-i+j][j] * 3 ** j
        BoardStateNumbers[3].append(Num_i)
    for i in range(5):
        Num_i = 0
        for j in range(7-i):
            Num_i += Board2D[j][1+i+j] * 3 ** j
        BoardStateNumbers[3].append(Num_i)

    return BoardStateNumbers

#10進法表記の数字xをN進法表記の文字列に変換して返す。
def Base_10toN(X,n):
    if (int(X/n)):
        return Base_10toN(int(X/n), n)+str(X%n)
    return str(X%n)

def BoardStateNumbers_to_Board2D(BoardStateNumbers):
    Board2D = []
    for i in BoardStateNumbers[0]:
        Base3 = Base_10toN(i,3).zfill(8)
        Board2D.append(list(map(int,Base3)))
    return Board2D

Board2D =   [[0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,2,1,0,0,0],
            [0,0,0,1,2,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,2,0],
            [0,0,0,0,0,0,0,0]]

Board2D_2 =[[2,2,2,2,2,2,2,2],
            [2,2,2,2,2,2,2,2],
            [2,2,2,2,2,2,2,2],
            [2,2,2,2,2,2,2,2],
            [2,2,2,2,2,2,2,2],
            [2,2,2,2,2,2,2,2],
            [2,2,2,2,2,2,2,2],
            [2,2,2,2,2,2,2,2]]

# print(Board2D_to_BoardStateNumbers(Board2D))
# print(BoardStateNumbers_to_Board2D(Board2D_to_BoardStateNumbers(Board2D)))
#
#
#
# a = Board2D_to_BoardStateNumbers(Board2D)
# a2 = CuclBoardStateNumber_OnePut(a,3,2,1)
#
# for i in a2:
#     print(i)
#
# print()
#
# for i in BoardStateNumbers_to_Board2D(a2):
#     print(i)
