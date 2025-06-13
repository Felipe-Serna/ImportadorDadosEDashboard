import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("IOT-Temp.csv")

df.rename(columns={
    'room_id/id': 'device_id',
    'noted_date': 'date_time',
    'temp': 'temperature',
    'out/in': 'location'
}, inplace=True)

df['date_time'] = pd.to_datetime(df['date_time'], format='%d-%m-%Y %H:%M')

engine = create_engine("postgresql://postgres:123456@localhost:5432/iotdb")
df.to_sql("temperature_readings", engine, if_exists="replace", index=False)

print("✅ Dados importados com sucesso!")
