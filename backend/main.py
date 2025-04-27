from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define request body structure
class CodeRequest(BaseModel):
    code: str

# Define endpoint to run code
@app.post("/run")
async def run_code(request: CodeRequest):
    user_code = request.code
    # Dummy response to check if the request is being received
    return {"output": f"Received code: {user_code}"}
