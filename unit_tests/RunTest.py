import unittest
from TestBoard import TestBoard
from TestTile import TestTile
from TestTilebag import TestTilebag
from TestPlayer import TestPlayer
from TestDictionary import TestDictionary
from TestManager import TestManager

boardSuite = unittest.TestLoader().loadTestsFromTestCase(TestBoard)
tileSuite = unittest.TestLoader().loadTestsFromTestCase(TestTile)
tilebagSuite = unittest.TestLoader().loadTestsFromTestCase(TestTilebag)
playerSuite = unittest.TestLoader().loadTestsFromTestCase(TestPlayer)
dictionarySuite = unittest.TestLoader().loadTestsFromTestCase(TestDictionary)
managerSuite = unittest.TestLoader().loadTestsFromTestCase(TestManager)



unittest.TextTestRunner(verbosity=2).run(boardSuite)
unittest.TextTestRunner(verbosity=2).run(tileSuite)
unittest.TextTestRunner(verbosity=2).run(tilebagSuite)
unittest.TextTestRunner(verbosity=2).run(playerSuite)
unittest.TextTestRunner(verbosity=2).run(dictionarySuite)
unittest.TextTestRunner(verbosity=2).run(managerSuite)

