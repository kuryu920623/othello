from Convert_StateNumbers_Board2D import *
import unittest

Board2D_1 =[[0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,2,1,0,0,0],
            [0,0,0,1,2,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0]]

Board2D_2 =[[2,2,2,2,2,2,2,2],
            [2,2,2,2,2,2,2,2],
            [2,2,2,2,2,2,2,2],
            [2,2,2,2,2,2,2,2],
            [2,2,2,2,2,2,2,2],
            [2,2,2,2,2,2,2,2],
            [2,2,2,2,2,2,2,2],
            [2,2,2,2,2,2,2,2]]

Board2D_3 =[[1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1]]

Board2D_4 =[[0,1,2,0,1,2,0,1],
            [0,1,2,0,1,2,0,1],
            [0,1,2,0,1,2,0,1],
            [0,1,2,0,1,2,0,1],
            [0,1,2,0,1,2,0,1],
            [0,1,2,0,1,2,0,1],
            [0,1,2,0,1,2,0,1],
            [0,1,2,0,1,2,0,1]]

Board2D_5 =[[0,1,2,0,1,2,0,1],
            [1,2,0,1,2,0,1,2],
            [1,1,1,1,1,1,1,1],
            [0,1,2,0,1,2,0,1],
            [1,1,1,1,1,1,1,1],
            [1,2,0,1,2,0,1,2],
            [0,1,2,0,1,2,0,1],
            [1,2,0,1,2,0,1,2]]

BoardStateNum_1 =   [[0,0,0,189,135,0,0,0]
                    ,[0,0,0,189,135,0,0,0]
                    ,[0,0,0,0,54,108,54,0,0,0,0]
                    ,[0,0,0,0,27,216,27,0,0,0,0]]

BoardStateNum_2 =   [[6560,6560,6560,6560,6560,6560,6560,6560]
                    ,[6560,6560,6560,6560,6560,6560,6560,6560]
                    ,[26,80,242,728,2186,6560,2186,728,242,80,26]
                    ,[26,80,242,728,2186,6560,2186,728,242,80,26]]

BoardStateNum_3 =   [[3280,3280,3280,3280,3280,3280,3280,3280]
                    ,[3280,3280,3280,3280,3280,3280,3280,3280]
                    ,[13,40,121,364,1093,3280,1093,364,121,40,13]
                    ,[13,40,121,364,1093,3280,1093,364,121,40,13]]

BoardStateNum_4 =   [[1261,1261,1261,1261,1261,1261,1261,1261]
                    ,[0,3280,6560,0,3280,6560,0,3280]
                    ,[21,21,102,588,588,2775,925,308,102,34,11]
                    ,[21,21,102,588,588,2775,925,308,102,34,11]]

class Test_Convert(unittest.TestCase):
    def test_BoardStateNumbers_to_Board2D(self):
        self.assertEqual(BoardStateNumbers_to_Board2D(BoardStateNum_1),Board2D_1)
        self.assertEqual(BoardStateNumbers_to_Board2D(BoardStateNum_2),Board2D_2)
        self.assertEqual(BoardStateNumbers_to_Board2D(BoardStateNum_3),Board2D_3)
        self.assertEqual(BoardStateNumbers_to_Board2D(BoardStateNum_4),Board2D_4)

    def test_Board2D_to_BoardStateNumbers(self):
        self.assertEqual(Board2D_to_BoardStateNumbers(Board2D_1),BoardStateNum_1)
        self.assertEqual(Board2D_to_BoardStateNumbers(Board2D_2),BoardStateNum_2)
        self.assertEqual(Board2D_to_BoardStateNumbers(Board2D_3),BoardStateNum_3)
        self.assertEqual(Board2D_to_BoardStateNumbers(Board2D_4),BoardStateNum_4)

if __name__ == '__main__':
    unittest.main()
