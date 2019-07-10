import functools
from flask import session,jsonify,g
from cars import constant

def login_required(func):

    @functools.wraps(func)#修饰内层函数，防止当前的装饰器去修改被装饰函数的__name__属性
    def inner(*args,**kwargs):

        user_id = session.get('user_id')
        print('这是取出来的user_id',user_id)
        if not user_id:
            return jsonify(errmsg='用户未登录',errcode=constant.RET_LOGIN)
        else:
            g.user_id = user_id
            return func(*args,**kwargs)

    return inner










