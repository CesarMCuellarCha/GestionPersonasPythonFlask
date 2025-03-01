#importar librerias necesarias
from flask import Flask, render_template, request

#crear un objeto de tipo flask
app = Flask(__name__)

#lista para almacenar personas
personas=[]

#definir la ruta raíz que renderiza la plantilla HTML con la lista de personas
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('personas.html', personas=personas)
    else:
        if request.method == 'POST':
            # obtener los datos del formulario
            nombre = request.form['nombre']
            apellido = request.form['apellido']
            correo = request.form['correo']
            #crear un objeto persona de tipo diccionario
            persona = {'nombre': nombre, 'apellido':apellido,               
                    'correo': correo}
            #agregar la persona a la lista de personas
            personas.append(persona)
            #redireccionar a la raíz para mostrar la lista actualizada                        
            return render_template('personas.html', personas=personas)

#ejecutar el programa
if __name__ == '__main__':
    #correr el servidor en el puerto 4200 con depuración activada
    app.run(port=4200,debug=True)