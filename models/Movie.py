from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from config.database import Base
from sqlalchemy import Column, Float, Integer, String


class Movie(BaseModel):
    id: Optional[int] = None

    title: str = Field(
        min_length=1,
        max_length=50,
        default="Unknown Title"
    )

    overview: str = Field(
        min_length=1,
        max_length=350,
        default="No overview available."
    )

    year: int = Field(
        ge=1900,
        le=2100,
    )

    rating: float = Field(
        ge=0.0,
        le=10.0,
        default=0.0,
    )

    category: str = Field(
        min_length=1,
        max_length=20,
        default="Unknown Category"
    )

    model_config = ConfigDict(
        json_schema_extra = {
            "example": {
                "title": "Star Wars: Episode IV - A New Hope",
                "overview": "Luke Skywalker joins forces with a Jedi Knight, a cocky pilot, a Wookiee and two droids to save the galaxy from the Empire's world-destroying battle station, while also attempting to rescue Princess Leia from the mysterious Darth Vader.",
                "year": 1977,
                "rating": 8.6,
                "category": "Science Fiction"
            }
        }
    )


class BaseMovie(Base):
    __tablename__ = "movie"

    id          = Column(Integer, primary_key=True)
    title       = Column(String(50), nullable=False)
    overview    = Column(String(350), nullable=False)
    year        = Column(Integer, nullable=False)
    rating      = Column(Float, nullable=False)
    category    = Column(String(20), nullable=False)
