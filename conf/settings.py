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

# ADMIN_ACCOUNT_DATABASE = {
#     'engine': 'file_storage',
#     'name': 'admin_accounts',
#     'username': None,
#     'password': None,
#     'path': "%s/db" % BASE_DIR
# }
#
# TEACHER_ACCOUNT_DATABASE = {
#     'engine': 'file_storage',
#     'name': 'teacher_accounts',
#     'username': None,
#     'password': None,
#     'path': "%s/db" % BASE_DIR
# }

BASE_DATABASE = {
    'engine': 'file_storage',
    'name': 'base',
    'username': None,
    'password': None,
    'path': "%s/db" % BASE_DIR
}

DEFAULT_ADMIN_ACCOUNT = 'admin'
DEFAULT_ADMIN_PASSWORD = 'admin'