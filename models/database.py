from playhouse.pool import PooledMySQLDatabase
from playhouse.shortcuts import RetryOperationalError
from backend_common.config import database as database_config


class RetryDB(RetryOperationalError, PooledMySQLDatabase):
    pass
database = RetryDB(database_config.database, **database_config.connect_options)
