import re
from typing import Dict, Any, Optional
from asteval import Interpreter

class MotorActuarial:
    """
    Motor actuarial configurable: permite evaluar fórmulas matemáticas seguras,
    con parámetros y factores dinámicos.
    """
    def __init__(self, reglas: Dict[str, Dict[str, Any]]):
        """
        reglas: diccionario de reglas, donde cada clave es el nombre de la regla,
        y el valor es un diccionario con 'fórmula' y 'parámetros'.
        """
        self.reglas = reglas
        self.asteval = Interpreter()

    def _resolver_factores(self, parametros: Dict[str, Any], entrada: Dict[str, Any]) -> Dict[str, Any]:
        """
        Combina los parámetros de la regla y los datos de entrada,
        resolviendo factores por edad, zona, etc.
        """
        contexto = parametros.copy()
        # Resolver factor_edad
        if "factor_edad" in contexto and "edad" in entrada:
            edad = int(entrada["edad"])
            for rango, factor in contexto["factor_edad"].items():
                if "+" in rango and edad >= int(rango.split("+")[0]):
                    contexto["factor_edad"] = factor
                    break
                elif "-" in rango:
                    min_e, max_e = map(int, rango.split("-"))
                    if min_e <= edad <= max_e:
                        contexto["factor_edad"] = factor
                        break
        # Resolver factor_zona
        if "factor_zona" in contexto and "zona" in entrada:
            zona = entrada["zona"]
            contexto["factor_zona"] = contexto["factor_zona"].get(zona, contexto["factor_zona"].get("Otras", 1.0))
        # Otros factores personalizables aquí...
        return contexto

    def calcular(self, nombre_regla: str, entrada: Dict[str, Any]) -> Dict[str, Any]:
        """
        Evalúa la fórmula de la regla indicada usando los datos de entrada.
        Devuelve un diccionario con el resultado y la trazabilidad.
        """
        if nombre_regla not in self.reglas:
            raise ValueError(f"Regla '{nombre_regla}' no encontrada.")
        regla = self.reglas[nombre_regla]
        parametros = regla.get("parámetros", {})
        contexto = self._resolver_factores(parametros, entrada)
        # Agregar a contexto los datos de entrada (suma_asegurada, etc.)
        contexto.update(entrada)
        formula = regla["fórmula"]
        # Solo permitimos expresiones matemáticas simples (validación básica)
        if not re.match(r'^[\w\s\*\+\-\/\(\)\.]+$', formula):
            raise ValueError("Fórmula contiene caracteres no permitidos.")
        # Evaluar fórmula
        self.asteval.symtable.clear()
        for k, v in contexto.items():
            self.asteval.symtable[k] = v
        resultado = self.asteval(formula)
        if self.asteval.error:
            raise ValueError(f"Error al evaluar la fórmula: {self.asteval.error[0].get_error()}")
        return {
            "resultado": resultado,
            "regla": nombre_regla,
            "formula": formula,
            "parametros_evaluados": contexto
        }

# Ejemplo de uso:
if __name__ == "__main__":
    reglas = {
        "prima_auto": {
            "fórmula": "suma_asegurada * tasa_base * factor_edad * factor_zona",
            "parámetros": {
                "tasa_base": 0.025,
                "factor_edad": {"18-25": 1.15, "26-40": 1.00, "41-65": 1.10, "66+": 1.30},
                "factor_zona": {"CDMX": 1.20, "GDL": 1.10, "MTY": 1.15, "Otras": 1.00}
            }
        }
    }
    entrada = {
        "suma_asegurada": 200000,
        "edad": 30,
        "zona": "CDMX"
    }
    motor = MotorActuarial(reglas)
    resultado = motor.calcular("prima_auto", entrada)
    print("Resultado del cálculo:", resultado)
