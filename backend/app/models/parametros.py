from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, JSON, DateTime
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class ParametroComercial(Base):
    __tablename__ = "parametro_comercial"
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    valor = Column(Float)
    tipo = Column(String)  # Ej: factor, límite, comisión
    producto_id = Column(Integer, ForeignKey("producto.id"), nullable=True)
    cobertura_id = Column(Integer, ForeignKey("cobertura.id"), nullable=True)
    producto = relationship("Producto", back_populates="parametros_comerciales")
    cobertura = relationship("Cobertura", back_populates="parametros_comerciales")
    detalles = Column(JSON)

class FormaPago(Base):
    __tablename__ = "forma_pago"
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(Text)
    producto_id = Column(Integer, ForeignKey("producto.id"))
    producto = relationship("Producto", back_populates="formas_pago")

class MetodoPago(Base):
    __tablename__ = "metodo_pago"
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(Text)
    producto_id = Column(Integer, ForeignKey("producto.id"))
    producto = relationship("Producto", back_populates="metodos_pago")

class Recargo(Base):
    __tablename__ = "recargo"
    id = Column(Integer, primary_key=True)
    concepto = Column(String)
    porcentaje = Column(Float)
    condicion = Column(String)
    producto_id = Column(Integer, ForeignKey("producto.id"), nullable=True)
    cobertura_id = Column(Integer, ForeignKey("cobertura.id"), nullable=True)
    producto = relationship("Producto", back_populates="recargos")
    cobertura = relationship("Cobertura", back_populates="recargos")

class Descuento(Base):
    __tablename__ = "descuento"
    id = Column(Integer, primary_key=True)
    concepto = Column(String)
    porcentaje = Column(Float)
    condicion = Column(String)
    producto_id = Column(Integer, ForeignKey("producto.id"), nullable=True)
    cobertura_id = Column(Integer, ForeignKey("cobertura.id"), nullable=True)
    producto = relationship("Producto", back_populates="descuentos")
    cobertura = relationship("Cobertura", back_populates="descuentos")

class CostoAdicional(Base):
    __tablename__ = "costo_adicional"
    id = Column(Integer, primary_key=True)
    concepto = Column(String)
    monto = Column(Float)
    producto_id = Column(Integer, ForeignKey("producto.id"), nullable=True)
    cobertura_id = Column(Integer, ForeignKey("cobertura.id"), nullable=True)
    producto = relationship("Producto", back_populates="costos_adicionales")
    cobertura = relationship("Cobertura", back_populates="costos_adicionales")

class Impuesto(Base):
    __tablename__ = "impuesto"
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    porcentaje = Column(Float)
    producto_id = Column(Integer, ForeignKey("producto.id"), nullable=True)
    cobertura_id = Column(Integer, ForeignKey("cobertura.id"), nullable=True)
    producto = relationship("Producto", back_populates="impuestos")
    cobertura = relationship("Cobertura", back_populates="impuestos")
