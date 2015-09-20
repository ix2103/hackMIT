from app import db 

class Search(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	query = db.Column(db.String(150), index = True, unique = False)

	def __repr__():
		return 'Search is %r' % (self.query)

class Results(db.Model):
	tweet = db.Column(db.String(150), index = False, unique = False)
	# JSON shit 
