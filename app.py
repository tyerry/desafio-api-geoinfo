import math
from typing import Optional
from fastapi import FastAPI, Depends, Query
from sqlalchemy import func
from sqlalchemy.orm import Session
from database import SessionLocal
from model import Country

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/countries-all")
def get_countries(db: Session = Depends(get_db)):
    countries = db.query(Country).all()
    return countries

@app.get("/countries")
def get_countries(db: Session = Depends(get_db), region: Optional[int] = None, keyword: Optional[str] = None, page: Optional[int] = 1, perPage: int = Query(3, alias="per_page") ):
    query = db.query(Country)
    if region is not None:
        query = query.filter(Country.region == region)
    if keyword is not None:
        query = query.filter(Country.keyword == keyword)
    total = query.count()    
    skip = (page - 1) * perPage
    countries = query.offset(skip).limit(perPage).all()
    result = {
        "page":page,
        "perPage":perPage,
        "total":total,
        "totalPages":(math.ceil(total / perPage)),
        "data":[{"name":country.name, "region":country.region, "population":country.population} for country in countries]
    }
    return result
