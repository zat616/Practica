
def mostrar_encabezado_escuela():
    print("=" * 50)
    print("         UNIVERSIDAD TECNOLÓGICA DE XICOTEPEC        ")
    print("      REPORTE DE REGISTRO Y EVALUACIÓN DE NOTAS      ")
    print("=" * 50)


def obtener_nota_minima_aprobatoria():
    return 6.0


def evaluar_rendimiento(nota_final):
    if nota_final < 7.0:
        return "Reprobado"
    elif 7.0 <= nota_final <= 9.4:
        return "Aprobado"
    else:  # De 9.5 a 10
        return "Excelente"


def calcular_promedio(nota_examenes, nota_tareas):
    final = (nota_examenes * 0.70) + (nota_tareas * 0.30)
    return round(final, 1)


def generar_boleta(nombre_alumno, nota_examenes, nota_tareas):
    mostrar_encabezado_escuela()
    
    
    nota_final = calcular_promedio(nota_examenes, nota_tareas)
    nota_minima = obtener_nota_minima_aprobatoria()
    estado = evaluar_rendimiento(nota_final)
    
    
    necesita_extraordinario = "SÍ" if nota_final < nota_minima else "NO"
    
    
    print(f"Alumno:                        {nombre_alumno}")
    print(f"Nota Exámenes (70%):           {nota_examenes}")
    print(f"Nota Tareas (30%):             {nota_tareas}")
    print(f"Nota Final Ponderada:          {nota_final}")
    print(f"Estado Académico:              {estado}")
    print(f"Nota Mínima Requerida:         {nota_minima}")
    print(f"¿Requiere Examen Extraordinario?: {necesita_extraordinario}")
    print("=" * 50)



if __name__ == "__main__":
    
    generar_boleta("Juan Pérez", 8.5, 9.0)