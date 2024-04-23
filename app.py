
import requests
import uuid
import csv
from flask import Flask, render_template, request

app = Flask(__name__)   

def api():
    url = "https://api.adviceslip.com/advice"

    try:
        response = requests.get(
            url,
            cookies={"session": str(uuid.uuid4())},
            headers={"Accept": "*/*", "User-Agent": "python-requests"},
        )
        response.raise_for_status()

        # Extract advice from response
        advice = response.json()
        return advice
    except (KeyError, IndexError, ValueError):
        return None

@app.route('/')
def index():
    if request.method == 'GET':
        quote = api()
        return render_template("index.html", quote = quote)

if __name__ =="__main__":
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000)