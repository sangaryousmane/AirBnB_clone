#!/usr/bin/env python3

""" 
Magic __init__.py - turns a directory to a python package
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
