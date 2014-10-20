__author__ = 'Bernhard Schwertberger'

import unittest
from unittest.mock import Mock

#Test der Methode um den Thruput auszulesen
#Parameter bitte anpassen falls unzureichend oder falsch.
#Test wird erfolgreich abgeschlossen wenn die Rückgabe nicht None war.
class ThruPutTest(unittest.TestCase):
    def test_something(self):
        thru = Mock("50", "V3", "10.0.100.10", "1.3.6.1.4.1.3224.1.14")
        self.assertIsNotNone(thru)

if __name__ == '__main__':
    unittest.main()
