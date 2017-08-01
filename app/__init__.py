from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login.login_manager import LoginManager
from config import config  #flasky/config.py

#创建flask扩展的对象，但不初始化对象
bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
#LoginManager类时用来存放有关用户登陆的设置，不跟任一个app绑定，而是create one instance of
#login_manager in the main body and then bind it to app in a factory function.
login_manager = LoginManager()
login_manager.session_protection = 'strong'
#默认情况下，当未登录的用户尝试访问一个 login_required
#装饰的视图，Flask-Login 会闪现一条消息并且重定向到登录视图
#默认的闪现消息是 Please log in to access this page
login_manager. login_view= 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    #加载配置选项，使用app.config.from_object(),参数是module/class
    app.config.from_object(config[config_name])
    #初始化app
    config[config_name].init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    # 此时app还不完整，没有附加路由和自定义的错误页面
    #创建完蓝本后，注册蓝本到程序app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    #注册auth蓝本
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    return app
