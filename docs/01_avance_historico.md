# Bitácora de avances y decisiones – Motor de Cálculo Actuarial

## 2025-06-22

### Decisiones clave y respuestas

- **Jerarquía y relación de entidades:**
  - Una aseguradora puede tener múltiples negocios, y cada negocio múltiples productos.
  - Un producto puede estar en varios negocios o puede ser exclusivo de uno, según el caso de uso.
  - Los planes pueden tener descripciones similares entre productos, pero cada configuración es independiente (ejemplo: “oro/plata/bronce” en autos vs hogar).
  - Cada negocio puede tener reglas propias de pago, factores, cargos, etc., independientes del producto.

- **Requerimientos funcionales y técnicos:**
  - Se tendrá una interfaz web para que el equipo técnico (actuarios) gestione proyectos, productos, planes y coberturas de forma ágil.
  - El motor de cálculo debe ser digital, end-to-end y automatizado.
  - La interfaz debe incluir módulos para: seguridad, control de cambios, auditoría, buscadores, versionado, cumplimiento normativo.
  - Se debe incluir un módulo de simulación de escenarios (“matriz de pruebas”).
  - El resultado principal es exponer servicios para cotización e integración con cualquier canal de venta: portales, marketplace, chat, WhatsApp, app móvil, voz, etc.

- **Sugerencias agregadas:**
  - Roles y permisos avanzados.
  - Workflows de aprobación/publicación.
  - Documentación y trazabilidad de cambios.
  - Reportes, monitoreo y alertas.
  - Soporte multi-idioma, multimoneda y multi-región.
  - Sandbox para integradores externos.
  - Automatización de respaldos y versionado.
  - Soporte explícito a normatividad local (CNSF/SAT) y privacidad (GDPR/LFPDPPP).
  - Integraciones a CRM/ERP y facturación electrónica.

- **Decisión técnica:**
  - Todo el avance será respaldado en GitHub, con estructura modular y documentación en Markdown.
  - Se utilizarán archivos `.gitkeep` para mantener la estructura de carpetas en Git.
  - Toda la documentación y definiciones importantes del chat se copiarán aquí para no perder conocimiento.

---

### Próximos pasos sugeridos

1. Continuar documentando requerimientos funcionales y técnicos.
2. Modelar la base de datos y arquitectura técnica.
3. Definir y crear los primeros archivos de configuración y ejemplos de reglas.
4. Avanzar con el motor de cálculo y la matriz de pruebas.
5. Seguir poblando cada carpeta conforme avance el proyecto.

---

_Última actualización: 2025-06-22_
