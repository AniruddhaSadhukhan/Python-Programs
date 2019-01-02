""" 
Program to Build a Website with Python and Flask
	by Aniruddha
"""

from flask import Flask,render_template

ani_app = Flask(__name__)


@ani_app.route('/about/')	#decorator
def about():
	return render_template("about.html")


@ani_app.route('/')	#decorator
def home():
	return render_template("home.html")
	
if __name__ == "__main__":
	ani_app.run(debug = True)
