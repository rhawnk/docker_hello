from flask import Flask, render_template
from redis import Redis, RedisError
import os
import socket

# Connect to Redis
redis = Redis(host=os.getenv('REDISSERVER'), db=0)

app = Flask(__name__)

def printme():
    try:
        visits = redis.incr('counter')
    except RedisError:
        visits = "cannot connect to Redis, counter disabled"
    return visits

@app.route("/")
def hello():
    name = os.getenv('NAME', "world")
    redis = os.getenv('REDISSERVER')
    hostname = socket.gethostname()
    # visitcount = printme()
    return render_template('page.html', name=name, redis=redis, hostname=hostname, visitcount=printme())

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80)
