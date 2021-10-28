import hashlib
from flask  import Blueprint,render_template,request,redirect, url_for
from sqlalchemy import or_
from application.user.modle import User
from application import db

user_bp =Blueprint('userbak',__name__)

#用户注册
@user_bp.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method =='POST':
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        phone = request.form.get('phone')
        db.create_all()
        if password == repassword:
            #于模型结合，找到模型并创建对象，给对象的属性赋值
            user = User()
            user.username = username
            user.password = hashlib.sha256(password.encode('utf-8')).hexdigest()
            user.phone = phone
            db.session.add(user)
            #提交缓存
            db.session.commit()
            #注册成功，跳转页面
            return redirect(url_for('userbak.user_center'))
            #return  redirect('/show')
        else:
            return '两次密码不一致'

    return render_template('userbak/register.html')

#用户信息展示
@user_bp.route('/show')
def user_center():
    #查询数据库数据
    users = User.query.filter(User.isdelete==0).all()
    return  render_template('userbak/show.html',users=users)


#用户修改信息
@user_bp.route('/user_update',methods=['POST','GET'])
def user_update():
    if request.method == 'POST':
        username = request.form.get('username')
        phone = request.form.get('phone')
        id = request.form.get('id')
        #定位用户
        user = User.query.get(id)
        #修改用户信息
        user.username = username
        user.phone = phone
        #提交数据库
        db.session.commit()
        return redirect(url_for('userbak.user_center'))
    else:
        id = request.args.get('id')
        user = User.query.get(id)
        return render_template('userbak/update.html',user=user)

#删除用户
@user_bp.route('/user_del',methods=['POST','GET'])
def user_del():
    id = request.args.get('id')
    user = User.query.get(id)
    #逻辑删除
    user.isdelete = 1
    db.session.commit()
    return redirect(url_for('userbak.user_center'))

#用户搜索
@user_bp.route('/user_search',methods=['POST','GET'])
def user_search():
    user_input = request.form.get('search')
    users = User.query.filter(User.isdelete==0).filter(or_(
        User.username.contains(user_input),
        User.phone.contains(user_input))).all()
    return  render_template('userbak/show.html',users=users)

#用户登录
@user_bp.route('/login',methods=['POST','GET'])
def user_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        r_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        login_user = User.query.filter_by(isdelete = 0).filter_by(username=username).all
        for u in login_user():
            if u.password == r_password:
                users = User.query.filter_by(isdelete = 0).filter_by(username=username).all()
                return render_template('userbak/show2.html',users=users)
            else:
                return render_template('userbak/login.html',msg='账号或密码错误')
    else:
        return render_template('userbak/login.html')
