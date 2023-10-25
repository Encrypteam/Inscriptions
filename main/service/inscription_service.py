from main.repositories import IncriptionRepository
from main.models import Inscription


class InscriptionService:
    def __init__(self):
        self.repository = IncriptionRepository()

    def create(self, inscription: Inscription) -> Inscription:
        inscription = self.repository.create(inscription)
        return inscription

    def find_by_inscription(self, inscription: str) -> Inscription:
        return self.repository.find_by_inscription(inscription)

    def find_by_id(self, id):
        inscription = self.repository.find_by_id(id)
        return inscription

    def find_all(self):
        inscriptions = self.repository.find_all()
        return inscriptions

    def update(self, inscription: Inscription) -> Inscription:
        inscription = self.repository.update(inscription)
        return inscription