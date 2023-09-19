
def fizz_buzz_by_id(item_id: int):
    if item_id % 3 == 0 and item_id % 5 == 0:
        return [{"item_id": item_id, "message": "fizzbuzz"}]
    elif item_id % 3 == 0:
        return [{"item_id": item_id, "message": "fizz"}]
    elif item_id % 5 == 0:
        return [{"item_id": item_id, "message": "buzz"}]
    else:
        return [{"item_id": item_id, "message": "No es Primo de 3 o 5"}]

def fizz_buzz(item_a: int = 1, item_b: int = 101):
    results = []
    for i in range(item_a, item_b):
        if i % 3 == 0 and i % 5 == 0:
            results.append({"item_id": i, "message": "fizzbuzz"})
        elif i % 3 == 0:
            results.append({"item_id": i, "message": "fizz"})
        elif i % 5 == 0:
            results.append({"item_id": i, "message": "buzz"})
        else:
            results.append({"item_id": i, "message": str(i)})
    return results