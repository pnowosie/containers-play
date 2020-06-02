from cow_say.extensions import db

class Quote(db.Model):
    __tablename__ = 'quotes'

    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String, nullable=True)
    quote = db.Column(db.String, nullable=False)