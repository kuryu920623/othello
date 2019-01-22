from Convert_StateNumbers_Board2D import *
from CulcBoardStateNumbers import *
import unittest



class Test_CuclBoardStateNumbers(unittest.TestCase):

    def test_CuclBoardStateNumber_OneStone(self):
        Board2D_1 =[[0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,2,1,0,0,0],
                    [0,0,0,1,2,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0]]

        BoardStateNum_1 = Board2D_to_BoardStateNumbers(Board2D_1)

        #(1,4)に2を追加
        Board2D_2 =[[0,0,0,0,0,0,0,0],
                    [0,0,0,0,2,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,2,1,0,0,0],
                    [0,0,0,1,2,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0]]

        BoardStateNum_2 = Board2D_to_BoardStateNumbers(Board2D_2)

        #(6,5)に1を追加
        Board2D_3 =[[0,0,0,0,0,0,0,0],
                    [0,0,0,0,2,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,2,1,0,0,0],
                    [0,0,0,1,2,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,1,0,0],
                    [0,0,0,0,0,0,0,0]]

        BoardStateNum_3 = Board2D_to_BoardStateNumbers(Board2D_3)

        #(0,7)に1を追加
        Board2D_4 =[[0,0,0,0,0,0,0,1],
                    [0,0,0,0,2,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,2,1,0,0,0],
                    [0,0,0,1,2,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,1,0,0],
                    [0,0,0,0,0,0,0,0]]

        BoardStateNum_4 = Board2D_to_BoardStateNumbers(Board2D_4)

        #(7,7)に2を追加
        Board2D_5 =[[0,0,0,0,0,0,0,1],
                    [0,0,0,0,2,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,2,1,0,0,0],
                    [0,0,0,1,2,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,1,0,0],
                    [0,0,0,0,0,0,0,2]]

        BoardStateNum_5 = Board2D_to_BoardStateNumbers(Board2D_5)

        #(0,0)に1を追加
        Board2D_6 =[[1,0,0,0,0,0,0,1],
                    [0,0,0,0,2,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,2,1,0,0,0],
                    [0,0,0,1,2,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,1,0,0],
                    [0,0,0,0,0,0,0,2]]

        BoardStateNum_6 = Board2D_to_BoardStateNumbers(Board2D_6)
        self.assertEqual(BoardStateNum_2,CuclBoardStateNumber_OneStone(BoardStateNum_1,1,4,2))
        self.assertEqual(BoardStateNum_3,CuclBoardStateNumber_OneStone(BoardStateNum_2,6,5,1))
        self.assertEqual(BoardStateNum_4,CuclBoardStateNumber_OneStone(BoardStateNum_3,0,7,1))
        self.assertEqual(BoardStateNum_5,CuclBoardStateNumber_OneStone(BoardStateNum_4,7,7,2))
        self.assertEqual(BoardStateNum_6,CuclBoardStateNumber_OneStone(BoardStateNum_5,0,0,1))

    def test_CuclBoardStateNumber_OnePut(self):
        Board2D_11 =    [[0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,2,1,0,0,0],
                         [0,0,0,1,2,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0]]
        BoardStateNum_11 = Board2D_to_BoardStateNumbers(Board2D_11)
        #(3,5)に2を置く
        Board2D_12 =    [[0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,2,2,2,0,0],
                        [0,0,0,1,2,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0]]
        BoardStateNum_12 = Board2D_to_BoardStateNumbers(Board2D_12)

        Board2D_21 =    [[0,0,2,0,0,2,0,0],
                         [2,0,1,0,1,0,0,0],
                         [0,1,1,1,0,0,0,0],
                         [2,1,0,1,1,1,1,2],
                         [0,1,1,1,0,0,0,0],
                         [2,0,1,0,1,0,0,0],
                         [0,0,1,0,0,1,0,0],
                         [0,0,2,0,0,0,2,0]]
        BoardStateNum_21 = Board2D_to_BoardStateNumbers(Board2D_21)
        #(3,2)に2を置く
        Board2D_22 =    [[0,0,2,0,0,2,0,0],
                         [2,0,2,0,2,0,0,0],
                         [0,2,2,2,0,0,0,0],
                         [2,2,2,2,2,2,2,2],
                         [0,2,2,2,0,0,0,0],
                         [2,0,2,0,2,0,0,0],
                         [0,0,2,0,0,2,0,0],
                         [0,0,2,0,0,0,2,0]]
        BoardStateNum_22 = Board2D_to_BoardStateNumbers(Board2D_22)

        Board2D_31 =    [[0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0]]
        BoardStateNum_31 = Board2D_to_BoardStateNumbers(Board2D_31)

        self.assertEqual(BoardStateNum_12,CuclBoardStateNumber_OnePut(BoardStateNum_11,3,5,2))
        self.assertEqual(BoardStateNum_22,CuclBoardStateNumber_OnePut(BoardStateNum_21,3,2,2))
if __name__ == '__main__':
    unittest.main()
