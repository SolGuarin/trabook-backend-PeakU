from sqlalchemy import Column, Integer, String, Float, Date, case
from sqlalchemy.ext.hybrid import hybrid_property
from trabook_backend.orm.database import Base, engine


class Trip(Base):
    __tablename__ = "trip"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String)
    country = Column(String)
    score = Column(Float)
    promo_price = Column(Float)
    price = Column(Float)
    days_trip = Column(Integer)
    image = Column(String)
    date = Column(Date)

    @hybrid_property
    def discount(self):
        return 100 * ((self.price - self.promo_price)/self.price) if self.promo_price is not None and self.price != 0 else 0

    @discount.expression
    def discount(self):
        return case((self.promo_price != None, 100 * (self.price / self.promo_price)), else_=0)


class Review(Base):
    __tablename__ = "review"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    score = Column(Float)
    reviewer = Column(String)
    city = Column(String)
    country = Column(String)
    image = Column(String)


class Blog(Base):
    __tablename__ = "blog"

    id = Column(Integer, primary_key=True, index=True)
    image = Column(String)
    date = Column(Date)
    title = Column(String)
    text = Column(String)


Base.metadata.create_all(bind=engine)
