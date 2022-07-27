from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "llo2ay"
password = "123"
facebook_friends=["Loai","Yonathan","Adan", "George", "Fouad", "Celina"]


@app.route('/', methods=['GET', 'POST'])  # '/' for the default page
def login():
  if request.method == 'GET':
        return render_template('login.html')
  else:
  	username = request.form['username']
  	password = request.form['password']
  	if username== "llo2ay" and password == "123":
  		return render_template('home.html')
  	else: 
  		return render_template('login.html')
  		
          

@app.route('/home', methods=['GET', 'POST'])  # '/' for the default page
def home():
	return render_template('home.html', friends= facebook_friends)


@app.route('/friend_exists/<string:name>', methods=['GET', 'POST'])  # '/' for the default page
def friend_exists(name):
	if name in facebook_friends:
		return render_template('friend_exists.html', name=name, idk="True (Exist)")
	else: 
		return render_template('friend_exists.html', name=name, idk="False (Does Not Exist)")



if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)