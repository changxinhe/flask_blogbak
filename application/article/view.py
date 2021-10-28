from flask import Blueprint, request, render_template

from application.datasource import db
from application.user.modle import User
from application.article.modle import Article

article_bp = Blueprint('article',__name__)

@article_bp.route('/publish',methods=['POST','GET'])
def publish_article():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        uid = request.form.get('uid')
        #添加文章
        article = Article()
        article.title = title
        article.content = content
        article.user_id = uid
        db.session.add(article)
        db.session.commit()
        return '添加成功！'
    else:
        users = User.query.filter_by(isdelete = False).all()
        return render_template('article/add_article.html',users=users)
    pass

@article_bp.route('/shows')
def show_article():
    articles = Article.query.all()
    return render_template('/article/show.html',articles=articles)

@article_bp.route('/shows2')
def shows2_article():
    id =request.args.get('id')
    users = User.query.get(id)
    return render_template('/article/show2.html',users=users)

@article_bp.route('/test')
def test():
    return render_template('user/register.html')