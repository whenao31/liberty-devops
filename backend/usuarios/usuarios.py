"""This API is in charge to handle the CRUD for 'usuarios' """

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

@app.route("/usuarios", methods = ['GET', 'POST'])
def usuarios():
  """ usuarios route.
    get:
        summary: usuarios endpoint.
        description: Get all of the users.
        parameters: none
        responses:
            200:
                description: Usuarios object to be returned.
                schema: usuarios
            404:
                description: Usuarios not found.
      get:
        summary: usuarios endpoint.
        description: Get a single user with the user name.
        parameters:
            - name: usuario
              in: path
              description: User name
              type: string
              required: true
        responses:
            200:
                description: Usuario object to be returned.
                schema: usuarios
            404:
                description: Foo not found.
    post:
        summary: usuarios endpoint.
        description: Create a single user.
        parameters: 
            - name: usuario
              in: body
              description: User name
              type: string
              required: true
        responses:
            201:
                description: Usuario object to be returned.
                schema: usuarios
            400:
                description: Usuario not specified.
    """
  if request.method == 'POST':
    data = request.get_json()
    if 'usuario' not in data.keys():
      return Response("Usuario no especificados.", status=400, mimetype='text/plain')
    usuario = data['usuario']

    if cur:
      print("Database initialized")
      cur.execute("INSERT INTO usuarios VALUES (?);", (usuario,))
      cur.execute("INSERT INTO detalles VALUES (?,?,?,?);", (usuario,'',0,''))

    return Response("Usuario añadido: " + usuario, status=201, mimetype='text/plain')
  else:
    return get_usuarios(request.args.get("usuario", None))

def get_usuarios(usuario=None):
  print("get_usuarios")
  if usuario == None:
    lista_usuarios = []
    cur.execute("SELECT usuario FROM usuarios;")
    for (usuario, ) in cur:
      lista_usuarios.append({"usuario":usuario})
    return lista_usuarios
  cur.execute("SELECT usuario FROM usuarios WHERE usuario=?;", (usuario,),)
  row = cur.fetchone()
  return {"usuario":row[0]} if row and len(row) > 0 else {}

# if __name__ == '__main__': 
#     app.run()