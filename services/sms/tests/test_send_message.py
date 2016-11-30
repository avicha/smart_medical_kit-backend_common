# coding=utf-8
import sys
sys.path.append('..')
import pytest


def test_send_message_success():
    import random
    import sms
    verifycode = random.randint(100000, 999999)
    res = sms.sendMessage(13632324433, u'尊敬的用户，注册验证码为：%s，2分钟内有效【一起社区】' % verifycode)
    assert 'errcode' in res
    assert 'errmsg' in res
    assert 'result' in res
    errcode = res.get('errcode')
    errmsg = res.get('errmsg')
    result = res.get('result')
    assert errcode == 0
    assert 'message_id' in result
