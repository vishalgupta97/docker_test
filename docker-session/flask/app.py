from flask import Flask, request  # , current_app, jsonify

app = Flask(__name__)

@app.route('/test/<name>')
def test(name):
    return "It works, "+name+"!"

if __name__ == "__main__":
    # app.run(debug=True, threaded=True)
    app.run(threaded=True, host="0.0.0.0", port=5000)
