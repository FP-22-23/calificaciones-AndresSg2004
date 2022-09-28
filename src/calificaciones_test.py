
import calificaciones

def Execute():
  #  Er, Ac, Total = calificaciones.pregunta_datos_cuestionario()
   # nota_cues = calificaciones.calcula_nota_cuestionario(Er,Ac,Total)

 #   print(f"Tu nota en el cuestionario ha sido de: {nota_cues}.")
import csv
csv.reader()

    Cues = calificaciones.pregunta_cues()
    Parc = calificaciones.pregunta_prac()
    Proy = calificaciones.pregunta_proy()
    
    nota_cuat = calificaciones.calcula_nota_evaluacion_continua(Parc,Cues,Proy)

    print(f"Tu nota del cuatrimestre ha sido: {nota_cuat}")

if __name__ == '__main__':
    Execute()