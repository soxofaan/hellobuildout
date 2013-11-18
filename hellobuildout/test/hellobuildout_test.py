
import sys
import unittest
import StringIO

import hellobuildout


class HelloBuildoutTest(unittest.TestCase):

    def setUp(self):
        self._original_stdout = sys.stdout
        sys.stdout = StringIO.StringIO()

    def tearDown(self):
        sys.stdout = self._original_stdout

    def test_hello_world(self):
        hellobuildout.hello_world()
        result = sys.stdout.getvalue()
        self.assertEqual(result, 'Hello world.\n')

    def test_hello_world_loud(self):
        hellobuildout.hello_world(True)
        result = sys.stdout.getvalue()
        self.assertEqual(result, 'HELLO WORLD!\n')


    def test_hello_buildout_default(self):
        hellobuildout.hello_buildout()
        result = sys.stdout.getvalue()
        self.assertEqual(result, 'Hello zc.buildout.\n')

    def test_hello_buildout_nonpicky(self):
        hellobuildout.hello_buildout(False)
        result = sys.stdout.getvalue()
        self.assertEqual(result, 'Hello Buildout.\n')
