from myapp import db

class TopCity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String(64), unique=True, index=True)
    city_rank = db.Column(db.Integer, unique=True)
    visited = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return f'<{self.city_rank}: {self.city_name}>'
