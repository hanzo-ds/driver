import sys
from datastore_driver import Client

query = "SELECT * FROM perftest.ontime WHERE FlightDate < '{}'".format(sys.argv[1])
client = Client.from_url('datastore://localhost')

for row in client.execute_iter(query):
  pass
