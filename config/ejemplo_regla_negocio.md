# Ejemplo de Configuración de Regla de Negocio

Este archivo muestra cómo estructurar una regla de negocio o configuración de cálculo usando formato YAML (puede adaptarse a JSON o tablas según necesidades).

## 1. Ejemplo: Regla de cálculo de prima para un seguro de autos

```yaml
regla_id: AUTO-PRIMA-2025-01
nombre: "Cálculo de Prima Base – Autos Particular"
entidad_aplica: "Producto"
referencia_entidad: "Auto Premium"
version: 1
estatus: "ACTIVA"
vigencia:
  inicio: "2025-07-01"
  fin: "2026-06-30"
formula: "prima_base = suma_asegurada * tasa_base * factor_edad * factor_zona + recargos - descuentos"
parametros:
  tasa_base: 0.025
  factor_edad:
    18-25: 1.15
    26-40: 1.00
    41-65: 1.10
    66+: 1.30
  factor_zona:
    CDMX: 1.20
    GDL: 1.10
    MTY: 1.15
    Otras: 1.00
  recargos:
    uso_comercial: 0.10
    blindado: 0.20
  descuentos:
    buen_conductor: 0.10
    multianual: 0.05
restricciones:
  - "Suma asegurada mínima: $100,000"
  - "Edad máxima: 70 años"
  - "Solo aplica a vehículos particulares"
notas: |
  - Esta regla es solo para el producto Auto Premium, versión 1.
  - Los factores pueden modificarse en la configuración sin desplegar código.
  - Los parámetros y restricciones son auditables y versionables.
```

## 2. Consideraciones

- Cada regla/configuración debe tener un identificador único, nombre, versión y rango de vigencia.
- La fórmula debe estar expresada de forma clara y auditable.
- Los parámetros y factores deben poder modificarse por el usuario autorizado.
- Las restricciones ayudan a validar los escenarios válidos para la aplicación de la regla.
- Las reglas se pueden asociar a cualquier nivel de la jerarquía (producto, plan, cobertura, etc.).

---

_Última actualización: 2025-06-22_
