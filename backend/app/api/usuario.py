from fastapi import APIRouter, HTTPException
from app.models.usuarios import Usuario
from app.models import SessionLocal
from pydantic import BaseModel

router = APIRouter(prefix="/usuarios", tags=["Usuario"])

class UsuarioSchema(BaseModel):
    nombre: str
    email: str

@router.get("/", response_model=list[UsuarioSchema])
def listar_usuarios():
    db = SessionLocal()
    usuarios = db.query(Usuario).all()
    return [UsuarioSchema(nombre=u.nombre, email=u.email) for u in usuarios]

@router.post("/", response_model=UsuarioSchema)
def crear_usuario(item: UsuarioSchema):
    db = SessionLocal()
    usuario = Usuario(nombre=item.nombre, email=item.email)
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return item
