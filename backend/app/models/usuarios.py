from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuario"
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String)
    estado = Column(String, default="activo")
    rol_id = Column(Integer, ForeignKey("rol.id"))
    rol = relationship("Rol")
    fecha_creacion = Column(DateTime)

class Rol(Base):
    __tablename__ = "rol"
    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True, nullable=False)
    descripcion = Column(String)
    permisos = relationship("Permiso", secondary="rol_permiso", back_populates="roles")

class Permiso(Base):
    __tablename__ = "permiso"
    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True, nullable=False)
    descripcion = Column(String)
    roles = relationship("Rol", secondary="rol_permiso", back_populates="permisos")

class RolPermiso(Base):
    __tablename__ = "rol_permiso"
    rol_id = Column(Integer, ForeignKey("rol.id"), primary_key=True)
    permiso_id = Column(Integer, ForeignKey("permiso.id"), primary_key=True)
