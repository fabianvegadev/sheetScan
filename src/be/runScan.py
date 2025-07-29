import pandas as pd
import re

def runScan(df: pd.DataFrame, output_path: str = "special_characters_report.csv") -> pd.DataFrame:
    """
    Escanea un DataFrame para detectar caracteres especiales y guarda un informe detallado en un archivo CSV.

    Args:
        df (pd.DataFrame): El DataFrame a escanear.
        output_path (str): Ruta donde se guardará el archivo CSV con el informe.

    Returns:
        pd.DataFrame: Un DataFrame con los caracteres especiales encontrados y su ubicación.
    """
    # Expresión regular para caracteres especiales (exceptuando letras, números y espacios)
    special_char_pattern = re.compile(r'[^\w\s]', re.UNICODE)

    results = []

    for row_idx, row in df.iterrows():
        for col in df.columns:
            cell_value = str(row[col])
            matches = special_char_pattern.findall(cell_value)
            for match in matches:
                results.append({
                    "row_index": row_idx,
                    "column": col,
                    "character": match,
                    "original_value": cell_value
                })

    result_df = pd.DataFrame(results)

    if not result_df.empty:
        result_df.to_csv(output_path, index=False, encoding='utf-8')
        print(f"Informe generado correctamente en '{output_path}'")
    else:
        print("No se encontraron caracteres especiales en el DataFrame.")

    return result_df
