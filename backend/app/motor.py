import re
from typing import Dict, Any, List
from asteval import Interpreter

class MotorActuarial:
    """
    Motor actuarial configurable y multiproducto.
    Permite fórmulas dinámicas, factores, recargos y descuentos.
    """

    def __init__(self, reglas: Dict[str, Dict[str, Any]]):
        """
        reglas: Dict[str, Dict] - Cada clave es un producto/regla, valor es dict con:
            - 'fórmula': string
            - 'parámetros': dict
            - 'restricciones': lista de strings (opcional)
        """
        self.reglas = reglas
        self.asteval = Interpreter()

    def _resolver_factores(self, parametros: Dict[str, Any], entrada: Dict[str, Any]) -> Dict[str, Any]:
        ctx = parametros.copy()

        # Factores por edad
        if "factor_edad" in ctx and "edad" in entrada:
            edad = int(entrada["edad"])
            for rango, factor in ctx["factor_edad"].items():
                if "+" in rango and edad >= int(rango.split("+")[0]):
                    ctx["factor_edad"] = factor
                    break
                elif "-" in rango:
                    min_e, max_e = map(int, rango.split("-"))
                    if min_e <= edad <= max_e:
                        ctx["factor_edad"] = factor
                        break
        # Factores por zona
        if "factor_zona" in ctx and "zona" in entrada:
            zona = entrada["zona"]
            ctx["factor_zona"] = ctx["factor_zona"].get(zona, ctx["factor_zona"].get("Otras", 1.0))
        # Factores adicionales pueden añadirse aquí

        # Recargos y descuentos (se suman/multiplican según flags)
        recargos = 0.0
        if "recargos" in ctx:
            for nombre, val in ctx["recargos"].items():
                if entrada.get(nombre):
                    recargos += val
        ctx["recargos"] = recargos

        descuentos = 0.0
        if "descuentos" in ctx:
            for nombre, val in ctx["descuentos"].items():
                if entrada.get(nombre):
                    descuentos += val
        ctx["descuentos"] = descuentos

        return ctx

    def calcular(self, nombre_regla: str, entrada: Dict[str, Any]) -> Dict[str, Any]:
        if nombre_regla not in self.reglas:
            raise ValueError(f"Regla '{nombre_regla}' no encontrada.")
        regla = self.reglas[nombre_regla]
        parametros = regla.get("parámetros", {})
        restricciones = regla.get("restricciones", [])

        # Validación de restricciones simples (ejemplo)
        errores = []
        for restr in restricciones:
            if "Suma asegurada mínima" in restr:
                minimo = float(re.findall(r"\$([\d,\.]+)", restr)[0].replace(",", ""))
                if float(entrada.get("suma_asegurada", 0)) < minimo:
                    errores.append(f"Suma asegurada menor al mínimo permitido: {minimo}")
            if "Edad máxima" in restr:
                max_e = int(re.findall(r"(\d+)", restr)[0])
                if int(entrada.get("edad", 0)) > max_e:
                    errores.append(f"Edad superior al máximo permitido: {max_e}")

        if errores:
            return {
                "resultado": None,
                "errores": errores,
                "regla": nombre_regla,
                "formula": regla["fórmula"]
            }

        # Resolver factores dinámicos
        ctx = self._resolver_factores(parametros, entrada)
        # Agregar los datos de entrada
        ctx.update(entrada)

        # Validar fórmula
        formula = regla["fórmula"]
        if not re.match(r'^[\w\s\*\+\-\/\(\)\.]+$', formula):
            raise ValueError("Fórmula contiene caracteres no permitidos.")

        # Evaluar fórmula
        self.asteval.symtable.clear()
        for k, v in ctx.items():
            self.asteval.symtable[k] = v
        resultado = self.asteval(formula)
        if self.asteval.error:
            raise ValueError(f"Error al evaluar la fórmula: {self.asteval.error[0].get_error()}")

        return {
            "resultado": resultado,
            "detalle": {
                "regla": nombre_regla,
                "formula": formula,
                "parametros_evaluados": ctx,
                "restricciones": restricciones
            }
        }

# Ejemplo de uso:
if __name__ == "__main__":
    reglas = {
        "auto_particular": {
            "fórmula": (
                "suma_asegurada * tasa_base * factor_edad * factor_zona "
                "* (1 + recargos) * (1 - descuentos)"
            ),
            "parámetros": {
                "tasa_base": 0.025,
                "factor_edad": {
                    "18-25": 1.15,
                    "26-40": 1.00,
                    "41-65": 1.10,
                    "66+": 1.30
                },
                "factor_zona": {
                    "CDMX": 1.20,
                    "GDL": 1.10,
                    "MTY": 1.15,
                    "Otras": 1.00
                },
                "recargos": {
                    "uso_comercial": 0.10,
                    "blindado": 0.20
                },
                "descuentos": {
                    "buen_conductor": 0.10,
                    "multianual": 0.05
                }
            },
            "restricciones": [
                "Suma asegurada mínima: $100,000",
                "Edad máxima: 70 años",
                "Solo aplica a vehículos particulares"
            ]
        }
    }

    entrada = {
        "suma_asegurada": 200000,
        "edad": 30,
        "zona": "CDMX",
        "uso_comercial": False,
        "blindado": False,
        "buen_conductor": True,
        "multianual": False
    }

    motor = MotorActuarial(reglas)
    resultado = motor.calcular("auto_particular", entrada)
    print("Resultado del cálculo:", resultado)
