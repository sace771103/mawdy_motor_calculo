# 🏦 Motor Actuarial y Comercial de Seguros – Estructura Base

## Resumen

Este proyecto es un backend escalable, flexible y profesional para la gestión integral de productos aseguradores, cotización, facturación, reglas actuariales y administración comercial.  
Incluye jerarquía completa de entidades: aseguradora, cliente, broker, canal, proyecto, producto, planes, coberturas, configuración comercial, usuarios, auditoría y más.

---

## Estructura de carpetas

```
backend/
  app/
    models/           # Modelos SQLAlchemy agrupados por dominio
    api/              # Endpoints de FastAPI (ejemplos incluidos)
    seed.py           # Script para poblar datos de ejemplo
    motor.py          # Motor actuarial puro
    main.py           # Entrada de la app FastAPI
  alembic/            # Migraciones automáticas
  README.md
```

---

## Requisitos

- Python 3.10+
- pip (recomendada venv)
- Base de datos (SQLite por defecto, puedes migrar a Postgres/MySQL fácilmente)
- Dependencias iniciales:
  - sqlalchemy
  - alembic
  - fastapi
  - uvicorn
  - pydantic

```bash
pip install sqlalchemy alembic fastapi uvicorn pydantic
```

---

## Primeros pasos

1. **Clona el repositorio y navega a `/backend`**

2. **Inicializa la base de datos**

   ```bash
   alembic upgrade head
   ```

3. **Carga datos de ejemplo**

   ```bash
   python app/seed.py
   ```

4. **Levanta el servidor**

   ```bash
   uvicorn app.main:app --reload
   ```

5. **Accede a la documentación interactiva**

   Ir a: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## Modelos principales y relaciones

- **Aseguradora**  
  └─ Cliente  
      └─ Proyecto  
          └─ Producto  
              ├─ Plan  
              │    └─ Cobertura  
              ├─ Parámetros comerciales  
              ├─ Reglas  
              ├─ Configuración comercial  
              └─ ... (formas de pago, recargos, costos, facturación, etc.)

- **Broker** y **Canal**: transversales, asociados a proyecto/producto según tu negocio.

- **Cotización, Factura, Póliza**: registros operativos ligados a Producto, Canal, Usuario, etc.

- **Usuario, Rol, Permiso**: administración y seguridad.

- **Auditoría, Logs**: trazabilidad total.

---

## Migraciones y seed

- **Migraciones**:  
  Mantén el esquema actualizado con Alembic.  
  Si modificas modelos, ejecuta:
  ```bash
  alembic revision --autogenerate -m "tu mensaje"
  alembic upgrade head
  ```

- **Datos de ejemplo**:  
  Usa `python app/seed.py` para poblar datos básicos y empezar a probar.

---

## Endpoints de ejemplo (FastAPI)

Los endpoints REST están en `/app/api/`.  
Aquí algunos ejemplos (ver más en el código):

- **Aseguradora**
    - `GET    /aseguradoras/` — Listar aseguradoras
    - `POST   /aseguradoras/` — Crear aseguradora
    - `GET    /aseguradoras/{id}` — Detalle aseguradora

- **Cliente**
    - `GET    /clientes/`
    - `POST   /clientes/`
    - `GET    /clientes/{id}`

- **Broker, Canal, Proyecto, Producto, Plan, Cobertura**  
  (Mismos métodos CRUD)

- **Usuario (autenticación simple)**
    - `POST /login` — Login ejemplo (retorna token falso)

---

## Buenas prácticas

- Usa los modelos de ejemplo como referencia para tus propias extensiones.
- Documenta cada regla de negocio especial en los modelos o endpoints.
- Usa los logs y auditoría para trazabilidad.
- Crea scripts de migración cada vez que alteres el esquema.
- Mantén los seeds actualizados para nuevos equipos/desarrolladores.

---

## Equipo

- Arquitectura, modelos y semilla: **Copilot**
- Contacto: [Tu equipo aquí]

---

# ¡A desarrollar y cotizar!
