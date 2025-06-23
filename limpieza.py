import pandas as pd
import unicodedata

def limpiar_texto(texto):
    """
    Limpia el texto eliminando caracteres especiales, normalizando y convirtiendo a minúsculas.
    """
    if not isinstance(texto, str):
        return texto  # No modificar si no es texto
    
    # Eliminar caracteres especiales
    texto = ''.join(c for c in texto if c.isalnum() or c.isspace())
    
    # Normalizar el texto para eliminar acentos y caracteres especiales
    texto = unicodedata.normalize('NFKD', texto)
    
    # Eliminar los caracteres de combinación (como acentos)
    texto = ''.join(c for c in texto if not unicodedata.combining(c))
    
    # Convertir a minúsculas
    return texto.lower()

def cargar_datos(ruta_archivo):
    """
    Carga los datos desde un archivo CSV y limpia solo las columnas de texto.
    """
    df = pd.read_csv(ruta_archivo, encoding='utf-8')     # Carga el archivo CSV en un DataFrame (tabla de pandas)

    # Itera sobre las columnas que contienen texto (tipo 'object') y aplica la limpieza
    for columna in df.select_dtypes(include='object').columns:
        if columna != "correo":  # Excluir la columna 'correo' de la limpieza
            df[columna] = df[columna].apply(limpiar_texto)
    
    lista_dicts = df.to_dict('records')  # Convierte el DataFrame a una lista de diccionarios

    return lista_dicts  # Devuelve la lista de diccionarios 