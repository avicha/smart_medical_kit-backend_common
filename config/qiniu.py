# coding=utf-8
import backend_common.env as common_env


class config:

    """数据库相关配置"""

    def __init__(self, mode):
        self.resource_domain = common_env.QINIU_API_RESOURCE_DOMAIN
        self.access_key = common_env.QINIU_API_ACCESS_KEY
        self.secret_key = common_env.QINIU_API_SECRET_KEY
