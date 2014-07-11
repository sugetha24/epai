import unittest
from eapi import *
import socket

class eapiTestCases (unittest.TestCase):
    def test_connect_box (self):
        self.assertRaises (IOError, connect_box ("url.txt"))
    
    def test_run_cmds (self):
        self.assertRaises (socket.error, run_cmds())

    def test_get_cmds (self):
        self.assertRaises (IOError, get_cmds ("cmd.txt"))
    
if __name__ == "__main__":
    unittest.main()
