__author__ = 'Bernhard Schwertberger'

import unittest

#Test der Methode um den Thruput auszulesen
#Parameter bitte anpassen falls unzureichend oder falsch.
#Test wird erfolgreich abgeschlossen wenn die Rückgabe nicht None war.
class ThruPutTest(unittest.TestCase):
    def test_something(self):
        thru = ThruPut(refreshrate, snmpEngine, routerip, mib)
        self.assertIsNotNone(thru)


if __name__ == '__main__':
    unittest.main()
