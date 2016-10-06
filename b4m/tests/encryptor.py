#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: chat@jat.email -*-

import os
import unittest

from b4m.libs import encryptor


class TestEncryptor(unittest.TestCase):
    def test_verify_password(self):
        password = 'this is a password'
        encrypted_password, key = encryptor.encrypt_password(password)

        self.assertTrue(encryptor.verify_password(password, key, encrypted_password))
        self.assertFalse(encryptor.verify_password('wrong password', key, encrypted_password))
        self.assertFalse(encryptor.verify_password(password, encryptor.encode('wrong key'.encode('utf-8')), encrypted_password))
        self.assertFalse(encryptor.verify_password(password, key, 'wrong encrypted password'))

    def test_gcm_decrypt(self):
        message = u'我能吞下玻璃而不伤身体。'
        key = encryptor.encode(os.urandom(32))
        ciphertext, iv, tag = encryptor.gcm_encrypt(message, key, 'authenticated but not encrypted payload')

        self.assertEqual(message, encryptor.gcm_decrypt(ciphertext, key, 'authenticated but not encrypted payload', iv, tag))
        self.assertFalse(encryptor.gcm_decrypt(encryptor.encode('wrong ciphertext'.encode('utf-8')), key, 'wrong authenticated data', iv, tag))
        self.assertFalse(encryptor.gcm_decrypt(ciphertext, key, 'wrong authenticated data', iv, tag))
        self.assertFalse(encryptor.gcm_decrypt(ciphertext, key, 'authenticated but not encrypted payload', encryptor.encode('wrong iv'.encode('utf-8')), tag))
        self.assertFalse(encryptor.gcm_decrypt(ciphertext, key, 'authenticated but not encrypted payload', iv, 'wrong tag'))

    def test_decrypt(self):
        message = u'我能吞下玻璃而不伤身体。'
        key = encryptor.encode(os.urandom(32))
        ciphertext, iv = encryptor.encrypt(message, key)

        self.assertEqual(message, encryptor.decrypt(ciphertext, key, iv))
        self.assertFalse(encryptor.decrypt(encryptor.encode('wrong ciphertext'.encode('utf-8')), key, iv))
        self.assertFalse(encryptor.decrypt(ciphertext, key, 'wrong iv'))
        self.assertFalse(encryptor.decrypt(ciphertext, key, encryptor.encode(os.urandom(16))))


if __name__ == '__main__':
    unittest.main()
