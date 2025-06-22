from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Auditoria(Base):
    __tablename__ = "auditoria"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuario.id"))
    accion = Column(String)
    entidad = Column(String)
    entidad_id = Column(Integer)
    detalle = Column(Text)
    fecha = Column(DateTime)

class CambioRegla(Base):
    __tablename__ = "cambio_regla"
    id = Column(Integer, primary_key=True)
    regla_id = Column(Integer, ForeignKey("regla.id"))
    usuario_id = Column(Integer, ForeignKey("usuario.id"))
    descripcion = Column(Text)
    fecha = Column(DateTime)

class LogSistema(Base):
    __tablename__ = "log_sistema"
    id = Column(Integer, primary_key=True)
    nivel = Column(String)
    mensaje = Column(Text)
    fecha = Column(DateTime)
