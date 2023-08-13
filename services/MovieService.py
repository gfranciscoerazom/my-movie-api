from models.Movie import BaseMovie, Movie


class MovieService():
    def __init__(self, db) -> None:
        self.db = db


    def get_all_movies(self):
        return self.db.query(BaseMovie).all()


    def get_movie_by_id(self, movie_id: int):
        return self.db.query(BaseMovie).filter(BaseMovie.id == movie_id).first()


    def create_movie(self, movie: Movie):
        base_movie = BaseMovie(**movie.model_dump())

        self.db.add(base_movie)
        self.db.commit()
        self.db.refresh(base_movie)

        return base_movie


    def update_movie(self, movie_id: int, movie: Movie):
        movie_to_update = self.db.query(BaseMovie).filter(BaseMovie.id == movie_id).first()

        if not movie_to_update:
            return None

        movie_to_update.title    = movie.title
        movie_to_update.overview = movie.overview
        movie_to_update.year     = movie.year
        movie_to_update.rating   = movie.rating
        movie_to_update.category = movie.category

        self.db.commit()
        self.db.refresh(movie_to_update)

        return movie_to_update


    def delete_movie(self, movie_id: int):
        movie_to_delete = self.db.query(BaseMovie).filter(BaseMovie.id == movie_id).first()

        if not movie_to_delete:
            return None

        self.db.delete(movie_to_delete)
        self.db.commit()

        return movie_to_delete
