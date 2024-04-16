#!/usr/bin/env python3
'''A class to manage the API authentication'''
from flask import request
from typing import List


class Auth:
    def require_auth(self, path: str, excluded_paths: list) -> bool:
        '''Check if the authentication is required for the given path.'''
        return False

        return True

    def authorization_header(self, request=None) -> str:
        '''Get the authorization header from the request'''
        return None

    def current_user(self, request=None) -> type:
        '''Get the current user from the request'''
        return None
