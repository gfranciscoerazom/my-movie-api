from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from models.Movie import Movie

app = FastAPI()
app.title = "My First API with FastAPI"
app.version = "v0.0.1"
app.description = "This is my first API with FastAPI. This is a simple API to manage movies. It is for the Platzi FastAPI course."
app.contact = {
    'name': 'Gabriel Erazo',
    'url': "https://www.linkedin.com/in/gfranciscoerazom/",
    'email': 'gfranciscoerazom@protonmail.com',
}

movies = [
    Movie(
        id          = 1,
        title       = "Avatar",
        overview    = "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        year        = 2009,
        rating      = 7.8,
        category    = "Acción"
    ),
    Movie(
        id          = 2,
        title       = "Avatar",
        overview    = "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        year        = 2009,
        rating      = 7.8,
        category    = "Acción"
    ),

]

@app.get("/", tags=["Home"])
def home():
    """
    Returns the home page of the API.

    Returns:
        HTMLResponse: The home page of the API.
    """    
    return HTMLResponse("""
        <html>
            <head>
                <title>My First API with FastAPI</title>
            </head>
            <body>
                <h1>Welcome to my API</h1>
                <p>See the docs at <a href="/docs">/docs</a> and <a href="/redoc">/redoc</a></p>
            </body>
        </html>
    """)


@app.get("/movies", tags=["Movies"])
def get_movies():
    """
    Returns a list of all movies in the database.

    Returns:
        list: A list of all movies in the database.
    """    
    return movies


@app.get("/movies/{movie_id}", tags=["Movies"])
def get_movie(movie_id: int):
    """
    Returns the movie with the given ID from the list of movies.

    Args:
        movie_id (int): The ID of the movie to retrieve.

    Returns:
        dict: The movie with the given ID, or None if no movie was found.
    """
    for movie in movies:
        if movie.id == movie_id:
            return movie
        
    return None


@app.get("/movies/", tags=["Movies"])
def get_movies_by_category(category: str = "All", year: int = None):
    """
    Returns a list of movies filtered by category and/or year.

    Args:
        category (str, optional): The category to filter by. Defaults to "All".
        year (int, optional): The year to filter by. Defaults to None.

    Returns:
        list: A list of movies filtered by category and/or year.
    """
    return_movies = movies

    if category != "All":
        return_movies = list(filter(lambda movie: movie.category == category, return_movies))

    if year != None:
        return_movies = list(filter(lambda movie: movie.year == year, return_movies))

    return return_movies


@app.post("/movies", tags=["Movies"])
def post_movie(movie: Movie):
    """
    Creates a new movie with the given parameters and adds it to the list of movies.

    Args:
        id (int): The ID of the movie.
        title (str): The title of the movie.
        overview (str): A brief overview of the movie.
        year (str): The year the movie was released.
        rating (float): The rating of the movie.
        category (str): The category of the movie.

    Returns:
        dict: A dictionary containing the details of the newly created movie.
    """
    movies.append(movie)

    return movie


@app.put("/movies/{movie_id}", tags=["Movies"])
def put_movie(movie_id: int, movie: Movie):
    """
    Updates the movie with the given ID with the provided information.

    Args:
        movie_id (int): The ID of the movie to update.
        title (str, optional): The new title of the movie. Defaults to Body().
        overview (str, optional): The new overview of the movie. Defaults to Body().
        year (str, optional): The new year of the movie. Defaults to Body().
        rating (float, optional): The new rating of the movie. Defaults to Body().
        category (str, optional): The new category of the movie. Defaults to Body().

    Returns:
        dict: The updated movie information.
        None: If no movie with the given ID was found.
    """
    for m in movies:
        if m.id == movie_id:
            m.title = movie.title
            m.overview = movie.overview
            m.year = movie.year
            m.rating = movie.rating
            m.category = movie.category

            return movie


@app.delete("/movies/{movie_id}", tags=["Movies"])
def delete_movie(movie_id: int):
    """
    Deletes a movie from the list of movies by its ID.

    Args:
        movie_id (int): The ID of the movie to delete.

    Returns:
        dict or None: The deleted movie as a dictionary, or None if the movie was not found.
    """
    for movie in movies:
        if movie.id == movie_id:
            movies.remove(movie)
            return movie