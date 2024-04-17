#!/usr/bin/env python3
'''Import request and List'''
from flask import request
from typing import List


class Auth:
    '''Class for managing API authentication'''
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''Check if the authentication is required for the given path.'''
        if path is None:
            return True
        if excluded_paths is None or not excluded_paths:
            return True

        path = path.rstrip('/') + '/'

        for excluded_path in excluded_paths:
            if path.startswith(excluded_path):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        '''Get the authorization header from the request'''
        return None

    def current_user(self, request=None) -> type:
        '''Get the current user from the request'''
        return None
