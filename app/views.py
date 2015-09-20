from flask import render_template
from app import app 
from .forms import SearchForm 

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
	form = SearchForm() 
	if form.validate_on_submit():		# will have to be a POST method 
		# redirect to the results page 
		pass 
	return render_template('index.html', form = form)