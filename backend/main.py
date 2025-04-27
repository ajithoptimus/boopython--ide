# from fastapi import FastAPI
# from pydantic import BaseModel
# from fastapi.middleware.cors import CORSMiddleware

# app = FastAPI()

# # Define request body structure
# class CodeRequest(BaseModel):
#     code: str

# # Define endpoint to run code
# @app.post("/run")
# async def run_code(request: CodeRequest):
#     user_code = request.code
#     # Dummy response to check if the request is being received
#     return {"output": f"Received code: {user_code}"}


# @app.get("/")
# def read_root():
#     return {"message": "Hello, world!"}



# @app.post("/run")
# async def run_code(request: CodeRequest):
#     user_code = request.code
#     # Dummy response, in the future, we'll actually run the code
#     return {"output": f"Received code: {user_code}"}


#     # Add this
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Allow all origins (for now)
#     allow_credentials=True,
#     allow_methods=["*"],  # Allow all HTTP methods like GET, POST
#     allow_headers=["*"],  # Allow all headers
# )

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Allow frontend to communicate
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CodeRequest(BaseModel):
    code: str

@app.get("/")
def read_root():
    return {"message": "Hello, world!"}

@app.post("/run")
async def run_code(request: CodeRequest):
    user_code = request.code
    return {"output": f"Received code: {user_code}"}
