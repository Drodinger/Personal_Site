from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def about():
	return render_template('about.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')