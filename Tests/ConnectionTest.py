from array import array
from unittest.mock import Mock

__author__ = 'Bernhard Schwertberger'

import unittest

# Test der Rückgabe von der Connection Methoden vorzeitig mit m
class ConnectionTest(unittest.TestCase):
    def test_connect(self):
        m = Mock()
        m.method(1,2,3)
        m.method.assert_called_with(1,2,3)

    def test_connectFail(self):
        m = Mock()
        m.method(2,2,3)
        m.method.assert_called_with(1,2,3)

    def test_disconnect(self):
        m = Mock(return_value=True)
        self.assertTrue(m())

    def test_disconnectFail(self):
        m = Mock(return_value=False)
        self.assertTrue(m())

    def test_gCurVer(self):
        m = Mock()
        m.version = "V2"
        cversion = m.version
        sversion = "V3"
        self.assertEqual(sversion, cversion)

    def test_gCurVerRight(self):
        m = Mock(return_value="V3")
        sversion = "V3"
        cversion = m()
        self.assertEqual(sversion, cversion)

if __name__ == '__main__':
    unittest.main()
