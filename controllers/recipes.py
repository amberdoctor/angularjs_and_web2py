# coding: utf8

import gluon.contrib.simplejson
def index():
    rows = db(db.recipe).select().as_list()
    return dict(recipe_list=gluon.contrib.simplejson.dumps(rows))

def get_ingredients():
    recipe_id = request.args[0]
    rows = db(db.ingredient.recipe_ref==recipe_id).select().as_list()
    return dict(ingredient_list=rows)

def get_recipe(recipe_id):
    recipe = db(db.recipe.id==recipe_id).select().first().as_dict()
    ingredients = db(db.ingredient.recipe_ref==recipe_id).select().as_list()
    recipe['ingredient_list'] = ingredients
    return recipe

def add_recipe():
    new_recipe = gluon.contrib.simplejson.loads(request.body.read())
    recipe_id = db.recipe.validate_and_insert(name=new_recipe['name'],
                                              instructions=new_recipe['instructions'])['id']
    for ingredient in new_recipe['ingredient_list']:
        db.ingredient.validate_and_insert(recipe_ref=recipe_id,
                                          name=ingredient['name'],
                                          quantity=ingredient['quantity'],
                                          unit=ingredient['unit'])
    new_recipe = get_recipe(recipe_id)
    return gluon.contrib.simplejson.dumps(dict(newRecipe=new_recipe))

def add_update_recipe():
    for item in converted_data:
        if item['user_inventory']['id']:
            db.user_inventory[item['user_inventory']['id']] = item['user_inventory']
        else:
            db.user_inventory.insert(item['user_inventory'])
    data = manage_inventory()
    return dict(data=data)
