from flask import Flask
import redis
import os

app = Flask(__name__)

# Read Redis connection details from env variables
redis_host = os.environ.get('REDIS_HOST', 'localhost')
redis_port = int(os.environ.get('REDIS_PORT', 6379))
redis_client = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

@app.route('/')
def welcome():
    return "Welcome to the Flask + Redis Challenge!"

@app.route('/count')
def count():
    visits = redis_client.incr('counter')
    return f"Visit count: {visits} bro"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
from flask import Flask
import redis
import os

app = Flask(__name__)

# Read Redis connection details from env variables
redis_host = os.environ.get('REDIS_HOST', 'localhost')
redis_port = int(os.environ.get('REDIS_PORT', 6379))
redis_client = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

@app.route('/')
def welcome():
    return "Welcome to the Flask + Redis Challenge!"

@app.route('/count')
def count():
    visits = redis_client.incr('counter')
    return f"Visit count: {visits}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)