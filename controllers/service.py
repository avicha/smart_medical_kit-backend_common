# coding=utf-8

import random
from flask import current_app, request
import backend_common.services.sms
from base import BaseController
import backend_common.constants.http_code as http_code


class ServiceController(BaseController):

    @classmethod
    def send_verifycode(cls):
        data = request.json or request.form or request.args
        phone_number = data.get('phone_number')
        if not phone_number:
            return cls.error_with_message(http_code.FORBIDDEN, u'请传递手机号码')
        else:
            old_verifycode = current_app.cache.get('verifycode:' + phone_number)
            if old_verifycode:
                return cls.error_with_message(http_code.FORBIDDEN, u'您已经发送过验证码')
            else:
                verifycode = str(random.randint(100000, 999999))
                res = backend_common.services.sms.sendMessage(phone_number, u'尊敬的用户，注册验证码为：%s，2分钟内有效【一起社区】' % verifycode)
                if res.get('errcode') == 0:
                    current_app.cache.set('verifycode:' + phone_number, verifycode, timeout=2*60)
                    return cls.success_with_result(None)
                else:
                    current_app.logger.error(u'发送短信验证码失败，手机号码为%s，验证码为%s：%s' % (phone_number, verifycode, res.get('errmsg')))
                    return cls.error_with_message(res.get('errcode'), res.get('errmsg'))
