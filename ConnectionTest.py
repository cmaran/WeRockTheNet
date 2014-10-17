from array import array
from ControlConnect import ControlConnect
from unittest.mock import MagicMock

__author__ = 'Bernhard Schwertberger'

import unittest

#Test der Rückgabe von der Connection Methoden
class ConnectionTest(unittest.TestCase):

    def test_connect(self):
        con = Connection()
        self.assertTrue(con.connect(ip, user, pw))

    def test_disconnect(self):
        con = Connection()
        self.assertTrue(con.disconnect())

    def test_gCurVer(self):
        con = Connection()
        m = MagicMock(return_value = none)


        cversion = con.getCurrentVersion()
        self.assertIsNotNOne(self,cversion)

if __name__ == '__main__':
    unittest.main()
