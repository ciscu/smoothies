from app import db
from werkzeug.security import generate_password_hash, check_password_hash

Model = db.Model
Column = db.Column
String = db.String
Integer = db.Integer
ForeignKey = db.ForeignKey
relationship = db.relationship
Table = db.Table

class ValidationError(ValueError):
    pass


Recipe = Table(
    'recipes',
    Column('smoothie_id', Integer, ForeignKey('smoothie.id')),
    Column('ingredient_id', Integer, ForeignKey('ingredient.id'))
)


class Smoothie(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(64), index=True, unique=True)
    recipe = relationship('Ingredient', secondary=Recipe, backref="recipes", lazy="dynamic")

    def __repr__(self):
        return '<title {}>'.format(self.name)

    def export_data(self):
        return {
            "id": self.id,
            "name": self.name,
            "ingredients": [ingredient.name for ingredient in self.recipe]
        }

    def import_data(self, data):
        try:
            self.name = data["name"]

        except KeyError as e:
            raise ValidationError('Invalid Smoothie: missing' + e.args[0])



class Ingredient(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(64), index=True, unique=True)
    smoothie_id = Column(Integer, ForeignKey("smoothie.id"))

    def import_data(self, data):
        try:
            self.name = data
        except KeyError as e:
            raise ValidationError('Invalid Ingredient: messing' + e.args[0])


    def __repr__(self):
        return '<Ingredient: {}>'.format(self.name)



class User(Model):
    id = Column(Integer, primary_key=True)
    username = Column(String(32), index=True)
    password_hash = Column(String(128))

    def hash_password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_pasword(self, password):
        return check_password_hash(self.password_hash, password)

