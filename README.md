# **Desarrollo aplicaciones Web en Python**

Inicialmente vamos a trabajar con un micro-framework de Python llamado Flask para el desarrollo de aplicaciones web. Flask está basado en Werkzeug, Jinja 2 y buenas intenciones. Mediante Flask podemos construir aplicaciones web y servicios Restful con Python de una forma extraordinariamente sencilla. Con pocas líneas podemos llegar a tener un servicio Restful funcionando.

**Características de Flask**

Ser un micro-framework no es indicativo de que es para aplicaciones pequeñas, por el contrario, significa que añade pocos elementos, permitiendo estar más cercano al lenguaje base, mejorando el rendimiento de la aplicación.
Estructura de un proyecto Flask
Por convención los proyectos Flask tienen la siguiente estructura:

- static, para los ficheros estáticos, como hojas de estilos, imágenes, javascript, etc.
- Templates, para los documentos html.
- app.py: Archivo Python que inicia la aplicación (Puede llamarse diferente de app.py)

**Requisitos para utilizar el framework Flask**

Flask depende de librerías externas como Werkzeug y Jinja2. Werkzeug es un toolkit para aplicaciones WSGI, que es un interface entre aplicaciones Python y servidores web. Jinja2 es un engine para el renderizado de plantillas (o templates) web. Para poder utilizar Flask debes de tener, al menos, Python 2.6 instalado. Flask también funciona con Python 3.

**Creación primer Proyecto web con Flask**

- Crear una carpeta de trabajo
- Desde visual studio code abrir la carpeta.

En la raíz de la carpeta crear un archivo llamado **app.py**

**Copiar librerías en archivo requeriments.txt**

Como estamos utilizando un entorno virtual es importante que a futuro para la instalación de la aplicación conozcamos las librerías que utilizamos en el proyecto y que conocemos que con esas librerías el proyecto funciono de forma correcta.  Por lo anterior creamos un archivo requirements.txt en la raíz de nuestro proyecto y ejecutamos el siguiente comando para copiar los nombres de las librerías utilizadas.

**pip freeze > requirements.txt**


**Referencias:**

1.	Documentación oficial Jinja: https://jinja.palletsprojects.com/en/stable/
2.	Documentación oficial en español sobre Flask: https://flask-es.readthedocs.io/
3.	Entornos virtuales en pythpon: https://www.freecodecamp.org/espanol/news/entornos-virtuales-de-python-explicados-con-ejemplos/
