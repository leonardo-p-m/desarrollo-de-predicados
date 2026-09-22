# se define el universo como diccionario de diccionarios

u = {
    "matriculas": {
        "Rodolfo": [1],
        "Fabian": [2],
        "Lalo": [3]
    },

    "estudiantes": {
        "Rodolfo": ["Redes"],
        "Fabian": ["Algebra"],
        "Lalo": ["Programacion"]
    },

    "profesores": {
        "Cosio": ["Redes"],
        "Rodriguez": ["Algebra"],
        "Perez": ["Programacion"]
    },

    "asignaturas": {
        "Redes": ["Rodolfo"],
        "Algebra": ["Fabian"],
        "Programacion": ["Lalo"]
    },

    "carreras": {
        "Sistemas": ["Rodolfo", "Fabian", "Lalo"]
    },

    "salones": {
        207: ["Rodolfo"],
        208: ["Fabian"],
        209: ["Lalo"]
    },

    "coordinadores": {
        "Gael": ["Sistemas"]
    },

    "edificios": {
        200: [207, 208, 209]
    },

}

#se definen las funciones para obtener la información del universo  
#7 predicados

#1
def estudiante(x):
    return u["estudiantes"].get(x, [])   
#2   
def profesor(p):
    return u["profesores"].get(p, [])      
#3
def asignatura(a):
    return u["asignaturas"].get(a, [])             
#4
def salon(s):
    return u["salones"].get(s, [])     
#5 
def edificio(e):
    return u["edificios"].get(e, []) 
#6
def inscrito_en(x, a):
    return x in u["asignaturas"].get(a, [])     
#7
def imparte_asignatura(p, a):
    return a in u["profesores"].get(p, [])

#verificar que un estudiante pertenece a una carrera
#motor de inferencia: cuestionar información del universo

print("Fabian tiene la asignatura de:", estudiante("Fabian"))

print("El profesor Rodriguez imparte la asignatura de:", profesor("Rodriguez"))

print("La asignatura de Algebra tiene los estudiantes:", asignatura("Algebra"))

print("El salon 207 tiene los estudiantes:", salon(207))

print("Rodolfo es estudiante de la carrera de Sistemas:", "Rodolfo" in u["carreras"]["Sistemas"]) 

print("El profesor Cosio imparte la asignatura de Redes:", imparte_asignatura("Cosio", "Redes"))

print("El estudiante Rodolfo está inscrito en la asignatura de Algebra:", inscrito_en("Rodolfo", "Algebra"))