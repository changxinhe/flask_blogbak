import hashlib
from flask import Blueprint, request, render_template
from application import db
from application.user.modle import User

user_bp=Blueprint('user',__name__,url_prefix='/user')

#用户注册
@user_bp.route('/register',methods=['POST','GET'])
def user_register():
    if request.method == 'POST':
            if request.form.get('password') == request.form.get('repassword'):
                db.create_all()
                newuser=User()
                newuser.show_name = request.form.get('show_name')
                newuser.username = request.form.get('username')
                password =request.form.get('password')
                newuser.password = hashlib.sha256(password.encode('utf-8')).hexdigest()
                newuser.phone = request.form.get('phone')
                newuser.email = request.form.get('email')
                db.session.add(newuser)
                db.session.commit()
                return '注册成功'
            else:
                return '两次密码不一致'
    else:
        return render_template('user/register.html')

@user_bp.route('/login',methods=['POST','GET'])
def user_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        users =User.query.filter_by(isdelete=0).filter_by(username=username).all
        # login_user = User.query.filter_by(isdelete = 0).filter_by(username=username).all
        for u in users():
            if u.password == password:
                return '登录成功'
            else:
                return '账号或密码错误'
        pass
    else:
        return render_template('user/login.html')