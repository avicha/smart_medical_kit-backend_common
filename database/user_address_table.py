# coding=utf-8
from backend_common.models.user_address import UserAddress
from backend_common.models.user import User


def migrate():
    if UserAddress.table_exists():
        UserAddress.drop_table()
    UserAddress.create_table()
    user = User.get(User.username == '13632324433')
    UserAddress.create(user_id=user.id, region_code='440606', street='勒流镇众涌村仁厚街2号', is_default=True, consignee='卢炳成', contact='13632324433')
