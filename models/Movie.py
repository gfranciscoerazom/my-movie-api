from pydantic import BaseModel
from typing import Optional


class Movie(BaseModel):
    __module__ = 'models.Movie'
    id: Optional[int] = None
    title: str
    overview: str
    year: int
    rating: float
    category: str