import os
from flask import Flask
import redis

app = Flask(__name__)
r = redis.Redis(host="redis", port=6379, password=os.environ["REDIS_PASSWORD"])

@app.route("/")
def home():
    count = r.incr("visits")
    return f"Visits: {count}\n"

app.run(host="0.0.0.0", port=5000)
