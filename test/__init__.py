#!/usr/bin/python3
"""
This module initialize the models package
"""

from engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()