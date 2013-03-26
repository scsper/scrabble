import unittest
from TestBoard import TestBoard
from TestTile import TestTile
from TestTilebag import TestTilebag
from TestPlayer import TestPlayer

boardSuite = unittest.TestLoader().loadTestsFromTestCase(TestBoard)
tileSuite = unittest.TestLoader().loadTestsFromTestCase(TestTile)
tilebagSuite = unittest.TestLoader().loadTestsFromTestCase(TestTilebag)
playerSuite = unittest.TestLoader().loadTestsFromTestCase(TestPlayer)

unittest.TextTestRunner(verbosity=2).run(boardSuite)
unittest.TextTestRunner(verbosity=2).run(tileSuite)
unittest.TextTestRunner(verbosity=2).run(tilebagSuite)
unittest.TextTestRunner(verbosity=2).run(playerSuite)
