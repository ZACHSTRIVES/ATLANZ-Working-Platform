import os
import pymysql

DEBUG = False

SECRET_KEY = os.urandom(24)

db = pymysql.connect(host='localhost', user='root',
                     password='wangziqi123', db='ATLANZ', port=3306)