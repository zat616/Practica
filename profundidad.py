def maxima_profundidad(comentarios: list) -> int:
    if not comentarios:
        return 0
    return max(
        1 + maxima_profundidad(elem) if isinstance(elem, list) else 1
        for elem in comentarios
    )

# Prueba
hilo = ["Comentario 1", ["Respuesta 1.1", ["Respuesta 1.1.1"]], "Comentario 2"]
print(maxima_profundidad(hilo))