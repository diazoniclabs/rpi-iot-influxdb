# rpi-iot-influxdb

In this tutorial, we will see how to write sensor data from Raspberry Pi to InfluxDB cloud.

Step 1: Go to https://cloud2.influxdata.com/ and signup for an account.

Step 2: Select the Provider and region, enter the company name , read and agree to service agreements.

Step 3: Select a free plan as its easier to get started with FREE PLAN

Step 4: Select Python as the programming language


Step 5: Install the influxdb-client module which is a python library for playing with InfluxDB. adafruit-circuitpython-dht is needed for working of DHT sensor

```pip3 install influxdb-client
pip3 install adafruit-circuitpython-dht
sudo apt-get install libgpiod2
```

Step 6: InfluxDB Cloud uses Tokens to authenticate API access.

Create a Token and store it as an environment variable

Step 7: Initializing the Client

Here, we initialize the token, organization info, and server url that are needed to set up the initial connection to InfluxDB. The client connection is then established with the InfluxDBClient initialization.

```import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
token = os.environ.get("INFLUXDB_TOKEN")
org = "abc@gmail.com"
url = "https://us-east-1-1.aws.cloud2.influxdata.com"
client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
```

Step 8 : Write the data on the InfluxDB Cloud

To start writing data, we need a place to store our time-series data. We call these buckets. Create a bucket and give it a name.

The following code sends data from 0 to 4 after having a delay of 1 second.

```bucket="temp_bucket"
write_api = client.write_api(write_options=SYNCHRONOUS)
   
for value in range(5):
  point = (
    Point("measurement1")
    .tag("tagname1", "tagvalue1")
    .field("field1", value)
  )
  write_api.write(bucket=bucket, org="abc@gmail.com", record=point)
  time.sleep(1) # separate points by 1 second
```
Note : We can change the code by adding the DHT Sensor code embedded inside this

Step 9 : Connect DHT11 sensor to Raspberry Pi

```import adafruit_dht as a
import time
s= a.DHT11(3) #GPIO pin 3
while True:
        h=s.humidity
        t = s.temperature
        print(f"Humidity: {h}% and Temperature {t} C")
        time.sleep(5)
```
        
Step 10: Visualization using a Dashboard

Create a Dashboard


Click on Add cell and follow the hierarchy.


You can create multiple widgets and get a cleaner dashboard for monitoring

Follow this blog for more tutorials on Artificial Intelligence, Data Science, Internet of Things, Edge Computing etc

https://diazoniclabs.medium.com/ 


