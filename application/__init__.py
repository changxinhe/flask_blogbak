from flask import  Flask
from application import config
from application.article.view import article_bp
from application.datasource import db, bootstrap
from application.user.view import user_bp
from application.config import Config

def create_app():
    app = Flask(__name__,
                template_folder=Config.template_folder,
                static_folder='')

    #初始化配置文件
    app.config.from_object(config.DevelopmentConfig)

    #初始化数据库
    db.init_app(app=app)
    #初始化bootstrap
    bootstrap.init_app(app=app)

    #注册视图函数
    app.register_blueprint(user_bp)
    app.register_blueprint(article_bp)
    return app