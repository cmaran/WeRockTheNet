__author__ = 'Berni'

import unittest
from Read import Read

#Methode zum Auslesen der Regeln.
#Parameter bitte anpassen falls unzureichend oder falsch.
#Test wird erfolgreich abgeschlossen wenn die Rückgabe nicht None war.
class ReadTest(unittest.TestCase):
    def testRead(self):
        read = Read()
        oidtuple = read.readRules(snmpEngine, routerip, mib)
        self.assertIsNotNone(oidtuple)

if __name__ == '__main__':
    unittest.main()
