# coding=utf-8
from backend_common.models.user_address import UserAddress


def migrate():
    if UserAddress.table_exists():
        UserAddress.drop_table()
    UserAddress.create_table()
