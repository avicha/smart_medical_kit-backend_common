# coding=utf-8
from flask import request


def user_exists(f):
    from backend_common.models.user import User as UserModel

    def decorator(*args, **kwargs):
        data = request.json or request.form or request.args
        user_id = data.get('user_id')
        if user_id:
            try:
                user = UserModel.get(UserModel.id == user_id, UserModel.deleted_at == None)
                kwargs.update({'user': user})
                return f(*args, **kwargs)
            except UserModel.DoesNotExist as e:
                raise UserModel.NotFoundError(u'该用户不存在')
        else:
            raise UserModel.LackOfFieldError(u'请传入用户ID')
    return decorator


def user_address_exists(f):
    from backend_common.models.user_address import UserAddress as UserAddressModel

    def decorator(*args, **kwargs):
        data = request.json or request.form or request.args
        user_address_id = data.get('user_address_id')
        if user_address_id:
            try:
                user_address = UserAddressModel.get(UserAddressModel.id == user_address_id, UserAddressModel.deleted_at == None)
                kwargs.update({'user_address': user_address})
                return f(*args, **kwargs)
            except UserAddressModel.DoesNotExist as e:
                raise UserAddressModel.NotFoundError(u'该用户地址不存在')
        else:
            raise UserAddressModel.LackOfFieldError(u'请传入用户地址ID')
    return decorator
