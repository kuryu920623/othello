import unittest
from Othello_Make6561TurnableRange import *

class Test_PutableRange(unittest.TestCase):
    def test_TurnStoneRange_Left(self):
        self.assertEqual(TurnStoneRange_Left(black,"01201201",0),0)
        self.assertEqual(TurnStoneRange_Left(black,"01201201",1),0)
        self.assertEqual(TurnStoneRange_Left(black,"01201201",2),0)
        self.assertEqual(TurnStoneRange_Left(black,"01201201",3),1)
        self.assertEqual(TurnStoneRange_Left(white,"21021021",2),1)
        self.assertEqual(TurnStoneRange_Left(white,"00100100",4),0)
        self.assertEqual(TurnStoneRange_Left(black,"12222220",7),6)
        self.assertEqual(TurnStoneRange_Left(black,"12222220",0),0)
        self.assertEqual(TurnStoneRange_Left(white,"10110100",1),0)
        self.assertEqual(TurnStoneRange_Left(white,"00000000",5),0)
        self.assertEqual(TurnStoneRange_Left(black,"12201220",7),2)
        self.assertEqual(TurnStoneRange_Left(black,"22202100",6),0)

    def test_TurnStoneRange_Right(self):
        self.assertEqual(TurnStoneRange_Right(black,"21021021",0),0)
        self.assertEqual(TurnStoneRange_Right(black,"21021021",1),0)
        self.assertEqual(TurnStoneRange_Right(black,"21021021",2),1)
        self.assertEqual(TurnStoneRange_Right(black,"21021021",5),1)
        self.assertEqual(TurnStoneRange_Right(white,"21021021",2),0)
        self.assertEqual(TurnStoneRange_Right(black,"21021021",5),1)
        self.assertEqual(TurnStoneRange_Right(black,"01201201",0),0)
        self.assertEqual(TurnStoneRange_Right(black,"01201201",3),0)
        self.assertEqual(TurnStoneRange_Right(white,"21021021",2),0)
        self.assertEqual(TurnStoneRange_Right(white,"00100100",4),0)
        self.assertEqual(TurnStoneRange_Right(black,"02222221",0),6)
        self.assertEqual(TurnStoneRange_Right(black,"02222221",7),0)
        self.assertEqual(TurnStoneRange_Right(black,"12222220",0),0)
        self.assertEqual(TurnStoneRange_Right(white,"10110100",1),0)
        self.assertEqual(TurnStoneRange_Right(white,"00000000",5),0)
        self.assertEqual(TurnStoneRange_Right(black,"12200221",4),2)
        self.assertEqual(TurnStoneRange_Right(black,"22202100",6),0)

if __name__ == '__main__':
    unittest.main()
