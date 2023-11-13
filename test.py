from flask import Flask, jsonify
import os
import pymysql
#from flask_cors import CORS

app = Flask(__name__)
#CORS(app, resources={r'*':{ 'origins' : 'http://localhost:8080'}}) client와 통신 안해서 이거 필요없음

def Dbconnect():
    conn = pymysql.connect(host = "fortestflaskaws.chkgnehk1uff.ap-northeast-2.rds.amazonaws.com",
                      user = "testFlask",
                      password = "12345678",
                      db = "disease",
                      charset = "utf8")

    return conn

def Dbclose(conn):
    conn.close


def SelectId(TABLE, DISEASE_ID):
    
    conn = Dbconnect()
    cursor = conn.cursor()

    sql = '''SELECT {id_code} 
    FROM {table}
    ORDER BY {id_code}'''.format(table = TABLE, id_code = DISEASE_ID)

    cursor.execute(sql)
    result = cursor.fetchall()
    
    result_list = [0] * len(result)


    for i in range(len(result)):
        result_list[i] = result[i][0]
    
    Dbclose(conn)

    return result_list



@app.route('/')
def home() :
    return "Hello World"


@app.route("/getId")
def getId() :
    
    result = SelectId("DISEASE", "id")
    return result
    
    
@app.route("/getJsonId")
def getJsonId() :
    
    result = SelectId("DISEASE", "id")
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

