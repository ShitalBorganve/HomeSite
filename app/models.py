from app import db

class Painting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    artist = db.Column(db.String(120))
    href = db.Column(db.String(120))

    def __repr__(self):
        return '<Title %r Artist %r>' % (self.title, self.artist)

