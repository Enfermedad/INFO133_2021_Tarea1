from pymongo import MongoClient
import base64
def mongo_connection():
    try:
        connection = MongoClient('localhost')
        print("MongoDB conectado correctamente")
        return connection
    except Exception as e:
        print("Error de conexión : ",e)

db = mongo_connection()["mydb"]
nombre=input("Introduzca su primer nombre: ")
apellido=input("Introduzca su apellido: ")
rut = input("Introduzca su RUT con puntos y guión: ")
if (not (db["users"].find_one({'rut':rut}))):
    db["users"].insert_one({'nombre':nombre,'apellido':apellido,'rut':rut})
    print("Nuevo usuario registrado.")
fecha = input("Introduzca fecha de suceso (DD/MM/AA): ")    
latitud = input ("Introduzca latitud del suceso: ")
longitud = input ("Introduzca longitud del suceso: ")
exterior = input ("Exterior: 1 / Interior : 0 ")
categoria = input ("Introduzca categoria : 1:Humano 2:Musica 3:Animal 4:Climatico/Natural 5:Mecanico 6:Vehiculo 7:Alerta :")
archivo = input("Introduzca nombre del archivo (debe estar en la carpeta desde donde se ejecuta add_wavfile.py) Ej. ejemplo.wav: ")
f = open (archivo,"rb")
encode = base64.b64encode(f.read())
entry =db["files"].insert_one({'fecha':fecha,'latitud':latitud,'longitud':longitud,'exterior':exterior,'categoria':categoria,'data':encode,'usuario':{'rut':rut,'nombre':nombre,'apellido':apellido}})
f.close()
id_aux = entry.inserted_id
aux =(db["sources"].find_one({'_id':int(categoria)}))['archivos']
db["sources"].update_one({'_id':int(categoria)},{'$set':{'archivos': aux+[id_aux]}},upsert=False)
print("Archivo ingresado correctamente")
