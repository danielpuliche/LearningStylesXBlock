"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources
import psycopg
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

    # GET QUESTIONS AND ANSWERS
    questions = []
    stylesAnswers = {}

    try:
        with psycopg.connect("dbname=LearningStyleDB user=postgres password=password123 host=localhost") as conn:

            with conn.cursor() as cur:

                cur.execute("SELECT * from tbl_test_question")
                questions_ = cur.fetchall()
                cur.execute("SELECT description, id_question, learning_style from tbl_test_answer")
                answers = cur.fetchall()
                
        for question in questions_:
            dictPregunta = {}
            dictPregunta["pregunta"] = question[1]
            listRespuestasPregunta = []
            for ans in answers:
                if question[0] == ans[1]:
                    listRespuestasPregunta.append(ans[0])
                    stylesAnswers[ans[0]] = ans[2]
            dictPregunta["respuestas"] = listRespuestasPregunta
            questions.append(dictPregunta)

    except Exception as e:
        question = []
        stylesAnswers = {}

	# Fields
    testResults = Field(
		default="", scope=Scope.user_info,
		help="Shows the test result"
	)
	
    testSolved = Boolean(
		default=False, scope=Scope.user_info,
		help="Flag to identify uf the user already solved the VARK test"
	)

    userLearningStyle = String(
		default="", scope=Scope.user_info,
		help="Shows user's learning style"
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
        resultsTest = {
            "Visual":0,
            "Auditive":0,
            "Reading":0,
            "Kinesthetic":0
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
            'testResults':self.testResults,
            'userLearningStyle':self.userLearningStyle
        }
        
        html = self.render_template("static/html/learningstylesxblock.html", context)		
        frag = Fragment(html.format(self=self))
        
        frag.add_css(self.resource_string("static/css/learningstylesxblock.css"))
        frag.add_css_url("https://cdn.jsdelivr.net/npm/sweetalert2@11.7.0/dist/sweetalert2.min.css")
        frag.add_javascript_url("https://cdn.jsdelivr.net/npm/chart.js@latest/dist/Chart.min.js")
        frag.add_javascript_url("https://cdn.jsdelivr.net/npm/sweetalert2@11.7.0/dist/sweetalert2.all.min.js")
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
        learningStyleAux = [key for key, value in self.testResults.items() if value == max(self.testResults.values())]
        if ("Visual" in learningStyleAux):
            self.userLearningStyle += "/Visual"
        if("Auditive" in learningStyleAux):
            self.userLearningStyle += "/Auditivo"
        if("Reading" in learningStyleAux):
            self.userLearningStyle += "/Lector"
        if("Kinesthetic" in learningStyleAux):
            self.userLearningStyle += "/Quinestésico"
        self.userLearningStyle = self.userLearningStyle[1:]
        self.testSolved = True

        try:
            with psycopg.connect("dbname=LearningStyleDB user=postgres password=password123 host=localhost") as conn:
                with conn.cursor() as cur:
                    cur.execute("INSERT INTO tbl_vark_test_result (visual_result, auditive_result, reading_result, kinesthetic_result, learning_style) VALUES (%s, %s, %s, %s, %s)",(int(self.testResults["Visual"]),int(self.testResults["Auditive"]),int(self.testResults["Reading"]),int(self.testResults["Kinesthetic"]),str(self.userLearningStyle)))
                    conn.commit()
            
            return {
                'testSolved': self.testSolved,
                'testResults':self.testResults,
                'userLearningStyle':self.userLearningStyle
                }
                
        except Exception as e:

            return {
                'testSolved': self.testSolved,
                'testResults':self.testResults,
                'userLearningStyle': str(e)
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