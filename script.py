from usuario import Usuario
import json

def escribir_log (excepcion):
    with open('error.log', 'a') as archivo_error:
        archivo_error.write(str(excepcion) + '\n')
        archivo_error.close()

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