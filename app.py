import adafruit_dht as a
import time
import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
token = os.environ.get("INFLUXDB_TOKEN")
org = "abc@gmail.com"
url = "https://us-east-1-1.aws.cloud2.influxdata.com"
client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

s= a.DHT11(3) #GPIO pin 3
bucket="temp_bucket"
write_api = client.write_api(write_options=SYNCHRONOUS)
   
while True:
  h=s.humidity
  t = s.temperature
  print(f"Humidity: {h}% and Temperature {t} C")
  point = (
    Point("measurement1")
    .tag("tagname1", "tagvalue1")
    .field("field1", t,"field2",h)
  )
  write_api.write(bucket=bucket, org="abc@gmail.com", record=point)
  time.sleep(10) # separate points by 10 seconds
