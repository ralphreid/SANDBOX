# from https://www.digitalocean.com/community/tutorials/docker-explained-how-to-containerize-python-web-applications

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()