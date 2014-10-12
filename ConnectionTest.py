from array import array
from Connection import Connection

__author__ = 'Berni'

import unittest

#Test der Rückgabe von der Connection Methoden
class ConnectionTest(unittest.TestCase):

    def test_connect(self):
        con = Connection()
        self.assertTrue(con.connect())

    def test_disconnect(self):
        con = Connection()
        self.assertTrue(con.disconnect())

if __name__ == '__main__':
    unittest.main()
