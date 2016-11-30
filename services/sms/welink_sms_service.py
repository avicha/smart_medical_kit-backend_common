# coding=utf-8
import httplib
import urllib
import xml.dom.minidom as minidom
import datetime


class WelinkSMSService(object):

    """http://www.lmobile.cn/ch/api.html"""

    def __init__(self, config):
        super(WelinkSMSService, self).__init__()
        self.server_host = 'jiekou.51welink.com'
        self.server_path = '/submitdata/service.asmx'
        self.sname = config.sname
        self.spwd = config.spwd
        self.scorpid = config.scorpid
        self.sprdid = config.sprdid

    def sendMessage(self, phone_number, message):
        print('%s %s调用乐信接口发送短信：%s' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'), phone_number, message.encode('utf-8')))
        conn = httplib.HTTPConnection(self.server_host)
        payload = {'sname': self.sname, 'spwd': self.spwd, 'scorpid': self.scorpid, 'sprdid': self.sprdid, 'sdst': phone_number, 'smsg': message.encode('utf-8')}
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        conn.request('POST', self.server_path + '/g_Submit', body=urllib.urlencode(payload), headers=headers)
        response = conn.getresponse()
        data = response.read()
        if response.status == 200:
            dom = minidom.parseString(data)
            root = dom.documentElement
            State = root.getElementsByTagName("State")
            MsgID = root.getElementsByTagName("MsgID")
            MsgState = root.getElementsByTagName("MsgState")
            Reserve = root.getElementsByTagName("Reserve")
            resp = {'errcode': int(State[0].firstChild.data), 'errmsg': MsgState[0].firstChild.data, 'result': {'message_id': int(MsgID[0].firstChild.data)}}
        else:
            resp = {'errcode': response.status, 'errmsg': data}
        conn.close()
        print '%s 乐信接口返回，errcode:%s，errmsg：%s' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'), resp.get('errcode'), resp.get('errmsg').encode('utf-8'))
        return resp
