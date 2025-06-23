# Importaciones
from fastapi import FastAPI # Framework fastaopi
from pydantic import BaseModel # Entidad que define usuarios
from limpieza import cargar_datos # Función para limpiar y hacer la lista de datos

app = FastAPI() # Instancia de la aplicación

# Definición de la entidad Usuario
class Usuario(BaseModel):
    id: int
    nombreCompleto: str
    matricula: int
    edad: int
    carrera: str
    genero: str
    facultad: str
    correo: str
    semestre: int
    ciudadEstado: str
    lenguajeProgramacion: str
    especialidad: str
    nivelIngles: str
    estadoCivil: str


# Lista de usuarios
lista_dicts = cargar_datos('Modelos de Desarrollo Web.csv')  # Cargar y limpieza de los datos desde el archivo CSV
lista_usuarios = [Usuario(**usuario_dict)for usuario_dict in lista_dicts] # Convertir los diccionarios a instancias de Usuario

# Endpoints de la API - CRUD para usuarios

################### GET ###################
# Obtener todos los usuarios
@app.get("/usuarios", tags=["Get Usuarios"])
async def get_usuarios():
    return lista_usuarios

################### POST ###################
# Crear un nuevo usuario
@app.post("/usuarios", tags=["Post Usuarios"])
async def post_nuevo_usuario(usuario: Usuario):
    found = False
    
    for index, saved_user in enumerate(lista_usuarios):
        if saved_user.id == usuario.id:
            return {"error": "Usuario con este ID ya existe."}
    else:
        lista_usuarios.append(usuario)
        return {"message": "Usuario creado exitosamente.", "usuario": usuario}

#################### PUT ###################
# Actualizar un usuario existente
@app.put("/usuarios", tags=["Put Usuarios"])
async def put_usuario(usuario: Usuario):
    found = False
    
    for index, saved_user in enumerate(lista_usuarios):
        if saved_user.id == usuario.id:
            lista_usuarios[index] = usuario
            found = True
        
    if not found:
        return {"error": "No se actualizo el usuario, no existe."}
    else:
        return {"message": "Usuario actualizado exitosamente.", "usuario": usuario}

################### DELETE ###################
# Eliminar un usuario
@app.delete("/usuarios/{usuario_id}", tags=["Delete Usuarios"])
async def delete_usuario(usuario_id: int):
    found = False
    
    for index, saved_user in enumerate(lista_usuarios):
        if saved_user.id == usuario_id:
            del lista_usuarios[index]
            found = True
            
    if not found:
        return {"error": "No se elimino el usuario, no existe."}
    else:
        return {"message": "Usuario eliminado exitosamente.", "ID del usuario eliminado": usuario_id}
