import pymysql
#from Flask_DBConfig
#<- only need this when not hardcoding user & password
#write fake password before uploading to Github
connection = pymysql.connect(host='localhost', user="root", passwd="123")

try:
    with connection.cursor() as cursor: ##the beginning of sql code

        #needed to set the SQL dialect to MySQL for both global and project in order for sql to get recognized
        sql = "CREATE DATABASE meteorstrike IF NOT EXISTS meteorstrike_db"
        cursor.execute(sql)
        sql = """CREATE TABLE IF NOT EXISTS meteorstrike (
id int NOT NULL AUTO_INCREMENT,
latitude FLOAT(10,6),
longitude FLOAT(10,6),
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