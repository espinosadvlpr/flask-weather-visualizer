from random import randint
from flask import Flask, render_template, request
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
    query = """select ciudad, 
            round(sum(temperatura)/count(departamento),2) as temperatura, 
            round(sum(humedad)/count(departamento),2) as humedad
            from datos_meteorologicos group by 1;"""
    data = database_query(query)
    return render_template('first.html', averages=data)

@app.route('/second')
def Second():
    query = """select ciudad,
            round(sum(velocidad_viento)/count(departamento),2),
            max(temperatura), min(temperatura)
            from datos_meteorologicos
            group by 1
            order by 3;"""
    data = database_query(query)
    return render_template('second.html', data_max_min=data)

@app.route('/third')
def Third():
    cities = """select ciudad from datos_meteorologicos
            group by ciudad;"""
    dates = """select fecha from datos_meteorologicos
            group by fecha;"""
    cities_data = database_query(cities)
    dates_data = database_query(dates)
    return render_template('third.html',cities=cities_data, dates=dates_data)

@app.route('/third_info',methods=['POST'])
def ThirdInfo():
    if request.method == 'POST':
        city = request.form['city']
        date = request.form['date']
        query = f"""select hora,pronostico,temperatura,velocidad_viento,humedad
        from datos_meteorologicos where ciudad = '{city}' and 
        fecha = '{date}' and cast(hora as time) between time('13:00:00') and time('20:00:00');"""
        data = database_query(query)
        forecast = data[randint(0, 7)][1]
    return render_template('third_info.html',city=city,date=date,forecast=forecast,weather=data)

@app.route('/fourth')
def Fourth():
    cities = """select ciudad from datos_meteorologicos
            group by ciudad;"""
    cities_data = database_query(cities)
    return render_template('fourth.html',cities=cities_data)

@app.route('/fourth_chart',methods=['POST'])
def FourthChart():
    if request.method == 'POST':
        city = request.form['city']
        variable = request.form['variable']
        query = f"""select fecha, round(sum({variable})/count(fecha),2)
                from datos_meteorologicos where ciudad = '{city}' group by 1;"""
        data = database_query(query)
        labels = [row[0] for row in data]
        values = [row[1] for row in data]
        chart_title = variable.replace("_", " ").title()
    return render_template('fourth_chart.html',city=city,title=chart_title,labels=labels,values=values)

def temperature_for_city(city):
    query = f"""select temperatura
            from datos_meteorologicos where ciudad = '{city}';"""
    return database_query(query)

@app.route('/fifth')
def Fifth():
    labels = list(range(1,80))
    tunja = [row[0] for row in temperature_for_city('Tunja')]
    bucaramanga =[row[0] for row in  temperature_for_city('Bucaramanga')]
    barranquilla =[row[0] for row in  temperature_for_city('Barranquilla')]
    bogota =[row[0] for row in  temperature_for_city('Bogotá')]
    cartagena =[row[0] for row in  temperature_for_city('Cartagena')]
    barranca =[row[0] for row in  temperature_for_city('Barranca')]
    return render_template('fifth.html',labels=labels,tunja=tunja,bucaramanga=bucaramanga,
                           barranquilla=barranquilla,bogota=bogota,
                           cartagena=cartagena,barranca=barranca)

if __name__ == "__main__":
    app.run(port=3000,debug=True)
