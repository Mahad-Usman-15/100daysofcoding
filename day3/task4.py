# Use the requests library to make a POST request to a public API.

import requests
mockuser={
"username":"rashid",
"email":"mahad@gmail.com",
"password":"impo$$ible1",
"isAdmin":True
}
def post_user():
    try:
        response = requests.post("https://pizzabackend-omega.vercel.app/api/create-admin", json=mockuser)
        response.raise_for_status()
        if response.ok:
            print("user created")
        else:
            print("failed to create a user")
    except:
         print("failed to create") 

post_user()                    
