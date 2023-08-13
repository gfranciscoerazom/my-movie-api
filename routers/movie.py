from fastapi import APIRouter, Depends, Path, Query
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from config.database import Session
from key.JWTBearer import JWTBearer

from models.Movie import BaseMovie, Movie

movie_router = APIRouter()

@movie_router.get(
    path            = "/movies",
    tags            = ["Movies"],
    response_model  = list[Movie],
    status_code     = 200,
    dependencies    = [Depends(JWTBearer())]
)
def get_movies() -> list[Movie]:
    """
    Returns a list of all movies in the database.

    Returns:
        list: A list of all movies in the database.
    """
    db = Session()
    movies = db.query(BaseMovie).all()
    return JSONResponse(
        content = jsonable_encoder(movies)
    )


@movie_router.get(
    "/movies/{movie_id}",
    tags=["Movies"],
    response_model=Movie,
    status_code=200,
)
def get_movie(
    movie_id: int = Path(ge=1)
) -> Movie:
    """
    Returns the movie with the given ID from the list of movies.

    Args:
        movie_id (int): The ID of the movie to retrieve.

    Returns:
        dict: The movie with the given ID, or None if no movie was found.
    """
    db = Session()
    movies = db.query(BaseMovie).filter(BaseMovie.id == movie_id).first()

    if not movies:
        return JSONResponse(
            content = {
                "error": "Movie not found."
            },
            status_code = 404
        )

    return JSONResponse(
        content = jsonable_encoder(movies),
        status_code=200,
    )


@movie_router.get(
    "/movies/",
    tags=["Movies"],
    response_model=list[Movie],
    status_code=200,
)
def get_movies_by_category(
    category: str = Query(
        default="All",
        min_length=1,
        max_length=20,
    ),
    year: int = Query(
        default=None,
        ge=1900,
        le=2100,
    ),
) -> list[Movie]:
    """
    Returns a list of movies filtered by category and/or year.

    Args:
        category (str, optional): The category to filter by. Defaults to "All".
        year (int, optional): The year to filter by. Defaults to None.

    Returns:
        list: A list of movies filtered by category and/or year.
    """
    db = Session()

    return_movies = db.query(BaseMovie).all()

    if category != "All":
        return_movies = list(filter(lambda movie: movie.category == category, return_movies))

    if year != None:
        return_movies = list(filter(lambda movie: movie.year == year, return_movies))

    return JSONResponse(
        content = jsonable_encoder(return_movies),
    )


@movie_router.post(
    "/movies",
    tags=["Movies"],
    response_model=dict,
    status_code=201,
)
def post_movie(movie: Movie) -> dict:
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
    db = Session()
    new_movie = BaseMovie(**movie.model_dump())
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)

    return JSONResponse(
        content = {
            "message": "Movie created successfully.",
            "movie": jsonable_encoder(new_movie),
        }
    )


@movie_router.put(
    "/movies/{movie_id}",
    tags=["Movies"],
    response_model=dict,
    status_code=200,
)
def put_movie(movie_id: int, movie: Movie) -> dict:
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
    db = Session()
    movies = db.query(BaseMovie).filter(BaseMovie.id == movie_id).first()

    if not movies:
        return JSONResponse(
            content = {
                "error": "Movie not found."
            },
            status_code = 404
        )

    movies.title    = movie.title
    movies.overview = movie.overview
    movies.year     = movie.year
    movies.rating   = movie.rating
    movies.category = movie.category
    db.commit()
    db.refresh(movies)

    return JSONResponse(
        content = {
            "message": "Movie updated successfully.",
            "movie": jsonable_encoder(movies),
        }
    )


@movie_router.delete(
    "/movies/{movie_id}",
    tags=["Movies"],
    response_model=dict,
    status_code=200,
)
def delete_movie(movie_id: int) -> dict:
    """
    Deletes a movie from the list of movies by its ID.

    Args:
        movie_id (int): The ID of the movie to delete.

    Returns:
        dict or None: The deleted movie as a dictionary, or None if the movie was not found.
    """
    db = Session()
    movies = db.query(BaseMovie).filter(BaseMovie.id == movie_id).first()

    if not movies:
        return JSONResponse(
            content = {
                "error": "Movie not found."
            },
            status_code = 404
        )

    db.delete(movies)
    db.commit()

    return JSONResponse(
        content = {
            "message": "Movie deleted successfully.",
            "movie": jsonable_encoder(movies),
        }
    )

