import serial
import time
import requests
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Sting de conexión, se obtiene directamente de Atlas, cuando se consultan las formas de conexión.
# CAMBIARLO SEGUN EL SERVIDOR QUE HAYAN CREADO
uri = "mongodb+srv://amira:amira@monitoreo.lqigicj.mongodb.net/?retryWrites=true&w=majority"

# Se crea un nuevo cliente y se conecta al servidor
client = MongoClient(uri, server_api=ServerApi('1'))

# Se envía un "ping" para confirmar que se conector satisfacoriamente 
try:
    client.admin.command('ping')
    print("La conexión a MongoDB fue exitosa!")
except Exception as e:
    print(e)

# Seleccionar la base de datos y la colección adecuada
db = client['monitoreo'] # CAMBIAR ACORDE A LA BASE DE DATOS CREADA
collection = db['temp-humidity'] # CAMBIAR ACORDE A LA COLECCIÓN CREADA

def publish_data(json_data):
    # Insertar el documento en la colección de la base de datos
    collection.insert_one(json_data)
    print('Datos publicados en la base de datos MongoDB!')


def extract_info(data):
    # Se construye un mensaje en formato json (diccionario) para poder publicar el dato
    print(data)
    temp, humidity = data.split(",")
    temp = float(temp.split(":")[1])
    humidity = float(humidity.split(":")[1])

    return {"lugar": "udea", "temperatura": temp, "humedad": humidity}

def main():
    # Seleccionar el puerto COM del arduino
    SerialPort = "COM8"
    print("hola")
    try:
        dev = serial.Serial(SerialPort, 115200, timeout=1)
        dev.close() # Se cierra el puerto en caso de que este abierto
        dev.open() # Se abre el puerto
        print("Conectado al puerto serial: " + SerialPort)
        
        dev.flushInput() # Se limpia el bufer de entrada
        dev.flushOutput() # Se limpia el bufer de salida

        while (1):
            dev.write(str.encode("ENVIAR")) # Se envia la instruction al Arduino para enviar las mediciones
            
            # Se lee la respuesta del arduiono
            data = dev.readline().decode("utf-8").strip() # strip remueve los espacios y el final de linea

            # Si no es un dato vacio... 
            if data != "":
                data = extract_info(data)
                print(data)
                res= requests.post("http://localhost:8000/monitoreo", json=data)
                print(res.text)

            time.sleep(2)

    except Exception as error:
        print(error)

    except KeyboardInterrupt:
        dev.close()

    finally:
        dev.close()


if __name__ == '__main__':
    main()