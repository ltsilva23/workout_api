from fastapi import APIRouter, Query
from fastapi_pagination import Page
from workout_api.atleta.controller import router as atleta
from workout_api.categorias.controller import router as categorias
from workout_api.centro_treinamento.controller import router as centro_treinamento
from workout_api.atleta.schema import AtletaListOut  # Importe o modelo de saída personalizado

api_router = APIRouter()

@api_router.get('/atletas', response_model=Page[AtletaListOut], tags=['atletas'])
async def listar_atletas(
    nome: str = Query(None, title="Nome do Atleta"),
    cpf: str = Query(None, title="CPF do Atleta"),
    limit: int = Query(10, description="Número máximo de resultados por página"),
    offset: int = Query(0, description="Índice do primeiro resultado a retornar"),
):
    return await atleta.listar_atletas(nome, cpf, limit, offset)

# Endpoint para listar categorias
@api_router.get('/categorias', tags=['categorias'])
async def listar_categorias():
   categorias_mock = [
        {"id": 1, "nome": "Categoria A"},
        {"id": 2, "nome": "Categoria B"},
    ]
    return categorias_mock

# Endpoint para listar centros de treinamento
@api_router.get('/centros_treinamento', tags=['centros_treinamento'])
async def listar_centros_treinamento():
     centros_treinamento_mock = [
        {"id": 1, "nome": "Centro A", "endereco": "Rua A, 123"},
        {"id": 2, "nome": "Centro B", "endereco": "Av. B, 456"},
    ]
    return centros_treinamento_mock

api_router.include_router(categorias, prefix='/categorias', tags=['categorias'])
api_router.include_router(centro_treinamento, prefix='/centros_treinamento', tags=['centros_treinamento'])
