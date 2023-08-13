from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from models.Movie import Movie
from config.database import engine, Base
from middlewares.ErrorHandler import ErrorHandler
from routers.movie import movie_router
from routers.auth import auth_router

app = FastAPI()
app.title = "My First API with FastAPI"
app.version = "v0.0.1"
app.description = "This is my first API with FastAPI. This is a simple API to manage movies. It is for the Platzi FastAPI course."
app.contact = {
    'name': 'Gabriel Erazo',
    'url': "https://www.linkedin.com/in/gfranciscoerazom/",
    'email': 'gfranciscoerazom@protonmail.com',
}
app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(auth_router)

Base.metadata.create_all(bind=engine)

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
        title       = "Matrix",
        overview    = "Un pirata informático recibe una misteriosa visita: alguien ha ...",
        year        = 1999,
        rating      = 8.7,
        category    = "Ciencia Ficción"
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
