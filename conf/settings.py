# -*-coding: utf-8 -*-
# Auther： Henry Yuan
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ACCOUNT_DATABASE = {
    'engine': 'file_storage',
    'name': 'accounts',
    'username': None,
    'password': None,
    'path': "%s/db" % BASE_DIR
}

BASE_DATABASE = {
    'engine': 'file_storage',
    'name': 'base',
    'username': None,
    'password': None,
    'path': "%s/db" % BASE_DIR
}