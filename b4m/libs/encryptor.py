#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: chat@jat.email -*-

import os
import base64
from binascii import Error

from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend as _default_backend
from cryptography.exceptions import InvalidSignature, InvalidTag


default_backend = _default_backend()


def encode(*bytes):
    return base64.b64encode(bytes[0]).decode('ascii') if len(bytes) == 1 else [encode(i) for i in bytes]


def decode(*str):
    return base64.b64decode(str[0], validate=True) if len(str) == 1 else [decode(i) for i in str]


def encrypt_password(password, key=None):
    if key:
        key = decode(key)
        verify = True
    else:
        key = os.urandom(32)
        verify = False

    h = hmac.HMAC(key, hashes.SHA256(), backend=default_backend)
    h.update(password.encode('utf-8'))

    if verify:
        return h

    return encode(h.finalize(), key)


def verify_password(password, key, encrypted_password):
    try:
        encrypt_password(password, key).verify(decode(encrypted_password))
    except (Error, InvalidSignature):
        return False

    return True


def gcm_encrypt(plaintext, key, associated_data):
    # AES len(decode(key))*8 GCM
    # only 128, 192 or 256 bits long supported.

    try:
        key = decode(key)
    except Error:
        return False

    # 12 bytes IV is strongly suggested. do NOT change it.
    iv = os.urandom(12)

    encryptor = Cipher(algorithms.AES(key), modes.GCM(iv), backend=default_backend).encryptor()

    encryptor.authenticate_additional_data(associated_data.encode('utf-8'))

    return encode(encryptor.update(plaintext.encode('utf-8')) + encryptor.finalize(), iv, encryptor.tag)


def gcm_decrypt(ciphertext, key, associated_data, iv, tag):
    try:
        ciphertext, key, iv, tag = decode(ciphertext, key, iv, tag)
    except Error:
        return False

    decryptor = Cipher(algorithms.AES(key), modes.GCM(iv, tag), backend=default_backend).decryptor()

    decryptor.authenticate_additional_data(associated_data.encode('utf-8'))

    try:
        return (decryptor.update(ciphertext) + decryptor.finalize()).decode('utf-8')
    except InvalidTag:
        return False


def encrypt(plaintext, key):
    # AES len(decode(key))*8 CBC
    # only 128, 192 or 256 bits long supported.

    try:
        key = decode(key)
    except Error:
        return False

    # iv size = aes block size = 128 bits = 16 bytes
    iv = os.urandom(16)

    encryptor = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend).encryptor()

    plaintext = plaintext.encode('utf-8')

    if len(plaintext) % 16 != 0:
        plaintext += b' ' * (16 - len(plaintext) % 16)

    return encode(encryptor.update(plaintext) + encryptor.finalize(), iv)


def decrypt(ciphertext, key, iv):
    try:
        ciphertext, key, iv = decode(ciphertext, key, iv)
    except Error:
        return False

    decryptor = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend).decryptor()

    try:
        return (decryptor.update(ciphertext) + decryptor.finalize()).decode('utf-8').strip()
    except UnicodeDecodeError:
        return False
