def reemplaza_valor(df,col_1,col_2,*args):
    """Reemplaza los nan de la columna 2 (col_2) con los parámetros dados en base a si existe coincidencia con los valores de la columna 1
    (col_1)
    PARÁMETROS
    --------------------
    df: pd.DataFrame
    col_1:string (nombre de la columna a chequear en las condiciones)
    col_2:string (nombre de la columna que contiene los nulos)
    *args: argumentos ordenados que van a sustituir a los nan
    
    RETURN
    --------------------
    Pd.Dataframe"""

    nulos = df[df[col_2].isnull()]
    sin_dato = nulos[col_1].unique()
    asigna_dato =dict(zip(sin_dato,args))
    
    for row in range(len(df)):
        for dato in sin_dato:
            if df.loc[row,col_1] == dato:
                df.loc[row,col_2] = asigna_dato[dato]
            else:
                continue 
    return df.info()
