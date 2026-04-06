# Importamos librerias
import datetime
import random
from typing import List, Dict

MemoriaAgente = List[Dict[str, str]]

class PseudoAgente:
    def __init__(self, nombre):
        # El agente guarda el nombre del que entro
        self.nombre = nombre
        self.tokens = 100
        self.historial_chat: MemoriaAgente = []

    def _quitar_tokens(self, cuanto):
        # Si no hay puntos, devuelve Falso
        if self.tokens < cuanto:
            return False
        self.tokens = self.tokens - cuanto
        return True

    def gestionar_historial(self, accion):
        # Guardar cosas gasta 5 puntos
        if self._quitar_tokens(5) == False: return "AGOTADO"
        reloj = datetime.datetime.now().strftime("%H:%M:%S")
        self.historial_chat.append({"hora": reloj, "accion": accion})
        return "Ok"

    def fecha_hoy(self):
        if self._quitar_tokens(2) == False: return "AGOTADO"
        return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def contar_letras(self, texto):
        if self._quitar_tokens(3) == False: return "AGOTADO"
        return "Letras: " + str(len(texto.strip()))

    def ejecutar_calculadora(self, n1, op, n2):
        if self._quitar_tokens(4) == False: return "AGOTADO"
        if op == "+": res = n1 + n2
        elif op == "-": res = n1 - n2
        elif op == "*": res = n1 * n2
        elif op == "/": res = n1 / n2 if n2 != 0 else "Error"
        else: res = "Signo mal puesto"
        return str(res)

    def lanzar_dado(self):
        if self._quitar_tokens(1) == False: return "AGOTADO"
        return "Dado: " + str(random.randint(1, 6))

    def hacer_ping(self):
        if self._quitar_tokens(2) == False: return "AGOTADO"
        return "pong!"