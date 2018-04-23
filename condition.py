from flask import Flask,render_template
app=Flask(__name__)

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
	return render_template('condition.html',name=name)

@app.route('/users/')
def users():
	names=['Thomas','simon','lee','jamie','sylvester']
	return render_template('loop.html',names=names)


@app.route('/inherits/')
def inherits():
	return render_template('base.html')

@app.route('/inherits/one/')
def inherits_one():
	return render_template('in1.html')

@app.route('/inherits/two/')
def inherits_two():
	return render_template('in2.html')

if __name__=="__main__":
	app.run(debug=True)