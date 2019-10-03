from db_class import *

server = 'localhost,1433'
database = 'Chefsparta'
username = 'SA'
password = 'Passw0rd2018'

recipe = Recipe_db(server, database, username, password)

# recipe.create_recipes("recipe", "Sandwich", "Bread, cheese, butter", "E162RJ")

# recipe.retrieving_all_recipe("recipe")

recipe.retrieving_one_recipe("recipe", "andwich")