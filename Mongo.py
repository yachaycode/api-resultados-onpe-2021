import os
import json
import sys
from pymongo import MongoClient
from settings import setting

# classConectionDb = None
class SingletonDecorator:
    def __init__(self, klass):
        self.klass = klass
        self.instance = None

    def __call__(self, *args, **kwds):
        if self.instance == None:
            self.instance = self.klass(*args, **kwds)
        return self.instance

class classConectionDb:
    def __init__(self):
        self.cone = None

class classConectionMongo:
    def __init__(self):
        client = MongoClient(setting.CONNECTION_MONGODB_HOST, setting.CONNECTION_MONGODB_PORT)
        db = client[setting.CONNECTION_MONGODB_DB_AUTH]
        db.authenticate(setting.CONNECTION_MONGODB_USER, setting.CONNECTION_MONGODB_PASSWORD)
        self.db = client[setting.CONNECTION_MONGODB_DB]


class Db:
    # Here will be the instance stored.
    __instance = None
    session = ""
    # mongo database connection
    @staticmethod
    def conectionMongo():
        global classConectionDb
        classConectionDb = SingletonDecorator(classConectionDb)
        x = classConectionMongo()
        return x.db

