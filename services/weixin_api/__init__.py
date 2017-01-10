# coding=utf-8
import httplib
import urllib
import json
import time
import random
import string
import hashlib


class WeixinAPIError(Exception):

    """docstring for WeixinAPIError"""

    def __init__(self, errcode, errmsg):
        self.errcode = errcode
        self.errmsg = errmsg

    def handle(self):
        import sys
        from flask import jsonify, current_app
        if not current_app.testing:
            current_app.log_exception(sys.exc_info())
        return jsonify({'errcode': self.errcode, 'errmsg': self.errmsg})


class WeixinAPI(object):

    def __init__(self, config):
        super(WeixinAPI, self).__init__()
        self.server_host = 'api.weixin.qq.com'
        self.appid = config.appid
        self.secret = config.secret

    def get(self, path, payload={}):
        from flask import current_app
        start = time.time()
        # 建立连接
        conn = httplib.HTTPSConnection(self.server_host)
        # 发送请求
        url = path + '?' + urllib.urlencode(payload, True)
        conn.request('GET', url)
        # 获取返回数据
        response = conn.getresponse()
        data = response.read()
        # 关闭连接
        conn.close()
        end = time.time()
        current_app.logger.info('GET %s%s，耗时%sms', self.server_host, url, (end - start)*1000)
        # HTTP正常返回
        if response.status == 200:
            ret = json.loads(data)
            errcode = ret.get('errcode')
            errmsg = ret.get('errmsg')
            if errcode:
                raise WeixinAPIError(errcode, errmsg)
            else:
                return ret
        else:
            # HTTP请求错误
            raise WeixinAPIError(response.status, data)

    def get_access_token(self):
        from flask import current_app
        if current_app.cache and current_app.cache.get('weixin_api_%s_access_token' % self.appid):
            accesss_token = current_app.cache.get('weixin_api_%s_access_token' % self.appid)
            return accesss_token
        else:
            result = self.get('/cgi-bin/token', {'grant_type': 'client_credential', 'appid': self.appid, 'secret': self.secret})
            access_token = result.get('access_token')
            if current_app.cache:
                current_app.cache.set('weixin_api_%s_access_token' % self.appid, access_token, timeout=result.get('expires_in'))
            return access_token

    def getcallbackip(self):
        access_token = self.get_access_token()
        payload = {'access_token': access_token}
        return self.get('/cgi-bin/getcallbackip', payload)

    def get_jsapi_ticket(self):
        from flask import current_app
        if current_app.cache and current_app.cache.get('weixin_api_%s_ticket' % self.appid):
            ticket = current_app.cache.get('weixin_api_%s_ticket' % self.appid)
            return ticket
        else:
            access_token = self.get_access_token()
            payload = {'access_token': access_token, 'type': 'jsapi'}
            result = self.get('/cgi-bin/ticket/getticket', payload)
            ticket = result.get('ticket')
            if current_app.cache:
                current_app.cache.set('weixin_api_%s_ticket' % self.appid, ticket, timeout=result.get('expires_in'))
            return ticket

    def __create_nonce_str(self):
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(15))

    def __create_timestamp(self):
        return int(time.time())

    def get_jsapi_params(self, url):
        jsapi_ticket = self.get_jsapi_ticket()
        params = {
            'noncestr': self.__create_nonce_str(),
            'jsapi_ticket': jsapi_ticket,
            'timestamp': self.__create_timestamp(),
            'url': url
        }
        params_str = '&'.join(['%s=%s' % (key.lower(), params[key]) for key in sorted(params)])
        signature = hashlib.sha1(params_str).hexdigest()
        return {'appId': self.appid, 'timestamp': params['timestamp'], 'nonceStr': params['noncestr'], 'signature': signature}

    def get_media(self, media_id):
        from flask import current_app
        start = time.time()
        file_server_host = 'file.api.weixin.qq.com'
        access_token = self.get_access_token()
        # 建立连接
        conn = httplib.HTTPConnection(file_server_host)
        payload = {'access_token': access_token, 'media_id': media_id}
        # 发送请求
        url = '/cgi-bin/media/get?' + urllib.urlencode(payload, True)
        conn.request('GET', url)
        # 获取返回数据
        response = conn.getresponse()
        data = response.read()
        # 关闭连接
        conn.close()
        end = time.time()
        current_app.logger.info('GET %s%s，耗时%sms', file_server_host, url, (end - start)*1000)
        # HTTP正常返回
        if response.status == 200:
            return data
        else:
            ret = json.loads(data)
            errcode = ret.get('errcode')
            errmsg = ret.get('errmsg')
            # HTTP请求错误
            raise WeixinAPIError(errcode, errmsg)
