# Modelo de Datos y Arquitectura Técnica

## 1. Entidades principales y relaciones

```
Aseguradora
   |
   |-- Negocio
         |
         |-- Producto
                |
                |-- Plan/Paquete
                        |
                        |-- Cobertura
                        |-- Regla / Configuración
```

- **Aseguradora:** Organización propietaria de los negocios y productos.
- **Negocio:** Línea o ramo de seguros (auto, vida, gastos médicos, etc).
- **Producto:** Producto asegurador específico (ej. Auto Premium, Vida Temporal).
- **Plan/Paquete:** Nivel de agrupación o variante del producto (ej. “Oro”, “Plata”, “Básico”).
- **Cobertura:** Beneficio o protección incluida en un plan (ej. robo, daños, responsabilidad civil).
- **Regla/Configuración:** Fórmulas, factores, tarifas, condiciones, métodos de pago, comisiones, impuestos, etc.

## 2. Atributos sugeridos por entidad

| Entidad     | Atributos principales                                           |
|-------------|----------------------------------------------------------------|
| Aseguradora | id, nombre, clave, estatus, fecha_alta, usuario_admin          |
| Negocio     | id, aseguradora_id, nombre, clave, tipo, estatus, fecha_alta   |
| Producto    | id, negocio_id, nombre, clave, descripción, estatus, version   |
| Plan        | id, producto_id, nombre, clave, descripción, estatus, version  |
| Cobertura   | id, plan_id, nombre, clave, suma_asegurada, deducible, estatus |
| Regla       | id, entidad_id, tipo, version, descripcion, expresion, params  |

> Nota: Se sugiere usar claves técnicas y versionado para cada entidad que requiera historial de cambios.

## 3. Diagrama ERD inicial (texto)

```
[ASEGURADORA] 1---n [NEGOCIO] 1---n [PRODUCTO] 1---n [PLAN] 1---n [COBERTURA]
                                                        |
                                                        +---n [REGLA/CONFIG]
```

## 4. Justificación de la estructura

- Permite un control jerárquico y versionable de productos y reglas de negocio.
- Facilita la trazabilidad de cambios y la configuración independiente por entidad.
- La entidad "Regla" es flexible para representar tarifas, factores, fórmulas, condiciones, etc., asociadas a cualquier nivel.

## 5. Siguientes pasos sugeridos

- Detallar atributos de cada entidad.
- Modelar tablas auxiliares (usuarios, roles, logs, auditoría, catálogos).
- Crear diagramas visuales (UML, Lucidchart, dbdiagram.io, etc.).
- Documentar ejemplos de reglas/configuraciones en formato JSON/YAML.

---

_Última actualización: 2025-06-22_
