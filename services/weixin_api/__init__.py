# coding=utf-8
import httplib
import urllib
import json
import time
import random
import string
import hashlib


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
        current_app.logger.info('GET %s%s，耗时%sms', self.server_host, path, (end - start)*1000)
        # HTTP正常返回
        if response.status == 200:
            ret = json.loads(data)
            errcode = ret.get('errcode')
            # 如果是token过期导致请求数据失败，则重新获取token请求一次
            if errcode:
                return ret
            else:
                return {'errcode': 0, 'result': ret}
        else:
            # HTTP请求错误
            return {'errcode': response.status, 'errmsg': data}

    def get_access_token(self):
        from flask import current_app
        if current_app.cache and current_app.cache.get('weixin_api_%s_access_token' % self.appid):
            accesss_token = current_app.cache.get('weixin_api_%s_access_token' % self.appid)
            return {'errcode': 0, 'result': accesss_token}
        else:
            resp = self.get('/cgi-bin/token', {'grant_type': 'client_credential', 'appid': self.appid, 'secret': self.secret})
            if resp.get('errcode'):
                return resp
            else:
                access_token = resp.get('result').get('access_token')
                if current_app.cache:
                    current_app.cache.set('weixin_api_%s_access_token' % self.appid, access_token, timeout=resp.get('result').get('expires_in'))
                return {'errcode': 0, 'result': access_token}

    def getcallbackip(self):
        access_token_resp = self.get_access_token()
        if access_token_resp.get('errcode'):
            return access_token_resp
        else:
            access_token = access_token_resp.get('result')
            payload = {'access_token': access_token}
            return self.get('/cgi-bin/getcallbackip', payload)

    def get_jsapi_ticket(self):
        from flask import current_app
        if current_app.cache and current_app.cache.get('weixin_api_%s_ticket' % self.appid):
            ticket = current_app.cache.get('weixin_api_%s_ticket' % self.appid)
            return {'errcode': 0, 'result': ticket}
        else:
            access_token_resp = self.get_access_token()
            if access_token_resp.get('errcode'):
                return access_token_resp
            else:
                access_token = access_token_resp.get('result')
                payload = {'access_token': access_token, 'type': 'jsapi'}
                resp = self.get('/cgi-bin/ticket/getticket', payload)
                if resp.get('errcode'):
                    return resp
                else:
                    ticket = resp.get('result').get('ticket')
                    if current_app.cache:
                        current_app.cache.set('weixin_api_%s_ticket' % self.appid, ticket, timeout=resp.get('result').get('expires_in'))
                    return {'errcode': 0, 'result': ticket}

    def __create_nonce_str(self):
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(15))

    def __create_timestamp(self):
        return int(time.time())

    def get_jsapi_params(self, url):
        jsapi_ticket_resp = self.get_jsapi_ticket()
        if jsapi_ticket_resp.get('errcode'):
            return jsapi_ticket_resp
        else:
            params = {
                'noncestr': self.__create_nonce_str(),
                'jsapi_ticket': jsapi_ticket_resp.get('result'),
                'timestamp': self.__create_timestamp(),
                'url': url
            }
            string = '&'.join(['%s=%s' % (key.lower(), params[key]) for key in sorted(params)])
            signature = hashlib.sha1(string).hexdigest()
            return {'errcode': 0, 'result': {'appId': self.appid, 'timestamp': params['timestamp'], 'nonceStr': params['noncestr'], 'signature': signature, 'url': url}}
