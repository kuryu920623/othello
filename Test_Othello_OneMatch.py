from Convert_StateNumbers_Board2D import *
from Othello_OneMatch import *
import unittest

Board2D_1 =[[0,1,2,0,1,2,0,1],
            [0,1,2,0,1,2,0,1],
            [0,1,2,0,1,2,0,1],
            [0,1,2,0,1,2,0,1],
            [0,1,2,0,1,2,0,1],
            [0,1,2,0,1,2,0,1],
            [0,1,2,0,1,2,0,1],
            [0,1,2,0,1,2,0,1]]
BoardStateNum_1 = Board2D_to_BoardStateNumbers(Board2D_1)

Board2D_2 =[[0,1,2,0,1,2,0,0],
            [1,2,0,1,2,0,1,0],
            [1,1,1,1,1,1,1,1],
            [0,0,2,0,0,2,0,1],
            [1,1,0,0,0,1,1,1],
            [1,2,0,1,2,0,1,0],
            [0,1,2,0,1,2,0,1],
            [1,2,0,1,2,0,1,0]]
BoardStateNum_2 = Board2D_to_BoardStateNumbers(Board2D_2)

print(MakePutablePositionList(BoardStateNum_1,2))

print(MakePutablePositionList(BoardStateNum_1,1))

print(MakePutablePositionList(BoardStateNum_2,2))

print(MakePutablePositionList(BoardStateNum_2,1))

class Test(unittest.TestCase):
    a = 1
