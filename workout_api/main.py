from fastapi import FastAPI, Request
from fastapi_pagination import add_pagination
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError
from workout_api.routers import api_router

app = FastAPI(title='WorkoutApi')

@app.exception_handler(IntegrityError)
async def integrity_error_handler(request: Request, exc: IntegrityError):
    if 'atleta' in str(exc.orig):
        return JSONResponse(
            status_code=303,
            content={"detail": f"Já existe um atleta cadastrado com o cpf: {request.json()['cpf']}"}
        )
    return JSONResponse(
        status_code=400,
        content={"detail": "Erro de integridade de dados"}
    )

app.include_router(api_router)
add_pagination(app)
