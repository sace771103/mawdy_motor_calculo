from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Cotizacion(Base):
    __tablename__ = "cotizacion"
    id = Column(Integer, primary_key=True)
    producto_id = Column(Integer, ForeignKey("producto.id"))
    usuario_id = Column(Integer, ForeignKey("usuario.id"))
    canal_id = Column(Integer, ForeignKey("canal.id"))
    entrada = Column(JSON)
    resultado = Column(JSON)
    fecha = Column(DateTime)
    estado = Column(String, default="pendiente")
    producto = relationship("Producto")
    usuario = relationship("Usuario")
    canal = relationship("Canal")

class Factura(Base):
    __tablename__ = "factura"
    id = Column(Integer, primary_key=True)
    cotizacion_id = Column(Integer, ForeignKey("cotizacion.id"))
    monto_total = Column(Float)
    moneda = Column(String, default="MXN")
    fecha_emision = Column(DateTime)
    estado = Column(String, default="emitida")
    cotizacion = relationship("Cotizacion")

class Poliza(Base):
    __tablename__ = "poliza"
    id = Column(Integer, primary_key=True)
    factura_id = Column(Integer, ForeignKey("factura.id"))
    numero_poliza = Column(String, unique=True)
    fecha_inicio = Column(DateTime)
    fecha_fin = Column(DateTime)
    estado = Column(String, default="vigente")
    factura = relationship("Factura")
