# services/users/project/config.py


import os  # new


class BaseConfig:
    """Base configuration"""
    TESTING = False
    MONGO_TRACK_MODIFICATIONS = False  # new


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    MONGO_URI = 'mongodb://mongo:27017/api'


class TestingConfig(BaseConfig):
    """Testing configuration"""
    TESTING = True
    MONGO_DATABASE_URI = os.environ.get('DATABASE_TEST_URL')  # new


class ProductionConfig(BaseConfig):
    """Production configuration"""
    MONGO_DATABASE_URI = os.environ.get('DATABASE_URL')  # new
