# Use the requests library to make a GET request to a public API.
import requests

def fetch_products():
  try:
    response = requests.get("https://pizzabackend-omega.vercel.app/api/products")
    response.raise_for_status()
    products = response.json()
    print(products)
  except:
    return "Does not found request"
  finally:
    return 
  

  

fetch_products()


  