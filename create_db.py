from pymongo import MongoClient
fuentes = [{'_id':1,'nombre':"humanos",'archivos':[]},{'_id':2,'nombre':"musica",'archivos':[]},{'_id':3,'nombre':"animales",'archivos':[]},{'_id':4,'nombre':"climaticos",'archivos':[]},{'_id':5,'nombre':"mecanicos",'archivos':[]},{'_id':6,'nombre':"vehiculos",'archivos':[]},{'_id':7,'nombre':"alertas",'archivos':[]}]
def mongo_connection():
    try:
        connection = MongoClient('localhost')
        print("MongoDB conectado correctamente")
        return connection
    except Exception as e:
        print("Error de conexión : ",e)

db = mongo_connection()["mydb"]
col_usuarios = db["users"]
col_fuentes = db["sources"]
col_archivos = db["files"]
if ('users' not in db.list_collection_names()):
    col_usuarios.insert_one({'_id':0,'nombre':"root",'apellido':"root",'rut':"00.000.000-0"})
if ('sources' not in db.list_collection_names()):
    col_fuentes.insert_many(fuentes)
if ('files' not in db.list_collection_names()):
    col_archivos.insert_one({'_id':0,'fecha':"0",'latitud':0,'longitud':0,'exterior':0,'categoria':0,'data':0,'usuario':{'rut':"00.000.000-0",'nombre':"root",'apellido':"root"}})
print("Base de datos creada correctamente.")
