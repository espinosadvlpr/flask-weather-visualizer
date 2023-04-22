from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin1234'
app.config['MYSQL_DB'] = 'flask'
mysql = MySQL(app)

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/first')
def First():
    cursor = mysql.connection.cursor()
    query = """select departamento, 
            round(sum(temperatura)/count(departamento),2) as temperatura, 
            round(sum(humedad)/count(departamento),2) as humedad
            from datos_meteorologicos group by 1;"""
    cursor.execute(query)
    data = cursor.fetchall()
    return render_template('first.html', averages=data)

if __name__ == "__main__":
    app.run(port=3000,debug=True)
