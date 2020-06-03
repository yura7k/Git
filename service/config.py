import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    FLASK_DEBUG=1
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    ### Flask SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:123456@localhost/service'

    ### Flask-security
    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_HASH = 'pbkdf2_sha256'
    
    ### Google maps API key
    GOOGLEMAPS_KEY = 'AIzaSyA452LdHNov83aWa2feptPwDSbLMMhMMYE'

    # Flask mail
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'vasyaxxxx'
    MAIL_PASSWORD = 'motherlandvasyaxxxx'
    ADMINS = ['your-email@example.com']
    POSTS_PER_PAGE = 25
