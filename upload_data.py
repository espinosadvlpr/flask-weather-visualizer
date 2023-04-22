import pymysql
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine, text

print("Uploading CSV file ...")
data_frame = pd.read_csv("./datos_metereologicos.csv", encoding="utf-8")
data_frame.columns = map(str.lower, data_frame.columns)
print(data_frame)
print("CSV data successfully charged. Loading into the database...")

table_name = "datos_meteorologicos"
sql_engine = create_engine(
    'mysql+pymysql://[user]:[password]@127.0.0.1/[database_name]', pool_recycle=3600)
db_connection = sql_engine.connect()

try:
    frame = data_frame.to_sql(table_name, db_connection, if_exists='replace', index=True, index_label='id')
except ValueError as value_error:
    print(value_error)
except Exception as exception:
    print(exception)
else:
    print(f'Data successfully charged to table {table_name}.')
finally:
    db_connection.close()
