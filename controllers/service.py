# coding=utf-8
import random
from urlparse import urlparse
from flask import current_app, request

from base import BaseController
from backend_common.middlewares.request_service import get_request_params
import backend_common.constants.http_code as http_code

from backend_common.services.sms import WelinkSMSService
from backend_common.config import welink_sms as welink_sms_api_config
welink_sms_api = WelinkSMSService(welink_sms_api_config)

from backend_common.services.weixin_api import WeixinAPI
from backend_common.config import weixin as weixin_api_config
weixin_api = WeixinAPI(weixin_api_config)


class ServiceController(BaseController):

    @classmethod
    @get_request_params()
    def send_verifycode(cls, data):
        phone_number = data.get('phone_number')
        if not phone_number:
            return cls.error_with_message(http_code.BAD_REQUEST, u'请传递手机号码')
        else:
            phone_number = phone_number.encode('utf-8')
            old_verifycode = current_app.cache.get('verifycode:' + phone_number)
            if old_verifycode:
                return cls.error_with_message(http_code.FORBIDDEN, u'您已经发送过验证码')
            else:
                verifycode = random.randint(100000, 999999)
                res = welink_sms_api.sendMessage(phone_number, u'尊敬的用户，注册验证码为：%s，2分钟内有效【智能药盒】' % verifycode)
                if res.get('errcode') == 0:
                    current_app.cache.set('verifycode:' + phone_number, verifycode, timeout=2*60)
                    return cls.success_with_result(None)
                else:
                    current_app.logger.error('发送短信验证码失败，手机号码为%s，验证码为%s：%s' % (phone_number, verifycode, res.get('errmsg').encode('utf-8')))
                    return cls.error_with_message(res.get('errcode'), res.get('errmsg'))

    @classmethod
    @get_request_params()
    def get_weixin_jsapi_params(cls, data):
        url = urlparse(request.headers.get('Referer')).geturl()
        result = weixin_api.get_jsapi_params(url)
        return cls.success_with_result(result)
