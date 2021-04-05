import unittest
from mkvhost.sysconfig import *

class TestSysConfig(unittest.TestCase):

    def test_init_sysconfig(self):
        self.assertEqual(SysConfig().path_avail[0], '/etc/nginx/sites-available')
