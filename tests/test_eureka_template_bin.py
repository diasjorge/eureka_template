import unittest
import os
import subprocess


class TestEurekaTemplateBin(unittest.TestCase):

    def test_help(self):
        bin_file = os.path.join(os.path.dirname(__file__),
                                '..', 'bin', 'eureka-template')
        self.assertEqual(0,
                         subprocess.check_call([bin_file, '-h'],
                                               stdout=open(os.devnull, 'wb')))
