import redis


class Config():
    '''项目设置'''
    #密钥的配置，session,csrf_token等会用到
    SECRET_KEY = 'lkhsgfjnfjdgjkndviudfogkndiguojdkgniofdikjnvbudfoinf'

    #关系性数据库的配置
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/cars'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #非关系性数据库的配置

    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    #配置session扩展
    SESSION_TYPE = 'redis'#告诉flask＿session这个扩展，把session存储到redis中
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST,port=REDIS_PORT)#创建redis连接
    SESSION_USE_SIGNER = True #签名，将cookis中的session_id进行加密处理
    PERMANENT_SESSION_LIFETIME = 60*60*24*1#过期时间，妙为单位




class DevelopmentConfig(Config):
    #开启调试模式
    DEBUG = True

class OnlineConfig(Config):
    #正是的产品发布运行模式
    pass

config={
    'development':DevelopmentConfig,
    'online':OnlineConfig,

}























