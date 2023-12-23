"""This API is in charge to handle the CRUD for 'detalles' """


from flask import Flask, Response, request
from flask_cors import CORS
import mariadb
import atexit
import os

def exit_handler():
  conn.close()

atexit.register(exit_handler)

app = Flask(__name__)
CORS(app)

conn = None
user = os.getenv('user')
password = os.getenv('password')
host = os.getenv('host')
port = int(os.getenv('port'))
database = os.getenv('database')

try:
  conn = mariadb.connect(
    user=user,
    password=password,
    host=host,
    port=port,
    database=database,
    autocommit=True
  )
except mariadb.Error as e:
  print(f"Error connecting to MariaDB Platform: {e}")

# Get Cursor
cur = conn.cursor()

@app.route("/detalles", methods = ['GET', 'POST'])
def detalles():
  if request.method == 'POST':
    data = request.get_json()
    if 'usuario' not in data.keys():
      return Response("Usuario no especificado.", status=400, mimetype='text/plain')
    usuario = data['usuario']
    nombre = data['nombre']
    edad = data['edad']
    pais = data['pais']

    if cur:
      print("Database initialized")
      cur.execute(f"UPDATE detalles SET nombre='{nombre}', edad={edad}, pais='{pais}' WHERE usuario='{usuario}';")

    return Response("Usuario actualizado: %s, %s, %s, %s" % (usuario, nombre, edad, pais), status=201, mimetype='text/plain')
  else:
    return get_detalles(request.args.get("usuario", None))

def get_detalles(usuario=None):
  print("get_detalles")
  lista_usuarios = []
  if usuario == None:
    cur.execute("SELECT usuario, nombre, edad, pais FROM detalles;")
  else:
    cur.execute(f"SELECT usuario, nombre, edad, pais FROM detalles WHERE usuario LIKE '%{usuario}%';")
  for (usuario, nombre, edad, pais) in cur:
    lista_usuarios.append({"usuario":usuario, "nombre":nombre, "edad":edad, "pais":pais})
  return lista_usuarios
