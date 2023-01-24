/* Javascript for LearningStylesXBlock. */
function LearningStylesXBlock(runtime, element) {

	var handlerUrl = runtime.handlerUrl(element, 'get_formdata');

    console.log(handlerUrl);
    $('#Send', element).click(function(eventObject) {
        eventObject.preventDefault();
        // var answers = [];
        // for (let i = 1; i <= 16; i++) {
        //     answers.push($(`input[name="pregunta-${i}"]:checked`).val())   
        // }	
        // $.ajax({
        //     type: "POST",
        //     url: handlerUrl,
        //     data: JSON.stringify({
        //     	"answers": answers
        //     }),
        //     success: location.reload
        // });
    });

    // $(function ($) {        
    //     // Unused for now
    // });
}
