# coding=utf-8
import sys
sys.path.append('..')
import backend_common.database.admin_table as AdminModel
import backend_common.database.user_table as UserModel
import backend_common.database.user_token_table as UserTokenModel
import backend_common.database.address_table as AddressModel
import backend_common.database.user_address_table as UserAddressModel

AdminModel.migrate()
UserModel.migrate()
UserTokenModel.migrate()
AddressModel.migrate()
UserAddressModel.migrate()
