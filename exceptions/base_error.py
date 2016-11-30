# coding=utf-8
from flask import jsonify


class BaseError(Exception):

    """docstring for BaseError"""

    def __init__(self, errcode=500, errmsg=''):
        self.errcode = errcode
        self.errmsg = errmsg

    def handle(self):
        import sys
        import traceback
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_exception(exc_type, exc_value, exc_traceback)
        return jsonify({'errcode': self.errcode, 'errmsg': self.errmsg})
