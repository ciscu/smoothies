from app import app
from app import db
from app.models import Smoothie
from app.models import Ingredient
from app.models import Recipe

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Smoothie': Smoothie, 'Ingredient': Ingredient, 'Recipe':Recipe}