#!/usr/bin/env python
import pika
 
credentials = pika.PlainCredentials('philip', 'Passw0rd')
parameters = pika.ConnectionParameters(credentials=credentials, host='localhost')
connection = pika.BlockingConnection(parameters=parameters)
