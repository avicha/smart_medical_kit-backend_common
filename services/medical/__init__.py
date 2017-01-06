# coding=utf-8
import httplib
import urllib
import json
import time


class MedicalAPIError(Exception):

    """docstring for MedicalAPIError"""

    def __init__(self, errcode, errmsg):
        self.errcode = errcode
        self.errmsg = errmsg

    def handle(self):
        import sys
        from flask import jsonify, current_app
        if not current_app.testing:
            current_app.log_exception(sys.exc_info())
        return jsonify({'errcode': self.errcode, 'errmsg': self.errmsg})


class MedicalAPI(object):

    def __init__(self, config):
        super(MedicalAPI, self).__init__()

    @classmethod
    def scan(self, barcode):
        from flask import current_app
        start = time.time()
        server_host = 'weixinsrv.39.net'
        # 建立连接
        conn = httplib.HTTPConnection(server_host)
        # 发送请求
        url = '/39ypt/DocInfo.ashx?' + urllib.urlencode({'actionType': 'Scan', 'number': barcode}, True)
        conn.request('GET', url)
        # 获取返回数据
        response = conn.getresponse()
        data = response.read()
        # 关闭连接
        conn.close()
        end = time.time()
        current_app.logger.info('GET %s%s，耗时%sms', server_host, url, (end - start)*1000)
        # HTTP正常返回
        if response.status == 200:
            ret = json.loads(data)
            status = ret.get('status')
            extra = ret.get('results')
            if status == 'Ok':
                if 'DrugId' in extra:
                    medical_info = self.__crawl_ypk39(extra.get('DrugId'))
                    medical_info.update({'barcode': barcode, 'extra': json.dumps(extra)})
                    return medical_info
                else:
                    raise MedicalAPIError(400, '抱歉，找不到该药品的基本信息')
            else:
                raise MedicalAPIError(status, extra)
        else:
            print data
            # HTTP请求错误
            raise MedicalAPIError(response.status, '抱歉，服务出了些小问题，请稍后重试')

    @classmethod
    def __crawl_ypk39(self, drug_id):
        from flask import current_app
        from bs4 import BeautifulSoup
        start = time.time()
        server_host = 'ypk.39.net'
        # 建立连接
        conn = httplib.HTTPConnection(server_host)
        # 发送请求
        url = '/%s/' % drug_id
        conn.request('GET', url)
        # 获取返回数据
        response = conn.getresponse()
        data = response.read()
        # 关闭连接
        conn.close()
        end = time.time()
        current_app.logger.info('GET %s%s，耗时%sms', server_host, url, (end - start)*1000)
        # HTTP正常返回
        if response.status == 200:
            soup = BeautifulSoup(data, 'html5lib')
            name_doms = soup.select('.t1 h1')
            if len(name_doms):
                name = name_doms[0].get_text()
            else:
                name = ''
            english_name_doms = soup.select('.t2')
            if len(english_name_doms):
                english_name = english_name_doms[0].get_text()
            else:
                english_name = ''
            image_doms = soup.select('.imgbox img')
            if len(image_doms):
                image = image_doms[0]['src']
            else:
                image = ''
            company_doms = soup.select('.company')
            if len(company_doms):
                company = company_doms[0].get_text()
            else:
                company = ''
            address_doms = soup.select('.address')
            if len(address_doms):
                address = address_doms[0].get_text()
            else:
                address = ''
            functions_doms = soup.select('.whatsthis li')
            functions = []
            for x in functions_doms:
                functions.append(x.get_text())
            functions = ','.join(functions)
            doms = soup.select('.ps p')
            constituent = ''
            functions_desc = ''
            amount_desc = ''
            for x in doms:
                if x.strong:
                    strong = x.strong.extract()
                    strong_text = strong.get_text().strip('\n ')
                    dom_text = x.get_text().strip('\n ')
                    if strong_text == u'成  分':
                        constituent = dom_text
                    elif strong_text == u'适应症':
                        functions_desc = dom_text
                    elif strong_text == u'用法用量':
                        amount_desc = dom_text
            tips = ''
            props = []
            props_doms = soup.select('.xxs li,.showlis li')
            for x in props_doms:
                prop_name = x.cite.extract().get_text().strip(u'：')
                if x.script:
                    x.script.extract()
                prop_value = x.get_text().strip('\n ')
                props.append(prop_name + ':' + prop_value)
            props = ';'.join(props)
            return {
                'name': name,
                'english_name': english_name,
                'image': image,
                'company': company,
                'address': address,
                'functions': functions,
                'functions_desc': functions_desc,
                'constituent': constituent,
                'amount_desc': amount_desc,
                'tips': tips,
                'props': props
            }
        else:
            print data
            # HTTP请求错误
            raise MedicalAPIError(response.status, '抱歉，找不到该药品的详细信息')
