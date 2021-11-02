#ORM 类---》表
#类对象 ---》表中记录
from application.datasource   import db
# from datetime import  datetime
import datetime

class Article(db.Model):
    __tatlename__ = 'article'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title =db.Column(db.String(50),nullable=False)
    content = db.Column(db.Text,nullable=False)
    pdatetime = db.Column(db.DateTime,default=datetime.datetime.now)
    click_num = db.Column(db.Integer,default=0)
    save_num = db.Column(db.Integer,default=0)
    love_num = db.Column(db.Integer,default=0)
    #外键
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)

class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    comment = db.Column(db.String(255),nullable=False)
    #外键用户
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    #外键文章
    article_id = db.Column(db.Integer,db.ForeignKey('article.id'),nullable=False)