# coding: utf8
db.define_table('recipe',
                Field('name', 'string'),
                Field('instructions', 'text'),
                format='%(name)s')

db.define_table('ingredient',
                Field('recipe_ref', 'reference recipe'),
                Field('name', 'string'),
                Field('quantity', 'float'),
                Field('unit', 'string'),
                format='%(quantity)s %(unit)s %(name)s')
