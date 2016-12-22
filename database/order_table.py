# coding=utf-8
from backend_common.models.order import Order
from backend_common.models.user import User
from backend_common.models.user_address import UserAddress
import backend_common.constants.order_status as order_status


def migrate():
    if Order.table_exists():
        Order.drop_table()
    Order.create_table()
    user = User.get(User.phone_number == '13632324433')
    user_address = UserAddress.get(UserAddress.user_id == user.id, UserAddress.is_default == True)
    Order.create(user_id=user.id, logistics_user_address_id=user_address.id, status=order_status.COMPLETED, remark='这是测试的订单', total_price=597, paid_price=577)
