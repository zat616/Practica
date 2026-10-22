from collections import deque 
import time
cola_reproduccion=deque()
#AGREGAR ELEMENTOS DE REPRODUCCION
cola_reproduccion.append("1.- Mochila azul")
cola_reproduccion.append("2.- Aerolinea Carrillo")
cola_reproduccion.append("3.- La cabeza")
#MOSTRAR LAS CANCIONES
print("Canciones en espera")
for cancion in cola_reproduccion:
    print("_", cancion)
    print("INICIANDO REPRODUCCIÓN")
#DESENCOLAR
while cola_reproduccion:
    cancion_actual=cola_reproduccion.popleft()
    print(f"Sonando ahora:{cancion_actual}")
    time.sleep(1) #SIMULA LA DURACIÓN DEL TEMA
    print(f"Finalizo:{cancion_actual}")
    #MUESTRA CUÁNTAS CANCIONES QUEDAN EN LA COLA
    print(f"(Quedan{len(cola_reproduccion)}canciones ne la cola)")
    print("LA COLA DE REPRODUCCION HA FINALIZADO")