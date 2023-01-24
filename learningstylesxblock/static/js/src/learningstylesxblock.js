/* Javascript for LearningStylesXBlock. */
function LearningStylesXBlock(runtime, element) {
	// var handlerUrl = runtime.handlerUrl(element, 'get_formdata');
    // $('#Send', element).click(function(eventObject) {
    //     var answers = [];
    //     for (let i = 1; i <= 16; i++) {
    //         answers.push($(`input[name="pregunta-${i}"]:checked`).val())   
    //     }	
    //     $.ajax({
    //         type: "POST",
    //         url: handlerUrl,
    //         data: JSON.stringify({
    //         	"answers": answers
    //         }),
    //         success: location.reload
    //     });
    // });

    function showResults(result) {
        // $('.count', element).text(result.count);
        console.log(result)
    }

    var handlerUrl = runtime.handlerUrl(element, 'get_formdata');

    $('#Send', element).click(function(eventObject) {
        var answers = [];
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
    });

    $(function ($) {
        /* Here's where you'd do things on page load. */
    });
}
