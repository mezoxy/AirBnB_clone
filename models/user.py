#!/usr/bin/python3
"""The module: user"""
from models.base_model import BaseModel


class User(BaseModel):
    """User: Subclass of BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
