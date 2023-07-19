from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "poli"
password = "123"
facebook_friends=["Loai","Yonathan","Adam", "George", "Eva", "Liem","Marina","Tim","Ilya"]


@app.route('/',methods=["GET","POST"])  # '/' for the default page
def login():
	if request.method=="POST":
		use_n=request.form["username"]
		pass_w=request.form["password"]
		if use_n==username and pass_w==password:
			return redirect(url_for('home'))
		else:
			return render_template('login.html')
	else:
		return render_template('login.html')

@app.route('/home')
def home():
	return render_template("home.html",friends=facebook_friends)
  
@app.route("/friend/<string:friend>")
def friend(friend):
	if friend in facebook_friends:
		return  render_template('friend_exists.html', n=friend, b= True)
	else:
		return render_template('friend_exists.html', n=friend, b= False)



if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)