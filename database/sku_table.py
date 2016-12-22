# coding=utf-8
from backend_common.models.sku import Sku


def migrate():
    if Sku.table_exists():
        Sku.drop_table()
    Sku.create_table()
    Sku.create(product_id=1, market_price=299, sales_price=199, image='', props='颜色:纯白', stock_count=10000, sales_count=0, comment_count=0)
    Sku.create(product_id=1, market_price=299, sales_price=199, image='', props='颜色:粉红', stock_count=10000, sales_count=0, comment_count=0)
    Sku.create(product_id=1, market_price=299, sales_price=199, image='', props='颜色:天蓝', stock_count=10000, sales_count=0, comment_count=0)
