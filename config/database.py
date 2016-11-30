# coding=utf-8
import backend_common.env as common_env


class config:

    """数据库相关配置"""

    def __init__(self, mode):
        self.database = common_env.DB_DATABASE
        self.connect_options = {
            'max_connections': common_env.DB_MAX_CONNECTIONS,
            'stale_timeout': common_env.DB_STALE_TIMEOUT,
            'host': common_env.DB_HOST,
            'port': common_env.DB_PORT,
            'user': common_env.DB_USERNAME,
            'password': common_env.DB_PASSWORD,
        }
