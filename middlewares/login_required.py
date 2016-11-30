# coding=utf-8
from flask import g


def admin_required(f):
    from backend_common.models.admin import Admin as AdminModel

    def decorator(*args, **kwargs):
        if g.admin:
            kwargs.update({'admin': g.admin})
            return f(*args, **kwargs)
        raise AdminModel.NotAuthError()
    return decorator


def user_required(f):
    from backend_common.models.user import User as UserModel

    def decorator(*args, **kwargs):
        if g.user:
            kwargs.update({'user': g.user})
            return f(*args, **kwargs)
        raise UserModel.NotAuthError()
    return decorator
