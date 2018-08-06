#*******************************************************************#
#																	#
# Author: Ellis Sanjay Tarmaster									#
# Date: 06/08/2018													#
#																	#
#*******************************************************************#

# Important Imports
from libraries.scrape import *
from flask import Flask, request, render_template

# important to run the flask application
app = Flask(__name__)
app.secret_key = "killer091"

# Login page
@app.route('/', methods=['GET', 'POST'])
def login():

	return render_template('login.html')

# Index page
@app.route('/index', methods=['GET', 'POST'])
def index():

	if request.method == 'POST':

		if str(request.form.get('username')).lower() == "admin" and str(request.form.get('password')).lower() == "asdf1234":

			username = request.form.get('username')

			return render_template('index.html', username=username)

	else:
		return render_template('login.html')

# Result Page
@app.route('/result', methods=['GET', 'POST'])
def result_page():

	return_result = []

	if request.method == 'POST':

		keyword = request.form.get('search')
		number_of_results = int(request.form.get('number_of_pages'))

		keyword_result_without_filter, html_result_without_filter = fetch_results(str(keyword), number_of_results, 'en')
		results = parse_results(html_result_without_filter, keyword_result_without_filter)

		for i in results:
			return_result += [[i['rank'], i['title'], i['description'], i['link']]]

		return render_template('results.html', result=return_result)

# Logout
@app.route('/login', methods=['GET', 'POST'])
def logout():

	return render_template('login.html')


# Main Function
if __name__ == '__main__':
	app.run(host='localhost', debug=True)