#!/usr/bin/env python3
'''Import request and List'''
from flask import request
from typing import List


class Auth:
    '''Class for managing API authentication'''
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''Check if the authentication is required for the given path.'''
        return False

    def authorization_header(self, request=None) -> str:
        '''Get the authorization header from the request'''
        return None

    def current_user(self, request=None) -> type:
        '''Get the current user from the request'''
        return None
