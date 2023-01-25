"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources
import csv
from xblock.fragment import Fragment
from django.template import Context, Template
from xblock.core import XBlock
from xblock.fields import Field, Integer, Scope, Boolean, JSONField, String
from django.views.decorators.csrf import csrf_exempt

@XBlock.needs("user")
class LearningStylesXBlock(XBlock):

    """
    This xblock is designed to identify the user's learning style throught a VARK test.
    """

    questions = [
    {
        "pregunta":"Necesito encontrar el camino a una tienda que me recomendó un amigo. Yo:",
        "respuestas":[
            "Buscaría dónde está la tienda en relación con algún lugar que conozco.",
            "Le diría a mi amigo que me diera las indicaciones.",
            "Escribiría el nombre de la calle que debo recordar.",
            "Usaría un mapa."
        ]
    },
    {
        "pregunta":"Una página web tiene un vídeo que muestra cómo hacer un gráfico o una tabla especial. Hay una persona hablando, algunas listas y palabras que describen lo que hay que hacer y algunos diagramas. Aprendería más:",
        "respuestas":[
            "Viendo los diagramas.",
            "Escuchando.",
            "Leyendo las palabras.",
            "Viendo las acciones."
        ]
    },
    {
        "pregunta":"Quiero saber más sobre una excursión a la que voy a ir. Yo:",
        "respuestas":[
            "Hablaría con la persona que planificó la excursión o con otras personas que vayan a hacerla.",
            "Miraría los detalles sobre los aspectos más destacados y las actividades de la excursión.",
            "Usaría un mapa y vería dónde están los lugares.",
            "Leería sobre la excursión en el itinerario.",
        ]
    },
		{
        "pregunta":"A la hora de elegir una carrera o un área de estudio, esto es importante para mí:",
        "respuestas":[
            "Comunicarme con otros a través del diálogo.",
            "Aplicar mis conocimientos en situaciones reales.",
            "Trabajar con diseños, mapas o gráficos.",
            "Utilizar bien las palabras en las comunicaciones escritas.",
        ]
    },
		{
        "pregunta":"Cuando aprendo:",
        "respuestas":[
            "Me gusta hablar de las cosas.",
            "Uso ejemplos y aplicaciones.",
            "Veo patrones en las cosas.",
            "Leo libros, artículos y folletos.",
        ]
    },
		{
        "pregunta":"Quiero ahorrar más dinero y decidir entre una serie de opciones. Yo:",
        "respuestas":[
            "Hablaría con un experto sobre las opciones.",
            "Consideraría ejemplos de cada opción utilizando mi información financiera.",
            "Utilizaría gráficos que muestren diferentes opciones para diferentes periodos de tiempo.",
            "Leería un folleto impreso que describa las opciones en detalle.",
        ]
    },
		{
        "pregunta":"Quiero aprender a jugar un nuevo juego de mesa o de cartas. Yo:",
        "respuestas":[
            "Utilizaría los diagramas que explican las distintas fases, movimientos y estrategias del juego.",
            "Observaría a otros jugar antes de unirme al juego.",
            "Utilizaría los diagramas que explican las distintas fases, movimientos y estrategias del juego.",
            "Leería las instrucciones.",
        ]
    },
		{
        "pregunta":"Tengo un problema en el corazón. Preferiría que el médico:",
        "respuestas":[
            "Describiera lo que está mal.",
            "Utilizara un modelo de plástico para mostrar lo que está mal.",
            "Le mostrara un diagrama de lo que está mal.",
            "Le diera algo que leer para explicar lo que está mal.",
        ]
    },
		{
        "pregunta":"Quiero aprender a hacer algo nuevo en una computadora. Yo:",
        "respuestas":[
            "Hablaría con personas que conozcan el programa.",
            "Empezaría a utilizarlo y aprender por ensayo y error.",
            "Seguiría los diagramas de un libro.",
            "Leería las instrucciones escritas que vienen con el programa.",
        ]
    },
		{
        "pregunta":"Cuando aprendo de Internet, me gusta:",
        "respuestas":[
            "Los canales de audio donde puedo escuchar podcasts o entrevistas.",
            "Los vídeos que muestran cómo hacer o fabricar algo.",
            "El diseño y las características visuales interesantes.",
            "Descripciones, listas y explicaciones escritas interesantes.",
        ]
    },
		{
        "pregunta":"Quiero aprender sobre un nuevo proyecto. Me gustaría pedir:",
        "respuestas":[
            "Una oportunidad para hablar sobre el proyecto.",
            "Ejemplos en los que el proyecto se haya utilizado con éxito.",
            "Diagramas que muestren las etapas del proyecto con gráficos de beneficios y costes.",
            "Un informe escrito que describa las principales características del proyecto.",
        ]
    },
		{
        "pregunta":"Quiero aprender a tomar mejores fotos. Yo:",
        "respuestas":[
            "Haría preguntas y hablaría sobre la cámara y sus características.",
            "Utilizaría ejemplos de fotos buenas y malas mostrando cómo mejorarlas.",
            "Utilizaría diagramas que muestren la cámara y lo que hace cada parte.",
            "Utilizaría las instrucciones escritas sobre lo que hay que hacer.",
        ]
    },
		{
        "pregunta":"Prefiero un presentador o un profesor que utilice:",
        "respuestas":[
            "Preguntas y respuestas, charlas, discusiones en grupo u oradores invitados.",
            "Demostraciones, modelos o sesiones prácticas.",
            "Diagramas, cuadros, mapas o gráficos.",
            "Folletos, libros o lecturas.",
        ]
    },
		{
        "pregunta":"Acabo de terminar una competencia o una prueba y me gustaría recibir una opinión. Me gustaría recibirla:",
        "respuestas":[
            "Utilizando ejemplos de lo que he hecho.",
            "Mediante gráficos que muestren lo que alcancé.",
            "Mediante una descripción escrita de mis resultados.",
            "De alguien que lo hable conmigo."
        ]
    },
		{
        "pregunta":"Quiero informarme sobre una casa o un apartamento. Antes de visitarla quisiera:",
        "respuestas":[
            "Ver un vídeo de la propiedad.",
            "Un plano que muestre las habitaciones y un mapa de la zona.",
            "Una descripción impresa de las habitaciones y las características.",
            "Una conversación con el propietario."
        ]
    },
		{
        "pregunta":"Quiero montar una mesa de madera que viene por partes. Aprendería mejor con:",
        "respuestas":[
            "Un vídeo de una persona montando una mesa similar.",
            "Diagramas que muestren cada etapa del montaje.",
            "Las instrucciones escritas que vienen con las piezas de la mesa.",
            "Los consejos de alguien que lo haya hecho antes."
        ]
    }
	]

    stylesAnswers = {

        "Buscaría dónde está la tienda en relación con algún lugar que conozco.":"K",
        "Le diría a mi amigo que me diera las indicaciones.": "A",
        "Escribiría el nombre de la calle que debo recordar.":"R",
        "Usaría un mapa.": "V",

        "Viendo los diagramas.":"V",
        "Escuchando.":"A",
        "Leyendo las palabras.":"R",
        "Viendo las acciones.":"K",

        "Miraría los detalles sobre los aspectos más destacados y las actividades de la excursión.":"K",
        "Usaría un mapa y vería dónde están los lugares.":"V",
        "Leería sobre la excursión en el itinerario.":"R",
        "Hablaría con la persona que planificó la excursión o con otras personas que vayan a hacerla.":"A",

        "Aplicar mis conocimientos en situaciones reales.":"K",
        "Comunicarme con otros a través del diálogo.":"A",
        "Trabajar con diseños, mapas o gráficos.":"V",
        "Utilizar bien las palabras en las comunicaciones escritas.":"R",

        "Me gusta hablar de las cosas.":"A",
        "Veo patrones en las cosas.":"V",
        "Uso ejemplos y aplicaciones.":"K",
        "Leo libros, artículos y folletos.":"R",

        "Consideraría ejemplos de cada opción utilizando mi información financiera.":"K",
        "Leería un folleto impreso que describa las opciones en detalle.":"R",
        "Utilizaría gráficos que muestren diferentes opciones para diferentes periodos de tiempo.":"V",
        "Hablaría con un experto sobre las opciones.":"A",

        "Observaría a otros jugar antes de unirme al juego.":"K",
        "Utilizaría los diagramas que explican las distintas fases, movimientos y estrategias del juego.":"A",
        "Utilizaría los diagramas que explican las distintas fases, movimientos y estrategias del juego.":"V",
        "Leería las instrucciones.":"R",

        "Le diera algo que leer para explicar lo que está mal.":"R",
        "Utilizara un modelo de plástico para mostrar lo que está mal.":"K",
        "Describiera lo que está mal.":"A",
        "Le mostrara un diagrama de lo que está mal.":"V",

        "Leería las instrucciones escritas que vienen con el programa.":"R",
        "Hablaría con personas que conozcan el programa.":"A",
        "Empezaría a utilizarlo y aprender por ensayo y error.":"K",
        "Seguiría los diagramas de un libro.":"V",

        "Los vídeos que muestran cómo hacer o fabricar algo.":"K",
        "El diseño y las características visuales interesantes.":"V",
        "Descripciones, listas y explicaciones escritas interesantes.":"R",
        "Los canales de audio donde puedo escuchar podcasts o entrevistas.":"A",

        "Diagramas que muestren las etapas del proyecto con gráficos de beneficios y costes.":"V",
        "Un informe escrito que describa las principales características del proyecto.":"R",
        "Una oportunidad para hablar sobre el proyecto.":"A",
        "Ejemplos en los que el proyecto se haya utilizado con éxito.":"K",

        "Haría preguntas y hablaría sobre la cámara y sus características.":"A",
        "Utilizaría las instrucciones escritas sobre lo que hay que hacer.":"R",
        "Utilizaría diagramas que muestren la cámara y lo que hace cada parte.":"V",
        "Utilizaría ejemplos de fotos buenas y malas mostrando cómo mejorarlas.":"K",

        "Demostraciones, modelos o sesiones prácticas.":"K",
        "Preguntas y respuestas, charlas, discusiones en grupo u oradores invitados.":"A",
        "Folletos, libros o lecturas.":"R",
        "Diagramas, cuadros, mapas o gráficos.":"V",

        "Utilizando ejemplos de lo que he hecho.":"K",
        "Mediante una descripción escrita de mis resultados.":"R",
        "De alguien que lo hable conmigo.":"A",
        "Mediante gráficos que muestren lo que alcancé.":"V",

        "Ver un vídeo de la propiedad.":"K",
        "Una conversación con el propietario.":"A",
        "Una descripción impresa de las habitaciones y las características.":"R",
        "Un plano que muestre las habitaciones y un mapa de la zona.":"V",

        "Diagramas que muestren cada etapa del montaje.":"V",
        "Los consejos de alguien que lo haya hecho antes.":"A",
        "Las instrucciones escritas que vienen con las piezas de la mesa.":"R",
        "Un vídeo de una persona montando una mesa similar.":"K",

    }

	# Fields
    testResults = Field(
		default="", scope=Scope.user_state,
		help="Shows the test result"
	)
	
    testSolved = Boolean(
		default=False, scope=Scope.user_state,
		help="Flag to identify uf the user already solved the VARK test"
	)
	# Render views
    def load_resource(self, resource_path):
        """
        Gets the content of a resource
		"""
        resource_content = pkg_resources.resource_string(__name__, resource_path)
        return resource_content.decode("utf8")
        
	# Default code
    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")
	
	# Render with context
    def render_template(self, template_path, context={}):
        template_str = self.load_resource(template_path)
        return Template(template_str).render(Context(context))

    def results(self, results):
        lenResults = len(results)
        resultsTest = {
            "V":0,
            "A":0,
            "R":0,
            "K":0
        }
        for r in results:
            resultsTest[r]+=1
        return resultsTest

	# TO-DO: change this view to display your data your own way.
    @csrf_exempt
    def student_view(self, context=None):
        """
        The primary view of the LearningStylesXBlock, shown to students
        when viewing courses.
        """ 
        context = {
            'testSolved': self.testSolved,
            'testQuestions': self.questions,
            'testResults':self.testResults
        }
        
        html = self.render_template("static/html/learningstylesxblock.html", context)		
        frag = Fragment(html.format(self=self))
        
        frag.add_css(self.resource_string("static/css/learningstylesxblock.css"))
        frag.add_javascript_url("https://cdn.jsdelivr.net/npm/chart.js@latest/dist/Chart.min.js")
        frag.add_javascript_url("https://d3js.org/d3.v7.min.js")
        frag.add_javascript(self.resource_string("static/js/src/learningstylesxblock.js"))
        frag.initialize_js('LearningStylesXBlock')
        return frag

	# HANDLER	
    @XBlock.json_handler
    def get_formdata(self, data, suffix=''):		
        y = []
        for x in data["answers"]:
            try: 
                y.append(self.stylesAnswers[x])
            except:
                y.append("-")
        self.testResults = self.results(y)
        self.testSolved = True
        return {
            'testSolved': self.testSolved,
            'testResults':self.testResults
            }

	# TO-DO: change this to create the scenarios you'd like to see in the
	# workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("LearningStylesXBlock",
                """<learningstylesxblock/>
                """),
        ]