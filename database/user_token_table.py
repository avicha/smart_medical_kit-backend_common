# coding=utf-8
from backend_common.models.user_token import UserToken


def migrate():
    if UserToken.table_exists():
        UserToken.drop_table()
    UserToken.create_table()
