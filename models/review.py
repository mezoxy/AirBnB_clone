#!/usr/bin/python3
"""The module: review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review: A subclass of BaseModel"""

    place_id = ""
    user_id = ""
    text = ""
