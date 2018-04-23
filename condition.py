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

if __name__=="__main__":
	app.run(debug=True)