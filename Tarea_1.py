import random
import time
import bisect
import os
import sys

N = 10_000_000
Archivo = "numeros.txt"
Busquedas = 1000
Min = -50_000_000
Max = 50_000_000


def generar_archivo():
    with open(Archivo,"w") as f:
        for _ in range(N):
            f.write(str(random.randint(Min, Max)) + "\n")
    print("Archivo generado.")

def cargar_datos():
    with open(Archivo, "r") as f:
        datos = [int(line.strip()) for line in f]
        print("Datos cargados.")
        return datos  
    
class Nodo:
    __slots__ = ("valor", "izq", "der")

    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
            return
        
        actual = self.raiz
        while True:
            if valor < actual.valor:
                if actual.izq is None:
                    actual.izq = Nodo(valor)
                    return
                actual = actual.izq
            else:
                if actual.der is None:
                    actual.der = Nodo(valor)
                    return
                actual = actual.der

    def buscar(self, valor):
        actual = self.raiz
        while actual:
            if valor == actual.valor:
                return True
            elif valor < actual.valor:
                actual = actual.izq
            else:
                actual = actual.der
        return False

def medir_busquedas_estructura(estructura, tipo, datos):
    tiempos = []

    for _ in range(Busquedas):
        objetivo = random.choice(datos)
        inicio = time.perf_counter()

        if tipo == "lista":
            idx = bisect.bisect_left(estructura, objetivo)
            encontrado = idx < len(estructura) and estructura[idx] == objetivo

        elif tipo == "set":
            encontrado = objetivo in estructura

        elif tipo == "arbol":
            encontrado = estructura.buscar(objetivo)

        fin = time.perf_counter()
        tiempos.append(fin - inicio)

    return sum(tiempos) / len(tiempos)

if __name__ == "__main__":

    if not os.path.exists(Archivo):
        generar_archivo()

    datos = cargar_datos()

    print("\nConstruyendo estructuras...")

    # Lista ordenada
    lista = sorted(datos)

    # Hash
    tabla_hash = set(datos)

    # Arbol binario
    arbol = ArbolBinario()
    for num in datos:
        arbol.insertar(num)

    print("Estructuras construidas.\n")

    print("Midiendo tiempos...")

    t_lista = medir_busquedas_estructura(lista, "lista", datos)
    t_hash = medir_busquedas_estructura(tabla_hash, "set", datos)
    t_arbol = medir_busquedas_estructura(arbol, "arbol", datos)

    print("\n===== RESULTADOS =====")
    print(f"Lista ordenada (binaria): {t_lista*1000:.4f} ms")
    print(f"Tabla Hash (set): {t_hash*1000:.4f} ms")
    print(f"Arbol Binario: {t_arbol*1000:.4f} ms")