from unittest.mock import Mock

__author__ = 'Isabella Dall Oglio'

import unittest

# list Pol:String

class MyTestCase(unittest.TestCase):
    def test_ListE(self):
        m = Mock()
        m.method()
        m.method.assertIsNone()

    def test_ListNotE(self):
        m = Mock()
        m.method()
        m.method.assertIsNotNone()

    def test_ListreturnString(self):
        m = Mock()
        st=m.method(return_value="Hallo")
        s="Policies"
        m.method.assertEqual(s,st)



if __name__ == '__main__':
    unittest.main()
