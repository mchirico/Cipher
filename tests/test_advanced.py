# -*- coding: utf-8 -*-

from .context import clib
from clib.util.cipher import Cipher

from unittest import TestCase


class AdvancedTestSuite(TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(clib.hmm())

    def test_cipher(self):
        cipher = Cipher()
        shift = 7
        expected_result = 'tvbzl pz jbal'

        s = 'mouse is cute'

        print(cipher.stringEncrypt(s, shift))

        self.assertEqual(expected_result, cipher.stringEncrypt(s, shift))
