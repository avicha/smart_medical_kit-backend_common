# coding=utf-8
from backend_common.models.medical import Medical


def migrate():
    if Medical.table_exists():
        Medical.drop_table()
    Medical.create_table()
