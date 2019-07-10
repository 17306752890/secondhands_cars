from flask import request,jsonify,session,json



from . import api
from cars import redis_store
from cars.models import User
from cars import db
from cars.utils.login_required import login_required
from cars import constant

@api.route('/index',methods=['post'])
@login_required
def index():
    return '这是首页'

@api.route('/logout',methods=['delete'])
@login_required
def logout():
    session.pop('user_id')
    session.pop('user_phone')
    return jsonify(msg='已经退出',errcode=constant.RET_OK)


@api.route('/register',methods=['POST'])
def register():
    #注意瓜子二手车是登录注册一体的
    print('#################',request.data)
    request_1 = request.json
    #todo 获取参数
    phone = request_1['phone']
    print(phone)
    input_msg_code = request_1['pwd']
    #todo 校验参数是否为空
    if not all([phone,input_msg_code]):
        return jsonify(err_msg='参数不完整')
    #todo 校验参数是否合法
    # todo 从redis里取出正确的验证码
    local_msg_code = redis_store.get('msg_%s'%phone).decode()
    print('这是本地存储的验证码：',local_msg_code)
    #todo 比对用户传递过来的验证码是否正确
    if input_msg_code!=local_msg_code:
        return jsonify(err_msg='验证码输入错误')
    # todo 判断数据库中是否已经存在该用户
    user_obj = User.query.filter_by(phone=phone).first()
    if not user_obj:
        #当数据库中不存在时，添加用户
        new_user_obj = User(phone=phone)
        try:
            db.session.add(new_user_obj)
            db.session.commit()
            user_obj = new_user_obj
        except Exception as e:
            print(e)
            db.session.rollback()
            return jsonify(errmsg='数据保存失败')

    # todo 如果不存在就添加到数据库中
    # todo 将用户数据添加到session中
    session['user_id']=user_obj.id
    session['user_phone']=user_obj.phone

    return jsonify(msg='登录成功')


























































