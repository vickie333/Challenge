import pandas as pd

def load_ohlcv_csv(file_path, start_date=None, end_date=None, drop_cols=['unix', 'symbol']):
    """
    Carga datos OHLCV desde un archivo CSV, filtra columnas innecesarias y fechas.

    Parámetros:
        file_path (str): Ruta al archivo CSV.
        start_date (str): Fecha de inicio en formato 'YYYY-MM-DD'.
        end_date (str): Fecha de fin en formato 'YYYY-MM-DD'.
        drop_cols (list): Columnas a eliminar.

    Retorna:
        pd.DataFrame: Datos limpios filtrados por fecha e índice datetime.
    """

    data = pd.read_csv(file_path, skiprows=1)

    data.set_index('date', inplace=True)
    data.index = pd.to_datetime(data.index)

    if drop_cols:
        data.drop(columns=drop_cols, inplace=True)

    data.sort_index(inplace=True)

    if start_date and end_date:
        data = data.loc[start_date:end_date]

    return data
