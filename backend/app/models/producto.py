from sqlalchemy import Column, Integer, String, Text, Float, DateTime, Boolean, ForeignKey, JSON
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Producto(Base):
    __tablename__ = "producto"
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(Text)
    proyecto_id = Column(Integer, ForeignKey("proyecto.id"))
    proyecto = relationship("Proyecto", back_populates="productos")
    planes = relationship("Plan", back_populates="producto")
    coberturas = relationship("Cobertura", back_populates="producto")
    parametros_comerciales = relationship("ParametroComercial", back_populates="producto")
    formas_pago = relationship("FormaPago", back_populates="producto")
    metodos_pago = relationship("MetodoPago", back_populates="producto")
    recargos = relationship("Recargo", back_populates="producto")
    descuentos = relationship("Descuento", back_populates="producto")
    costos_adicionales = relationship("CostoAdicional", back_populates="producto")
    impuestos = relationship("Impuesto", back_populates="producto")
    reglas = relationship("Regla", back_populates="producto")
    facturacion = relationship("ConfiguracionFacturacion", back_populates="producto")
    estado = Column(String, default="activo")

class Plan(Base):
    __tablename__ = "plan"
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    producto_id = Column(Integer, ForeignKey("producto.id"))
    descripcion = Column(Text)
    producto = relationship("Producto", back_populates="planes")
    coberturas = relationship("Cobertura", back_populates="plan")

class Cobertura(Base):
    __tablename__ = "cobertura"
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(Text)
    producto_id = Column(Integer, ForeignKey("producto.id"))
    plan_id = Column(Integer, ForeignKey("plan.id"), nullable=True)
    producto = relationship("Producto", back_populates="coberturas")
    plan = relationship("Plan", back_populates="coberturas")
    reglas = relationship("Regla", back_populates="cobertura")
    parametros_comerciales = relationship("ParametroComercial", back_populates="cobertura")
    recargos = relationship("Recargo", back_populates="cobertura")
    descuentos = relationship("Descuento", back_populates="cobertura")
    costos_adicionales = relationship("CostoAdicional", back_populates="cobertura")
    impuestos = relationship("Impuesto", back_populates="cobertura")
    estado = Column(String, default="activo")
