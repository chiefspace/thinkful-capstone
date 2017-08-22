import os
class DevelopmentConfig(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://ubuntu:SupplySergeant@localhost:5432/supplysergeant.db"
    DEBUG = True
    SECRET_KEY = os.environ.get("SUPPLY_SERGEANT_SECRET_KEY", os.urandom(12))