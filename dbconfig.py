import pymysql
import dbconfig
connection = pymysql.connect(host='localhost', user="root", passwd=123)

try:
    with connection.cursor() as cursor: ##the beginning of sql code

        sql = "CREATE DATABASE IF NOT EXISTS meteorstrike"
        cursor.execute(sql)
        sql = """CREATE TABLE IF NOT EXISTS meteorstrike.strikes (
id int NOT NULL AUTO_INCREMENT,
latitude FLOAT(10,6)
longitude FLOAT(10,6)
date DATETIME,
category VARCHAR(50),
description VARCHAR(1000),
updated_at TIMESTAMP,
PRIMARY KEY (id)
)"""
        cursor.execute(sql);
    connection.commit()
finally:
    connection.close()