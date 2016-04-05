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
    container = os.getenv('HOSTNAME', socket.gethostname())
    host = os.getenv('DOCKER_HOST', 'UNKNOWN')
    color = os.getenv('BG-COLOR','#673ab7')

    visitcount = printme()
    f = open('myfile.txt','a')
    f.write('hi there ' + str(visitcount)) # python will convert \n to os.linesep
    f.write('\n') # python will convert \n to os.linesep
    f.close() # you can omit in most cases as the destructor will call it

    return render_template('page.html', name=name, redis=redis, bg_color=color, container=container, visitcount=visitcount)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80)

