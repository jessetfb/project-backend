
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from Modals.properties import Property
from Modals.users import User
import sys
import os

from backend.Modals.properties import Property


app = FastAPI()

properties = Property.find_all()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
def login_user(user):
    existing_user = User.find_by_email_and_password(user.email, user.password)
    if existing_user:
        return HTMLResponse(content="<h1>Logged in successfully!</h1>", status_code=200)
    else:
        return HTMLResponse(content="<h1>Invalid credentials</h1>", status_code=401)
    
@app.post("/register", response_class=HTMLResponse)
def register_user(user):
    existing_user = User.find_by_email(user.email)
    if not existing_user:
        new_user = User(email=user.email, password=user.password)
        new_user.save()
        return HTMLResponse(content="<h1>Registration successful!</h1>", status_code=201)
    else:
        raise HTTPException(status_code=400, detail="Email already registered")

@app.get("/properties")
def get_properties():
    properties = Property.find_all()
    return [{"id": p.id, "image": p.image, "description": p.description, "price": p.price} for p in properties]