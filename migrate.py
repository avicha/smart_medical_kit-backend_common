# coding=utf-8
import sys
sys.path.append('..')
import backend_common.database.admin_table as AdminModel
import backend_common.database.user_table as UserModel
import backend_common.database.user_token_table as UserTokenModel

AdminModel.migrate()
UserModel.migrate()
UserTokenModel.migrate()
