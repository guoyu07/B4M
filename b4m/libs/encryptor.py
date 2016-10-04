#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: chat@jat.email -*-

import os

from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend as _default_backend
from cryptography.exceptions import InvalidSignature


default_backend = _default_backend()


def encrypt_password(password, key=None):
    if key:
        key = bytes.fromhex(key)
        verify = True
    else:
        key = os.urandom(32)
        verify = False

    h = hmac.HMAC(key, hashes.SHA256(), backend=default_backend)
    h.update(password.encode('utf-8'))

    if verify:
        return h

    return h.finalize().hex(), key.hex()


def verify_password(password, key, encrypted_password):
    try:
        encrypt_password(password, key).verify(bytes.fromhex(encrypted_password))
    except InvalidSignature:
        return False
    else:
        return True


def encrypt(plaintext, key, associated_data):
    iv = os.urandom(12)

    encryptor = Cipher(
        algorithms.AES(bytes.fromhex(key)),
        modes.GCM(iv),
        backend=default_backend
    ).encryptor()

    encryptor.authenticate_additional_data(associated_data.encode('utf-8'))

    return (encryptor.update(plaintext.encode('utf-8')) + encryptor.finalize()).hex(), iv.hex(), encryptor.tag.hex()


def decrypt(ciphertext, key, associated_data, iv, tag):
    decryptor = Cipher(
        algorithms.AES(bytes.fromhex(key)),
        modes.GCM(bytes.fromhex(iv), bytes.fromhex(tag)),
        backend=default_backend
    ).decryptor()

    decryptor.authenticate_additional_data(associated_data.encode('utf-8'))

    return (decryptor.update(bytes.fromhex(ciphertext)) + decryptor.finalize()).decode('utf-8')


if __name__ == '__main__':
    password = 'this is a password'
    encrypted_password, key = encrypt_password(password)
    print(encrypted_password, key)
    print(
        verify_password(password, key, encrypted_password),
        verify_password('wrong password', key, encrypted_password)
    )

    key = os.urandom(32).hex()
    ciphertext, iv, tag = encrypt(
        u'我能吞下玻璃而不伤身体。',
        key,
        'authenticated but not encrypted payload'
    )
    print(ciphertext, key, iv, tag)
    print(decrypt(
        ciphertext,
        key,
        'authenticated but not encrypted payload',
        iv,
        tag
    ))
