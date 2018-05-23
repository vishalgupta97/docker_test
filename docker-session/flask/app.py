from flask import Flask, request, send_from_directory

app = Flask(__name__,static_url_path='')

@app.route('/test/<name>')
def test(name):
    return "It works, "+name+"!"

@app.route('/',methods=['GET','POST'])
def test1():
	if request.method=='GET':
		return send_from_directory('','index.html')
	elif request.method=='POST':
		expr=request.form.get('expr')
		result=eval(expr)
		return 'result: %s' % result 
	
@app.route('/hello')
def test2():
    return "Hello World1!"

if __name__ == "__main__":
    # app.run(debug=True, threaded=True)
    app.run(threaded=True, host="0.0.0.0", port=5000,debug=True)
