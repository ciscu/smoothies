from flask import request, abort, url_for, g
from app import app, db
from app.models import Smoothie
from app.models import User
from app.models import Ingredient
from flask_httpauth import HTTPBasicAuth


auth = HTTPBasicAuth()
@auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    user = User.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = User.query.filter_by(username=username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True




@app.route('/api/v1/smoothies/', methods=['GET'])
def smoothies():
    return {'smoothies': [{"name": smoothie.name, "id": smoothie.id} for smoothie in Smoothie.query.all()]}


@app.route('/api/v1/smoothies/<name>')
def get_smoothie(name):
    return Smoothie.query.filter_by(name=name).first_or_404().export_data()


@app.route('/api/v1/smoothies/new', methods=["POST"])
def new_smoothie():
    if not request.json or not 'name' in request.json:
        abort(400)

    if Smoothie.query.filter_by(name=request.json["name"]).first() is not None:
        return {"error": "Smoothie {} already present in application".format(request.json["name"])}, 400

    smoothie = Smoothie()
    smoothie.import_data(request.json)

    for new_ingredient in request.json["ingredients"]:
        ingredient = Ingredient()
        # Check if ingredient is already in the database
        if Ingredient.query.filter_by(name=new_ingredient).first() is None:
            ingredient.import_data(new_ingredient)
            db.session.add(ingredient)
        else:
            ingredient = Ingredient.query.filter_by(name=new_ingredient).first()
        smoothie.recipe.append(ingredient)


    db.session.add(smoothie)
    db.session.commit()

    return {}, 201

@app.route('/api/v1/smoothies/delete/<smoothie_id>', methods=["DELETE"])
def delete_smoothie(smoothie_id):
    smoothie = Smoothie.query.get_or_404(smoothie_id)
    db.session.delete(smoothie)
    db.session.commit()
    return {'result': True}, 200


@app.route('/api/v1/smoothies/edit/<id>', methods=["PUT"])
def edit_smoothie(id):
    smoothie = Smoothie.query.get_or_404(id)
    if not smoothie:
        return {"error": "no resource found"}, 404

    smoothie.import_data(request.json)
    smoothie.recipe = []
    for ingredient in request.json["ingredients"]:
        new_ingredient = Ingredient.query.filter_by(name=ingredient).first()
        if new_ingredient is None:
            new_ingredient = Ingredient()
            new_ingredient.import_data(ingredient)
            db.session.add(new_ingredient)
        else:
            new_ingredient = Ingredient.query.filter_by(name=ingredient).first()
        smoothie.recipe.append(new_ingredient)


    db.session.add(smoothie)
    db.session.commit()


    db.session.add(smoothie)
    db.session.commit()
    return {"message": "Resource succesfully updated"}


@app.route('/api/v1/users', methods=["POST"])
def new_user():
    username = request.json["username"]
    password = request.json["password"]

    # Username and password validation
    if username is None or password is None:
        abort(400)
    if User.query.filter_by(username=username).first() is not None:
        abort(400)
    user = User(username=username)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return {'username': user.username,
            'location': url_for('get_user', id=user.id, _external=True)}, 201

@app.route('/api/v1/user/<id>')
def get_user(id):
    user = User.query.get_or_404(id)
    if not user:
        abort(400)

    return {'username': user.username}
