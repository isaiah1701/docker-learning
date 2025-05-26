from flask import Flask, render_template
import redis
import os

app = Flask(__name__)

# Read Redis connection details from env variables
redis_host = os.environ.get('REDIS_HOST', 'localhost')
redis_port = int(os.environ.get('REDIS_PORT', 6379))
redis_client = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

@app.route('/')
def welcome():
    visits = redis_client.incr('counter')
    return render_template("index.html", count=visits)

@app.route('/count')
def count():
    visits = redis_client.incr('counter')
    return render_template("count.html", count=visits)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
