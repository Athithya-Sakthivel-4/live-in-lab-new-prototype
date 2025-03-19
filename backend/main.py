from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import auth, routes
from models.database import engine, Base
from scripts.init_db import init_db

# Initialize Database
Base.metadata.create_all(bind=engine)
init_db()  # Run DB initialization script

# Create FastAPI instance
app = FastAPI(title="Child Recovery Platform API", version="1.0")

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to specific frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(auth.router)
app.include_router(routes.children_router)
app.include_router(routes.face_router)
app.include_router(routes.admin_router)
app.include_router(routes.health_router)

# Root Endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Child Recovery Platform API"}
