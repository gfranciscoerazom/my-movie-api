from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


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
                "id": 1,
                "title": "The Matrix",
                "overview": "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
                "year": 1999,
                "rating": 8.7,
                "category": "Science Fiction",
            }
        }
    )