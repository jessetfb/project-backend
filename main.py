import sys
import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List

from backend.modules.properties import properties, Property  # Adjust the import as per your file structure

# Assuming 'Modals' is located at the same level as 'backend/'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Modals')))

app = FastAPI()

# CORS middleware setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# Define Pydantic models for request/response handling
class LoginRequest(BaseModel):
    email: str
    password: str

class RegisterRequest(BaseModel):
    email: str
    password: str

# Routes
@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <body>
            <h1>Welcome to Real Estate API</h1>
        </body>
    </html>
    """

@app.post("/login", response_class=HTMLResponse)
def login_user(user: LoginRequest):
    # Placeholder for user login logic
    return HTMLResponse(content="<h1>Logged in successfully!</h1>", status_code=200)

@app.post("/register", response_class=HTMLResponse)
def register_user(user: RegisterRequest):
    # Placeholder for user registration logic
    return HTMLResponse(content="<h1>Registration successful!</h1>", status_code=201)

# Endpoint to return properties as a plain JSON response
@app.get("/properties")
def get_properties_plain():
    return properties

@app.get("/properties/{id}")
async def read_property(id: int):
    for prop in properties:
        if prop.id == id:
            return prop
    raise HTTPException(status_code=404, detail="Property not found")
