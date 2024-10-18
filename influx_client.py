from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from datetime import datetime
import os, dotenv
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class InfluxClient:
    def __init__(self):
        self.token = os.getenv('TOKEN')
        self.org = os.getenv('ORG')
        self.bucket = os.getenv('BUCKET')
        self.url = os.getenv('URL')

        self.client = InfluxDBClient(url=self.url, token=self.token)
        self.write_api = self.client.write_api(write_options=SYNCHRONOUS)
        self.query_api = self.client.query_api()
        self.delete_api = self.client.delete_api()

    # Create/Insert data
    def write_data(self, stock_name, open_price, high_price, low_price, timestamp=None):
        point = Point(stock_name) \
            .tag("stock", stock_name) \
            .field("Open", open_price) \
            .field("High", high_price) \
            .field("Low", low_price) \
            .time(timestamp or datetime.utcnow(), WritePrecision.NS)

        self.write_api.write(self.bucket, self.org, point)
        print(f"Data written for {stock_name}.")

    # Read data
    def query_data(self, stock_name, start_time):
        query = f'''from(bucket: "{self.bucket}")
        |> range(start: {start_time})
        |> filter(fn: (r) => r._measurement == "{stock_name}")
        |> filter(fn: (r) => r._field == "High")'''
        result = self.query_api.query(org=self.org, query=query)
        
        records = [(record.get_time(), record.get_value()) for table in result for record in table.records]
        return records

    def update_data(self, stock_name, open_price, high_price, low_price, timestamp):
        print(f"Updating data for {stock_name} at {timestamp}")
        self.write_data(stock_name, open_price, high_price, low_price, timestamp)

    def delete_data(self, stock_name, start, stop):
        delete_query = f'_measurement="{stock_name}"'
        self.delete_api.delete(start, stop, delete_query, bucket=self.bucket, org=self.org)
        print(f"Data for {stock_name} deleted from {start} to {stop}")
