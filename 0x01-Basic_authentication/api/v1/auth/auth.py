#!/usr/bin/env python3
'''A class to manage the API authentication'''
from flask import request
from typing import List, TypeVar


class Auth:
    def require_auth(self, path: str, excluded_paths: list) -> bool:
        '''Check if the authentication is required for the given path.'''
        if path is None:
            return True

        if excluded_paths is None or excluded_paths == []:
            return True

        if path in excluded_paths:
            return False

        for excluded_path in excluded_paths:
            if excluded_path.startwith(path):
                return False
            elif path.startwith(excluded_path):
                return False
            elif excluded_path[-1] == "*":
                if path.startswith(excluded_path[:-1]):
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        '''Get the authorization header from the request'''
        if request is None:
            return None
        header = request.headers.get('Authentication')
        if header is None:
            return None
        return header

    def current_user(self, request=None) -> type:
        '''Get the current user from the request'''
        return None
