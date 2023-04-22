from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin1234'
app.config['MYSQL_DB'] = 'flask'
mysql = MySQL(app)

@app.route('/')
def Index():
    return 'hello world'

if __name__ == "__main__":
    app.run(port=3000,debug=True)
