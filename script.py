from usuario import Usuario
import datetime
import os
import json

def escribir_log (excepcion):
    '''
        Método que escribe error en un log diario. Este log escribe la fecha y hora del error más la descripción.
        Parameter
        -----------
        excepcion
            Type:   Exception
            
        '''
    try:
        archivo = f"log.{datetime.date.today()}.log"
        fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(os.path.abspath('logs/'+archivo), 'a') as log:
            log.write(f"[{fecha_hora}]  ERROR:  {str(excepcion)}\n")
            log.close()
    except OSError as e:
        print(f"Error al intentar crear el archivo log: {str(e)}")

usuarios = []
# Leer el archivo usuarios.txt línea por línea
try:
    with open('usuarios.txt', 'r') as archivo_usuarios:
        for linea in archivo_usuarios:
            try:
                usuario = json.loads(linea)
                
                # Crear una instancia de Usuario con los datos del JSON
                usuarios.append(Usuario(usuario.get("nombre"),usuario.get("apellido"),usuario.get("email"),usuario.get("genero")))
            except json.JSONDecodeError as e:
                escribir_log(e)
            except Exception as e:
                escribir_log(e)
    archivo_usuarios.close()
except FileNotFoundError as e:
    escribir_log(e)
except Exception as e:
    escribir_log(e)
    
    
for u in usuarios:
    print(u.nombre)