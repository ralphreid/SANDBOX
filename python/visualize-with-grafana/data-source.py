from bottle import Bottle, HTTPResponse, run, request, response

app = Bottle()

@app.get("/")
def index():
    return "OK"

@app.hook("after_request")
def enable_cors():
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type"



if __name__ == "__main__":
    run(app, host="localhost", port=8081)
