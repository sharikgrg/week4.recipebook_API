from db_class import *

server = 'localhost,1433'
database = 'Chefsparta'
username = 'SA'
password = 'Passw0rd2018'

recipe = Recipe_db(server, database, username, password)


                # as a user i can create one recipe #
# recipe.create_recipes("recipe", "Sandwich", "Bread, cheese, butter", "E162RJ")
# recipe.create_recipes("recipe", "Bagel", "Flour, water, oil", "E162RD")
# recipe.create_recipes("recipe", "MOMO", "dough, oil, mince meat, onion", "TN231JZ")
# recipe.create_recipes("recipe", "Rice", "Rice, water", "TN231JX")

                # as a user i can get all recipes #
# print(recipe.retrieving_all_recipe("recipe"))

                # as a user i can read one recipe #
# print(recipe = recipe.retrieving_one_recipe("recipe", "andwich"))

                # as a user i can destroy one recipe #
# recipe.destroy_one_recipe("recipe", "RecipeName", "Rice")

                # as a user i should be able to export one recipe to database #
# recipe.reading_one_recipe('sandwich', 'recipe.txt')

                # as a user i should be able to get more info on the location where the websites are created#
# print(recipe.location_finder('sandwich'))