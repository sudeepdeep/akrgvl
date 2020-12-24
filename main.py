from flask import Flask,render_template,url_for
app = Flask(__name__)

@app.route('/')

def home():
	return render_template('home.html')

@app.route('/c')
def c():
	return render_template('c.html')

@app.route('/c++')
def c1():
	return render_template('c++.html')

@app.route('/python')
def python():
	return render_template('python.html')

@app.route('/java')
def java():
	return render_template('java.html')

@app.route('/htm')
def htm():
	return render_template('htm.html')

@app.route('/sql')
def sql():
	return render_template('sql.html')

if __name__ == "__main__":
	app.run(debug = True)