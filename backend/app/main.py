from fastapi import FastAPI
from app.api import aseguradora, cliente, broker, canal, proyecto, producto, plan, cobertura, usuario

app = FastAPI(
    title="Motor Actuarial y Comercial de Seguros",
    description="Backend completo para gestión de productos, cotización, administración comercial y auditoría.",
    version="1.0.0"
)

app.include_router(aseguradora.router)
app.include_router(cliente.router)
app.include_router(broker.router)
app.include_router(canal.router)
app.include_router(proyecto.router)
app.include_router(producto.router)
app.include_router(plan.router)
app.include_router(cobertura.router)
app.include_router(usuario.router)

@app.get("/")
def root():
    return {"msg": "Motor Actuarial y Comercial de Seguros listo"}
