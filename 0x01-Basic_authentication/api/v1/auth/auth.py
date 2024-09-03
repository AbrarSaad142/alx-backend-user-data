#!/usr/bin/env python3
"""Authentication module"""
from typing import List, TypeVar
from flask import request
import fnmatch


class Auth:
    """Authentication class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """hat returns False - path and excluded_paths"""
        if path:
            return False

    def authorization_header(self, request=None) -> str:
        """that returns None - request will be the Flask request object"""
        if request:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """that returns None - request will be the Flask request object"""
        return None
