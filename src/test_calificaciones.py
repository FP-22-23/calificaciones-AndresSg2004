
import calificaciones

def Execute():
  Er, Ac, Total = calificaciones.pregunta_datos_cuestionario()
  nota_cues = calificaciones.calcula_nota_cuestionario(Er,Ac,Total)

  print(f"Tu nota en el cuestionario ha sido de: {nota_cues}.")
 
if __name__ == '__main__':
    Execute()