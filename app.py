from flask import Flask, render_template, redirect, request, url_for
import os
from flask_pymongo import PyMongo
from forms import CreateRecipeForm, EditRecipeForm, ConfirmDelete
from config import Config
from bson.objectid import ObjectId
import math
import re

app=Flask(__name__)

app.config["MONGO_DBNAME"] = 'recipes_manager'
app.config["MONGO_URI"] = 'mongodb+srv://vic_user_26:v!cky!99!&!989@myfirstcluster-ziitx.mongodb.net/recipes_manager?retryWrites=true&w=majority'
app.config.from_object(Config)

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
   
# Search Recipes
@app.route('/search')
def search():
    user_query = request.args['query']
    query = {'$regex': re.compile('.*{}.*'.format(user_query))}
    results = mongo.db.recipes.find({
        '$or': [
            {'title': query},
            {'tags': query},
            {'ingredients': query}
        ]
    })
    return render_template('search.html', query=user_query, results=results)

# Create, add and insert the information for the new recipe
@app.route('/create_recipe', methods=['POST', 'GET'])
def create_recipe():
    #connects the correct form from forms.py
    form = CreateRecipeForm(request.form)
    if form.validate_on_submit():
        #sets the collection that its being added to
        recipes_db = mongo.db.recipes
        #adds the new recipe
        recipes_db.insert_one({
            'title': request.form['title'],
            'description': request.form['description'],
            'ingredients': request.form['ingredients'],
            'method': request.form['method'],
            'tags': request.form['tags'],
            'image': request.form['image'],
            'views': 0
        })
        return redirect(url_for('index', title='New Recipe Added'))
    return render_template('create_recipe.html', title='create a recipe', form=form)
 

# Edit a previously uploaded recipe 
@app.route('/edit_recipe/<recipe_id>', methods=['POST', 'GET'])
def edit_recipe(recipe_id):
    recipe_db = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    if request.method == 'GET':
        form = EditRecipeForm(data=recipe_db)
        return render_template('edit_recipe.html', recipe=recipe_db, form=form)
    form = EditRecipeForm(request.form)
    if form.validate_on_submit():
        recipes_db = mongo.db.recipes
        recipes_db.update_one({
            '_id': ObjectId(recipe_id),
        }, {
            '$set': {
                'title': request.form['title'],
                'description': request.form['description'],
                'ingredients': request.form['ingredients'],
                'method': request.form['method'],
                'tags': request.form['tags'],
                'image': request.form['image'],
            }
        })
        return redirect(url_for('index', title='New Recipe Added'))
    return render_template('edit_recipe.html', recipe=recipe_db, form=form)

# Delete Recipe
@app.route('/delete_recipe/<recipe_id>', methods=['POST'])
def delete_recipe(recipe_id):
    recipe_db = mongo.db.recipes.find_one_and_delete({'_id': ObjectId(recipe_id)})
    form = ConfirmDelete(data=recipe_db)
    if form.validate_on_submit():
        recipes_db = mongo.db.recipes_db
        recipes_db.delete_one({
            '_id': ObjectId(recipe_id)
        })
        return redirect(url_for('index', title='Updated List of Recipes'))
    return render_template('delete_recipe.html', title="delete recipe", recipe=recipe_db, form=form)



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True)
    