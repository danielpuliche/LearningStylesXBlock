/* Javascript for LearningStylesXBlock. */
function LearningStylesXBlock(runtime, element) {

    function showResults(result) {
        location.reload();
    }

    var handlerUrl = runtime.handlerUrl(element, 'get_formdata');

    $('#Send', element).click(function(eventObject) {
        var answers = [];
        for (let i = 1; i <= 16; i++) {
            answers.push($(`input[name="pregunta-${i}"]:checked`).val())   
        }
        eventObject.preventDefault();
        $.ajax({
            type: "POST",
            url: handlerUrl,
            data: JSON.stringify({
                "answers": answers
            }),
            success: showResults
        });
    });

    $(function ($) {
        if($("#grafica").length){
            let results = $('.results').map(function() {
                return this.innerHTML;
            }).get();
            graficarResultados(results);   
            graficaD3(results);     
        }
    });

    function graficarResultados(results){
        // Obtener una referencia al elemento canvas del DOM
        const $grafica = document.querySelector("#grafica");
        // Las etiquetas son las porciones de la gráfica
        const etiquetas = ["Visual", "Audio", "Reading", "Kinestesico"]
        // Podemos tener varios conjuntos de datos. Comencemos con uno
        const datosIngresos = {
            data: results, // La data es un arreglo que debe tener la misma cantidad de valores que la cantidad de etiquetas
            // Ahora debería haber tantos background colors como datos, es decir, para este ejemplo, 4
            backgroundColor: [
                'rgb(240, 108, 100)',
                'rgb(255, 215,0)',
                'rgb(136, 206, 210)',
                'rgb(32, 99, 155)',
            ],// Color de fondo
            borderColor: [
                'rgba(0,0,0,1)',
                'rgba(0,0,0,1)',
                'rgba(0,0,0,1)',
                'rgba(0,0,0,1)',
            ],// Color del borde
            borderWidth: 1,// Ancho del borde
        };
        new Chart($grafica, {
            type: 'pie',// Tipo de gráfica. Puede ser dougnhut o pie
            data: {
                labels: etiquetas,
                datasets: [
                    datosIngresos,
                    // Aquí más datos...
                ]
            },
            animation: {
                animateRotate: true
            }
        });        
    }

    function graficaD3(results){
        var data = results;
        var width = 300;
        var height = 300;
        var radius = Math.min(width, height) / 2;

        var color = d3.scaleOrdinal()
            .range(["#ff0000", "#0000ff", "#00ff00", "#00ff00"]);

        var arc = d3.arc()
            .outerRadius(radius - 10)
            .innerRadius(0);

        var labelArc = d3.arc()
            .outerRadius(radius - 40)
            .innerRadius(radius - 40);

        var pie = d3.pie()
            .sort(null)
            .value(function(d) { return d; });

        var svg = d3.select("#grafica").append("svg")
            .attr("width", width)
            .attr("height", height)
            .append("g")
            .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

        var g = svg.selectAll(".arc")
            .data
    }
}
