import datetime
def saludar():
    print("Hola,Bienvenidos")
saludar()

def mostrar_hora():
    hora_actual=datetime.datetime.now().strftime("%H:%M:%S")
    print(f"La hora actual es:{hora_actual}")
mostrar_hora()

def calcular_area_triangulo(base,altura):
    area=(base*altura)/2
    return area
resultado=calcular_area_triangulo(10,5)
print(f"El área del triángulo es:{resultado}")

def saludar_persona(nombre,edad):
    print(f"Hola {nombre}, tienes {edad} años")
saludar_persona("Zaid",20)

def carrera_grupo(carrera,grupo):
    print(f"Carrera {carrera}, grupo {grupo}")
carrera_grupo("DSM","B")

def matricula(matricula):
    print(f"Matricula {matricula},")
matricula(250478)

def gracias():
    print("Gracias por contestar")
gracias()

def vuelve_pronto():
    print("Vuelve pronto")
vuelve_pronto()
