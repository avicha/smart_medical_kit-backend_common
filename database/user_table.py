# coding=utf-8
from backend_common.models.user import User


def migrate():
    if User.table_exists():
        User.drop_table()
    User.create_table()
    import bcrypt
    import backend_common.constants.sex as sex
    import backend_common.constants.register_type as register_type
    password = bcrypt.hashpw(u'123456'.encode('utf-8'), bcrypt.gensalt())
    q = User.insert(username=u'13632324433', password=password, nick=u'avicha', sex=sex.MAN, phone_number=u'13632324433', register_type=register_type.TAOBAO)
    q.execute()
