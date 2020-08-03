from app.models import Smoothie
from app.models import Ingredient
from app import db

smoothies = ["Exotic", "Banana", "Strawberry"]
ingredients = ["Banana", "Orange Juice", "Strawberry", "Pineapple", "Passion Fruit"]


# Create Smoothies
print("Creating Smoothies")
for smoothie in smoothies:
    print("Checking if {} smoothie is already in database".format(smoothie))
    if Smoothie.query.filter_by(name=smoothie).first() is None:
        print("Adding {} smoothie to database".format(smoothie))
        new_smoothie = Smoothie(name=smoothie)
        db.session.add(new_smoothie)
        db.session.commit()
    else:
        print("{} already in database".format(smoothie))

# Create Ingredients
print("")
print("Creating Ingredients")
print("====================")
for ingredient in ingredients:
    print("Checking if {} ingredient is already in database".format(smoothie))
    if Ingredient.query.filter_by(name=ingredient).first() is None:
        print("Adding {} ingredient to database".format(smoothie))
        new_ingredient = Ingredient(name=ingredient)
        db.session.add(new_ingredient)
        db.session.commit()
    else:
        print("{} already in database".format(smoothie))


# Add ingredients to Smoothie recipe

## Get Banana Smoothie
banana_smoothie = Smoothie.query.filter_by(name="Banana").first()
print("Getting the Banana Smoothie")
if banana_smoothie is not None:
    print("Succesfully retrieved the banana smoothie")
## Create list of ingredients
print("Collecting ingredients from database")
banana_smoothie_ingredients = []
banana_smoothie_ingredients.append(Ingredient.query.filter_by(name="Banana").first())
banana_smoothie_ingredients.append(Ingredient.query.filter_by(name="Orange Juice").first())

print("Adding ingredients to smoothie recipe")
banana_smoothie.recipe.extend(banana_smoothie_ingredients)

print('Adding smoothie to database for update')
db.session.add(banana_smoothie)
db.session.commit()

## Strawberry Smoothie
strawberry_smoothie = Smoothie.query.filter_by(name="Strawberry").first()

strawberry_smoothie_ingredients = []
strawberry_smoothie_ingredients.append(Ingredient.query.filter_by(name="Banana").first())
strawberry_smoothie_ingredients.append(Ingredient.query.filter_by(name="Orange Juice").first())
strawberry_smoothie_ingredients.append(Ingredient.query.filter_by(name="Strawberry").first())

strawberry_smoothie.recipe.extend(strawberry_smoothie_ingredients)
db.session.add(strawberry_smoothie)
db.session.commit()



