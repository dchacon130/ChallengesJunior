import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import fizzbuzz

app = FastAPI()

# Configura las cabeceras CORS
origins = [
    "http://127.0.0.1:5173/",
    "localhost:5173",
    "0.0.0.0:0"  # Reemplaza con el dominio de tu aplicación React
    # Agrega otros dominios permitidos si es necesario
]

app.add_middleware(
    CORSMiddleware,
    allow_origins={"*"},
    allow_credentials=True,
    allow_methods=["*"],  # Puedes configurar los métodos permitidos según tus necesidades
    allow_headers=["*"],  # Puedes configurar las cabeceras permitidas según tus necesidades
)

app.include_router(fizzbuzz.router)

@app.get('/', tags=['root'])
async def root() -> dict:
    return {"item_id": "123" , "message": "Hola Multiplos de 3 y 5!!!"}

#Run uvicorn server: uvicorn main:app --reload
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)