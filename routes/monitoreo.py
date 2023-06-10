from fastapi import APIRouter
from config.db import conn
from schemas.monitoreo import monitoreoEntity, muchosMonitoreosEntity
from models.monitoreo import Monitoreo
import datetime

monitoreo = APIRouter()

@monitoreo.get('/monitoreo')
def find_all_monitoreo():
    return muchosMonitoreosEntity(conn.monitoreo.dato.find())

@monitoreo.get('/monitoreo/temperatura/{temp}')
def find_monitoreo_temperatura(temp: float):
    return muchosMonitoreosEntity(conn.monitoreo.dato.find({"temperatura":{"$get":temp}}))

@monitoreo.get('/monitoreo/lugar/{lug}/autor/{aut}')
def find_monitoreo_place_author(lug: str, aut: str):
    return muchosMonitoreosEntity(conn.monitoreo.dato.find({"lugar":lug, "autor":aut}))

@monitoreo.post('/monitoreo')
def save_monitoreo(mon: Monitoreo):
    new_mon = dict(mon)
    new_mon["createdAt"] = datetime.datetime.utcnow()
    new_mon["updateAt"] = datetime.datetime.utcnow()
    conn.monitoreo.dato.insert_one(new_mon)
    return "Dato almacenado"

@monitoreo.put('/monitoreo')
def update_monitoreo():
    return "Actualización de dato de monitoreo"

@monitoreo.delete('/monitoreo')
def delete_monitoreo():
    return "Borrado de dato de monitoreo"

