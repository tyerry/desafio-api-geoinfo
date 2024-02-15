from app import app, SessionLocal
from util import generate_fake_country

if __name__ == "__main__":
    with SessionLocal() as db:
        generate_fake_country(db)

    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
