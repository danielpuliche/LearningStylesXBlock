/* Javascript for LearningStylesXBlock. */
function LearningStylesXBlock(runtime, element) {

    function showResults(result) {
        location.reload();
    }

    var handlerUrl = runtime.handlerUrl(element, 'get_formdata');

    $('#send', element).click(function(eventObject) {
        eventObject.preventDefault();
        let answers = [];
        let requiredFlag;
        for (let i = 1; i <= 16; i++) {
            if(!$(`input[name="pregunta-${i}"]:checked`).prop('checked')){
                requiredFlag = true;
                break;
            }
        }
        if(requiredFlag){
            Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: 'Marca al menos una respuesta en todas las preguntas!',
              });
        }else{
            for (let i = 1; i <= 16; i++) {
                answers.push($(`input[name="pregunta-${i}"]:checked`).val())   
            }
            $.ajax({
                type: "POST",
                url: handlerUrl,
                data: JSON.stringify({
                    "answers": answers
                }),
                success: showResults
            });
        }
    });

    $(function ($) {
        if($("#grafica").length){
            let results = $('.results').map(function() {
                return this.innerHTML;
            }).get();
            graficarResultados(results);                 
        }
        if($("#graficaB").length){
            let results = $('.results').map(function() {
                return this.innerHTML;
            }).get();
            graficarResultadosBarra(results);                 
        }
    });

    function graficarResultados(results){
        // Obtener una referencia al elemento canvas del DOM
        const $grafica = document.querySelector("#grafica");
        // Las etiquetas son las porciones de la gráfica
        const etiquetas = ["Auditive", "Kinesthetic", "Reading", "Visual" ];
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
            type: 'polarArea',// Tipo de gráfica. Puede ser dougnhut o pie
            data: {
                labels: etiquetas,
                datasets: [
                    datosIngresos,
                ]
            }            
        });        
    }
    
    function graficarResultadosBarra(results){
        // Obtener una referencia al elemento canvas del DOM
        const $graficaB = document.querySelector("#graficaB");
        // Las etiquetas son las porciones de la gráfica
        const etiquetasB = ["Auditive", "Kinesthetic", "Reading", "Visual" ];
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
        new Chart($graficaB, {
            type: 'bar',// Tipo de gráfica
            data: {
                labels: etiquetasB,
                datasets: [
                    datosIngresos,
                ]
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }],
                },
            }
        });        
    }
    
}
