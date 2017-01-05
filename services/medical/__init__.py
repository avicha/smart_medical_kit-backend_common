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
            if status == 'Ok' and 'DrugId' in extra:
                medical_info = self.__crawl_ypk39(extra.get('DrugId'))
                medical_info.update({'barcode': barcode, 'extra': json.dumps(extra)})
                return medical_info
            else:
                raise MedicalAPIError(status, results)
        else:
            # HTTP请求错误
            raise MedicalAPIError(response.status, data)

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
            functions_desc_doms = soup.select('.ps p:nth-of-type(2)')
            if len(functions_desc_doms):
                functions_desc_doms[0].strong.extract()
                functions_desc = functions_desc_doms[0].get_text().strip('\n ')
            else:
                functions_desc = ''
            constituent_doms = soup.select('.ps p:nth-of-type(1)')
            if len(constituent_doms):
                constituent_doms[0].strong.extract()
                constituent = constituent_doms[0].get_text().strip('\n ')
            else:
                constituent = ''
            amount_desc_doms = soup.select('.ps p:nth-of-type(3)')
            if len(amount_desc_doms):
                amount_desc_doms[0].strong.extract()
                amount_desc = amount_desc_doms[0].get_text().strip('\n ')
            else:
                amount_desc = ''
            tips = ''
            props = []
            props_doms = soup.select('.xxs li,.showlis li')
            for x in props_doms:
                prop_name = x.cite.extract().get_text().strip(u'：')
                prop_value = x.get_text()
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
            # HTTP请求错误
            raise MedicalAPIError(response.status, data)
