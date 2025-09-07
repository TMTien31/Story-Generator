from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core import settings

app = FastAPI( 
    title="Story Generator API",
    description="API for generating stories using LangChain and OpenAI",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)