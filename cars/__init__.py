from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect#配全局，
from flask_session import Session
import redis
import logging
from logging.handlers import RotatingFileHandler


from config import config

redis_store = None



#完成操作句柄的定义
db = SQLAlchemy()
# csrf = CSRFProtect()


# 日志等级的设置
logging.basicConfig(level=logging.DEBUG)
# 创建日志记录器，　　　　　　　　　　指定日志保存的路径　　　每个日志的大小　　　保存日志的上限
file_log_handler = RotatingFileHandler('logs/log',maxBytes=1024*1024,backupCount=10)
# 设置日志的格式       　　　　　　 日志等级    日志信息的文件名　行数　　　　日志信息
formatter = logging.Formatter('%(levelname)s %(filename)s %(lineno)d %(message)s')
# 将日志记录器指定日志格式
file_log_handler.setFormatter(formatter)
# 为全局的日志工具对象添加日志记录器，告诉flask的app来用的
logging.getLogger().addHandler(file_log_handler)



def create_app(config_name):
    #将来根据运行的模式，加载不同的配置对象
    app = Flask(__name__)
    # 加载配置文件，配置文件是一个类对象

    app.config.from_object(config[config_name])

    #数据库操作句柄关联app
    db.init_app(app)
    Session(app)
    # csrf.init_app(app)

    global redis_store
    redis_store = redis.StrictRedis(host=config[config_name].REDIS_HOST,port=config[config_name].REDIS_PORT)

    # 注册蓝图
    from cars.api_1_0 import api
    app.register_blueprint(api,url_prefix='/api/v1.0')#同drf中的一级路径
    # url_prefix:前缀，相当于一级目录


    return app



































