
---

# Cuisine Explorer 🍽️

Cuisine Explorer is a web application built using Flask that helps users discover delicious recipes from around the world. Users can search for recipes based on cuisine type, dietary restrictions, and ingredients. The application also allows users to save their favorite recipes to a MySQL database for easy access later.

## Features ✨

- **Search Recipes**: Users can search for recipes by entering cuisine types, dietary preferences, and specific ingredients.
- **Featured Recipes**: A section on the homepage displays a set of featured recipes to explore.
- **View Detailed Recipes**: Each recipe provides detailed instructions, ingredients, and nutritional information.
- **Add to Favorites**: Users can save their favorite recipes for quick access.
- **Manage Favorites**: Users can view and delete their saved recipes from the favorites page.

## Screenshots 📸

<img src="screenshots/Screenshot from 2024-10-24 23-02-13.png" alt="Cuisine Explorer Homepage" width="400">
<img src="path_to_screenshot2" alt="Recipe Results" width="400">

## Technologies Used 💻

- **Flask**: Web framework for building the application.
- **MySQL**: Database for storing favorite recipes.
- **Spoonacular API**: External API for fetching recipes and detailed information.
- **HTML/CSS**: Frontend UI design.
- **JavaScript**: For interactivity (if needed).
  
## Setup Instructions 🛠️

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- Flask
- MySQL Server
- Spoonacular API Key

### Installation Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/cuisine-explorer.git
    cd cuisine-explorer
    ```

2. **Install the required Python packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up the database**:
    - Create a MySQL database named `cuisine_explorer`.
    - Execute the following SQL query to create the `favorites` table:
      ```sql
      CREATE TABLE favorites (
          id INT AUTO_INCREMENT PRIMARY KEY,
          recipe_name VARCHAR(255),
          recipe_image VARCHAR(255),
          recipe_url VARCHAR(255),
          dietary_restrictions VARCHAR(255),
          ingredients TEXT
      );
      ```

4. **Add your API key**:
    - Open `app.py` and replace the existing Spoonacular API key with your own.
    ```python
    apiKey= "your_spoonacular_api_key"
    ```

5. **Run the Flask Application**:
    ```bash
    python app.py
    ```

6. **Open the Application**:
    Visit `http://127.0.0.1:5000/` in your browser to view the application.

## Usage 📖

- Navigate to the homepage and search for recipes by entering a cuisine, dietary preference, or specific ingredients.
- Explore the featured recipes displayed on the homepage.
- Click on any recipe to view detailed information and nutritional content.
- Save your favorite recipes to the favorites section for quick access later.
- Manage your saved recipes (view, delete) from the favorites page.


## Acknowledgments 🙏

- [Spoonacular API](https://spoonacular.com/food-api) for providing recipe data.
- Flask community for awesome web framework support.
  
---
