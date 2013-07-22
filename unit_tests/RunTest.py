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


print "\nRunning the board suite... "
unittest.TextTestRunner(verbosity=1).run(boardSuite)

print "\n\nRunning the tile suite... "
unittest.TextTestRunner(verbosity=1).run(tileSuite)

print "\n\nRunning the tilebag suite... "
unittest.TextTestRunner(verbosity=1).run(tilebagSuite)

print "\n\nRunning the player suite... "
unittest.TextTestRunner(verbosity=1).run(playerSuite)

print "\n\nRunning the dictionary suite... "
unittest.TextTestRunner(verbosity=1).run(dictionarySuite)

print "\n\nRunning the manager suite... "
unittest.TextTestRunner(verbosity=1).run(managerSuite)

