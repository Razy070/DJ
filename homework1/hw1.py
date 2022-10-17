import random

from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_index():
    rand = random.randint(1, 1001)
    return f"<h1>{rand}</h1>"


if __name__ == "__main__":
    app.run(threaded=True, port=5000)
