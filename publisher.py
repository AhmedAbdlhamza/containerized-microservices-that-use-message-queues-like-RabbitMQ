import pika

# Establish a connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue
channel.queue_declare(queue='my_queue')

# Publish a message
channel.basic_publish(exchange='', routing_key='my_queue', body='Hello, RabbitMQ!')

# Close the connection
connection.close()
