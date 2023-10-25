from main.models import Inscription
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, fields


class InscriptionSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Inscription
        load_instance = True
        include_relationships = True
        include_fk = True
