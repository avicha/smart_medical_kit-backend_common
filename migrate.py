# coding=utf-8
import sys
sys.path.append('..')
from backend_common.models.database import database
import backend_common.database.admin_table as AdminModel
import backend_common.database.user_table as UserModel
import backend_common.database.user_token_table as UserTokenModel
import backend_common.database.address_table as AddressModel
import backend_common.database.user_address_table as UserAddressModel
import backend_common.database.product_table as ProductModel
import backend_common.database.sku_table as SkuModel
import backend_common.database.order_table as OrderModel
import backend_common.database.order_sku_table as OrderSkuModel
import backend_common.database.product_instance_table as ProductInstanceModel

with database.transaction():
    AdminModel.migrate()
    UserModel.migrate()
    UserTokenModel.migrate()
    AddressModel.migrate()
    UserAddressModel.migrate()
    ProductModel.migrate()
    SkuModel.migrate()
    OrderModel.migrate()
    OrderSkuModel.migrate()
    ProductInstanceModel.migrate()
