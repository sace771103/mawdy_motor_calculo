from fastapi import APIRouter, HTTPException
from app.models.entidades import Cliente
from app.models import SessionLocal
from pydantic import BaseModel

router = APIRouter(prefix="/clientes", tags=["Cliente"])

class ClienteSchema(BaseModel):
    nombre: str
    descripcion: str = ""

@router.get("/", response_model=list[ClienteSchema])
def listar_clientes():
    db = SessionLocal()
    clientes = db.query(Cliente).all()
    return [ClienteSchema(nombre=c.nombre, descripcion=c.descripcion) for c in clientes]

@router.post("/", response_model=ClienteSchema)
def crear_cliente(item: ClienteSchema):
    db = SessionLocal()
    cliente = Cliente(nombre=item.nombre, descripcion=item.descripcion)
    db.add(cliente)
    db.commit()
    db.refresh(cliente)
    return item

@router.get("/{cliente_id}", response_model=ClienteSchema)
def obtener_cliente(cliente_id: int):
    db = SessionLocal()
    cliente = db.query(Cliente).get(cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="No encontrado")
    return ClienteSchema(nombre=cliente.nombre, descripcion=cliente.descripcion)
