from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app=FastAPI(title='Users',description="Api for users")

# Pydantic Model used for data validation
class User(BaseModel):
    id: int
    username: str
    email: str

# users inmemory db
users: list[User] = [
    User(id=1, username="alice", email="alice@example.com"),
    User(id=2, username="bob", email="bob@example.com"),
    User(id=3, username="charlie", email="charlie@example.com"),
    User(id=4, username="diana", email="diana@example.com"),
    User(id=5, username="ethan", email="ethan@example.com"),
    User(id=6, username="fiona", email="fiona@example.com"),
    User(id=7, username="george", email="george@example.com"),
    User(id=8, username="hannah", email="hannah@example.com"),
    User(id=9, username="ian", email="ian@example.com"),
    User(id=10, username="julia", email="julia@example.com"),
]

@app.get("/")
def get_users(user_id:int | None = None):
    if len(users)==0:
        if user_id is None:
            return users
    for user in users:
        if user.id==user_id:
            return user

    raise HTTPException(status_code=404, detail="Users not found")


# Here userid is a pathparameter
# HTTP Method:      GET
# Route:            /{userid}
# Endpoint function: get_users_by_id
@app.get("/{userid}",description="endpoint to get a user by id")
def get_users_by_id(userid:int):
    for user in users:
        if user.id==userid:
            return user
    
    raise HTTPException(status_code=404, detail="User not found")

# Here we use Query parameter to filter user with id.
# HTTP Method:      GET
# Route:            /           (with query param ?id=...)
# Endpoint function: get_users

# HTTP Method:      POST
# Route:            /createuser
# Endpoint function: create_user
@app.post("/createuser",description="endpoint to create a user")
def create_user(username:str,email: str):
    user=User(
        id=max((u.id for u in users), default=0) + 1,
        username=username,
        email=email
    )
    users.append(user)
    return f"{user.username} added successfully"



# HTTP Method:      DELETE
# Route:            /deleteuser/{username}
# Endpoint function: delete_user
@app.delete("/deleteuser/{username}",description="endpoint to delete a user")
def delete_user(username:str):
    for user in users:
        if user.username==username:
            users.remove(user)
            return "User removed successfully"
    
    raise HTTPException(status_code=404, detail="User not found")       
    

# HTTP Method:      PATCH
# Route:            /updateuser/{username}
# Endpoint function: update_user
@app.patch("/updateuser/{username}",description="endpoint to update a user")
def update_user(username:str,name:str,email: str):
    for i, user in enumerate(users):
      if user.username == username:
          users[i] = User(id=user.id, username=name, email=email)
          return "User updated successfully"
           
        
    raise HTTPException(status_code=404, detail="User not found")    