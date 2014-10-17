__author__ = 'Bernhard Schwertberger'

import unittest
from Model import Model

#Methode zum Auslesen der Regeln.
#Parameter bitte anpassen falls unzureichend oder falsch.
#Test wird erfolgreich abgeschlossen wenn die Rückgabe nicht None war.
class Modeltest(unittest.TestCase):

    def testGetAllData(self):
        model = Model()
        tuples = []
        tuples = model.getAllData()
        for x in tuples:
            self.assertIsNotNone(tuples[x])

    def testGetNext(self):
        model = Model()
        tuple = model.getNext()
        self.assertIsNotNone(tuple)

if __name__ == '__main__':
    unittest.main()
