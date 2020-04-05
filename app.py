from flask import Flask, render_template, redirect, request, url_for
import os
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import math
import re

app=Flask(__name__)

app.config["MONGO_DBNAME"] = 'recipes_manager'
app.config["MONGO_URI"] = 'mongodb+srv://vic_user_26:v!cky!99!&!989@myfirstcluster-ziitx.mongodb.net/recipes_manager?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/index')
def index():
    home_page_recipes = mongo.db.recipes.find().limit(4)
    return render_template("index.html", recipes=home_page_recipes)

# Get/Look at all recipes
@app.route('/get_all_recipes')
def get_all_recipes():
    recipes_per_page = 6
    page = int(request.args.get('page', 1))
    count_total = mongo.db.recipes.count_documents({})
    all_recipes = mongo.db.recipes.find().skip((page - 1)*recipes_per_page).limit(recipes_per_page)
    pages = range(1, int(math.ceil(count_total / recipes_per_page)) + 1)
    return render_template('get_all_recipes.html', recipes=all_recipes, page=page, pages=pages, count_total=count_total)

#Look at one recipe page  
@app.route('/one_recipe/<recipe_id>')
def one_recipe(recipe_id):
    #looks at the full individual recipe, including all details on the indivdiual recipe
    recipe_db = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    return render_template('one_recipe.html', recipe=recipe_db)
   





if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True)
    