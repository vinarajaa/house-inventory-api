from fastapi import FastAPI
from app import models
from app.database import engine
from app.routers import items  # add this
from app.routers import items, lookup  # add lookup
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
# Allow frontend access (adjust for safety in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to ["http://localhost:5500"] if you prefer
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(items.router)
app.include_router(lookup.router)  # register lookup routes
models.Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return {"message": "House Inventory API is running!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
