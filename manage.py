#管理文件
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
import logging


from cars import create_app,db


app = create_app('development')

manage = Manager(app)
Migrate(app,db)
manage.add_command('db_command',MigrateCommand)


@app.route('/index',methods=['get'])
def index():
    return '首页'


if __name__ == '__main__':
    manage.run()

























