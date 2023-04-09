from typing import Union
from pydantic import BaseModel
import datetime


class TripCreate(BaseModel):

    class Config:
        orm_mode = True

    city: str
    country: str
    score: float
    promo_price: float = None
    price: float
    days_trip: int
    image: str
    date: datetime.date


class ReviewCreate(BaseModel):

    class Config:
        orm_mode = True

    text: str
    score: Union[float, None]
    reviewer: str
    city: str
    country: str
    image: str


class BlogCreate(BaseModel):

    class Config:
        orm_mode = True

    image: str
    date: datetime.date
    title: str
    text: str


class Trip(BaseModel):

    class Config:
        orm_mode = True

    id: int
    city: Union[str, None]
    country: Union[str, None]
    score: Union[float, None]
    promo_price: Union[float, None]
    price: Union[float, None]
    days_trip: Union[int, None]
    image: Union[str, None]
    date: Union[datetime.date, None]
    discount: Union[float, None]


class Review(BaseModel):

    class Config:
        orm_mode = True

    id: int
    text: str
    score: Union[float, None]
    reviewer: str
    city: str
    country: str
    image: str


class Blog(BaseModel):

    class Config:
        orm_mode = True

    id: int
    image: str
    date: Union[datetime.date, None]
    title: Union[str, None]
    text: Union[str, None]
