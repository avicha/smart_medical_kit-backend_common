# coding=utf-8
from backend_common.models.admin import Admin


def migrate():
    if Admin.table_exists():
        Admin.drop_table()
    Admin.create_table()
    import bcrypt
    password = bcrypt.hashpw(u'123456'.encode('utf-8'), bcrypt.gensalt())
    q = Admin.insert(username=u'admin', password=password)
    q.execute()
