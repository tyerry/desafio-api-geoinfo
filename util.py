import random
from faker import Faker
from requests import Session
from database import SessionLocal
from model import Country

fake = Faker()

def generate_fake_country(db: Session):
    if db.query(Country).count() == 0:
        for _ in range(50):
            country_data = {
                'name': fake.country(),
                'region': random.randint(1, 7),
                'population': random.randint(1000000, 200000000),
                'keyword': fake.country_code(representation="alpha-3"),
            }
            db_country = Country(**country_data)
            db.add(db_country)

        db.commit()

generate_fake_country(SessionLocal())