import os
import sae.const
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'threeangel@qq.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'bwdkppbpagkvedfj'
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'IPythoner<threeangel@qq.com>'
    FLASKY_ADMIN = 'new_flasky@qq.com'
    FLASKY_POSTS_PER_PAGE = 20
    FLASKY_FOLLOWERS_PER_PAGE = 50
    FLASKY_COMMENTS_PER_PAGE = 30

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql://root@localhost:3306/app_ibymax'

class SAECloudConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://x5jwjmx5jw:mz0zxyxhj5ki04ji45j1yl3z3my5h0yzywzz52h3@w.rdc.sae.sina.com.cn:3307/app_ibymax' or \
        'mysql://'+ sae.const.MYSQL_USER +':' +sae.const.MYSQL_PASS +'@'+sae.const.MYSQL_HOST+':'+str(sae.const.MYSQL_PORT) +'/'+sae.const.MYSQL_DB

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig,
    'sae':SAECloudConfig
}