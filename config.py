import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-secret_key'
    JWT_SECRET_KEY = '42_Ot8Kyhjkllww_EWQ65VX1E68HhQadOsbXL2u445dYr6jz066Q'


    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ROOT_DIR = basedir
