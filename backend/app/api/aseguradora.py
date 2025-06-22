from fastapi import APIRouter, HTTPException
from app.models.entidades import Aseguradora
from app.models import SessionLocal
from pydantic import BaseModel

router = APIRouter(prefix="/aseguradoras", tags=["Aseguradora"])

class AseguradoraSchema(BaseModel):
    nombre: str
    descripcion: str = ""

@router.get("/", response_model=list[AseguradoraSchema])
def listar_aseguradoras():
    db = SessionLocal()
    aseguradoras = db.query(Aseguradora).all()
    return [AseguradoraSchema(nombre=a.nombre, descripcion=a.descripcion) for a in aseguradoras]

@router.post("/", response_model=AseguradoraSchema)
def crear_aseguradora(item: AseguradoraSchema):
    db = SessionLocal()
    aseguradora = Aseguradora(nombre=item.nombre, descripcion=item.descripcion)
    db.add(aseguradora)
    db.commit()
    db.refresh(aseguradora)
    return item

@router.get("/{aseguradora_id}", response_model=AseguradoraSchema)
def obtener_aseguradora(aseguradora_id: int):
    db = SessionLocal()
    aseguradora = db.query(Aseguradora).get(aseguradora_id)
    if not aseguradora:
        raise HTTPException(status_code=404, detail="No encontrada")
    return AseguradoraSchema(nombre=aseguradora.nombre, descripcion=aseguradora.descripcion)
