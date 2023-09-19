import requests
import json

def clean_data_from_url():
    url = "https://coderbyte.com/api/challenges/json/json-cleaning"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()

        def clean_json(obj):
            if isinstance(obj, dict):
                obj = {k: v for k, v in obj.items() if v not in ("N/A", "-", "")}
                for key, value in obj.items():
                    obj[key] = clean_json(value)
            return obj

        cleaned_data = clean_json(data)
        cleaned_json_string = json.dumps(cleaned_data, indent=2)
        
        # Agregar mensajes de depuración
        #print("Cleaned JSON:")
        #print(cleaned_json_string)
        
        return cleaned_json_string
    else:
        return "Failed to fetch data from the URL"

# Llamar a la función y mostrar el resultado
result = clean_data_from_url()
print("Result:")
print(result)
