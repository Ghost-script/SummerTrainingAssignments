$(document).ready(function(){

    $("input:radio[name=selectby]").change(function (){
        if ($(this).is("#time")){
            $("#day_for_time_span").show();
        } else {
            $("#day_for_time_span").hide();
        }
        if (!$(this).is("#all")){
            $("#selection_span").show();
        } else {
            $("#selection_span").hide();
        }
    });
    $.plot($("#plot"),plot_data, {xaxis : {mode : "time"}});

});
