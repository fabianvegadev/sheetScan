import re
from consts.consts import LINK_ARCHIVO

def getLinkDownload():
    """
    Extrae el ID del archivo de Google Sheets desde un enlace y construye el link de descarga en formato CSV.
    Returns:
        str: Link de descarga directa del archivo en formato CSV.
    Raises:
        ValueError: Si el enlace no contiene un ID válido.
        TypeError: Si LINK_ARCHIVO no es un string.
    """
    if not isinstance(LINK_ARCHIVO, str):
        raise TypeError("El valor de LINK_ARCHIVO debe ser un string.")

    match = re.search(r"/d/([a-zA-Z0-9-_]+)", LINK_ARCHIVO)
    if not match:
        raise ValueError("No se encontró un ID válido en el enlace proporcionado.")

    file_id = match.group(1)
    link = f"https://docs.google.com/spreadsheets/d/{file_id}/export?format=csv"
    return link
