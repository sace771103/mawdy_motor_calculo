# Requerimientos Funcionales y Técnicos

## 1. Requerimientos Funcionales

### 1.1. Jerarquía y configuración de productos
- El sistema debe permitir crear y mantener una jerarquía:
  - Aseguradora → Negocio → Producto → Plan/Paquete → Cobertura
- Los usuarios autorizados pueden configurar reglas de negocio, tarifas, factores, métodos de pago, comisiones e impuestos por cada nivel.
- Debe ser posible versionar cada configuración y mantener histórico de cambios.

### 1.2. Motor de cálculo actuarial
- El sistema debe exponer un motor digital centralizado para el cálculo de primas y cotizaciones.
- El motor debe ser parametrizable y soportar reglas complejas, incluyendo excepciones y condiciones especiales.
- Debe exponer APIs REST seguras para integración con otros sistemas y canales de venta.

### 1.3. Interfaz y experiencia de usuario
- Web app moderna dirigida a usuarios técnicos (actuarios, producto, TI) con experiencia intuitiva.
- Módulos para auditoría, control de cambios, simulaciones de cálculo y validaciones masivas (“matriz de pruebas”).
- Buscadores y filtros avanzados para localizar productos, planes, reglas y cotizaciones.

### 1.4. Seguridad, roles y auditoría
- Gestión de usuarios y roles: acceso granular por módulo y operación.
- Trazabilidad de cambios, logs de actividad y control de versiones.
- Workflows de aprobación/publicación de cambios.

### 1.5. Integraciones y exposición de servicios
- APIs RESTful documentadas y seguras para cotización, consulta de productos, reglas, versiones y resultados.
- Sandbox y documentación para integradores externos.
- Soporte para integración con portales, CRM, ERP, apps móviles, chatbots, marketplaces y otros canales.

### 1.6. Cumplimiento normativo y reportes
- Soporte explícito a normatividad CNSF, SAT, GDPR y LFPDPPP.
- Generación de reportes operativos y regulatorios.
- Alertas y monitoreo de eventos clave.

## 2. Requerimientos Técnicos

### 2.1. Plataforma y arquitectura
- Arquitectura modular, escalable y desacoplada.
- Backend basado en servicios (microservicios o modular monolith).
- Frontend responsivo y moderno (SPA preferentemente).
- Base de datos relacional (preferente: PostgreSQL) y soporte para logs/documentos (NoSQL opcional).

### 2.2. Seguridad y control de acceso
- Autenticación robusta (OAuth2, SSO, 2FA).
- Autorización por roles y permisos.
- Cifrado de datos sensibles en tránsito y reposo.

### 2.3. Integraciones y APIs
- REST API, preferente OpenAPI/Swagger documentado.
- Webhooks y eventos para integración con terceros.
- Soporte para pruebas y sandbox de APIs.

### 2.4. Versionado y despliegue
- Control de versiones en Git (GitHub).
- Workflows de CI/CD para pruebas, despliegue y rollback.
- Automatización de respaldos y migraciones.

### 2.5. Pruebas, monitoreo y calidad
- Estrategia de pruebas unitarias, integrales y de aceptación.
- Monitoreo de logs, métricas y alertas.
- Estrategia de recuperación ante fallos.

## 3. Restricciones y supuestos iniciales

- El sistema se desarrollará inicialmente en español y para normatividad mexicana.
- Todo cambio relevante debe quedar documentado y auditable.
- El motor de cálculo debe ser agnóstico al tipo de producto asegurador (vida, autos, daños, salud, etc.).
- Las reglas y configuraciones deben poderse modificar sin necesidad de despliegues de código (configuración en caliente).
- El acceso a APIs y la administración de usuarios debe ser seguro y auditable.

---

_Última actualización: 2025-06-22_
