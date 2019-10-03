# define a class to access our db
import pyodbc
class Recipe_db ():

    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.conn_recipedb = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+self.password)
        self.cursor = self.conn_recipedb.cursor()


    def execute_cursor(self, query):
        return self.cursor.execute(query)

    def create_recipes(self, table, recipename, ingredients, postcode):
        self.execute_cursor(f" INSERT INTO {table} (RecipeName, Ingredients, Postcode) VALUES ('{recipename}', '{ingredients}', '{postcode}')")
        self.conn_recipedb.commit()

    def retrieving_all_recipe(self, table):
        query = self.execute_cursor(f"SELECT * FROM {table}").fetchall()
        for data in query:
            print(f' {data[0]}) Recipe name: {data[1]} - Ingredients: {data[2]} - Postcode: {data[3]}')

    def retrieving_one_recipe(self,table, recipename):
        query = self.execute_cursor(f"SELECT * FROM {table} WHERE RecipeName like '%{recipename}%'").fetchall()
        print(query)

    def destroy_one_recipe(self,table, recipename):
        query = self.execute_cursor(f"DELETE FROM {}").fetchall()
        print(query)



#     # have a characteristics to access the db
#
#     # methods
#
#     # all() # should be a class method
#         # gets all the instances from DB
#         # get each records
#         # create individual instances of recipe
#         # store them in a list
#         # return_list