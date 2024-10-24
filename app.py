from flask import Flask, render_template, request, redirect, url_for, flash
import requests
import mysql.connector
import urllib.parse

app = Flask(__name__)
app.secret_key = 'secret_12345'  # Replace with your own secret key

# Database connection
db_config = {
    'user': 'explorer_user',
    'password': 'Siddarth@@1',
    'host': 'localhost',
    'database': 'cuisine_explorer'
}

# Fetch Featured Recipes function
def get_featured_recipes():
    api_key = '38eeff43161141f897cbbf600bce536f'
    url = f"https://api.spoonacular.com/recipes/random?number=5&apiKey={api_key}"  # Fetch 5 random recipes
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        featured_recipes = data.get('recipes', [])
    except requests.exceptions.RequestException as e:
        flash(f"Error fetching featured recipes: {e}", "danger")
        featured_recipes = []

    return featured_recipes

# Home route with featured recipes
@app.route('/', methods=['GET', 'POST'])
def index():
    featured_recipes = get_featured_recipes()  # Fetch featured recipes

    if request.method == 'POST':
        cuisine = request.form['cuisine']
        dietary = request.form['dietary']
        ingredients = request.form['ingredients']
        return redirect(url_for('results', cuisine=cuisine, dietary=dietary, ingredients=ingredients))

    return render_template('index.html', featured_recipes=featured_recipes)

# Results route
@app.route('/results', methods=['GET'])
def results():
    cuisine = request.args.get('cuisine')
    dietary = request.args.get('dietary')
    ingredients = request.args.get('ingredients')   

    # Build the query parameters safely
    query_params = {
        'cuisine': cuisine,
        'diet': dietary,
        'includeIngredients': ingredients,
        'apiKey': '38eeff43161141f897cbbf600bce536f'
    }
    encoded_params = urllib.parse.urlencode(query_params)

    # Fetch recipes from the API
    url = f"https://api.spoonacular.com/recipes/complexSearch?{encoded_params}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # This will raise an HTTPError if the status is not 200
        data = response.json()
        recipes = data.get('results', [])
    except requests.exceptions.RequestException as e:
        flash(f"Error fetching recipes: {e}", "danger")
        recipes = []

    return render_template('results.html', recipes=recipes)

# View Recipe route
@app.route('/view_recipe/<int:recipe_id>', methods=['GET'])
def view_recipe(recipe_id):
    try:
        # Fetch the detailed recipe information
        api_url = f"https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey=38eeff43161141f897cbbf600bce536f"
        recipe_response = requests.get(api_url)
        recipe_response.raise_for_status()
        recipe = recipe_response.json()

        # Fetch nutrition information
        nutrition_api_url = f"https://api.spoonacular.com/recipes/{recipe_id}/nutritionWidget.json?apiKey=38eeff43161141f897cbbf600bce536f"
        nutrition_response = requests.get(nutrition_api_url)
        nutrition_response.raise_for_status()
        nutrition = nutrition_response.json()

    except requests.exceptions.RequestException as e:
        flash(f"Error fetching recipe details: {e}", "danger")
        return redirect(url_for('index'))

    return render_template('recipe.html', recipe=recipe, nutrition=nutrition)

# Add to favorites route
@app.route('/add_favorite', methods=['POST'])
def add_favorite():
    recipe_name = request.form['recipe_name']
    recipe_image = request.form['recipe_image']
    recipe_url = request.form['recipe_url']
    dietary_restrictions = request.form.get('dietary_restrictions')  # Optional field
    ingredients = request.form.get('ingredients')  # Optional field

    # Connect to the database and insert the new favorite
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    query = """
        INSERT INTO favorites (recipe_name, recipe_image, recipe_url, dietary_restrictions, ingredients) 
        VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, (recipe_name, recipe_image, recipe_url, dietary_restrictions, ingredients))
    conn.commit()
    cursor.close()
    conn.close()
    
    flash("Recipe added to favorites!", "success")
    return redirect(url_for('favorites'))

# Favorites route
@app.route('/favorites', methods=['GET'])
def favorites():
    # Fetch all favorite recipes from the database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM favorites")
    favorites = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return render_template('favorites.html', favorites=favorites)

# Delete favorite route
@app.route('/delete_favorite/<int:favorite_id>', methods=['POST'])
def delete_favorite(favorite_id):
    # Remove a favorite from the database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM favorites WHERE id = %s", (favorite_id,))
    conn.commit()
    cursor.close()
    conn.close()
    
    flash("Recipe removed from favorites!", "danger")
    return redirect(url_for('favorites'))

if __name__ == '__main__':
    app.run(debug=True)

