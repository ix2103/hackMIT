from flask.ext.wtf import Form 
from wtforms import StringField, BooleanField 
from wtforms.validators import DataRequired 

class SearchForm(Form):
	search_text = StringField('SEARCH_TEXT', validators=[DataRequired()])

	def validate(self):
		if not Form.validate(self):
			return False
		else: 
			return True
