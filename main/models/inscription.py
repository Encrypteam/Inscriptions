from main import db


class Inscription(db.Model):
    tablename__ = 'Inscription'
    id = db.Column('id', db.Integer, primary_key=True)
    user_name = db.Column('user_name', db.String(50), nullable=False)
    user_lastname = db.Column('user_lastname', db.String(50), nullable=False)
    dni = db.Column('dni', db.Integer, nullable=False, unique=True)
    subject = db.Column('signature', db.String(50), nullable=False, unique=True)
    trasaction_id = db.Column('trasaction_id', db.String(120), nullable=False, unique=True)


    def __repr__(self):
        return f'<Inscription: {self.user_name} {self.user_lastname} {self.dni} {self.subject}>'