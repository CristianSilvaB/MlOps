


from fastapi import FastAPI
import pandas as pd
import scipy as sp
from sklearn.metrics.pairwise import cosine_similarity

#instanciar la aplicación

app = FastAPI()




tabla_user = pd.read_parquet("data/funcion.parquet")





@app.get("/UserForGenre/{genero}", name = "USERFORGENRE")
async def UserForGenre(genero):
    usuario= tabla_user[tabla_user["genres"]== genero]["user_id"].iloc[0] #obtengo usuario
    historial=tabla_user[(tabla_user['user_id'] == usuario) & (tabla_user['genres']==genero)] #filtro por el genero y usuario
    historial2 = historial[['Año', 'Horas jugadas']].copy() #me quedo con las columnas necesarias
    historial3=historial2.to_dict(orient="records")
    return {"Usuario":usuario ,"con más horas jugadas para": genero, "Historial acumulado": historial3 }



