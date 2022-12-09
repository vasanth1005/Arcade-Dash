import SQLConnection as sql

def IsNewHighScore(score: int):
    connection = sql.Connection()
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("SELECT MAX(SCORE) FROM RACER;")
        data = cursor.fetchone()
        if len(data)>0 and data[0]<score:
            connection.close()
            return True
    connection.close()
    return False

def AddScore(userID: int, score: int):
    connection = sql.Connection()
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("INSERT INTO RACER(ID,SCORE) VALUES ({},{});".format(userID,score))
        connection.commit()
    connection.close()

def GetHighScores(id: int):
    connection = sql.Connection()
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("SELECT MAX(SCORE) FROM RACER;")
        data = cursor.fetchone()
        cursor.execute("SELECT MAX(SCORE) FROM RACER WHERE ID = {};".format(id))
        x = cursor.fetchone()
        if len(data)>0 and len(x)>0:
            return data[0],x[0]
    connection.close()
    return 0,0