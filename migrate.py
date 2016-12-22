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
import backend_common.database.medical_kit_table as MedicalKitModel
import backend_common.database.medical_kit_instance_table as MedicalKitInstanceModel
import backend_common.database.medical_kit_instance_setting_table as MedicalKitInstanceSettingModel
import backend_common.database.medical_kit_instance_box_setting_table as MedicalKitInstanceBoxSettingModel

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
    MedicalKitModel.migrate()
    MedicalKitInstanceModel.migrate()
    MedicalKitInstanceSettingModel.migrate()
    MedicalKitInstanceBoxSettingModel.migrate()
