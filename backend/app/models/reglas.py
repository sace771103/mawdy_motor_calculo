from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey, JSON, DateTime
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Regla(Base):
    __tablename__ = "regla"
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(Text)
    tipo = Column(String)  # Ej: cálculo, validación, restricción
    version = Column(String, default="1.0")
    activa = Column(Boolean, default=True)
    producto_id = Column(Integer, ForeignKey("producto.id"), nullable=True)
    cobertura_id = Column(Integer, ForeignKey("cobertura.id"), nullable=True)
    producto = relationship("Producto", back_populates="reglas")
    cobertura = relationship("Cobertura", back_populates="reglas")
    formula = Column(Text)
    parametros = Column(JSON)
    restricciones = Column(JSON)
    fecha_creacion = Column(DateTime)
