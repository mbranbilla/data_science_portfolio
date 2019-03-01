from flask import Flask
import os
import socket


app = Flask(__name__)

@app.route("/")
def main():
    html = "<h3>Basic Docker Template.</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" 

    return html.format(hostname=socket.gethostname())


@app.route("/test")
def test():
    return "Success!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
