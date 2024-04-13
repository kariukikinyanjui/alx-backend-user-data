#!/usr/bin/env python3
'''a hash_password function'''
import bcrypt


def hash_password(password: str) -> bytes:
    '''hash a password'''

    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(stored_pwd: bytes, input_pwd: str) -> bool:
    '''validate user passwords'''
    return bcrypt.checkpw(input_pwd.encode(), stored_pwd)
