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
