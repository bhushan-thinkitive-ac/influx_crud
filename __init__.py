from influxdb_client import InfluxDBClient
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN')
org = os.getenv('ORG')
bucket = os.getenv('BUCKET')

client = InfluxDBClient(url="http://localhost:8086", token=token)
