from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = "My First API with FastAPI"
app.version = "v0.0.1"

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
                <p>Try to go to <a href="/docs">/docs</a></p>
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