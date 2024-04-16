#!/usr/bin/env python
'''A class to manage the API authentication'''
from flask import request


class Auth:
    def require_auth(self, path: str, excluded_paths: list) -> bool:
        '''Check if the authentication is required for the given path.'''
        return False

    def authorization_header(self, request=None) -> str:
        '''Get the authorization header from the request'''
        return None

    def current_user(self, request=None) -> type:
        '''Get the current user from the request'''
        return None
