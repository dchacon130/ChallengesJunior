from fastapi import FastAPI
from app.routers import fizzbuzz

app = FastAPI()

app.include_router(fizzbuzz.router)

@app.get('/')
async def root():
    return {"message": "Hola Multiplos de 3 y 5!!!"}

#Run uvicorn server: uvicorn main:app --reload