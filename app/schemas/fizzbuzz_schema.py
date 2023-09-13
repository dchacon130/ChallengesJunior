def fizz_buzz_schema(item_id: int):
    if item_id % 3 == 0 and item_id % 5 == 0:
        return {"item_id": item_id, "message": "Multipolo de 3 y 5"}
    elif item_id % 3 == 0:
        return {"item_id": item_id, "message": "Multipolo de 3"}
    elif item_id % 5 == 0:
        return {"item_id": item_id, "message": "Multipolo de 5"}
    else:
        return {"item_id": item_id, "message": "No es multiplo de 3 o 5"}

def fizz_buzz(item_a: int, item_b: int):
    for i in range(item_a, item_b):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)