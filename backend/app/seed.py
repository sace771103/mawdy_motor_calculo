from datetime import datetime
from models.entidades import Aseguradora, Cliente, Broker, Canal, Proyecto
from models.producto import Producto, Plan, Cobertura
from models.parametros import ParametroComercial, FormaPago, MetodoPago, Recargo, Descuento, CostoAdicional, Impuesto
from models.facturacion import ConfiguracionFacturacion
from models.reglas import Regla
from models.operaciones import Cotizacion
from models.usuarios import Usuario, Rol, Permiso
from models.auditoria import Auditoria
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Ajusta tu URI de base de datos aquí
engine = create_engine("sqlite:///db_actuarial.db")
Session = sessionmaker(bind=engine)
session = Session()

# 1. Entidades Superiores
aseguradora = Aseguradora(nombre="Aseguradora Demo", descripcion="Aseguradora de prueba")
cliente = Cliente(nombre="Cliente Demo", descripcion="Cliente institucional demo", aseguradora=aseguradora)
broker = Broker(nombre="Broker Demo", descripcion="Broker ejemplo", aseguradora=aseguradora)
canal = Canal(nombre="Web", descripcion="Cotizador web principal")

# 2. Proyecto y Producto
proyecto = Proyecto(
    nombre="Proyecto Demo",
    descripcion="Proyecto institucional demo",
    aseguradora=aseguradora,
    cliente=cliente,
    broker=broker,
    canal=canal
)
producto = Producto(
    nombre="Auto Particular",
    descripcion="Seguro de auto para particulares",
    proyecto=proyecto
)
plan = Plan(nombre="Plan Básico", descripcion="Plan base", producto=producto)
cobertura = Cobertura(nombre="Robo Total", descripcion="Cubre robo total del vehículo", producto=producto, plan=plan)

# 3. Parámetros y Configuración Comercial
param_factor_edad = ParametroComercial(nombre="factor_edad", valor=1.15, tipo="factor", producto=producto)
forma_pago = FormaPago(nombre="Contado", descripcion="Pago de contado", producto=producto)
metodo_pago = MetodoPago(nombre="Tarjeta", descripcion="Tarjeta de crédito/débito", producto=producto)
recargo = Recargo(concepto="Uso Comercial", porcentaje=0.1, producto=producto)
descuento = Descuento(concepto="Buen Conductor", porcentaje=0.05, producto=producto)
costo_adicional = CostoAdicional(concepto="Gastos de emisión", monto=300.0, producto=producto)
impuesto = Impuesto(nombre="IVA", porcentaje=0.16, producto=producto)

# 4. Facturación y Reglas
facturacion = ConfiguracionFacturacion(producto=producto, tipo_factura="digital", parametros={"folio":"A001"})
regla_prima = Regla(
    nombre="Cálculo Prima Base",
    tipo="cálculo",
    formula="suma_asegurada * factor_edad * (1 + recargo) * (1 - descuento)",
    version="1.0",
    activa=True,
    producto=producto,
    parametros={"factor_edad": 1.15, "recargo": 0.1, "descuento": 0.05}
)

# 5. Usuario y Seguridad
rol_admin = Rol(nombre="admin", descripcion="Administrador")
usuario_admin = Usuario(nombre="Admin", email="admin@demo.com", password_hash="hash", estado="activo", rol=rol_admin)

# 6. Cotización de ejemplo
cotizacion = Cotizacion(
    producto=producto,
    usuario=usuario_admin,
    canal=canal,
    entrada={"suma_asegurada": 200000, "edad": 30},
    resultado={"prima": 3500},
    fecha=datetime.now(),
    estado="emitida"
)

# 7. Commit de todo
session.add_all([
    aseguradora, cliente, broker, canal, proyecto, producto, plan, cobertura,
    param_factor_edad, forma_pago, metodo_pago, recargo, descuento, costo_adicional, impuesto,
    facturacion, regla_prima, rol_admin, usuario_admin, cotizacion
])
session.commit()
print("Datos de ejemplo insertados correctamente.")
