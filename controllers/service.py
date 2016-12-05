# coding=utf-8

import random
from flask import current_app
import backend_common.services.sms
from base import BaseController
import backend_common.constants.http_code as http_code
from backend_common.middlewares.request_service import get_request_params


class ServiceController(BaseController):

    @classmethod
    @get_request_params()
    def send_verifycode(cls, data):
        phone_number = data.get('phone_number')
        if not phone_number:
            return cls.error_with_message(http_code.FORBIDDEN, u'请传递手机号码')
        else:
            phone_number = phone_number.encode('utf-8')
            old_verifycode = current_app.cache.get('verifycode:' + phone_number)
            if old_verifycode:
                return cls.error_with_message(http_code.FORBIDDEN, u'您已经发送过验证码')
            else:
                verifycode = random.randint(100000, 999999)
                res = backend_common.services.sms.sendMessage(phone_number, u'尊敬的用户，注册验证码为：%s，2分钟内有效【智能药盒】' % verifycode)
                if res.get('errcode') == 0:
                    current_app.cache.set('verifycode:' + phone_number, verifycode, timeout=2*60)
                    return cls.success_with_result(None)
                else:
                    current_app.logger.error('发送短信验证码失败，手机号码为%s，验证码为%s：%s' % (phone_number, verifycode, res.get('errmsg').encode('utf-8')))
                    return cls.error_with_message(res.get('errcode'), res.get('errmsg'))
