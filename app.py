# -*- coding: utf-8 -*-
import time
import ConfigParser

from library.config_parser import configSectionParser
from library.mysql_db_connection import *
from controller.data_ticker import *
from controller.data_checker import *

#INIT CONFIG
config = ConfigParser.ConfigParser()
config.read("config/config.cfg")
 
#USER INFORMATION
cex_user = configSectionParser(config,"CEXAPI DATA")['user']
cex_key = configSectionParser(config,"CEXAPI DATA")['key']
cex_secret = configSectionParser(config,"CEXAPI DATA")['secret']

#DATABASE
host = configSectionParser(config,"DATABASE")['host']
db = configSectionParser(config,"DATABASE")['db']
user = configSectionParser(config,"DATABASE")['user']
password = configSectionParser(config,"DATABASE")['password']

#CURRENCY
currency = configSectionParser(config,"CURRENCY")['currency']

#DATABASE CONNECTION
conn = MyDB(host,db,user,password)
db = conn.connect_mysql()

#DATABASE QUERIES
query = Querys(db) 

#SECONDS PER QUERY
spq = configSectionParser(config,"SECONDS PER QUERY")['seconds']

#DAYS TO CHECK
dtc = configSectionParser(config,"DAYS TO CHECK")['days']

#TICKER
tick = Ticker(query,cex_user,cex_key,cex_secret,currency)

#DATA CHECKER
check = Checker(dtc,query,db,cex_user,cex_key,cex_secret,currency)

#START
while True:
    time.sleep(int(spq))
    tick.execute_insert()
    check.execute_check_data()

