# XBlock-Estilos-de-Aprendizaje

Este XBlock tiene como objetivo obtener el estilo de aprendizaje de los estudiantes de un curso de OpenEDX, realizando el <font color="green">test VARK</font> para que el profesor tenga conocimientos de qué material del curso debe subir para que se ajuste al estilo de aprendizaje que posea cada uno de los estudiantes. Esto mostrará, tanto al estudiante como al profesor, gráficas y valores que validen estos resultados.


# Contenido
- [Contenido](#contenido)
- [1. Test VARK](#1-Test-VARK)
- [2. Scripts](#2-Scripts)
  - [2.1 learningstylesxblock.py](#21-learningstylesxblock.py)

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

- Campos:
testResults: Es un campo de tipo Field que almacena los resultados del test. El alcance es "Scope.user_info" lo que significa que los datos se guardan por usuario.
testSolved: Es un campo de tipo Boolean que indica si el usuario ya ha resuelto el test. El alcance es "Scope.user_info" lo que significa que los datos se guardan por usuario.
userLearningStyle: Es un campo de tipo String que almacena el estilo de aprendizaje del usuario. El alcance es "Scope.user_info" lo que significa que los datos se guardan por usuario.

- Funciones:
load_resource: Es una función que se utiliza para obtener el contenido de un recurso.
resource_string: Es una función que se utiliza para obtener recursos de un kit.
render_template: Es una función que se utiliza para renderizar una plantilla con un contexto determinado.
results: Es una función que se utiliza para calcular los resultados del test y retornarlos en forma de diccionario.

- Vistas:
student_view: Es la vista principal del XBlock y se muestra a los estudiantes cuando están viendo cursos. La función recibe un contexto opcional y retorna un fragmento que contiene el HTML, CSS y JavaScript necesario para mostrar la vista.

- Manejadores:
get_formdata: Es un manejador que se utiliza para procesar los datos enviados por el formulario del test. La función recibe los datos del formulario y guarda los resultados en los campos correspondientes. La función también devuelve una respuesta en formato JSON para informar al usuario si el procesamiento fue exitoso o no.
En resumen, este XBlock es un ejemplo de código para crear un test de estilo de aprendizaje y mostrar los resultados a los usuarios en una plataforma de aprendizaje en línea.

