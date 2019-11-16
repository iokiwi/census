from census.app import db


class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reference = db.Column(db.String(80), nullable=False)
    origin_ip = db.Column(db.String(45))

    def __repr__(self):
        return f"<Submission: count='{self.id}' reference={self.reference}" \
               f" origin_ip='{self.origin_ip}'>"
