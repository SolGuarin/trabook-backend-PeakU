from typing import List

from fastapi import FastAPI, Depends
from sqlalchemy import select, desc
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import coalesce

from trabook_backend.orm.database import SessionLocal
from trabook_backend.orm import schemas
from trabook_backend.orm import models

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/trip/", response_model=schemas.Trip)
async def create_trip(trip: schemas.TripCreate, db: Session = Depends(get_db)):
    trip_db = models.Trip(**trip.dict())
    db.add(trip_db)
    db.commit()
    db.refresh(trip_db)
    return trip_db


@app.get("/trip/", response_model=List[schemas.Trip])
async def get_trips(db: Session = Depends(get_db), sort_by: str = None):
    query = db.query(models.Trip)
    if sort_by:
        query = query.order_by(desc(getattr(models.Trip, sort_by)))

    return query.all()


@app.post("/review/", response_model=schemas.Review)
async def create_review(review: schemas.ReviewCreate, db: Session = Depends(get_db)):
    review_db = models.Review(**review.dict())
    db.add(review_db)
    db.commit()
    db.refresh(review_db)
    return review_db


@app.get("/review/", response_model=List[schemas.Review])
async def get_reviews(db: Session = Depends(get_db)):
    return db.query(models.Review).all()


@app.post("/blog/", response_model=schemas.Blog)
async def create_blog(blog: schemas.BlogCreate, db: Session = Depends(get_db)):
    blog_db = models.Blog(**blog.dict())
    db.add(blog_db)
    db.commit()
    db.refresh(blog_db)
    return blog_db


@app.get("/blog/", response_model=List[schemas.Blog])
async def get_blogs(db: Session = Depends(get_db)):
    return db.query(models.Blog).all()
