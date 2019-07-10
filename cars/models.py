from datetime import datetime


from . import db



class BaseModel(object):
    is_delete = db.Column(db.Boolean,default=False)
    create_time = db.Column(db.DATETIME,default = datetime.now)
    update_time = db.Column(db.DATETIME,default = datetime.now,onupdate = datetime.now)#更新时间



#创建用户模型
class User(BaseModel,db.Model):
    __tablename__ = 'sc_users'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(10),unique=True,nullable=True)
    password = db.Column(db.String(100),nullable=True)
    phone = db.Column(db.String(11),nullable=False)
    ID_card = db.Column(db.String(18),nullable=True)
    cars = db.relationship('Car',backref='user')#写关系
    order_id = db.relationship('Order',backref='user')
    def __repr__(self):
        return self.name


class Car(BaseModel,db.Model):
    __tablename__ = 'sc_car'
    id = db.Column(db.Integer,primary_key=True)
    # user = db.Column(db.String(20),nullable=False)
    brande_id = db.Column(db.Integer,db.ForeignKey('sc_brande.id'))
    # introduction = db.Column(db.String(1000),nullable=False)
    sc_users_id = db.Column(db.Integer,db.ForeignKey('sc_users.id'))#车辆的拥有者，即该车所属的卖家
    price = db.Column(db.Integer,default=0,nullable=False)#default 默认值
    car_age = db.Column(db.Integer)#年龄
    car_model = db.Column(db.String(10))#车所属类型，比如suv
    car_gearbox = db.Column(db.Integer,default=1)#变速箱　0－－手动，1－－自动
    car_distance = db.Column(db.Integer)#里程数
    car_displacement = db.Column(db.Float)#排量
    car_register_time = db.Column(db.DateTime,default=datetime.now)#上牌时间
    car_num = db.Column(db.String(100))#车架号
    car_color = db.Column(db.String(10))#车辆的颜色
    car_oil_style = db.Column(db.String(10))#车辆的燃油类型
    car_emission_standard = db.Column(db.String(10))#排放标准
    car_seat_num = db.Column(db.Integer)#座位个数
    car_transfer_num = db.Column(db.Integer)#过户次数
    car_inspect_annually = db.Column(db.String(10))#年检
    car_compulsory_insurance = db.Column(db.String(10))#交强险
    car_commercial_insurance = db.Column(db.String(10))#商业险

    index_image_url = db.Column(db.String(100))#默认图片

    images = db.relationship('CarImage',backref='car')
    security_id = db.relationship('Security',backref='car')
    orders_id = db.relationship('Order',backref='car')
    outsideproperties_id = db.relationship('outsideproperties',backref='car')
    chassis_brake_id = db.relationship('Chassis_Brake',backref='car')
    sc_engine_id = db.relationship('Engine',backref='car')
    Basic_parameters_id = db.relationship('Basic_parameters',backref='car')



    def __repr__(self):
        return self.user


class CarImage(db.Model):
    __tablename__ = 'sc_image'
    id = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.Integer,db.ForeignKey('sc_car.id'))#车辆编号
    url = db.Column(db.String(100))#图片路径

    def __repr__(self):
        return 'car_id是：%s'%self.car_id
class Order(BaseModel,db.Model):
    __tablename__ = 'sc_order'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20),nullable=True)
    sc_users_id = db.Column(db.Integer,db.ForeignKey('sc_users.id'))#下订单的用户
    car_name = db.Column(db.Integer,db.ForeignKey('sc_car.id'))#车辆信息
    order_time = db.Column(db.DateTime,default=datetime.now)
    car_price = db.Column(db.Float)#车辆的原始价格
    service_charge = db.Column(db.Float)#手续费

    def __repr__(self):
        return self.name

class Brande(db.Model):
    __tablename__ = 'sc_brande'
    id = db.Column(db.Integer, primary_key=True)
    brandename = db.Column(db.String(20))#大众
    carstyle = db.Column(db.String(20))#型号
    carstyle_detail = db.Column(db.String(50))#2014款式
    car = db.relationship('Car',backref='brande')
    def __repr__(self):
        return self.brandename

