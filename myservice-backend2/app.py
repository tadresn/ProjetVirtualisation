from flask import Flask
from flask_cors import CORS
import os
import requests

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    response = {}
    url = os.environ.get("URL_TO_CHECK","NONE")
    if url != "NONE":
        res = requests.get(url)
        if res.status_code == 200 and res.text == "Hello, world":
            response["healthcheck"] = "Website is up ! :)"
        else:
            response["healthcheck"] = "Website is down ! :("

    return response, 200

if __name__ == "__main__":
    app.run()