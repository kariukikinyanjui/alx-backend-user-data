#!/usr/bin/env python3
'''Define the _hash_password method'''
from db import DB
from user import User
import bcrypt


class Auth:
    '''Auth class to interact with the authentication database'''

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        '''Register a new user'''
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            pass

        hashed_password = self._hash_password(password)

        user = self._db.add_user(email, hashed_password)
        return user

    def _hash_password(self, password: str) -> bytes:
        '''Hash a password using bcrypt'''
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def valid_login(self, email: str, password: str) -> bool:
        '''Validate login credentials'''
        try:
            user = self._db.find_user_by(email=email)
            hashed_password = user.hashed_password.encode('utf-8')
            provided_password = password.encode('utf-8')
            return bcrypt.checkpw(provided_password, hashed_password)
        except:
            return False
