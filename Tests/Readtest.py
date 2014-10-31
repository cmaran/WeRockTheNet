__author__ = 'Bernhard Schwertberger'

import unittest
from unittest.mock import Mock


#Methode zum Auslesen der Regeln.
#Parameter bitte anpassen falls unzureichend oder falsch.
#Test wird erfolgreich abgeschlossen wenn die Rückgabe nicht None war.
class Modeltest(unittest.TestCase):

    def testGetNext(self):
        model = Mock
        model.return_value = (1,2,3,4,5)
        tuple = model()
        self.assertIsNotNone(tuple)

    def testGetNext(self):
        model = Mock
        model.return_value = None
        tuple = model()
        self.assertIsNotNone(tuple)

if __name__ == '__main__':
    unittest.main()
