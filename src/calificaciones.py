
def calcula_nota_cuestionario(Ac,Er,Total):
    return 10*((Ac)/Total-(Er)/(50-Total))

def pregunta_datos_cuestionario():
    er = int(input("Inserte el número de errores: "))
    ac = int(input("Inserte el número de aciertos: "))
    total = int(input("Especifique el número total de preguntas: "))
    return er,ac,total 

def calcula_nota_cuatrimestre(Parc,Cues,Proy):
    to_return = 0.1*Cues+0.6*Parc+0.1*Proy
    if Proy < 5: to_return = 3
    return to_return

def calcula_nota_evaluacion_continua(Parc,Cues,Proy):
    Cuatr1 = calcula_nota_cuatrimestre(Parc[0],Cues[0] + Cues[1] + Cues[2],Proy[0])
    Cuatr2 = calcula_nota_cuatrimestre(Parc[1],Cues[3] + Cues[4] + Cues[5],Proy[1])
    to_return = (Cuatr1+Cuatr2)/2
    if Cuatr1 < 4 or Cuatr2 < 4:
        to_return = 4
    return to_return
        
def pregunta_cues():
    Cues = []
    for i in range(6):
        Cues.append(int(input(f"Nota del cuestionario número {i+1}:  ")))
    print("Gracias.")
    print("\n")
    tuple(Cues)
    return(Cues)
    
def pregunta_proy():
    Proy = [int(input("Nota del proyecto de python: ")),int(input("Nota del proyecto de java: "))]
    print("\n")
    tuple(Proy)
    return(Proy)

def pregunta_prac():
    Prac = [int(input("Nota del primer parcial: ")),int(input("Nota del segundo parcial: "))]
    print("\n")
    tuple(Prac)
    return(Prac)
