from flask import Flask, make_response

app = Flask(__name__)

@app.route("/")
def index():
	return make_response('Hello World!', 200)

if __name__ == "__main__":
    app.run(host='0.0.0.0')