

import logging
from logging.handlers import RotatingFileHandler




#日志等级设置
logging.basicConfig(level=logging.DEBUG)
# 创建日志记录器　指定日志的保存路径　每个日志的大小　保存日志的上限
file_log_handler = RotatingFileHandler('logs/log',maxBytes=1024*1024,backupCount=10)
# 设置日志的格式　日志等级　日志信息的文件名　行数　日志信息
formatter = logging.Formatter('%(levelname) %(filename)s %(lineno)d %(message)s')
# 将日志记录器制订日志格式
file_log_handler.setFormatter(formatter)
# 为全局的日志工具对象添加日志记录器，是用来钙素flask的app来用的
logging.getLogger().addHandler(file_log_handler)


# 首先在项目的__init__里创建蓝图
from flask import Blueprint
api = Blueprint('api_1_0',__name__,template_folder='templates',static_folder='static')


# 然后在cars里注册蓝图
from cars.api_1_0 import api
app.register_blueprint(api,url_prefix='/api/v1.0')#url_prefix:前缀，同django一级路径

#之后就在api_1_0你的项目文件夹里面创建py文件，用来写运行程序

#创建完成之后，在__init__里面把你创建的导进去
from . import register #比如你创的是register

# 最后就可以在register里面写运行的程序了
from . import api

@api.route('/index_1',methods=['post'])
def index():
    return jsonfiy(msg='首页')







# 装饰器















































