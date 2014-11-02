from unittest import TestCase
from Control.Connection import Connection


class TestConnection(TestCase):

    def test_ConnectionRight(self):
        con = Connection
        self.assertTrue(con.checkcon(con, "10.0.100.10", 161, "5xHIT"))

    def test_ConnectionIPerror(self):
        con = Connection
        self.assertFalse(con.checkcon(con, "123.456.789.10", 161, "5xHIT"))

    def test_ConnectionPorterror(self):
        con = Connection
        self.assertFalse(con.checkcon(con, "10.0.100.10", 0, "5xHIT"))

    def test_ConnectionGrouperror(self):
        con = Connection
        self.assertFalse(con.checkcon(con, "10.0.100.10", 161, "55555"))

    def test_getright(self):
        con = Connection
        a = con.get(con, '1.3.6.1.4.1.3224.10.1', '5xHIT', "10.0.100.10", 161)
        self.assertIsNotNone(a)

    def test_getfail(self):
        con = Connection
        a = con.get(con, '1.3.6.1.4.1.3224.10.1', '5xHIT', "10.0.100.10", 0)
        b = con.get(con, '1.3.6.1.4.1.3224.10.1', '5xHIT', "10.0.100.10", 161)
        self.assertNotEqual(a,b)


    def test_getBulkright(self):
        con = Connection
        a = con.getbulk(con, '1.3.6.1.4.1.3224.10.1', '5xHIT', "10.0.100.10", 161)
        self.assertIsNotNone(a)

    def test_getBulkfail(self):
        con = Connection
        a = con.getbulk(con, '1.3.6.1.4.1.3224.10.1', '5xHIT', "10.0.100.10", 0)
        b = con.getbulk(con, '1.3.6.1.4.1.3224.10.1', '5xHIT', "10.0.100.10", 161)
        self.assertNotEqual(a,b)
