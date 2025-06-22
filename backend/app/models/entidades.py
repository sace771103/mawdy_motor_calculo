from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Aseguradora(Base):
    __tablename__ = "aseguradora"
    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True, nullable=False)
    descripcion = Column(Text)
    clientes = relationship("Cliente", back_populates="aseguradora")
    brokers = relationship("Broker", back_populates="aseguradora")
    proyectos = relationship("Proyecto", back_populates="aseguradora")

class Cliente(Base):
    __tablename__ = "cliente"
    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True, nullable=False)
    descripcion = Column(Text)
    aseguradora_id = Column(Integer, ForeignKey("aseguradora.id"))
    aseguradora = relationship("Aseguradora", back_populates="clientes")
    proyectos = relationship("Proyecto", back_populates="cliente")

class Broker(Base):
    __tablename__ = "broker"
    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True, nullable=False)
    descripcion = Column(Text)
    aseguradora_id = Column(Integer, ForeignKey("aseguradora.id"))
    aseguradora = relationship("Aseguradora", back_populates="brokers")
    proyectos = relationship("Proyecto", back_populates="broker")

class Canal(Base):
    __tablename__ = "canal"
    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True, nullable=False)
    descripcion = Column(Text)
    proyectos = relationship("Proyecto", back_populates="canal")

class Proyecto(Base):
    __tablename__ = "proyecto"
    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True, nullable=False)
    descripcion = Column(Text)
    aseguradora_id = Column(Integer, ForeignKey("aseguradora.id"))
    cliente_id = Column(Integer, ForeignKey("cliente.id"))
    broker_id = Column(Integer, ForeignKey("broker.id"), nullable=True)
    canal_id = Column(Integer, ForeignKey("canal.id"), nullable=True)
    aseguradora = relationship("Aseguradora", back_populates="proyectos")
    cliente = relationship("Cliente", back_populates="proyectos")
    broker = relationship("Broker", back_populates="proyectos")
    canal = relationship("Canal", back_populates="proyectos")
    productos = relationship("Producto", back_populates="proyecto")
