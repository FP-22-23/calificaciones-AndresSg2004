
def GetMark(ac,er,total):
    return ((10*ac)/total-(10*er)/(50-total))

def InputVars():
    er = input("Inserte el número de errores: ")
    ac = input("Inserte el número de aciertos: ")
    total = input("Especifique el número total de preguntas: ")
    return er,ac,total 


    