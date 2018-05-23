from flask import Flask, request  # , current_app, jsonify

app = Flask(__name__)

@app.route('/name/<name>')
def test(name):
    return "It works, "+name+"!"

@app.route('/hello/<name>')
def test1(name):
    return "Hi, "+name+"!"
	
@app.route('/')
def test2():
	return "Hello World"

if __name__ == "__main__":
    # app.run(debug=True, threaded=True)
    app.run(threaded=True, host="0.0.0.0", port=5000)
