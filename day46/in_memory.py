from fastapi import FastAPI,Request,HTTPException,Depends
import time
app = FastAPI()
store = {}

def get_client_ip(req:Request)->str:
    return req.client.host
MAX_REQUESTS = 5
WINDOW = 60
CURRENT_TIME = time.time()

def rate_limit(req:Request):
    client_ip = get_client_ip(req)
    window_start = CURRENT_TIME - WINDOW
    
    timestamps = store.get(client_ip, [])
    timestamps = [t for t in timestamps if t > window_start]
    
    if len(timestamps)>MAX_REQUESTS:
        raise HTTPException(
            status_code=429,
            detail="Rate limit Exceeded.."
        )

    timestamps.append(CURRENT_TIME)
    store[client_ip] = timestamps
    

@app.get("/")
def read_root(_:None=Depends(rate_limit)):
    return {"message": "Task API is running"}

