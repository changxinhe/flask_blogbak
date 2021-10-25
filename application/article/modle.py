#ORM 类---》表
#类对象 ---》表中记录
from application.datasource   import db
from datetime import  datetime

class Article(db.Model):
    __tatlename__ = 'article'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title =db.Column(db.String(50),nullable=False)
    content = db.Column(db.Text,nullable=False)
    pdatetime = db.Column(db.DateTime,default=datetime.datetime.now())
    click_num = db.Column(db.Integer,default=0)
    save_num = db.Column(db.Integer,default=0)
    love_num = db.Column(db.Integer,default=0)
    #外键
    user_id = db.Column(db.Integer,db.Foreignkey('user.id'),nullable=False)
