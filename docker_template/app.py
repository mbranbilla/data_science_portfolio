from flask import Flask
import urllib.request


app = Flask(__name__)

@app.route("/teste")
def teste():
    return "Success!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
