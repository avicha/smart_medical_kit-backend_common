# coding=utf-8
import backend_common.env as common_env


class config:

    """数据库相关配置"""

    def __init__(self, mode):
        self.appid = common_env.WEIXIN_API_APPID
        self.secret = common_env.WEIXIN_API_SECRET
