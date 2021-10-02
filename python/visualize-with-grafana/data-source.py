from bottle import Bottle, HTTPResponse, run, request, response

app = Bottle()

@app.get("/")
def index():
    return "OK"

if __name__ == "__main__":
    run(app, host="localhost", port=8081)
