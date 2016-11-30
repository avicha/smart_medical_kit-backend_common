# coding=utf-8
from flask import jsonify, request, current_app
from backend_common.exceptions import BaseError


class BaseController():

    @staticmethod
    def success_with_result(result):
        return jsonify({'errcode': 0, 'result': result})

    @staticmethod
    def success_with_list_result(total_count, result):
        return jsonify({'errcode': 0, 'total_count': total_count, 'result': result})

    @staticmethod
    def error_with_message(code, message):
        data = request.json or request.form or request.args
        current_app.logger.error('请求URL：%s', request.url.encode('utf-8'))
        current_app.logger.error('请求参数：%s', data)
        current_app.logger.error('返回错误信息：%s', message.encode('utf-8'))
        raise BaseError(code, message)

    @staticmethod
    def response_with_json(json):
        return jsonify(json)
