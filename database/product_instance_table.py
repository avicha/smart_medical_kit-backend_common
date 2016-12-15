# coding=utf-8
from backend_common.models.product_instance import ProductInstance


def migrate():
    if ProductInstance.table_exists():
        ProductInstance.drop_table()
    ProductInstance.create_table()
    ProductInstance.create(sku_id=1, product_code='462551', order_id=1)
    ProductInstance.create(sku_id=2, product_code='763791', order_id=1)
    ProductInstance.create(sku_id=2, product_code='763792', order_id=1)