class Security(db.Model):
    __tablename__ = 'sc_security'
    id = db.Column(db.Integer, primary_key=True)
    main_airbags = db.Column(db.String(15))#主副安全气囊
    anterior_airbags = db.Column(db.String(15))#前后排侧安全气囊
    front_airbags = db.Column(db.String(15))#前后头部安全气囊
    tire = db.Column(db.String(15))#胎压
    car_lock = db.Column(db.String(15))#车内中控锁
    child_lock = db.Column(db.String(15))#儿童锁
    key_lock = db.Column(db.String(15))#钥匙锁
    abs_lock = db.Column(db.String(15))#ABS锁
    esp_lock = db.Column(db.String(15))#ESP锁
    sc_car_id = db.Column(db.Integer,db.ForeignKey('sc_car.id'))

    def __repr__(self):
        return 'sc_brande'

class outsideproperties(BaseModel,db.Model):
    __tablename__='outsideproperties'
    id = db.Column(db.Integer, primary_key=True)
    power_sunroof=db.Column(db.String(10))
    panoramic_sunroof=db.Column(db.String(10))
    Electric_suction_door=db.Column(db.String(10))
    Induction_trunk=db.Column(db.String(10))
    Rain_sensing_Wipers=db.Column(db.String(10))
    rear_wiper=db.Column(db.String(10))
    POWER_WINDOWS=db.Column(db.String(10))
    ELECTRIC_ADJUSTING_KNOB_EXTERIOR_REAR_VISION_MIRROR=db.Column(db.String(10))
    Rearview_mirror_heated=db.Column(db.String(10))
    sc_car_id = db.Column(db.Integer,db.ForeignKey('sc_car.id'))



class Chassis_Brake(db.Model):
    __tablename__ = 'chassis_brake'
    id = db.Column(db.Integer,primary_key=True)
    driving_mode = db.Column(db.String(15))#驱动方式
    help_type = db.Column(db.String(15))#助力类型
    front_suspension_type = db.Column(db.String(15))#前悬挂类型
    rear_suspension_type = db.Column(db.String(15))#后悬挂类型
    front_brake_type = db.Column(db.String(15))#前制动类型
    rear_brake_type = db.Column(db.String(15))#后制动类型
    parking_brake_type = db.Column(db.String(15))#驻车制动类型
    front_tire_specification = db.Column(db.String(20))#前轮胎规格
    rear_tire_specification = db.Column(db.String(20))#后轮胎规格
    sc_car_id = db.Column(db.Integer,db.ForeignKey('sc_car.id'))


class Engine(db.Model):
    __tablename__ = 'sc_engine'
    id = db.Column(db.Integer, primary_key=True)

    displacement = db.Column(db.Float)
    # 进气形式
    intake_form = db.Column(db.String(50))
    # 气缸
    cylinder = db.Column(db.String(50))
    # 最大马力
    max_horsepower = db.Column(db.Integer)
    # 最大扭矩
    max_torque = db.Column(db.Integer)
    # 燃油类型
    car_fuel = db.Column(db.String(10))
    # 燃油编号
    fuel_num = db.Column(db.Integer)
    # 供油方式
    fuel_method = db.Column(db.String(10))
    # 排放标准
    emission_standard = db.Column(db.String(10))

    sc_car_id = db.Column(db.Integer,db.ForeignKey('sc_car.id'))


class Basic_parameters(db.Model):
    __tablename__ = 'Basic_parameters'
    id = db.Column(db.Integer, primary_key=True)
    certificate=db.Column(db.String(20))#证件品牌型号
    manufacturer = db.Column(db.String(20))#厂商
    level=db.Column(db.Integer)#级别
    engine = db.Column(db.String(20))#发动机
    gearbox = db.Column(db.String(20))#变速箱
    body_structure = db.Column(db.String(20))#车身结构
    size=db.Column(db.String(20))#长*宽*高(mm)
    wheel_base=db.Column(db.Integer)#轴距(mm)
    luggage_compartment=db.Column(db.Integer)#行李箱容积(L)
    curb_weight=db.Column(db.Integer)#整备质量(kg)
    sc_car_id = db.Column(db.Integer,db.ForeignKey('sc_car.id'))

    def __repr__(self):
        return self.certificate
