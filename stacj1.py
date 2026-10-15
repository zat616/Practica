historial navegacion=[]

historial navegacion.append("google.com")
historial navegacion.append("youtube.com")
historial navegacion.append("wikipedia.org")

print("Historial cargado:", historial_navegacion)
#OPERACION CIMA (TO/PEEK)

pagina_actual=historial_navegacion[-1]
print("pagina actual en pantalla;",pagina_actual)

#OPERACION DE DESAPILAR(POP)
pagina_cerrada=historial_navegacion.pop()
print("saliendo de",pagina_cerrada)
print ("historial despues de presionar 'Atras':", historial navegacion)

#TAMAÑO DE LA PILA
total_paginas=len(historial_navegacion)
print("Paginas previas guardadas:",total_paginas)

#OPERACION VACIA(EMPTY)
sin_paginas=len(historial_navegacion)==0
print("El historial esta vacio?",sin_paginas)
