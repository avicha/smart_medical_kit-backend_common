# coding=utf-8
from backend_common.models.order_sku import OrderSku
from backend_common.models.product import Product
from backend_common.models.sku import Sku
from backend_common.models.order import Order


def migrate():
    if OrderSku.table_exists():
        OrderSku.drop_table()
    OrderSku.create_table()
    order = Order.select().first()
    for sku_id in range(1, 3):
        sku = Sku.get(Sku.id == sku_id)
        product = Product.get(Product.id == sku.product_id)
        OrderSku.create(order_id=order.id, sku_id=sku.id, product_name=product.name, product_description=product.description, product_images=product.images, product_intro=product.intro, sku_market_price=sku.market_price, sku_sales_price=sku.sales_price, sku_image=sku.image, sku_props=sku.props, amount=sku_id)
