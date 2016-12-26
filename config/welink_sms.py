# coding=utf-8
import backend_common.env as common_env


class config:

    """数据库相关配置"""

    def __init__(self, mode):
        self.sname = common_env.WELINK_SMS_API_SNAME
        self.spwd = common_env.WELINK_SMS_API_SPWD
        self.scorpid = common_env.WELINK_SMS_API_SCORPID
        self.sprdid = common_env.WELINK_SMS_API_SPRDID
