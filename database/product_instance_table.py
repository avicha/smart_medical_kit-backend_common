# coding=utf-8
from backend_common.models.product_instance import ProductInstance


def migrate():
    if ProductInstance.table_exists():
        ProductInstance.drop_table()
    ProductInstance.create_table()
    ProductInstance.create(sku_id=1, product_code='46255000000001', order_id=1)
    ProductInstance.create(sku_id=2, product_code='76379000000001', order_id=1)
    ProductInstance.create(sku_id=2, product_code='76379000000002', order_id=1)
