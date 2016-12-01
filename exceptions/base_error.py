# coding=utf-8
from flask import jsonify, current_app


class BaseError(Exception):

    """docstring for BaseError"""

    def __init__(self, errcode, errmsg):
        self.errcode = errcode
        self.errmsg = errmsg

    def handle(self):
        import sys
        current_app.log_exception(sys.exc_info())
        return jsonify({'errcode': self.errcode, 'errmsg': self.errmsg})
