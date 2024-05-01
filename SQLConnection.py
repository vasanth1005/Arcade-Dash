import mysql.connector as sql

def Connection():
    return sql.connect(user="****",
                        password="*****",
                        host="us-east.connect.psdb.cloud",
                        database="pythongames")
