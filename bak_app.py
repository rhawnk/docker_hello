from flask import Flask
from redis import Redis, RedisError
import os
import socket

# Connect to Redis
redis = Redis(host=os.getenv('REDISSERVER'), db=0)

app = Flask(__name__)


@app.route("/")
def hello():
    try:
        visits = redis.incr('counter')
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"

    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Should be connecting to redis server at:</b> {redisserv}<br/>" \
           "<b>Visits:</b> {visits}"
    return html.format(name=os.getenv('NAME', "world"), redisserv=os.getenv('REDISSERVER', "redis server env variable not set"), hostname=socket.gethostname(), visits=visits)


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80)
