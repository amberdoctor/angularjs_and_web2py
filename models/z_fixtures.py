# coding: utf8
RESET = False

if RESET:
    for table in db.tables:
        # Make sure to cascade, or this will fail
        # for tables that have FK references.
        db[table].truncate("CASCADE")
    db.commit()

def add_recipe(new_recipe):
    recipe_id = db.recipe.validate_and_insert(name=new_recipe['name'], instructions=new_recipe['instructions'])['id']
    for ingredient in new_recipe['ingredient_list']:
        db.ingredient.insert(recipe_ref=recipe_id, name=ingredient['name'], quantity=ingredient['quantity'], unit=ingredient['unit'])

def add_recipe_list(recipe_list):
    for recipe in recipe_list:
        add_recipe(recipe)

recipe_list = [{"ingredient_list":[{"name":"chocolate",
                                    "quantity":1,
                                    "unit":"bar"},
                                   {"name":"graham crackers",
                                    "quantity":1,
                                    "unit":"box"},
                                   {"name":"marshmallows",
                                    "quantity":1,
                                    "unit":"bag"}],
                "name":"Smores",
                "instructions":"Toast Marshmallow over fire.  Sandwich the toasted marshmallow and chocolate between two graham crackers."},
               {"ingredient_list":[{"name":"peanunt butter",
                                    "quantity":2,
                                    "unit":"tablespoon"},
                                   {"name":"celery",
                                    "quantity":1,
                                    "unit":"stalk"}],
                "name":"Peanut Butter & Celery",
                "instructions":"Spread Peanut Butter on Celery."},
               {"ingredient_list":[{"name":"Cheese",
                                    "quantity":.5,
                                    "unit":"cup"},
                                   {"name":"Corn Chips",
                                    "quantity":20,
                                    "unit":""}],
                "name":"Nachos",
                "instructions":"Melt Cheese over corn chips for 45 seconds in the microwave."},
               ]
if RESET:
    add_recipe_list(recipe_list)
