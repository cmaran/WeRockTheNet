__author__ = 'Bernhard Schwertberger'

import unittest
from unittest.mock import Mock


#Methode zum Auslesen der Regeln.
#Parameter bitte anpassen falls unzureichend oder falsch.
#Test wird erfolgreich abgeschlossen wenn die Rückgabe nicht None war.
class Modeltest(unittest.TestCase):

    def testGetAllData(self):
        model = Mock()
        tuples = model.getAllData(return_value = [(1,2,3,4,5),(1,2,3,4,5)])
        assert isinstance(tuples, object)
        for x in tuples:
            self.assertIsNotNone(tuples[x])

    def testGetNext(self):
        model = Mock
        tuple = model.getNext(return_value = (1,2,3,4,5))
        self.assertIsNotNone(tuple)

if __name__ == '__main__':
    unittest.main()
