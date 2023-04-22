from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin1234'
app.config['MYSQL_DB'] = 'flask'
mysql = MySQL(app)

def database_query(query):
    cursor = mysql.connection.cursor()
    cursor.execute(query)
    return cursor.fetchall()

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/first')
def First():
    query = """select departamento, 
            round(sum(temperatura)/count(departamento),2) as temperatura, 
            round(sum(humedad)/count(departamento),2) as humedad
            from datos_meteorologicos group by 1;"""
    data = database_query(query)
    return render_template('first.html', averages=data)

@app.route('/second')
def Second():
    query = """select departamento,
            round(sum(velocidad_viento)/count(departamento),2),
            max(temperatura), min(temperatura)
            from datos_meteorologicos
            group by 1
            order by 3;"""
    data = database_query(query)
    return render_template('second.html', data_max_min=data)

if __name__ == "__main__":
    app.run(port=3000,debug=True)
