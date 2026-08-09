from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import logs

app = FastAPI(title="AI-Driven SOC Framework API")

# CORS middleware (required for UI → Backend communication)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # allow all origins
    allow_credentials=True,
    allow_methods=["*"],          # allow POST, GET, OPTIONS, etc.
    allow_headers=["*"],          # allow all headers
)

# Include your logs router
app.include_router(logs.router)

@app.get("/")
def root():
    return {"message": "SOC Framework Running"}
