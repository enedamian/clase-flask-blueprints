from flask import Flask
from modelo.usuario import inicializar_usuarios

app = Flask(__name__) #creamos una instancia de la clase Flask

inicializar_usuarios()

# registramos el blueprint
from controlador.rutas_usuario import usuarios_bp
app.register_blueprint(usuarios_bp)

