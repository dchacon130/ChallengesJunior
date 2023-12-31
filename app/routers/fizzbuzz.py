"""
EL FAMOSO "FIZZ BUZZ”:
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""
from fastapi import APIRouter
from app.schemas.fizzbuzz_schema import fizz_buzz_by_id, fizz_buzz

router = APIRouter(prefix="/fizzbuzz",
                   tags=["Fizz Buzz"],
                   responses={404: {"message": "No encontrado"}})


@router.get('/')
async def fizz_buzzs():
    return fizz_buzz()

@router.get("/{item_a}/{item_b}")
def get_fizz_buzz(item_a: int, item_b: int):
    return fizz_buzz(item_a, item_b)

@router.get("/{item_id}")
async def fizz_buzz_by_number(item_id: int):
    return fizz_buzz_by_id(item_id)