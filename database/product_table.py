# coding=utf-8
from backend_common.models.product import Product


def migrate():
    if Product.table_exists():
        Product.drop_table()
    Product.create_table()
    Product.create(name='Pill Bot智能药盒', description='这是一款方便老人家药物管理的药盒', images='', intro='<p>这是一款方便老人家药物管理的药盒</p>', props='大小:30cm*20cm*20cm;适用人群:18-60岁')
