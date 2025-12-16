from fastapi import FastAPI
from api.routes.health import router as health_router
from api.routes.improver import router as improver_router
from api.routes.suggestion import router as suggestion_router
from api.routes.qa import router as qa_router

def create_app() -> FastAPI:
    app = FastAPI(
        title="Paper Plus API",
        description="AI-powered research assistant",
        version='1.0.0'
    )
    
    app.include_router(health_router)
    app.include_router(improver_router)
    app.include_router(suggestion_router)
    app.include_router(qa_router)
    
    return app

app = create_app()