# containerized-microservices-that-use-message-queues-like-RabbitMQ
To build containerized microservices that use message queues like  RabbitMQ using Python, you can follow these steps:

1. Set up a Docker environment: Install Docker on your machine and make sure it's running properly.

2. Create a new directory for your project and navigate to it using the terminal or command prompt.

3. Initialize a new Python project by running the following command:
   ```shell
   $ mkdir my_project
   $ cd my_project
   $ python3 -m venv venv
   $ source venv/bin/activate  # For Linux/Mac
   $ venv\Scripts\activate  # For Windows
   ```

4. Install the required Python packages. In this case, we'll need the messaging library for the specific message queue (ActiveMQ or RabbitMQ) and any other dependencies your microservices require. For example, to use RabbitMQ, you can install the `pika` package:
   ```shell
   $ pip install pika
   ```

5. Create a Python script for your microservice. Let's say you're building a publisher and subscriber model using RabbitMQ. Create two Python files: `publisher.py` and `subscriber.py`. In `publisher.py`, you can use the following code to publish messages:
   ```python
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
   ```

   In `subscriber.py`, you can use the following code to consume messages:
   ```python
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
   ```

6. Create a Dockerfile in the project directory to containerize your microservices. Here's an example Dockerfile for the publisher service:
   ```Dockerfile
   FROM python:3.9-slim

   WORKDIR /app

   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt

   COPY publisher.py .

   CMD ["python", "publisher.py"]
   ```

   And here's an example Dockerfile for the subscriber service:
   ```Dockerfile
   FROM python:3.9-slim

   WORKDIR /app

   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt

   COPY subscriber.py .

   CMD ["python", "subscriber.py"]
   ```

7. Create a `requirements.txt` file in the project directory to specify the Python dependencies for your microservices. In this case, you only need to include `pika`:
   ```
   pika
   ```

8. Build and run the Docker containers for your microservices. Open a terminal or command prompt, navigate to the project directory, and run the following commands:
   ```shell
   $ docker build -t publisher-service -f Dockerfile.publisher .


   $ docker build -t subscriber-service -f Dockerfile.subscriber .

   $ docker run -d --name publisher publisher-service
   $ docker run -d --name subscriber subscriber-service
   ```

   This will build the Docker images for each service and run the containers in the background.

9. Verify that the messages are being exchanged between the microservices by checking the output of the subscriber container. You can use the following command:
   ```shell
   $ docker logs subscriber
   ```

   You should see the received messages printed in the terminal.

That's it! You've containerized your microservices using message queues in Python and deployed them using Docker. You can scale and manage these services easily in a containerized environment.
