from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class ConfiguracionFacturacion(Base):
    __tablename__ = "configuracion_facturacion"
    id = Column(Integer, primary_key=True)
    producto_id = Column(Integer, ForeignKey("producto.id"))
    producto = relationship("Producto", back_populates="facturacion")
    tipo_factura = Column(String)
    parametros = Column(JSON)
    vigencia_inicio = Column(DateTime)
    vigencia_fin = Column(DateTime)
