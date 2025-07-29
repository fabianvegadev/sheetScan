import pandas as pd
import requests
from io import StringIO
from src.be.getLinkDownload import getLinkDownload


def getDataFrame() -> pd.DataFrame:
    """
    Descarga un archivo CSV desde un enlace generado por `getLinkDownload` y lo convierte en un DataFrame de pandas.

    Returns:
        pd.DataFrame: DataFrame resultante del archivo CSV descargado.

    Raises:
        Exception: Si ocurre un error en la solicitud HTTP o en la conversión del contenido a DataFrame.
    """
    link = getLinkDownload()

    try:
        response = requests.get(link)
        response.raise_for_status()  # Lanza un error si el status no es 200
    except requests.RequestException as e:
        raise Exception(f"Error al descargar el archivo: {e}")

    try:
        df = pd.read_csv(StringIO(response.text))
        print("Descarga y conversión exitosa")
        return df
    except Exception as e:
        raise Exception(f"Error al leer el CSV en DataFrame: {e}")
