#ORM 类---》表
#类对象 ---》表中记录
from application.datasource import db
from datetime import  datetime
import  time
import datetime


class User(db.Model):
    __tatlename__ = 'users'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    show_name = db.Column(db.String(15),default='用户X')
    username = db.Column(db.String(15),unique=True,nullable=False)
    password = db.Column(db.String(64),nullable=False)
    phone = db.Column(db.String(12),nullable=False,unique=True)
    email = db.Column(db.String(30))
    icon = db.Column(db.String(100))
    #默认使当前系统时间
    rdatetime =db.Column(db.DateTime,default=datetime.datetime.now)
    isdelete = db.Column(db.Boolean,default=0)
    #一对多，增加一个字段
    articles = db.relationship('Article',backref='user')

    def __init__(self):
        return self.username
