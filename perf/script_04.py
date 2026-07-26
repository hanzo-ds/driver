import sys
from datastore_driver import Client

query = "SELECT * FROM perftest.ontime WHERE FlightDate < '{}'".format(sys.argv[1])
client = Client.from_url('datastore://localhost')

data = client.execute(query)
