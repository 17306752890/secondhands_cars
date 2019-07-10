
from flask import request,jsonify,render_template
import re
import random
# __import__('random')
import logging


from . import api
from cars import redis_store
from cars.api_1_0.libs.yuntongxun.sms import CCP

@api.route('/smgcode',methods=['post','get'])
def send_msg_code():
    if request.method == 'POST':
        print('##########################################')
        # todo 1.获取参数
        # print(request.data)
        # print(request.form)
        # phone = request.form.get('phone')
        phone = request.data.decode()
        print('获取的手机号码',phone)

        # todo 2.校验参数是否为空
        if not all([phone]):
            return jsonify(msg='参数不能为空')

        # todo 3.校验手机号码是否合法
        if not re.match(r'1[3,4,5,7,8,9]\d{9}',phone):
            return jsonify(msg='手机号码不合法')

        # todo 4.生成短信验证码
        msg_code = '%04d'%random.randint(0,9999)
        print(msg_code)
        print(type(msg_code))
        logging.debug(msg_code)#打印到日志中

        # todo 5.存储短信验证码
        try:
            redis_store.set('msg_%s'%phone,msg_code,3600)
        except Exception as e:
            logging.error(e)
            return jsonify(msg='验证码保存错误')

        # todo 6.发送短信验证码
        ret = CCP().send_template_sms(phone,[msg_code,'1'],1)
        if ret == -1:
            return jsonify(msg='验证码发送失败')

        return jsonify(msg='发送成功')

        # todo 7.响应
    return render_template('register.html')










