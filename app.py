from flask import Flask
from modelo.usuarios import inicializar_usuarios

app = Flask(__name__) #creamos una instancia de la clase Flask

inicializar_usuarios()

# registramos el blueprint
from controlador.rutas_usuarios import usuarios_bp
app.register_blueprint(usuarios_bp)

