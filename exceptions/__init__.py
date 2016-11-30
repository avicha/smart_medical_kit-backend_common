# coding=utf-8
from base_error import BaseError
from backend_common.controllers.base import BaseController


def uncaught_error_handler(e):
    import backend_common.events as events
    result = events.uncaught_error.send(e, e=e)
    if len(result):
        return BaseController.error_with_message(500, result[0][1])
    else:
        return BaseController.error_with_message(500, u'服务器错误')


def init_app(server):
    exceptions = [BaseError]
    for e in exceptions:
        server.register_error_handler(e, e.handle)
    server.register_error_handler(Exception, uncaught_error_handler)
