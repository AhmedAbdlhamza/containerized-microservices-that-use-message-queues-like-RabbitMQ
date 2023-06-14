import pika

# Establish a connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue
channel.queue_declare(queue='my_queue')

# Define the callback function for consuming messages
def callback(ch, method, properties, body):
    print("Received message:", body)

# Start consuming messages
channel.basic_consume(queue='my_queue', on_message_callback=callback, auto_ack=True)

# Keep the script running and processing messages
print('Waiting for messages. To exit, press Ctrl+C')
channel.start_consuming()
