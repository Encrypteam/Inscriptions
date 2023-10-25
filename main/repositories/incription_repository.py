from .. import db
from main.repositories import Create, Read, Update
from main.models import Inscription


class IncriptionRepository(Create, Read, Update):

    def __init__(self):
        self.inscription = Inscription

    def create(self, model: db.Model) -> Inscription:
        db.session.add(model)
        db.session.commit()
        return model

    def find_all(self):
        return db.session.query(self.inscription).all()

    def find_by_id(self, id: int) -> Inscription:
        return db.session.query(self.inscription).get(id)

    def find_by_username(self, name: str) -> Inscription:
        return db.session.query(self.inscription).filter(self.inscription.name == name).first()

    def find_by_email(self, email: str) -> Inscription:
        return db.session.query(self.inscription).filter(self.inscription.email == email).first()

    def update(self, inscription: Inscription) -> Inscription:
        db.session.add(inscription)
        db.session.commit()
        return inscription