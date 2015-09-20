from flask import render_template, request 
from app import app 
from .forms import SearchForm 
from app.processTweet import getJSON

# @app.route('/')
# @app.route('/index')
# def index():
# 	return render_template('index.html')

# @app.route('/search_results', methods=['GET', 'POST'])
# def search():
# 	form = SearchForm() 
# 	if form.validate_on_submit():		# will have to be a POST method 
# 		# redirect to the results page 
		
# 		pass 
# 	return render_template('index.html', form = form)


@app.route('/')
def my_form():
    return render_template("index.html")

@app.route('/output.JSON', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = pt.getJSON(text)
    return processed_text
