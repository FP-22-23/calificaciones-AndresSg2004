
import calificaciones

def Execute():

    Cues = calificaciones.pregunta_cues()
    Parc = calificaciones.pregunta_prac()
    Proy = calificaciones.pregunta_proy()
    
    nota_cuat = calificaciones.calcula_nota_evaluacion_continua(Parc,Cues,Proy)

    print(f"Tu nota del cuatrimestre ha sido: {nota_cuat}")

if __name__ == '__main__':
    Execute()