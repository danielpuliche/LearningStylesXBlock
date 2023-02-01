# XBlock-Estilos-de-Aprendizaje

Este XBlock tiene como objetivo obtener el estilo de aprendizaje de los estudiantes de un curso de OpenEDX, realizando el <font color="green">test VARK</font> para que el profesor tenga conocimientos de qué material del curso debe subir para que se ajuste al estilo de aprendizaje que posea cada uno de los estudiantes. Esto mostrará, tanto al estudiante como al profesor, gráficas y valores que validen estos resultados.


# Contenido
- [XBlock-Estilos-de-Aprendizaje](#xblock-estilos-de-aprendizaje)
- [Contenido](#contenido)
- [1. Test VARK](#1-test-vark)
- [2. Scripts](#2-scripts)
  - [2.1 learningstylesxblock.py](#21-learningstylesxblockpy)
  - [2.2 setup.py](#22-setuppy)
  - [2.3 learningstylesxblock.js](#23-learningstylesxblockjs)
  - [2.4 learningstylesxblock.html](#24-learningstylesxblockhtml)
  - [2.5 learningstylesxblock.css](#25-learningstylesxblockcss)

# 1. Test VARK
VARK es un acrónimo que significa "Modalidad de Aprendizaje Vísuo, Auditivo, Read/Write y Kinestésico". Es un modelo que clasifica a los estudiantes en cuatro categorías según su preferencia de aprendizaje, basándose en la forma en que procesan y recuerdan la información.
Los estudiantes visuales aprenden mejor a través de imágenes, gráficos y videos.
Los estudiantes auditivos aprenden mejor a través del lenguaje hablado y música.
Los estudiantes read/write aprenden mejor a través de la escritura y la lectura.
Los estudiantes kinestésicos aprenden mejor a través de la experiencia práctica y la manipulación de objetos.

El test VARK es un cuestionario diseñado para identificar la modalidad de aprendizaje preferida de un individuo. Es importante tener en cuenta que muchas personas pueden tener preferencias múltiples y que estas preferencias pueden variar según el contexto. Sin embargo, comprender la modalidad de aprendizaje preferida puede ayudar a los estudiantes y a los profesores a adaptar su enfoque de enseñanza y aprendizaje para maximizar la comprensión y el retención de la información.[Test VARK]
(https://www.orientacionandujar.es/wp-content/uploads/2014/05/TEST-DE-VARK.pdf)

# 2. Scripts

## 2.1 learningstylesxblock.py
El código anterior es un ejemplo de un XBlock en Django para la plataforma Open edX, que se usa para crear bloques reutilizables y personalizados para el aprendizaje en línea. Este bloque en particular se llama "LearningStylesXBlock" y se diseñó para identificar el estilo de aprendizaje de un usuario a través de un test VARK.

La clase "LearningStylesXBlock" es una subclase de "XBlock" y se utiliza para crear un bloque de aprendizaje en línea que se puede utilizar en un curso. La clase contiene los siguientes componentes:

- **Campos:**
*testResults:* Es un campo de tipo Field que almacena los resultados del test. El alcance es "Scope.user_info" lo que significa que los datos se guardan por usuario.
*testSolved:* Es un campo de tipo Boolean que indica si el usuario ya ha resuelto el test. El alcance es "Scope.user_info" lo que significa que los datos se guardan por usuario.
*userLearningStyle:* Es un campo de tipo String que almacena el estilo de aprendizaje del usuario. El alcance es "Scope.user_info" lo que significa que los datos se guardan por usuario.

- **Funciones:**
*load_resource:* Es una función que se utiliza para obtener el contenido de un recurso.
*resource_string:* Es una función que se utiliza para obtener recursos de un kit.
*render_template:* Es una función que se utiliza para renderizar una plantilla con un contexto determinado.
*results:* Es una función que se utiliza para calcular los resultados del test y retornarlos en forma de diccionario.

- **Vistas:**
student_view: Es la vista principal del XBlock y se muestra a los estudiantes cuando están viendo cursos. La función recibe un contexto opcional y retorna un fragmento que contiene el HTML, CSS y JavaScript necesario para mostrar la vista.

- **Manejadores:**
*get_formdata:* Es un manejador que se utiliza para procesar los datos enviados por el formulario del test. La función recibe los datos del formulario y guarda los resultados en los campos correspondientes. La función también devuelve una respuesta en formato JSON para informar al usuario si el procesamiento fue exitoso o no.
En resumen, este XBlock es un ejemplo de código para crear un test de estilo de aprendizaje y mostrar los resultados a los usuarios en una plataforma de aprendizaje en línea.

## 2.2 setup.py
Este código es un archivo de configuración de paquete para un "XBlock"

En la primera línea se importa el módulo "absolute_import" desde el módulo "future". Esto es para garantizar que las importaciones se realicen de manera absoluta y no se confundan con módulos de nombres similares en el mismo paquete.

A continuación, se importa el módulo "os" que proporciona funciones para interactuar con el sistema operativo, y el módulo "setuptools" que proporciona funcionalidad para empaquetar y distribuir paquetes de Python.

La función "package_data" es una función genérica que busca los datos de paquete. Recibe dos argumentos: "pkg" y "roots". La función se usa para encontrar los archivos dentro de los directorios especificados por "roots", y declararlos como datos de paquete para el paquete "pkg". La función recorre cada uno de los "roots" y utiliza "os.walk" para recorrer los subdirectorios y archivos dentro de ellos. Luego, para cada archivo, se agrega su ruta relativa a la lista "data". Finalmente, se devuelve un diccionario con la clave "pkg" y el valor "data".

El método "setup" es una función que se usa para instalar el paquete. Tiene varios argumentos, incluyendo:

- name: Nombre del paquete.
- version: Versión del paquete.
- description: Descripción del paquete.
- license: Licencia del paquete.
- packages: Lista de paquetes incluidos en el paquete.
- install_requires: Lista de módulos necesarios para que el paquete funcione.
- entry_points: Un diccionario que especifica las entradas de los puntos de extensión de XBlock.
- package_data: Los datos de paquete, que se obtienen de la función "package_data".

En este caso, el paquete se llama "learningstylesxblock-xblock" y su versión es "0.1". Se requiere el módulo "XBlock" para su funcionamiento. La entrada del punto de extensión de XBlock es "learningstylesxblock = learningstylesxblock:LearningStylesXBlock", lo que significa que el bloque se registrará con el nombre "learningstylesxblock". Finalmente, los datos de paquete incluyen los archivos en los directorios "static" y "public".

## 2.3 learningstylesxblock.js

El código muestra una función en JavaScript llamada "LearningStylesXBlock". Esta función es un bloque de aprendizaje en un sistema de aprendizaje en línea que permite al usuario responder a un cuestionario con 16 preguntas y luego muestra los resultados de la encuesta en forma de gráficos.

La función showResults() recarga la página actual. La variable handlerUrl se utiliza para obtener la URL del controlador que se utilizará para enviar los datos del cuestionario.

El evento click del botón "Enviar" es gestionado por la función anónima registrada en el evento click. La función verifica si todas las preguntas han sido respondidas y, de ser así, recopila las respuestas en una matriz y las envía a la dirección especificada en handlerUrl. Si no se han respondido todas las preguntas, se muestra un mensaje de error utilizando una biblioteca de alertas llamada Swal.

La función $(function($) {}) se ejecuta al cargar la página y verifica si existen los elementos "#grafica" o "#graficaB". Si existen, se recopilan los resultados de las respuestas y se llaman a las funciones graficarResultados() o graficarResultadosBarra() para generar los gráficos.

Las funciones graficarResultados() y graficarResultadosBarra() utilizan la biblioteca de gráficos Chart.js para generar gráficos de áreas polares y de barras, respectivamente. Los gráficos muestran los resultados de la encuesta y están etiquetados con cuatro opciones: "Auditivo", "Cinético", "Lectura" y "Visual".

## 2.4 learningstylesxblock.html

Este código es una plantilla HTML que se está utilizando en algún marco de trabajo de desarrollo web que utiliza un lenguaje de plantilla para realizar ciertas operaciones dinámicas.
La plantilla incluye una estructura HTML principal con la clase "vark-test".
Dentro de ella, se usa una sentencia condicional "if" para determinar si se han resuelto los resultados del test (testSolved es una variable que es verdadera o falsa).
Si se han resuelto los resultados, se muestra el título "Resultados Test VARK" con una lista de resultados que se recorren mediante un bucle "for". Cada resultado consiste en una clave y un valor que se muestran en una lista.

Además, se muestra un gráfico (canvas) con la identificación "graficaB". También se muestra el resultado del estilo de aprendizaje del usuario (userLearningStyle) junto con otro gráfico (canvas) con la identificación "grafica". Si los resultados no se han resuelto, se muestra un título "El cuestionario VARK", un párrafo con texto explicativo y un formulario para enviar las respuestas del cuestionario. El formulario consiste en una serie de preguntas que se recorren mediante un bucle "for". Cada pregunta tiene una serie de respuestas que también se recorren mediante otro bucle "for". Las respuestas son opciones de radio con un valor determinado y deben ser seleccionadas antes de enviarse. Finalmente, hay un botón "Enviar" para enviar las respuestas del formulario.

## 2.5 learningstylesxblock.css

Este es un código CSS, utilizado para dar estilo a un documento HTML. Establece la familia de fuentes, colores, márgenes, rellenos, etc. de varios elementos HTML como body, encabezados, párrafos, botones, bloques de preguntas, etiquetas de respuestas, etc. El código utiliza selectores CSS como clases e identificadores para dirigirse a elementos específicos en la página y aplicar estilos a ellos. Los estilos incluyen estilos de fuentes como font-weight, font-size, text-align, font-family, line-height, etc. y estilos de diseño como padding, margin, display, border, etc.
