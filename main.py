from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse

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
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    },
    {
        'id': 2,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    } 
]

@app.get("/", tags=["Home"])
def home():
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
    return movies

@app.get("/movies/{movie_id}", tags=["Movies"])
def get_movie(movie_id: int):
    # return list(filter(lambda movie: movie['id'] == movie_id, movies))
    for movie in movies:
        if movie['id'] == movie_id:
            return movie
        
    return None

@app.get("/movies/", tags=["Movies"])
def get_movies_by_category(category: str = "All", year: int = None):
    return_movies = movies

    if category != "All":
        return_movies = list(filter(lambda movie: movie['category'] == category, return_movies))

    if year != None:
        return_movies = list(filter(lambda movie: int(movie['year']) == year, return_movies))

    return return_movies

@app.post("/movies", tags=["Movies"])
def post_movie(
    id: int = Body(),
    title: str = Body(),
    overview: str = Body(),
    year: str = Body(),
    rating: float = Body(),
    category: str = Body()
):
    new_movie = {
        'id': id,
        'title': title,
        'overview': overview,
        'year': year,
        'rating': rating,
        'category': category
    }

    movies.append(new_movie)

    return new_movie

@app.put("/movies/{movie_id}", tags=["Movies"])
def put_movie(
    movie_id: int,
    title: str = Body(),
    overview: str = Body(),
    year: str = Body(),
    rating: float = Body(),
    category: str = Body()
):
    for movie in movies:
        if movie['id'] == movie_id:
            movie['title'] = title
            movie['overview'] = overview
            movie['year'] = year
            movie['rating'] = rating
            movie['category'] = category

            return movie
        
    return None

@app.delete("/movies/{movie_id}", tags=["Movies"])
def delete_movie(movie_id: int):
    for movie in movies:
        if movie['id'] == movie_id:
            movies.remove(movie)
            return movie
        
    return None