import SQLConnection as sql

class User:

    def __init__(self):
        self.ID = 0
        self.Name = ""

    def login(self, username: str, password: str):
        connection = sql.Connection()
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT ID,NAME FROM USER WHERE USERNAME = '{}' AND PASSWORD = '{}';".format(username,password))
            data = cursor.fetchall()
            if len(data) == 1:
                self.ID = data[0][0]
                self.Name = data[0][1]
                connection.close()
                return True                                
        connection.close()
        return False